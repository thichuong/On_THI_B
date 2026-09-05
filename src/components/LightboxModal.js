/**
 * Lightbox Modal: Fullscreen image zoom
 */
import { eventBus } from '../core/eventBus.js';

export class LightboxModal {
  constructor() {
    this.modalEl = document.getElementById('lightbox-modal');
    this.imgEl = document.getElementById('lightbox-img');
    this.closeBtn = document.getElementById('close-lightbox-btn');

    this._bindEvents();

    // Listen to global open event
    eventBus.on('lightbox:open', (src) => this.open(src));
  }

  _bindEvents() {
    if (this.closeBtn) {
      this.closeBtn.addEventListener('click', () => this.close());
    }

    if (this.modalEl) {
      this.modalEl.addEventListener('click', (e) => {
        if (e.target === this.modalEl) {
          this.close();
        }
      });
    }
  }

  open(src) {
    if (!src || !this.imgEl || !this.modalEl) return;
    this.imgEl.src = src;
    this.modalEl.classList.add('show');
    this.modalEl.setAttribute('aria-hidden', 'false');
  }

  close() {
    if (!this.modalEl) return;
    this.modalEl.classList.remove('show');
    this.modalEl.setAttribute('aria-hidden', 'true');
  }

  isOpen() {
    return this.modalEl ? this.modalEl.classList.contains('show') : false;
  }
}

export const lightboxModal = new LightboxModal();

