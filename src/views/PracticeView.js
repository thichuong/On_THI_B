/**
 * Practice View: Manages practice modes (Critical 60, Mistakes, Bookmarks)
 */
import { BaseView } from './BaseView.js';
import { store } from '../core/store.js';
import { questionService } from '../services/questionService.js';
import { StorageService } from '../services/storageService.js';
import { QuestionCard } from '../components/QuestionCard.js';
import { QuestionPalette } from '../components/QuestionPalette.js';
import { $, scrollToQuestion } from '../utils/dom.js';

export class PracticeView extends BaseView {
  /**
   * @param {string} mode 'critical' | 'mistakes' | 'bookmarks'
   * @param {string} title
   */
  constructor(mode, title) {
    super(`PracticeView-${mode}`);
    this.mode = mode;
    this.title = title;
    this.questions = [];
  }

  mount(container) {
    this.container = container;
    this.loadQuestions();
    this.render();
  }

  loadQuestions() {
    if (this.mode === 'critical') {
      this.questions = questionService.getCriticalQuestions();
    } else if (this.mode === 'mistakes') {
      const wrongMap = StorageService.getWrongQuestions();
      const wrongIds = Object.keys(wrongMap).map(Number);
      this.questions = questionService.getByIds(wrongIds);
    } else if (this.mode === 'bookmarks') {
      const bookmarkIds = StorageService.getBookmarks();
      this.questions = questionService.getByIds(bookmarkIds);
    }

    const state = store.getState();
    if (state.currentPracticeIndex >= this.questions.length) {
      store.setState({ currentPracticeIndex: 0 });
    }
  }

  render() {
    if (!this.container) return;

    if (this.questions.length === 0) {
      this.renderEmptyState();
      return;
    }

    const state = store.getState();
    const savedScrollTop = QuestionPalette.preserveScroll('.exam-sidebar .palette-grid');

    const curIndex = Math.min(state.currentPracticeIndex, this.questions.length - 1);
    const q = this.questions[curIndex];
    const userAnswer = state.practiceAnswers[q.id];
    const totalQuestions = this.questions.length;

    const questionCardHtml = QuestionCard.render({
      question: q,
      currentIndex: curIndex,
      totalQuestions,
      userAnswer,
      isPractice: true,
      showInstantAnswer: state.showInstantAnswer,
      badgePrefix: this.title
    });

    const paletteHtml = QuestionPalette.render({
      questions: this.questions,
      currentIndex: curIndex,
      answers: state.practiceAnswers,
      isPractice: true,
      title: `Danh sách câu (${totalQuestions})`
    });

    this.container.innerHTML = `
      ${this.mode === 'mistakes' ? `
        <div class="mistakes-header-actions" style="margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem; background: var(--bg-card); padding: 0.85rem 1.25rem; border-radius: var(--radius-lg); border: 1px solid var(--border-color);">
          <div>
            <div style="font-weight: 700; color: #ef4444; display: flex; align-items: center; gap: 0.5rem; font-size: 1rem;">
              <span>❌ Danh sách ${totalQuestions} câu hỏi bạn đã làm sai</span>
            </div>
            <div style="font-size: 0.85rem; color: var(--text-secondary); margin-top: 0.2rem;">
              Ôn tập kỹ từng câu hoặc bấm nút bên cạnh để làm bài thi nhanh 20 câu sai có bấm giờ (làm đúng sẽ xóa khỏi danh sách).
            </div>
          </div>
          <button id="btn-quick-exam-wrong" class="btn-nav" style="background: linear-gradient(135deg, #ef4444, #dc2626); color: #fff; font-weight: 700; border: none; box-shadow: 0 4px 12px rgba(239, 68, 68, 0.35);">
            ⚡ Thi Nhanh 20 Câu Sai Này
          </button>
        </div>
      ` : ''}
      <div class="exam-layout">
        <div id="question-card-wrapper">
          ${questionCardHtml}
        </div>
        <div class="exam-sidebar">
          <div id="palette-wrapper">
            ${paletteHtml}
          </div>
        </div>
      </div>
    `;

    this.bindEvents(q, savedScrollTop);
  }

