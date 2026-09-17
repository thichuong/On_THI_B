/**
 * Confirm Modal: Confirmation dialog before submitting exam with unanswered questions
 */
import { $ } from '../utils/dom.js';

export class ConfirmModal {
  constructor() {
    this.modalEl = document.getElementById('result-modal');
  }

  /**
   * Show custom confirmation dialog
   * @param {Object} options
   * @param {string} options.title
   * @param {string} options.message
   * @param {string} [options.icon='⚠️']
   * @param {string} [options.confirmText='Xác Nhận']
   * @param {string} [options.cancelText='Hủy Bỏ']
   * @param {string} [options.confirmBtnClass='']
   * @param {Function} options.onConfirm
   * @param {Function} [options.onCancel]
   */
  showConfirmation({
    title,
    message,
    icon = '⚠️',
    confirmText = 'Xác Nhận',
    cancelText = 'Hủy Bỏ',
    confirmBtnClass = '',
    onConfirm,
    onCancel
  }) {
    if (!this.modalEl) return;

    this.modalEl.innerHTML = `
      <div class="modal-content" style="max-width: 440px;">
        <div style="font-size: 3rem;">${icon}</div>
        <h2 style="font-size: 1.25rem; font-weight: 700; color: var(--warning);">${title}</h2>
        <p class="result-message" style="margin: 0.5rem 0;">
          ${message}
        </p>
        <div class="modal-actions" style="margin-top: 1rem;">
          <button class="btn-nav" id="btn-cancel-submit" style="flex: 1;">
            ${cancelText}
          </button>
          <button class="btn-nav btn-primary ${confirmBtnClass}" id="btn-confirm-submit" style="flex: 1; background: var(--danger); border-color: var(--danger);">
            ${confirmText}
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

  /**
   * Show confirmation dialog before submitting exam
   * @param {number} unattemptedCount
   * @param {Object} callbacks
   * @param {Function} callbacks.onConfirm
   * @param {Function} [callbacks.onCancel]
   */
  show(unattemptedCount, { onConfirm, onCancel }) {
    this.showConfirmation({
      title: `Bạn còn ${unattemptedCount} câu chưa trả lời`,
      message: 'Các câu hỏi chưa làm sẽ được tính là sai. Bạn có chắc chắn muốn nộp bài thi ngay bây giờ?',
      icon: '⚠️',
      cancelText: '✏️ Làm Tiếp',
      confirmText: '📤 Nộp Bài Luôn',
      onConfirm,
      onCancel
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

