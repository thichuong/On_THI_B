/**
 * Central Reactive Application Store
 */
import { eventBus } from './eventBus.js';

class Store {
  constructor() {
    this.state = {
      currentMode: 'exam',
      examType: 'standard', // 'standard' (50 câu) | 'quick' (20 câu)

      // Exam state
      isExamStarted: false,
      isExamSubmitted: false,
      isReviewMode: false,
      examQuestions: [],
      currentExamIndex: 0,
      userAnswers: {},
      examResult: null,

      // Practice state
      selectedChapter: 1,
      currentPracticeIndex: 0,
      practiceAnswers: {},
      showInstantAnswer: false,

      // Search state
      searchQuery: '',
      filterType: 'all'
    };

    this.listeners = new Set();
  }

  getState() {
    return this.state;
  }

  /**
   * Update state with shallow merge and notify listeners
   * @param {Object} partialState
   */
  setState(partialState) {
    const prevState = { ...this.state };
    this.state = { ...this.state, ...partialState };

    this.listeners.forEach(listener => {
      try {
        listener(this.state, prevState);
      } catch (err) {
        console.error('Error in store listener:', err);
      }
    });

    eventBus.emit('store:updated', { state: this.state, prevState });
  }

  /**
   * Subscribe to state changes
   * @param {Function} listener
   * @returns {Function} unsubscribe function
   */
  subscribe(listener) {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  /**
   * Select a slice of state and only notify when that slice changes
   * @param {Function} selector
   * @param {Function} callback
   * @returns {Function} unsubscribe function
   */
  select(selector, callback) {
    let currentSlice = selector(this.state);
    return this.subscribe((nextState) => {
      const nextSlice = selector(nextState);
      if (nextSlice !== currentSlice) {
        const prevSlice = currentSlice;
        currentSlice = nextSlice;
        callback(nextSlice, prevSlice);
      }
    });
  }
}

export const store = new Store();

