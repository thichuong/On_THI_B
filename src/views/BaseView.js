/**
 * Base View Class: Standardizes lifecycle for all page views
 */
export class BaseView {
  constructor(name) {
    this.name = name;
    this.container = null;
    this.unsubscribers = [];
  }

  /**
   * Mount the view into a container element
   * @param {HTMLElement} container
   */
  mount(container) {
    this.container = container;
    this.render();
  }

  /**
   * Render the view content (must be implemented by subclass)
   */
  render() {
    throw new Error(`Render method not implemented in ${this.name}`);
  }

  /**
   * Unmount the view and cleanup resources
   */
  unmount() {
    this.unsubscribers.forEach(unsub => {
      if (typeof unsub === 'function') unsub();
    });
    this.unsubscribers = [];

    if (this.container) {
      this.container.innerHTML = '';
      this.container = null;
    }
  }

  /**
   * Handle keyboard shortcut when view is active
   * @param {string} key
   * @param {KeyboardEvent} event
   */
  onKeyboard(key, event) {
    // Override in subclass if view handles shortcuts
  }

  /**
   * Register a cleanup function to be executed on unmount
   * @param {Function} cleanupFn
   */
  registerCleanup(cleanupFn) {
    this.unsubscribers.push(cleanupFn);
  }
}

