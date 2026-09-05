/**
 * Search Explorer View: Search & filter the entire 600 questions dataset
 */
import { BaseView } from './BaseView.js';
import { store } from '../core/store.js';
import { questionService } from '../services/questionService.js';
import { StorageService } from '../services/storageService.js';
import { eventBus } from '../core/eventBus.js';
import { escapeHtml, $ } from '../utils/dom.js';

export class SearchExplorerView extends BaseView {
  constructor() {
    super('SearchExplorerView');
  }

  mount(container) {
    this.container = container;
    this.render();
  }

  render() {
    if (!this.container) return;
    const state = store.getState();

    const filtered = questionService.search(state.searchQuery, state.filterType);
    const totalWithImages = questionService.getQuestionsWithImages().length;

    this.container.innerHTML = `
      <div class="filter-bar">
        <div class="search-input-wrapper">
          <span class="search-icon">🔍</span>
          <input 
            type="text" 
            id="search-input" 
            class="search-input" 
            placeholder="Tìm kiếm theo từ khóa (nồng độ cồn, biển cấm, ngã tư...) hoặc số câu..." 
            value="${escapeHtml(state.searchQuery)}"
          />
        </div>

        <select id="filter-type-select" class="filter-select">
          <option value="all" ${state.filterType === 'all' ? 'selected' : ''}>Tất cả câu hỏi (600 câu)</option>
          <option value="critical" ${state.filterType === 'critical' ? 'selected' : ''}>⚠️ 60 Câu điểm liệt</option>
          <option value="with_image" ${state.filterType === 'with_image' ? 'selected' : ''}>🖼️ Câu có hình ảnh (${totalWithImages} câu)</option>
        </select>

        <div style="font-size: 0.875rem; color: var(--text-secondary); font-weight: 600;">
          Tìm thấy: ${filtered.length} câu
        </div>
      </div>

      <div class="questions-list" style="margin-top: 1.5rem;">
        ${filtered.length === 0 ? `
          <div class="empty-state">
            <div class="empty-icon">🔍</div>
            <h2>Không tìm thấy câu hỏi phù hợp</h2>
            <p>Hãy thử tìm bằng từ khóa khác hoặc xóa bộ lọc.</p>
          </div>
        ` : filtered.slice(0, 50).map(q => `
          <div class="question-card" style="padding: 1.5rem;">
            <div class="question-header" style="border: none; padding: 0;">
              <div class="question-meta">
                <span class="badge badge-index">Câu ${q.id}</span>
                <span class="badge badge-chapter">Chương ${q.chapter}</span>
                ${q.is_critical ? `<span class="badge badge-critical">⚠️ CÂU ĐIỂM LIỆT</span>` : ''}
              </div>
              <button class="btn-bookmark ${StorageService.isBookmarked(q.id) ? 'active' : ''}" data-bmid="${q.id}">
                <span>${StorageService.isBookmarked(q.id) ? '★ Đã lưu' : '☆ Lưu'}</span>
              </button>
            </div>

            <h3 class="question-title" style="font-size: 1.05rem;">${escapeHtml(q.question)}</h3>

            ${q.image ? `
              <div class="question-image-container" style="max-height: 260px;" data-zoomimg="${q.image}">
                <img src="${q.image}" alt="Câu ${q.id}" class="question-image" style="max-height: 240px;" />
                <div class="zoom-hint" title="Phóng to hình ảnh">🔍</div>
              </div>
            ` : ''}

            <div class="options-list">
              ${q.options.map((opt, idx) => `
                <div class="option-item ${idx + 1 === Number(q.correct_option) ? 'correct' : ''}" style="padding: 0.75rem 1rem;">
                  <span class="option-key">${idx + 1}</span>
                  <span class="option-text" style="font-size: 0.9375rem;">${escapeHtml(opt)}</span>
                </div>
              `).join('')}
            </div>
          </div>
        `).join('')}

        ${filtered.length > 50 ? `
          <div style="text-align: center; padding: 1rem; color: var(--text-muted); font-size: 0.875rem;">
            Đang hiển thị 50 câu đầu tiên. Vui lòng nhập từ khóa tìm kiếm để thu hẹp kết quả.
          </div>
        ` : ''}
      </div>
    `;

    this.bindEvents();
  }

  bindEvents() {
    // Search input
    const searchInp = $('#search-input', this.container);
    if (searchInp) {
      searchInp.addEventListener('input', (e) => {
        store.setState({ searchQuery: e.target.value });
        this.render();
        // Restore focus and cursor to the end
        const newInp = $('#search-input', this.container);
        if (newInp) {
          newInp.focus();
          newInp.setSelectionRange(newInp.value.length, newInp.value.length);
        }
      });
    }

    // Filter select
    const filterSel = $('#filter-type-select', this.container);
    if (filterSel) {
      filterSel.addEventListener('change', (e) => {
        store.setState({ filterType: e.target.value });
        this.render();
      });
    }

    // Bookmark buttons
    this.container.querySelectorAll('[data-bmid]').forEach(btn => {
      btn.addEventListener('click', () => {
        const qid = Number(btn.dataset.bmid);
        const isBm = StorageService.toggleBookmark(qid);
        btn.classList.toggle('active', isBm);
        btn.innerHTML = `<span>${isBm ? '★ Đã lưu' : '☆ Lưu'}</span>`;
      });
    });

    // Image zoom Lightbox
    this.container.querySelectorAll('[data-zoomimg]').forEach(wrap => {
      wrap.addEventListener('click', () => {
        eventBus.emit('lightbox:open', wrap.dataset.zoomimg);
      });
    });
  }
}

