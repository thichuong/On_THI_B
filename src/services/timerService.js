/**
 * Timer Service: Handles countdown timers with ticks, formatted strings, and event emission.
 */
import { eventBus } from '../core/eventBus.js';

export class TimerService {
  constructor() {
    this.intervalId = null;
    this.totalSeconds = 0;
    this.remainingSeconds = 0;
    this.isRunning = false;
  }

  /**
   * Start a new countdown timer
   * @param {number} seconds
   * @param {Object} [options]
   * @param {Function} [options.onTick]
   * @param {Function} [options.onTimeout]
   */
  start(seconds, { onTick = null, onTimeout = null } = {}) {
    this.stop();

    this.totalSeconds = seconds;
    this.remainingSeconds = seconds;
    this.isRunning = true;
    this.onTickCallback = onTick;
    this.onTimeoutCallback = onTimeout;

    // Trigger initial tick
    this._handleTick();

    this.intervalId = setInterval(() => {
      this.remainingSeconds--;
      this._handleTick();

      if (this.remainingSeconds <= 0) {
        this.stop();
        if (typeof this.onTimeoutCallback === 'function') {
          this.onTimeoutCallback();
        }
        eventBus.emit('timer:timeout');
      }
    }, 1000);
  }

  _handleTick() {
    const data = {
      remainingSeconds: this.remainingSeconds,
      totalSeconds: this.totalSeconds,
      formatted: TimerService.formatTime(this.remainingSeconds),
      status: this.getStatus()
    };

    if (typeof this.onTickCallback === 'function') {
      this.onTickCallback(data);
    }
    eventBus.emit('timer:tick', data);
  }

  /**
   * Stop and clear the timer
   */
  stop() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
    this.isRunning = false;
  }

  /**
   * Get status based on remaining time
   * @returns {'danger' | 'warning' | 'normal'}
   */
  getStatus() {
    if (this.remainingSeconds <= 120) return 'danger';
    if (this.remainingSeconds <= 300) return 'warning';
    return 'normal';
  }

  getRemaining() {
    return this.remainingSeconds;
  }

  getElapsed() {
    return Math.max(0, this.totalSeconds - this.remainingSeconds);
  }

  /**
   * Format seconds to mm:ss
   * @param {number} seconds
   * @returns {string}
   */
  static formatTime(seconds) {
    const s = Math.max(0, seconds);
    const minutes = Math.floor(s / 60);
    const remainingSec = s % 60;
    return `${String(minutes).padStart(2, '0')}:${String(remainingSec).padStart(2, '0')}`;
  }
}

