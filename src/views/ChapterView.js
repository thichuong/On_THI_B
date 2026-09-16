/**
 * Chapter View: Study and practice questions organized by 6 chapters
 */
import { BaseView } from './BaseView.js';
import { store } from '../core/store.js';
import { questionService, CHAPTERS } from '../services/questionService.js';
import { StorageService } from '../services/storageService.js';
import { QuestionCard } from '../components/QuestionCard.js';
import { QuestionPalette } from '../components/QuestionPalette.js';
import { $, scrollToQuestion } from '../utils/dom.js';

export class ChapterView extends BaseView {
  constructor() {
    super('ChapterView');
    this.questions = [];
  }

  mount(container) {
    this.container = container;
    this.loadChapterQuestions();
    this.render();
  }

  loadChapterQuestions() {
    const state = store.getState();
    this.questions = questionService.getByChapter(state.selectedChapter);
    if (state.currentPracticeIndex >= this.questions.length) {
      store.setState({ currentPracticeIndex: 0 });
    }
  }

  render() {
    if (!this.container) return;
    const state = store.getState();
    const chapterInfo = questionService.getChapterInfo(state.selectedChapter);
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
      badgePrefix: chapterInfo.shortName
    });

    const paletteHtml = QuestionPalette.render({
      questions: this.questions,
      currentIndex: curIndex,
      answers: state.practiceAnswers,
      isPractice: true,
      title: `${chapterInfo.shortName} (${totalQuestions} câu)`
    });

    this.container.innerHTML = `
      <div class="filter-bar">
        <div style="font-weight: 700; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem;">
          <span>📚 Chọn Chương Ôn Tập:</span>
        </div>
        <select id="chapter-select" class="filter-select" style="min-width: 340px;">
          ${CHAPTERS.map(ch => `
            <option value="${ch.id}" ${state.selectedChapter === ch.id ? 'selected' : ''}>
              ${ch.name}
            </option>
          `).join('')}
        </select>
      </div>

      <div class="exam-layout" style="margin-top: 1rem;">
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

  bindEvents(currentQuestion, savedScrollTop) {
    const state = store.getState();

    // Chapter select
    $('#chapter-select', this.container)?.addEventListener('change', (e) => {
      const newChapterId = Number(e.target.value);
      store.setState({
        selectedChapter: newChapterId,
        currentPracticeIndex: 0
      });
      this.loadChapterQuestions();
      this.render();
    });

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

    // Restore scroll
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

