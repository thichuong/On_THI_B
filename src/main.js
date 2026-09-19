/**
 * Application Entry Point
 * Initializes services, components, router, and keyboard handlers.
 */
import './styles/main.css';
import { header } from './components/Header.js';
import { router } from './core/router.js';
import { keyboardManager } from './utils/keyboard.js';
import { StorageService } from './services/storageService.js';
// Initialize lightbox listener
import './components/LightboxModal.js';
import { $ } from './utils/dom.js';

function initApp() {
  const appMain = $('#app-main');
  if (!appMain) {
    console.error('Root element #app-main not found in DOM');
    return;
  }

  // Initialize persistent storage (IndexedDB + cache)
  StorageService.init();

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

  // Register PWA Service Worker for offline support
  registerServiceWorker();
}

/**
 * Register Service Worker for PWA & Offline caching
 */
function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
        .then((reg) => {
          console.log('[PWA] Service Worker registered with scope:', reg.scope);
        })
        .catch((err) => {
          console.warn('[PWA] Service Worker registration failed:', err);
        });
    });
  }
}

// Kickstart on DOM load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}
