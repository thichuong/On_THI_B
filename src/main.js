/**
 * Application Entry Point
 * Initializes services, components, router, and keyboard handlers.
 */
import './styles/main.css';
import { header } from './components/Header.js';
import { router } from './core/router.js';
import { keyboardManager } from './utils/keyboard.js';
// Initialize lightbox listener
import './components/LightboxModal.js';
import { $ } from './utils/dom.js';

function initApp() {
  const appMain = $('#app-main');
  if (!appMain) {
    console.error('Root element #app-main not found in DOM');
    return;
  }

  // Initialize header navigation and theme toggle
  header.init({
    onModeChange: (mode) => router.navigate(mode)
  });

  // Initialize router with main container
  router.init(appMain);

  // Initialize centralized keyboard shortcut manager
  keyboardManager.init();

  // Start with default mode (Standard Mock Exam)
  router.navigate('exam');
}

// Kickstart on DOM load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}
