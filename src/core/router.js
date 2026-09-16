/**
 * Router: View navigation controller managing mount and unmount lifecycles
 */
import { store } from './store.js';
import { header } from '../components/Header.js';
import { ExamView } from '../views/ExamView.js';
import { PracticeView } from '../views/PracticeView.js';
import { ChapterView } from '../views/ChapterView.js';
import { SearchExplorerView } from '../views/SearchExplorerView.js';

class Router {
  constructor() {
    this.container = null;
    this.currentView = null;
    this.currentMode = null;
    this.routes = new Map();
  }

  /**
   * Initialize router with container element
   * @param {HTMLElement} container
   */
  init(container) {
    this.container = container;

    // Register standard routes
    this.register('exam', () => new ExamView('standard'));
    this.register('quick-exam', (subMode) => new ExamView('quick', subMode || 'new'));
    this.register('critical', () => new PracticeView('critical', '60 Câu Hỏi Điểm Liệt (Bắt Buộc Đúng)'));
    this.register('chapter', () => new ChapterView());
    this.register('all', () => new SearchExplorerView());
    this.register('mistakes', () => new PracticeView('mistakes', 'Danh Sách Câu Làm Sai Cần Ôn Lại'));
    this.register('bookmarks', () => new PracticeView('bookmarks', 'Câu Hỏi Đã Đánh Dấu Ghi Nhớ'));

    // Listen to custom navigation events
    window.addEventListener('app:navigate', (e) => {
      if (e.detail) {
        this.navigate(e.detail);
      }
    });
  }

  /**
   * Register a view factory for a mode
   * @param {string} mode
   * @param {Function} viewFactory
   */
  register(mode, viewFactory) {
    this.routes.set(mode, viewFactory);
  }

  /**
   * Navigate to a mode
   * @param {string|Object} target mode name or { mode, subMode }
   * @param {Object} [params={}]
   */
  navigate(target, params = {}) {
    let mode = typeof target === 'object' ? target.mode : target;
    const subMode = typeof target === 'object' ? target.subMode : (params.subMode || null);

    if (!this.routes.has(mode)) {
      console.warn(`Unknown mode: "${mode}", falling back to "exam"`);
      mode = 'exam';
    }

    // If same mode and view is already mounted, re-render or update subMode
    if (this.currentMode === mode && this.currentView) {
      if (subMode && typeof this.currentView.setSubMode === 'function') {
        this.currentView.setSubMode(subMode);
      } else {
        this.currentView.render();
      }
      return;
    }

    // Unmount current view
    if (this.currentView) {
      this.currentView.unmount();
      this.currentView = null;
    }

    this.currentMode = mode;
    store.setState({ currentMode: mode });

    // Update active tab in header
    header.setActiveTab(mode);

    // Create and mount new view
    const viewFactory = this.routes.get(mode);
    this.currentView = viewFactory(subMode);
    this.currentView.mount(this.container);
  }

  getCurrentView() {
    return this.currentView;
  }

  getCurrentMode() {
    return this.currentMode;
  }
}

export const router = new Router();

