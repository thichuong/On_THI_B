/**
 * Header Component: Top navbar with brand, mode navigation tabs, and theme toggle
 */
import { StorageService } from '../services/storageService.js';
import { $, $$ } from '../utils/dom.js';

export class Header {
  constructor() {
    this.headerEl = document.querySelector('.app-header');
    this.themeToggleBtn = $('#theme-toggle-btn');
    this.themeIcon = $('#theme-icon');
    this.navTabs = $$('.tab-btn');
    this.onModeChangeCallback = null;
  }

  init({ onModeChange } = {}) {
    this.onModeChangeCallback = onModeChange;
    this._initTheme();
    this._bindEvents();
  }

  _initTheme() {
    const savedTheme = StorageService.getTheme();
    document.documentElement.setAttribute('data-theme', savedTheme);
    this.updateThemeIcon(savedTheme);
  }

  _bindEvents() {
    // Theme toggle
    this.themeToggleBtn?.addEventListener('click', () => {
      this.toggleTheme();
    });

    // Nav tabs
    this.navTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const mode = tab.dataset.mode;
        if (typeof this.onModeChangeCallback === 'function') {
          this.onModeChangeCallback(mode);
        }
      });
    });
  }

  toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    StorageService.setTheme(newTheme);
    this.updateThemeIcon(newTheme);
  }

  updateThemeIcon(theme) {
    if (this.themeIcon) {
      this.themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
    }
  }

  setActiveTab(mode) {
    this.navTabs.forEach(tab => {
      const isActive = tab.dataset.mode === mode;
      tab.classList.toggle('active', isActive);
      if (isActive) {
        tab.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' });
      }
    });
  }
}

export const header = new Header();

