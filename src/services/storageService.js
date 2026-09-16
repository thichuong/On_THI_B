/**
 * Storage Service: Manages persistence for theme, bookmarks, wrong answers,
 * exam history, and exam cycles with IndexedDB backing and localStorage fallback.
 */
import { eventBus } from '../core/eventBus.js';
import { dbService } from './dbService.js';

const STORAGE_KEYS = {
  THEME: 'gplx_theme',
  BOOKMARKS: 'gplx_bookmarks',
  WRONG_QUESTIONS: 'gplx_wrong_questions',
  EXAM_HISTORY: 'gplx_exam_history',
  SETTINGS: 'gplx_settings',
  SEEN_STANDARD: 'gplx_seen_standard',
  SEEN_QUICK: 'gplx_seen_quick'
};

class StorageServiceImpl {
  constructor() {
    this._initialized = false;
    this._initPromise = null;
    this._cache = {
      theme: null,
      bookmarks: null,
      wrongQuestions: null,
      seenStandard: null,
      seenQuick: null
    };
  }

  /**
   * Initializes IndexedDB and hydrates cache
   */
  async init() {
    if (this._initPromise) return this._initPromise;

    this._initPromise = (async () => {
      try {
        await dbService.init();

        // Hydrate seen cycles from IndexedDB if available
        const [stdCycle, qkCycle] = await Promise.all([
          dbService.getExamCycle('standard'),
          dbService.getExamCycle('quick')
        ]);

        if (Array.isArray(stdCycle) && stdCycle.length > 0) {
          this._cache.seenStandard = new Set(stdCycle);
          localStorage.setItem(STORAGE_KEYS.SEEN_STANDARD, JSON.stringify(stdCycle));
        }

        if (Array.isArray(qkCycle) && qkCycle.length > 0) {
          this._cache.seenQuick = new Set(qkCycle);
          localStorage.setItem(STORAGE_KEYS.SEEN_QUICK, JSON.stringify(qkCycle));
        }

        this._initialized = true;
      } catch (err) {
        console.warn('StorageService init error:', err);
      }
    })();

    return this._initPromise;
  }

  // --- Theme ---

  getTheme() {
    return localStorage.getItem(STORAGE_KEYS.THEME) || 'dark';
  }

  setTheme(theme) {
    localStorage.setItem(STORAGE_KEYS.THEME, theme);
    dbService.setMeta('theme', theme).catch(() => {});
    eventBus.emit('theme:changed', theme);
  }

  // --- Bookmarks ---

  getBookmarks() {
    if (this._cache.bookmarks) return this._cache.bookmarks;
    try {
      const bms = JSON.parse(localStorage.getItem(STORAGE_KEYS.BOOKMARKS)) || [];
      this._cache.bookmarks = bms;
      return bms;
    } catch {
      return [];
    }
  }

