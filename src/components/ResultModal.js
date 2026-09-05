/**
 * Result Modal: Displays exam score, pass/fail status, and actions to review or retake.
 */
import { $ } from '../utils/dom.js';

export class ResultModal {
  constructor() {
    this.modalEl = document.getElementById('result-modal');
  }

  /**
   * Show the exam results modal
   * @param {Object} result
   * @param {Object} preset
   * @param {Object} callbacks
   * @param {Function} callbacks.onReview
   * @param {Function} callbacks.onRetry
   */
  show(result, preset, { onReview, onRetry }) {
    if (!this.modalEl || !result) return;

    const isPassed = result.passed;
    let statusHtml = '';

    if (isPassed) {
      statusHtml = `
        <div class="result-status-badge passed">
          <span>🎉 ĐẠT (${preset.shortName.toUpperCase()})</span>
        </div>
        <p class="result-message">
          Chúc mừng! Bạn đã hoàn thành xuất sắc bài thi với <strong>${result.score}/${result.total}</strong> điểm! (Yêu cầu đạt tối thiểu ${result.passThreshold}/${result.total} điểm).
        </p>
      `;
    } else {
      let failReason = `Chưa đủ điểm đạt chuẩn (${result.score}/${result.total} - yêu cầu tối thiểu ${result.passThreshold}/${result.total} điểm).`;
      if (result.failedCritical) {
        failReason = `❌ <strong>RỚT TRỰC TIẾP DO SAI CÂU ĐIỂM LIỆT!</strong><br/>Bạn đã trả lời sai câu điểm liệt bắt buộc (Câu ${result.failedCriticalQuestions.map(q => q.id).join(', ')}).`;
      }

      statusHtml = `
        <div class="result-status-badge failed">
          <span>❌ KHÔNG ĐẠT</span>
        </div>
        <p class="result-message" style="color: #f87171;">
          ${failReason}
        </p>
      `;
    }

    this.modalEl.innerHTML = `
      <div class="modal-content">
        ${statusHtml}

        <div class="score-circle" style="border-color: ${isPassed ? '#10b981' : '#ef4444'}; box-shadow: 0 0 24px ${isPassed ? 'rgba(16, 185, 129, 0.4)' : 'rgba(239, 68, 68, 0.4)'};">
          <span class="score-num" style="color: ${isPassed ? '#10b981' : '#ef4444'};">${result.score}</span>
          <span class="score-total">/ ${result.total} ĐIỂM</span>
        </div>

        <div class="result-stats-grid">
          <div class="result-stat-box">
            <span class="result-stat-val" style="color: #10b981;">${result.score}</span>
            <span class="result-stat-lbl">Số câu đúng</span>
          </div>
          <div class="result-stat-box">
            <span class="result-stat-val" style="color: #ef4444;">${result.wrongCount}</span>
            <span class="result-stat-lbl">Số câu sai</span>
          </div>
          <div class="result-stat-box">
            <span class="result-stat-val" style="color: #94a3b8;">${result.unattemptedCount}</span>
            <span class="result-stat-lbl">Chưa làm</span>
          </div>
        </div>

        <div class="modal-actions">
          <button class="btn-nav btn-primary" id="btn-review-test">
            🔍 Xem Lại Bài Thi Chi Tiết
          </button>
          <button class="btn-nav" id="btn-new-exam-modal">
            🔄 Thi Đề Khác (Trộn ${result.total} câu mới)
          </button>
        </div>
      </div>
    `;

    this.modalEl.classList.add('show');
    this.modalEl.setAttribute('aria-hidden', 'false');

    $('#btn-review-test', this.modalEl)?.addEventListener('click', () => {
      this.close();
      if (typeof onReview === 'function') onReview();
    });

    $('#btn-new-exam-modal', this.modalEl)?.addEventListener('click', () => {
      this.close();
      if (typeof onRetry === 'function') onRetry();
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

export const resultModal = new ResultModal();