  renderEmptyState() {
    this.container.innerHTML = `
      <div class="empty-state" style="margin-top: 1rem;">
        <div class="empty-icon">📭</div>
        <h2>Chưa có câu hỏi nào trong danh sách này</h2>
        <p>Hãy làm bài thi hoặc ôn tập các chương để lưu câu hỏi vào đây nhé!</p>
        <button class="btn-nav btn-primary" id="btn-back-to-exam" style="margin-top: 1rem;">
          📝 Làm Đề Thi Thử 30 Câu
        </button>
      </div>
    `;

    $('#btn-back-to-exam', this.container)?.addEventListener('click', () => {
      // Trigger router navigation to 'exam'
      window.dispatchEvent(new CustomEvent('app:navigate', { detail: 'exam' }));
    });
  }

  bindEvents(currentQuestion, savedScrollTop) {
    const state = store.getState();

    // QuestionCard events
    QuestionCard.bindEvents(this.container, {
      onSelectOption: (optNum) => this.selectOption(optNum),
      onPrev: () => this.prevQuestion(),
      onNext: () => this.nextQuestion(),
      onToggleBookmark: () => this.toggleBookmark(currentQuestion.id),
      onResetAnswer: () => this.resetAnswer(currentQuestion.id),
      onToggleInstantAnswer: (checked) => {
        store.setState({ showInstantAnswer: checked });
        this.render();
      },
      image: currentQuestion.image
    });

    // Palette events
    QuestionPalette.bindEvents(this.container, (idx) => {
      store.setState({ currentPracticeIndex: idx });
      this.render();
      scrollToQuestion();
    });

    // Quick exam wrong questions button
    $('#btn-quick-exam-wrong', this.container)?.addEventListener('click', () => {
      window.dispatchEvent(new CustomEvent('app:navigate', {
        detail: { mode: 'quick-exam', subMode: 'retry_wrong' }
      }));
    });

    // Restore scroll position
    QuestionPalette.restoreScroll(savedScrollTop, '.exam-sidebar .palette-grid');
  }

  selectOption(optNum) {
    const state = store.getState();
    const curIndex = Math.min(state.currentPracticeIndex, this.questions.length - 1);
    const q = this.questions[curIndex];
    if (!q) return;

    const newPracticeAnswers = { ...state.practiceAnswers, [q.id]: optNum };
    store.setState({ practiceAnswers: newPracticeAnswers });

    if (optNum !== Number(q.correct_option)) {
      StorageService.recordWrongQuestion(q.id);
    } else {
      StorageService.recordCorrectQuestion(q.id);
    }

    this.render();
  }

  resetAnswer(questionId) {
    const state = store.getState();
    const newAnswers = { ...state.practiceAnswers };
    delete newAnswers[questionId];

    store.setState({ practiceAnswers: newAnswers });
    this.render();
  }

  prevQuestion() {
    const state = store.getState();
    if (state.currentPracticeIndex > 0) {
      store.setState({ currentPracticeIndex: state.currentPracticeIndex - 1 });
      this.render();
      scrollToQuestion();
    }
  }

  nextQuestion() {
    const state = store.getState();
    if (state.currentPracticeIndex < this.questions.length - 1) {
      store.setState({ currentPracticeIndex: state.currentPracticeIndex + 1 });
      this.render();
      scrollToQuestion();
    }
  }

  toggleBookmark(questionId) {
    StorageService.toggleBookmark(questionId);
    if (this.mode === 'bookmarks') {
      this.loadQuestions();
    }
    this.render();
  }

  onKeyboard(key, event) {
    const state = store.getState();
    if (this.questions.length === 0) return;

    const curIndex = Math.min(state.currentPracticeIndex, this.questions.length - 1);
    const currentQ = this.questions[curIndex];

    if (['1', '2', '3', '4'].includes(key)) {
      const optNum = Number(key);
      if (currentQ && optNum <= currentQ.options.length) {
        this.selectOption(optNum);
      }
    }

    if (key === 'ArrowLeft' || key.toLowerCase() === 'a') {
      this.prevQuestion();
    } else if (key === 'ArrowRight' || key.toLowerCase() === 'd') {
      this.nextQuestion();
    }

    if (key.toLowerCase() === 'b' && currentQ) {
      this.toggleBookmark(currentQ.id);
    }

    if (key.toLowerCase() === 'r' && currentQ) {
      this.resetAnswer(currentQ.id);
    }
  }
}

