/**
 * Simple Event Bus for inter-component communication
 */
class EventBus {
  constructor() {
    this.listeners = new Map();
  }

  /**
   * Subscribe to an event
   * @param {string} event
   * @param {Function} handler
   * @returns {Function} unsubscribe function
   */
  on(event, handler) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, new Set());
    }
    this.listeners.get(event).add(handler);

    return () => this.off(event, handler);
  }

  /**
   * Unsubscribe from an event
   * @param {string} event
   * @param {Function} handler
   */
  off(event, handler) {
    if (this.listeners.has(event)) {
      this.listeners.get(event).delete(handler);
      if (this.listeners.get(event).size === 0) {
        this.listeners.delete(event);
      }
    }
  }

  /**
   * Emit an event with optional data
   * @param {string} event
   * @param {*} [data]
   */
  emit(event, data) {
    if (this.listeners.has(event)) {
      this.listeners.get(event).forEach(handler => {
        try {
          handler(data);
        } catch (err) {
          console.error(`Error in event handler for "${event}":`, err);
        }
      });
    }
  }

  /**
   * Listen to an event once
   * @param {string} event
   * @param {Function} handler
   */
  once(event, handler) {
    const unsub = this.on(event, (data) => {
      unsub();
      handler(data);
    });
  }
}

export const eventBus = new EventBus();

