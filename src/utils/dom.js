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

