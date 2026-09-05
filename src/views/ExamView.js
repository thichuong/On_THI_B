/**
 * Exam View: Manages mock tests (50-question standard & 20-question quick)
 */
import { BaseView } from './BaseView.js';
import { store } from '../core/store.js';
import { questionService } from '../services/questionService.js';
import { ExamEngine, EXAM_PRESETS } from '../services/examEngine.js';
import { StorageService } from '../services/storageService.js';
import { TimerService } from '../services/timerService.js';
import { QuestionCard } from '../components/QuestionCard.js';
import { QuestionPalette } from '../components/QuestionPalette.js';
import { confirmModal } from '../components/ConfirmModal.js';
import { resultModal } from '../components/ResultModal.js';
import { $ } from '../utils/dom.js';

export class ExamView extends BaseView {
  constructor(examType = 'standard') {
    super(`ExamView-${examType}`);
    this.examType = examType; // 'standard' | 'quick'
    this.timer = new TimerService();
  }

  mount(container) {
    this.container = container;
    const currentState = store.getState();

    // If starting a different exam type or exam hasn't started, prepare
    if (currentState.examType !== this.examType || !currentState.isExamStarted) {
      this.prepareExam();
    } else {
      this.render();
    }
  }

  prepareExam() {
    this.timer.stop();
    const preset = EXAM_PRESETS[this.examType] || EXAM_PRESETS.standard;

    store.setState({
      examType: this.examType,
      isExamStarted: false,
      isExamSubmitted: false,
      isReviewMode: false,
      examResult: null,
      examQuestions: [],
      currentExamIndex: 0,
      userAnswers: {}
    });

    this.render();
  }

  beginExam() {
    this.timer.stop();
    const preset = EXAM_PRESETS[this.examType] || EXAM_PRESETS.standard;
    const allQuestions = questionService.getAll();

    const questions = ExamEngine.generateExam(allQuestions, this.examType, {
      minCritical: preset.minCritical,
      maxCritical: preset.maxCritical,
      shuffleQuestions: true
    });

    store.setState({
      examType: this.examType,
      examQuestions: questions,
      currentExamIndex: 0,
      userAnswers: {},
      isExamStarted: true,
      isExamSubmitted: false,
      isReviewMode: false,
      examResult: null
    });

    // Start timer
    this.timer.start(preset.durationSeconds, {
      onTick: (timerData) => this.updateTimerUI(timerData),
      onTimeout: () => this.finalizeSubmission()
    });

    this.render();
  }

  updateTimerUI({ formatted, status }) {
    const timerElem = $('#timer-val', this.container);
    if (!timerElem) return;

    timerElem.textContent = formatted;
    timerElem.className = `timer-display ${status !== 'normal' ? status : ''}`;
  }

  render() {
    if (!this.container) return;
    const state = store.getState();

    if (!state.isExamStarted) {
      this.renderStartScreen();
      return;
    }

    if (state.examQuestions.length === 0) return;

    const savedScrollTop = QuestionPalette.preserveScroll('.exam-sidebar .palette-grid');

    const q = state.examQuestions[state.currentExamIndex];
    const userAnswer = state.userAnswers[q.id];
    const totalQuestions = state.examQuestions.length;
    const preset = EXAM_PRESETS[this.examType] || EXAM_PRESETS.standard;

    const isQuick = this.examType === 'quick';
    const examBadgeText = isQuick ? '⚡ THI NHANH (20 CÂU / 10 PHÚT)' : '📝 THI THỬ CHUẨN (50 CÂU / 33 PHÚT)';
    const examBadgeStyle = isQuick
      ? 'background: rgba(245, 158, 11, 0.2); color: #f59e0b; border-color: rgba(245, 158, 11, 0.4);'
      : 'background: rgba(99, 102, 241, 0.2); color: #818cf8; border-color: rgba(99, 102, 241, 0.4);';

    const questionCardHtml = QuestionCard.render({
      question: q,
      currentIndex: state.currentExamIndex,
      totalQuestions,
      userAnswer,
      isSubmitted: state.isExamSubmitted,
      isReviewMode: state.isReviewMode,
      isPractice: false,
      badgePrefix: examBadgeText,
      badgeStyle: examBadgeStyle
    });

    const paletteHtml = QuestionPalette.render({
      questions: state.examQuestions,
      currentIndex: state.currentExamIndex,
      answers: state.userAnswers,
      isSubmitted: state.isExamSubmitted,
      isPractice: false,
      title: `Danh sách ${totalQuestions} câu`
    });

    const timeStr = TimerService.formatTime(this.timer.getRemaining());

    this.container.innerHTML = `
      <div class="exam-layout">
        <!-- Question Area -->
        <div id="question-card-wrapper">
          ${questionCardHtml}
        </div>

        <!-- Right Exam Sidebar -->
        <div class="exam-sidebar">
          <div class="sidebar-card">
            <div class="timer-widget">
              <div class="timer-label">
                <span>⏱️ Thời gian:</span>
              </div>
              <div id="timer-val" class="timer-display ${this.timer.getStatus() !== 'normal' ? this.timer.getStatus() : ''}">
                ${timeStr}
              </div>
            </div>

            ${state.isExamSubmitted ? `
              <button class="btn-submit-exam" id="btn-retry-exam" style="background: linear-gradient(135deg, #6366f1, #4f46e5);">
                🔄 Thi Đề Mới (Trộn ${totalQuestions} câu)
              </button>
            ` : `
              <button class="btn-submit-exam" id="btn-submit-test">
                📤 Nộp Bài Thi ${isQuick ? 'Nhanh' : 'Sát Hạch'}
              </button>
            `}
          </div>

          <div id="palette-wrapper">
            ${paletteHtml}
          </div>
        </div>
      </div>
    `;

    this.bindActiveExamEvents(q, savedScrollTop);
  }

