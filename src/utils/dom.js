/**
 * DOM Utility Helpers
 */

/**
 * Escape HTML characters to prevent XSS.
 * @param {string} str
 * @returns {string}
 */
export function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

/**
 * Shortcut to query an element by selector.
 * @param {string} selector
 * @param {Element|Document} [context=document]
 * @returns {Element|null}
 */
export function $(selector, context = document) {
  return context.querySelector(selector);
}

/**
 * Shortcut to query all elements by selector.
 * @param {string} selector
 * @param {Element|Document} [context=document]
 * @returns {NodeListOf<Element>}
 */
export function $$(selector, context = document) {
  return context.querySelectorAll(selector);
}

/**
 * Smoothly scrolls the viewport to the question card, taking into account
 * the sticky app header height.
 * @param {boolean} [smooth=true]
 */
export function scrollToQuestion(smooth = true) {
  if (typeof window === 'undefined') return;
  const target = document.getElementById('question-card-wrapper') || document.querySelector('.question-card');
  if (!target) return;

  const header = document.querySelector('.app-header');
  const headerHeight = header ? header.getBoundingClientRect().height : 0;
  const targetTop = target.getBoundingClientRect().top + window.pageYOffset;
  const offsetPosition = Math.max(0, targetTop - headerHeight - 12);

  window.scrollTo({
    top: offsetPosition,
    behavior: smooth ? 'smooth' : 'auto'
  });
}


