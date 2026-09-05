/**
 * Confirm Modal: Confirmation dialog before submitting exam with unanswered questions
 */
import { $ } from '../utils/dom.js';

export class ConfirmModal {
  constructor() {
    this.modalEl = document.getElementById('result-modal');
  }

  /**
   * Show confirmation dialog
   * @param {number} unattemptedCount
   * @param {Object} callbacks
   * @param {Function} callbacks.onConfirm
   * @param {Function} [callbacks.onCancel]
   */
  show(unattemptedCount, { onConfirm, onCancel }) {
    if (!this.modalEl) return;

    this.modalEl.innerHTML = `
      <div class="modal-content" style="max-width: 440px;">
        <div style="font-size: 3rem;">⚠️</div>
        <h2 style="font-size: 1.25rem; font-weight: 700; color: var(--warning);">Bạn còn ${unattemptedCount} câu chưa trả lời</h2>
        <p class="result-message" style="margin: 0.5rem 0;">
          Các câu hỏi chưa làm sẽ được tính là sai. Bạn có chắc chắn muốn nộp bài thi ngay bây giờ?
        </p>
        <div class="modal-actions" style="margin-top: 1rem;">
          <button class="btn-nav" id="btn-cancel-submit" style="flex: 1;">
            ✏️ Làm Tiếp
          </button>
          <button class="btn-nav btn-primary" id="btn-confirm-submit" style="flex: 1; background: var(--danger); border-color: var(--danger);">
            📤 Nộp Bài Luôn
          </button>
        </div>
      </div>
    `;

    this.modalEl.classList.add('show');
    this.modalEl.setAttribute('aria-hidden', 'false');

    const cancelBtn = $('#btn-cancel-submit', this.modalEl);
    const confirmBtn = $('#btn-confirm-submit', this.modalEl);

    cancelBtn?.addEventListener('click', () => {
      this.close();
      if (typeof onCancel === 'function') onCancel();
    });

    confirmBtn?.addEventListener('click', () => {
      this.close();
      if (typeof onConfirm === 'function') onConfirm();
    });
  }

  close() {
    if (!this.modalEl) return;
    this.modalEl.classList.remove('show');
    this.modalEl.setAttribute('aria-hidden', 'true');
    this.modalEl.innerHTML = '';
  }

  isOpen() {
    return this.modalEl ? this.modalEl.classList.contains('show') : false;
  }
}

export const confirmModal = new ConfirmModal();

