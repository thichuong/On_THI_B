/**
 * Storage Manager for saving history, bookmarks, and wrong answers.
 */

const STORAGE_KEYS = {
  THEME: 'gplx_theme',
  BOOKMARKS: 'gplx_bookmarks',
  WRONG_QUESTIONS: 'gplx_wrong_questions',
  EXAM_HISTORY: 'gplx_exam_history',
  SETTINGS: 'gplx_settings'
};

export const Storage = {
  getTheme() {
    return localStorage.getItem(STORAGE_KEYS.THEME) || 'dark';
  },

  setTheme(theme) {
    localStorage.setItem(STORAGE_KEYS.THEME, theme);
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
    if (index === -1) {
      bookmarks.push(questionId);
    } else {
      bookmarks.splice(index, 1);
    }
    localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bookmarks));
    return bookmarks.includes(questionId);
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
  },

  recordCorrectQuestion(questionId) {
    const wrong = this.getWrongQuestions();
    if (wrong[questionId]) {
      wrong[questionId] -= 1;
      if (wrong[questionId] <= 0) {
        delete wrong[questionId];
      }
      localStorage.setItem(STORAGE_KEYS.WRONG_QUESTIONS, JSON.stringify(wrong));
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
      wrongQuestionsCount: result.wrongQuestionIds.length
    });
    // Keep last 50 tests
    if (history.length > 50) history.pop();
    localStorage.setItem(STORAGE_KEYS.EXAM_HISTORY, JSON.stringify(history));
  }
};
