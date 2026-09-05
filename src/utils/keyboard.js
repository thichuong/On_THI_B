/**
 * Keyboard Shortcuts Manager: Centralized keyboard dispatcher
 */
import { router } from '../core/router.js';
import { lightboxModal } from '../components/LightboxModal.js';
import { resultModal } from '../components/ResultModal.js';
import { confirmModal } from '../components/ConfirmModal.js';

class KeyboardManager {
  constructor() {
    this.boundHandler = this.handleKeyDown.bind(this);
    this.isInitialized = false;
  }

  init() {
    if (this.isInitialized) return;
    window.addEventListener('keydown', this.boundHandler);
    this.isInitialized = true;
  }

  destroy() {
    if (!this.isInitialized) return;
    window.removeEventListener('keydown', this.boundHandler);
    this.isInitialized = false;
  }

  handleKeyDown(e) {
    // Ignore shortcuts when typing in search or input fields
    const targetTag = e.target.tagName;
    if (targetTag === 'INPUT' || targetTag === 'TEXTAREA' || targetTag === 'SELECT') {
      return;
    }

    // Escape handles closing modals
    if (e.key === 'Escape') {
      if (lightboxModal.isOpen()) {
        lightboxModal.close();
        return;
      }
      if (confirmModal.isOpen()) {
        confirmModal.close();
        return;
      }
      if (resultModal.isOpen()) {
        resultModal.close();
        return;
      }
      return;
    }

    // Forward to current active view
    const currentView = router.getCurrentView();
    if (currentView && typeof currentView.onKeyboard === 'function') {
      currentView.onKeyboard(e.key, e);
    }
  }
}

export const keyboardManager = new KeyboardManager();