  renderStartScreen() {
    const isQuick = this.examType === 'quick';
    const preset = EXAM_PRESETS[this.examType] || EXAM_PRESETS.standard;

    this.container.innerHTML = `
      <div class="exam-start-container">
        <div class="exam-start-card">
          <div class="exam-start-header">
            <div class="exam-start-icon">
              ${isQuick ? '⚡' : '📝'}
            </div>
            <div class="badge badge-index" style="${isQuick ? 'background: rgba(245, 158, 11, 0.2); color: #f59e0b; border-color: rgba(245, 158, 11, 0.4);' : ''}">
              ${isQuick ? 'CHẾ ĐỘ THI NHANH (20 CÂU)' : 'CHẾ ĐỘ THI THỬ CHUẨN (50 CÂU)'}
            </div>
            <h2 class="exam-start-title">${isQuick ? 'Sẵn Sàng Thi Nhanh (20 Câu)' : 'Sẵn Sàng Làm Bài Thi Sát Hạch'}</h2>
            <p class="exam-start-desc">
              ${isQuick
                ? 'Bài thi nhanh 20 câu trong 10 phút giúp bạn kiểm tra kiến thức chớp nhoáng, đảm bảo có câu hỏi điểm liệt và chấm điểm tự động.'
                : 'Đề thi 50 câu (33 phút) được tạo ngẫu nhiên theo đúng cấu trúc chuẩn của Cục CSGT 2025. Đồng hồ chỉ đếm ngược sau khi bạn bấm Bắt đầu.'}
            </p>
          </div>

          <div class="exam-info-grid">
            <div class="exam-info-item">
              <div class="exam-info-item-icon timer">⏱️</div>
              <div class="exam-info-item-text">
                <span class="exam-info-item-label">Thời gian làm bài</span>
                <span class="exam-info-item-val">${preset.durationMinutes} Phút (${preset.durationMinutes * 60}s)</span>
              </div>
            </div>

            <div class="exam-info-item">
              <div class="exam-info-item-icon questions">📋</div>
              <div class="exam-info-item-text">
                <span class="exam-info-item-label">Tổng số câu hỏi</span>
                <span class="exam-info-item-val">${preset.totalQuestions} Câu trắc nghiệm</span>
              </div>
            </div>

            <div class="exam-info-item">
              <div class="exam-info-item-icon pass">🎯</div>
              <div class="exam-info-item-text">
                <span class="exam-info-item-label">Điểm đạt yêu cầu</span>
                <span class="exam-info-item-val">Từ ${preset.passThreshold}/${preset.totalQuestions} câu trở lên</span>
              </div>
            </div>

            <div class="exam-info-item">
              <div class="exam-info-item-icon critical">⚠️</div>
              <div class="exam-info-item-text">
                <span class="exam-info-item-label">Câu hỏi điểm liệt</span>
                <span class="exam-info-item-val">Không được làm sai</span>
              </div>
            </div>
          </div>

          <div class="exam-rules-card">
            <h4>📌 Quy định & Hướng dẫn làm bài:</h4>
            <ul class="exam-rules-list">
              <li>Mỗi câu hỏi chỉ có <strong>duy nhất 1 đáp án đúng</strong>.</li>
              <li>Đồng hồ đếm ngược sẽ <strong>bắt đầu tính thời gian</strong> ngay khi bạn bấm nút "Bắt Đầu Làm Bài".</li>
              <li>Làm sai bất kỳ <strong>câu hỏi điểm liệt</strong> nào, bài thi sẽ bị tính là <strong>Không Đạt</strong> ngay lập tức.</li>
              <li>Phím <kbd class="kbd">1</kbd> - <kbd class="kbd">4</kbd> để chọn đáp án, phím mũi tên <kbd class="kbd">←</kbd> <kbd class="kbd">→</kbd> để chuyển câu hỏi.</li>
            </ul>
          </div>

          <button id="btn-start-exam" class="btn-start-exam-main" aria-label="Bắt đầu làm bài thi">
            <span>🚀 Bắt Đầu Làm Bài</span>
          </button>
          <div class="exam-start-keyboard-hint">
            <span>(Hoặc nhấn phím <kbd class="kbd">Enter ↵</kbd> để bắt đầu ngay)</span>
          </div>
        </div>
      </div>
    `;

    $('#btn-start-exam', this.container)?.addEventListener('click', () => {
      this.beginExam();
    });
  }

