/**
 * Storage Service: Manages persistence for theme, bookmarks, wrong answers, and exam history.
 */
import { eventBus } from '../core/eventBus.js';

const STORAGE_KEYS = {
  THEME: 'gplx_theme',
  BOOKMARKS: 'gplx_bookmarks',
  WRONG_QUESTIONS: 'gplx_wrong_questions',
  EXAM_HISTORY: 'gplx_exam_history',
  SETTINGS: 'gplx_settings'
};

export const StorageService = {
  getTheme() {
    return localStorage.getItem(STORAGE_KEYS.THEME) || 'dark';
  },

  setTheme(theme) {
    localStorage.setItem(STORAGE_KEYS.THEME, theme);
    eventBus.emit('theme:changed', theme);
  },

  getBookmarks() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.BOOKMARKS)) || [];
    } catch {
      return [];
    }
  },

  toggleBookmark(questionId) {
    const bookmarks = this.getBookmarks();
    const index = bookmarks.indexOf(questionId);
    let isBookmarked;
    if (index === -1) {
      bookmarks.push(questionId);
      isBookmarked = true;
    } else {
      bookmarks.splice(index, 1);
      isBookmarked = false;
    }
    localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bookmarks));
    eventBus.emit('bookmark:changed', { questionId, isBookmarked, bookmarks });
    return isBookmarked;
  },

  isBookmarked(questionId) {
    return this.getBookmarks().includes(questionId);
  },

  getWrongQuestions() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.WRONG_QUESTIONS)) || {};
    } catch {
      return {};
    }
  },

  recordWrongQuestion(questionId) {
    const wrong = this.getWrongQuestions();
    wrong[questionId] = (wrong[questionId] || 0) + 1;
    localStorage.setItem(STORAGE_KEYS.WRONG_QUESTIONS, JSON.stringify(wrong));
    eventBus.emit('wrongQuestion:updated', { questionId, count: wrong[questionId] });
  },

  recordCorrectQuestion(questionId) {
    const wrong = this.getWrongQuestions();
    if (wrong[questionId]) {
      wrong[questionId] -= 1;
      if (wrong[questionId] <= 0) {
        delete wrong[questionId];
      }
      localStorage.setItem(STORAGE_KEYS.WRONG_QUESTIONS, JSON.stringify(wrong));
      eventBus.emit('wrongQuestion:updated', { questionId, count: wrong[questionId] || 0 });
    }
  },

  getExamHistory() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.EXAM_HISTORY)) || [];
    } catch {
      return [];
    }
  },

  saveExamResult(result) {
    const history = this.getExamHistory();
    history.unshift({
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
    });
    // Keep last 50 tests
    if (history.length > 50) history.pop();
    localStorage.setItem(STORAGE_KEYS.EXAM_HISTORY, JSON.stringify(history));
    eventBus.emit('examHistory:saved', history[0]);
  },

  clearExamHistory() {
    localStorage.removeItem(STORAGE_KEYS.EXAM_HISTORY);
    eventBus.emit('examHistory:cleared');
  }
};