  toggleBookmark(questionId) {
    const qid = Number(questionId);
    const bookmarks = [...this.getBookmarks()];
    const index = bookmarks.indexOf(qid);
    let isBookmarked;

    if (index === -1) {
      bookmarks.push(qid);
      isBookmarked = true;
    } else {
      bookmarks.splice(index, 1);
      isBookmarked = false;
    }

    this._cache.bookmarks = bookmarks;
    localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bookmarks));

    // Persist to IndexedDB
    dbService.saveQuestionProgress(qid, { isBookmarked }).catch(() => {});

    eventBus.emit('bookmark:changed', { questionId: qid, isBookmarked, bookmarks });
    return isBookmarked;
  }

  isBookmarked(questionId) {
    return this.getBookmarks().includes(Number(questionId));
  }

  // --- Wrong Questions ---

  getWrongQuestions() {
    if (this._cache.wrongQuestions) return this._cache.wrongQuestions;
    try {
      const wrong = JSON.parse(localStorage.getItem(STORAGE_KEYS.WRONG_QUESTIONS)) || {};
      this._cache.wrongQuestions = wrong;
      return wrong;
    } catch {
      return {};
    }
  }

  getWrongQuestionIds() {
    const wrongMap = this.getWrongQuestions();
    return Object.keys(wrongMap).map(Number);
  }

  recordWrongQuestion(questionId) {
    const qid = Number(questionId);
    const wrong = { ...this.getWrongQuestions() };
    wrong[qid] = (wrong[qid] || 0) + 1;

    this._cache.wrongQuestions = wrong;
    localStorage.setItem(STORAGE_KEYS.WRONG_QUESTIONS, JSON.stringify(wrong));

    // Save to IndexedDB
    dbService.getQuestionProgress(qid).then((existing) => {
      const attempts = (existing?.attemptsCount || 0) + 1;
      const wrongCount = (existing?.wrongCount || 0) + 1;
      dbService.saveQuestionProgress(qid, {
        status: 'wrong',
        attemptsCount: attempts,
        wrongCount,
        lastAttemptedAt: new Date().toISOString()
      }).catch(() => {});
    }).catch(() => {});

    eventBus.emit('wrongQuestion:updated', { questionId: qid, count: wrong[qid] });
  }

  recordCorrectQuestion(questionId) {
    const qid = Number(questionId);
    const wrong = { ...this.getWrongQuestions() };
    if (wrong[qid]) {
      wrong[qid] -= 1;
      if (wrong[qid] <= 0) {
        delete wrong[qid];
      }
      this._cache.wrongQuestions = wrong;
      localStorage.setItem(STORAGE_KEYS.WRONG_QUESTIONS, JSON.stringify(wrong));
      eventBus.emit('wrongQuestion:updated', { questionId: qid, count: wrong[qid] || 0 });
    }

    dbService.getQuestionProgress(qid).then((existing) => {
      const attempts = (existing?.attemptsCount || 0) + 1;
      const correctCount = (existing?.correctCount || 0) + 1;
      dbService.saveQuestionProgress(qid, {
        status: wrong[qid] ? 'wrong' : 'correct',
        attemptsCount: attempts,
        correctCount,
        lastAttemptedAt: new Date().toISOString()
      }).catch(() => {});
    }).catch(() => {});
  }

  /**
   * Completely removes a question from the wrong list (e.g. when answered correctly in wrong-redo mode)
   */
  removeWrongQuestion(questionId) {
    const qid = Number(questionId);
    const wrong = { ...this.getWrongQuestions() };
    if (wrong[qid] !== undefined) {
      delete wrong[qid];
      this._cache.wrongQuestions = wrong;
      localStorage.setItem(STORAGE_KEYS.WRONG_QUESTIONS, JSON.stringify(wrong));

      // Update in IndexedDB
      dbService.saveQuestionProgress(qid, {
        status: 'correct',
        wrongCount: 0,
        lastAttemptedAt: new Date().toISOString()
      }).catch(() => {});

      eventBus.emit('wrongQuestion:removed', { questionId: qid });
      eventBus.emit('wrongQuestion:updated', { questionId: qid, count: 0 });
      return true;
    }
    return false;
  }

  // --- Exam Cycles (Seen Questions per Exam Mode) ---

  getSeenExamQuestionIds(examType = 'standard') {
    const cacheKey = examType === 'quick' ? 'seenQuick' : 'seenStandard';
    const storageKey = examType === 'quick' ? STORAGE_KEYS.SEEN_QUICK : STORAGE_KEYS.SEEN_STANDARD;

    if (this._cache[cacheKey]) {
      return this._cache[cacheKey];
    }

    try {
      const raw = localStorage.getItem(storageKey);
      const arr = raw ? JSON.parse(raw) : [];
      const idSet = new Set(arr.map(Number));
      this._cache[cacheKey] = idSet;
      return idSet;
    } catch {
      const idSet = new Set();
      this._cache[cacheKey] = idSet;
      return idSet;
    }
  }

  addSeenExamQuestionIds(examType = 'standard', questionIds = []) {
    if (!questionIds || questionIds.length === 0) return;

    const seenSet = this.getSeenExamQuestionIds(examType);
    questionIds.forEach(id => seenSet.add(Number(id)));

    const storageKey = examType === 'quick' ? STORAGE_KEYS.SEEN_QUICK : STORAGE_KEYS.SEEN_STANDARD;
    const arr = Array.from(seenSet);
    localStorage.setItem(storageKey, JSON.stringify(arr));

    // Save to IndexedDB
    dbService.saveExamCycle(examType, arr).catch(() => {});

    eventBus.emit('examCycle:updated', { examType, seenCount: arr.length });
  }

  resetExamCycle(examType = 'standard') {
    const cacheKey = examType === 'quick' ? 'seenQuick' : 'seenStandard';
    const storageKey = examType === 'quick' ? STORAGE_KEYS.SEEN_QUICK : STORAGE_KEYS.SEEN_STANDARD;

    this._cache[cacheKey] = new Set();
    localStorage.removeItem(storageKey);

    // Reset in IndexedDB
    dbService.resetExamCycle(examType).catch(() => {});

    eventBus.emit('examCycle:reset', { examType });
  }

  getCycleStatus(examType = 'standard', totalAvailable = 600) {
    const seenSet = this.getSeenExamQuestionIds(examType);
    const seenCount = seenSet.size;
    const remainingCount = Math.max(0, totalAvailable - seenCount);
    return {
      seenCount,
      totalAvailable,
      remainingCount
    };
  }

  // --- Exam History ---

  getExamHistory() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.EXAM_HISTORY)) || [];
    } catch {
      return [];
    }
  }

  saveExamResult(result) {
    const history = this.getExamHistory();
    const item = {
      id: Date.now(),
      date: new Date().toISOString(),
      score: result.score,
      total: result.total,
      passed: result.passed,
      failedCritical: result.failedCritical,
      durationSeconds: result.durationSeconds,
      wrongQuestionsCount: result.wrongQuestionIds ? result.wrongQuestionIds.length : 0,
      examType: result.examType,
      examTitle: result.examTitle
    };

    history.unshift(item);
    if (history.length > 50) history.pop();
    localStorage.setItem(STORAGE_KEYS.EXAM_HISTORY, JSON.stringify(history));

    // Save to IndexedDB
    dbService.saveExamHistory(item).catch(() => {});

    eventBus.emit('examHistory:saved', history[0]);
  }

  clearExamHistory() {
    localStorage.removeItem(STORAGE_KEYS.EXAM_HISTORY);
    dbService.clearExamHistory().catch(() => {});
    eventBus.emit('examHistory:cleared');
  }
}

export const StorageService = new StorageServiceImpl();