  bindActiveExamEvents(currentQuestion, savedScrollTop) {
    const state = store.getState();

    // Bind QuestionCard events
    QuestionCard.bindEvents(this.container, {
      onSelectOption: (optNum) => this.selectOption(optNum),
      onPrev: () => this.prevQuestion(),
      onNext: () => this.nextQuestion(),
      onToggleBookmark: () => this.toggleBookmark(currentQuestion.id),
      image: currentQuestion.image
    });

    // Bind Palette events
    QuestionPalette.bindEvents(this.container, (idx) => {
      store.setState({ currentExamIndex: idx });
      this.render();
    });

    // Submit button
    $('#btn-submit-test', this.container)?.addEventListener('click', () => {
      this.submitExam();
    });

    // Retry button
    $('#btn-retry-exam', this.container)?.addEventListener('click', () => {
      this.prepareExam();
    });

    // Restore scroll position
    QuestionPalette.restoreScroll(savedScrollTop, '.exam-sidebar .palette-grid');
  }

  selectOption(optionIndex) {
    const state = store.getState();
    if (state.isExamSubmitted) return; // Answer locked

    const currentQ = state.examQuestions[state.currentExamIndex];
    const newUserAnswers = { ...state.userAnswers, [currentQ.id]: optionIndex };

    store.setState({ userAnswers: newUserAnswers });
    this.render();
  }

  prevQuestion() {
    const state = store.getState();
    if (state.currentExamIndex > 0) {
      store.setState({ currentExamIndex: state.currentExamIndex - 1 });
      this.render();
    }
  }

  nextQuestion() {
    const state = store.getState();
    const total = state.examQuestions.length;
    if (state.currentExamIndex < total - 1) {
      store.setState({ currentExamIndex: state.currentExamIndex + 1 });
    } else {
      store.setState({ currentExamIndex: 0 });
    }
    this.render();
  }

  toggleBookmark(questionId) {
    StorageService.toggleBookmark(questionId);
    this.render();
  }

  submitExam() {
    const state = store.getState();
    if (state.isExamSubmitted) return;

    const answeredCount = Object.keys(state.userAnswers).length;
    const total = state.examQuestions.length;

    if (this.timer.getRemaining() > 0 && answeredCount < total) {
      const unattempted = total - answeredCount;
      confirmModal.show(unattempted, {
        onConfirm: () => this.finalizeSubmission()
      });
      return;
    }

    this.finalizeSubmission();
  }

  finalizeSubmission() {
    const state = store.getState();
    if (state.isExamSubmitted) return;

    this.timer.stop();
    const preset = EXAM_PRESETS[this.examType] || EXAM_PRESETS.standard;

    // Grade exam
    const examResult = ExamEngine.gradeExam(state.examQuestions, state.userAnswers, preset.passThreshold);

    // Save history & track wrong questions
    StorageService.saveExamResult({
      examType: this.examType,
      examTitle: preset.name,
      score: examResult.score,
      total: examResult.total,
      passed: examResult.passed,
      failedCritical: examResult.failedCritical,
      durationSeconds: this.timer.getElapsed(),
      wrongQuestionIds: examResult.wrongQuestionIds
    });

    examResult.wrongQuestionIds.forEach(id => StorageService.recordWrongQuestion(id));

    store.setState({
      isExamSubmitted: true,
      isReviewMode: true,
      examResult
    });

    this.render();

    // Show Result Modal
    resultModal.show(examResult, preset, {
      onReview: () => {
        store.setState({ currentExamIndex: 0 });
        this.render();
      },
      onRetry: () => {
        this.prepareExam();
      }
    });
  }

  onKeyboard(key, event) {
    const state = store.getState();

    if (!state.isExamStarted) {
      if (key === 'Enter') {
        event.preventDefault();
        this.beginExam();
      }
      return;
    }

    // 1-4 for options
    if (['1', '2', '3', '4'].includes(key)) {
      const optNum = Number(key);
      const currentQ = state.examQuestions[state.currentExamIndex];
      if (currentQ && optNum <= currentQ.options.length) {
        this.selectOption(optNum);
      }
    }

    // Arrows
    if (key === 'ArrowLeft' || key.toLowerCase() === 'a') {
      this.prevQuestion();
    } else if (key === 'ArrowRight' || key.toLowerCase() === 'd') {
      this.nextQuestion();
    }

    // Bookmark with B
    if (key.toLowerCase() === 'b') {
      const currentQ = state.examQuestions[state.currentExamIndex];
      if (currentQ) {
        this.toggleBookmark(currentQ.id);
      }
    }
  }

  unmount() {
    this.timer.stop();
    confirmModal.close();
    resultModal.close();
    super.unmount();
  }
}

