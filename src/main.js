import { ExamEngine, EXAM_PRESETS } from './exam_engine.js';
import { Storage } from './storage.js';
import questionsData from './data/questions.json';

// App State
const state = {
  allQuestions: questionsData,
  currentMode: 'exam', // 'exam', 'quick-exam', 'critical', 'chapter', 'all', 'mistakes', 'bookmarks'
  examType: 'standard', // 'standard' (50 câu / 33 phút) | 'quick' (20 câu / 10 phút)
  
  // Mock Exam State
  examQuestions: [],
  currentExamIndex: 0,
  userAnswers: {}, // { [questionId]: optionIndex }
  isExamSubmitted: false,
  isReviewMode: false,
  examResult: null,
  timerSeconds: EXAM_PRESETS.standard.durationSeconds, // 33 minutes default
  examTotalSeconds: EXAM_PRESETS.standard.durationSeconds,
  timerInterval: null,

  // Practice / Explorer State
  practiceQuestions: [],
  currentPracticeIndex: 0,
  selectedChapter: 1,
  searchQuery: '',
  filterType: 'all', // 'all', 'with_image', 'critical'
  showInstantAnswer: false,
  practiceAnswers: {}, // { [questionId]: optionNumber }

  // Lightbox State
  lightboxImage: null
};

// DOM Elements Cache
const elements = {};

function initDOMElements() {
  elements.themeToggleBtn = document.getElementById('theme-toggle-btn');
  elements.themeIcon = document.getElementById('theme-icon');
  elements.navTabs = document.querySelectorAll('.tab-btn');
  elements.appMain = document.getElementById('app-main');
  
  // Modals
  elements.resultModal = document.getElementById('result-modal');
  elements.lightboxModal = document.getElementById('lightbox-modal');
  elements.lightboxImg = document.getElementById('lightbox-img');
  elements.closeLightboxBtn = document.getElementById('close-lightbox-btn');
}

// Initialize Application
function initApp() {
  initDOMElements();
  initTheme();
  setupEventListeners();
  setupKeyboardShortcuts();
  
  // Start with a fresh 50-question Standard Mock Exam (33 mins)
  startNewExam('standard');
}

// Theme handling
function initTheme() {
  const savedTheme = Storage.getTheme();
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  Storage.setTheme(newTheme);
  updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
  if (elements.themeIcon) {
    elements.themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
  }
}

// Tab Switching
function switchMode(newMode) {
  state.currentMode = newMode;
  elements.navTabs.forEach(tab => {
    tab.classList.toggle('active', tab.dataset.mode === newMode);
  });

  if (newMode === 'exam') {
    if (state.examQuestions.length === 0 || state.examType !== 'standard') {
      startNewExam('standard');
    } else {
      renderExamView();
    }
  } else if (newMode === 'quick-exam') {
    if (state.examQuestions.length === 0 || state.examType !== 'quick') {
      startNewExam('quick');
    } else {
      renderExamView();
    }
  } else if (newMode === 'critical') {
    state.practiceQuestions = state.allQuestions.filter(q => q.is_critical);
    state.currentPracticeIndex = 0;
    renderPracticeView('60 Câu Hỏi Điểm Liệt (Bắt Buộc Đúng)');
  } else if (newMode === 'chapter') {
    state.practiceQuestions = state.allQuestions.filter(q => q.chapter === state.selectedChapter);
    state.currentPracticeIndex = 0;
    renderChapterView();
  } else if (newMode === 'all') {
    renderAllQuestionsView();
  } else if (newMode === 'mistakes') {
    const wrongMap = Storage.getWrongQuestions();
    const wrongIds = Object.keys(wrongMap).map(Number);
    state.practiceQuestions = state.allQuestions.filter(q => wrongIds.includes(q.id));
    state.currentPracticeIndex = 0;
    renderPracticeView('Danh Sách Câu Làm Sai Cần Ôn Lại');
  } else if (newMode === 'bookmarks') {
    const bookmarkedIds = Storage.getBookmarks();
    state.practiceQuestions = state.allQuestions.filter(q => bookmarkedIds.includes(q.id));
    state.currentPracticeIndex = 0;
    renderPracticeView('Câu Hỏi Đã Đánh Dấu Ghi Nhớ');
  }
}

// ==========================================================================
// EXAM ENGINE LOGIC & TIMERS
// ==========================================================================

function startNewExam(examType = 'standard') {
  // Clear any active timer
  if (state.timerInterval) {
    clearInterval(state.timerInterval);
    state.timerInterval = null;
  }

  state.examType = examType;
  const preset = EXAM_PRESETS[examType] || EXAM_PRESETS.standard;

  state.examQuestions = ExamEngine.generateExam(state.allQuestions, examType, {
    minCritical: preset.minCritical,
    maxCritical: preset.maxCritical,
    shuffleQuestions: true
  });
  state.currentExamIndex = 0;
  state.userAnswers = {};
  state.isExamSubmitted = false;
  state.isReviewMode = false;
  state.examResult = null;
  state.timerSeconds = preset.durationSeconds;
  state.examTotalSeconds = preset.durationSeconds;

  startTimer();
  renderExamView();
}

function startTimer() {
  if (state.timerInterval) clearInterval(state.timerInterval);
  const preset = EXAM_PRESETS[state.examType] || EXAM_PRESETS.standard;
  
  state.timerInterval = setInterval(() => {
    if (state.isExamSubmitted) {
      clearInterval(state.timerInterval);
      return;
    }

    state.timerSeconds--;
    updateTimerDisplay();

    if (state.timerSeconds <= 0) {
      clearInterval(state.timerInterval);
      alert(`⏰ Đã hết thời gian làm bài thi (${preset.durationMinutes} phút)! Hệ thống sẽ tự động nộp bài.`);
      submitExam();
    }
  }, 1000);
}

function updateTimerDisplay() {
  const timerElem = document.getElementById('timer-val');
  if (!timerElem) return;

  const minutes = Math.floor(state.timerSeconds / 60);
  const seconds = state.timerSeconds % 60;
  const timeStr = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
  timerElem.textContent = timeStr;

  if (state.timerSeconds <= 120) {
    timerElem.className = 'timer-display danger';
  } else if (state.timerSeconds <= 300) {
    timerElem.className = 'timer-display warning';
  } else {
    timerElem.className = 'timer-display';
  }
}

function selectExamOption(optionIndex) {
  if (state.isExamSubmitted && !state.isReviewMode) return;
  if (state.isExamSubmitted && state.isReviewMode) return; // In review mode, answers are locked

  const currentQ = state.examQuestions[state.currentExamIndex];
  state.userAnswers[currentQ.id] = optionIndex;
  
  // Re-render current question and update palette
  renderExamView();
}

function submitExam() {
  if (state.isExamSubmitted) return;

  const answeredCount = Object.keys(state.userAnswers).length;
  const total = state.examQuestions.length;
  const preset = EXAM_PRESETS[state.examType] || EXAM_PRESETS.standard;

  if (state.timerSeconds > 0 && answeredCount < total) {
    const unattempted = total - answeredCount;
    const confirmSubmit = confirm(`Bạn còn ${unattempted} câu chưa trả lời. Bạn có chắc chắn muốn nộp bài thi không?`);
    if (!confirmSubmit) return;
  }

  if (state.timerInterval) {
    clearInterval(state.timerInterval);
    state.timerInterval = null;
  }

  state.isExamSubmitted = true;
  state.isReviewMode = true;

  // Grade exam
  state.examResult = ExamEngine.gradeExam(state.examQuestions, state.userAnswers, preset.passThreshold);

  // Save history & track wrong questions
  Storage.saveExamResult({
    examType: state.examType,
    examTitle: preset.name,
    score: state.examResult.score,
    total: state.examResult.total,
    passed: state.examResult.passed,
    failedCritical: state.examResult.failedCritical,
    durationSeconds: (state.examTotalSeconds || preset.durationSeconds) - Math.max(0, state.timerSeconds),
    wrongQuestionIds: state.examResult.wrongQuestionIds
  });

  state.examResult.wrongQuestionIds.forEach(id => Storage.recordWrongQuestion(id));

  // Update UI and show Result Modal
  renderExamView();
  showResultModal();
}

// ==========================================================================
// RENDERERS (EXAM, PRACTICE, CHAPTER, ALL 600)
// ==========================================================================

function renderExamView() {
  if (state.examQuestions.length === 0) return;

  const q = state.examQuestions[state.currentExamIndex];
  const userAnswer = state.userAnswers[q.id];
  const isBookmarked = Storage.isBookmarked(q.id);
  const totalQuestions = state.examQuestions.length;
  const answeredCount = Object.keys(state.userAnswers).length;
  const preset = EXAM_PRESETS[state.examType] || EXAM_PRESETS.standard;

  const minutes = Math.floor(state.timerSeconds / 60);
  const seconds = state.timerSeconds % 60;
  const timeStr = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

  const isQuick = state.examType === 'quick';
  const examBadgeText = isQuick ? '⚡ THI NHANH (20 CÂU / 10 PHÚT)' : '📝 THI THỬ CHUẨN (50 CÂU / 33 PHÚT)';
  const examBadgeStyle = isQuick
    ? 'background: rgba(245, 158, 11, 0.2); color: #f59e0b; border-color: rgba(245, 158, 11, 0.4);'
    : 'background: rgba(99, 102, 241, 0.2); color: #818cf8; border-color: rgba(99, 102, 241, 0.4);';

  elements.appMain.innerHTML = `
    <div class="exam-layout">
      <!-- Main Question Area -->
      <div class="question-card">
        <div class="question-header">
          <div class="question-meta">
            <span class="badge badge-index" style="${examBadgeStyle}">${examBadgeText}</span>
            <span class="badge badge-index">Câu ${state.currentExamIndex + 1} / ${totalQuestions}</span>
            <span class="badge badge-chapter">Chương ${q.chapter}</span>
            ${q.is_critical ? `<span class="badge badge-critical">⚠️ CÂU ĐIỂM LIỆT</span>` : ''}
          </div>
          <button class="btn-bookmark ${isBookmarked ? 'active' : ''}" id="btn-toggle-bookmark">
            <span>${isBookmarked ? '★ Đã lưu' : '☆ Lưu câu này'}</span>
          </button>
        </div>

        <h2 class="question-title">${escapeHtml(q.question)}</h2>

        ${q.image ? `
          <div class="question-image-container" id="question-img-wrap">
            <img src="${q.image}" alt="Hình minh họa câu ${q.id}" class="question-image" />
            <div class="zoom-hint">🔍 Nhấn để phóng to</div>
          </div>
        ` : ''}

        <div class="options-list">
          ${q.options.map((optText, idx) => {
            const optNum = idx + 1;
            const isSelected = userAnswer === optNum;
            let optClass = 'option-item';

            if (isSelected) optClass += ' selected';

            if (state.isExamSubmitted) {
              if (optNum === q.correct_option) {
                optClass += ' correct';
              } else if (isSelected && optNum !== q.correct_option) {
                optClass += ' incorrect';
              }
            }

            return `
              <button class="${optClass}" data-opt="${optNum}">
                <span class="option-key">${optNum}</span>
                <span class="option-text">${escapeHtml(optText)}</span>
              </button>
            `;
          }).join('')}
        </div>

        ${state.isExamSubmitted ? `
          <div class="explanation-box">
            <div class="explanation-title">
              <span>💡 Giải thích chi tiết & Đáp án đúng</span>
            </div>
            <div class="explanation-content">
              <strong>Đáp án đúng: Câu số ${q.correct_option}.</strong> ${q.explanation || (q.is_critical ? 'Đây là câu hỏi mất an toàn giao thông nghiêm trọng (câu điểm liệt), người lái xe bắt buộc phải nắm rõ và chấp hành nghiêm túc.' : 'Căn cứ theo Luật Trật tự, an toàn giao thông đường bộ và Quy chuẩn Báo hiệu đường bộ 2025.')}
            </div>
          </div>
        ` : ''}

        <!-- Bottom Controls -->
        <div class="question-controls">
          <button class="btn-nav" id="btn-prev-q" ${state.currentExamIndex === 0 ? 'disabled' : ''}>
            ⬅️ Câu trước <span class="kbd">←</span>
          </button>

          <div class="keyboard-hints">
            <span>Phím <span class="kbd">1-4</span>: Chọn đáp án</span>
            <span>|</span>
            <span>Phím <span class="kbd">←</span> <span class="kbd">→</span>: Chuyển câu</span>
          </div>

          <button class="btn-nav btn-primary" id="btn-next-q">
            ${state.currentExamIndex === totalQuestions - 1 ? (state.isExamSubmitted ? 'Xem lại từ đầu' : 'Xem câu 1 ➡️') : 'Câu tiếp ➡️'} <span class="kbd">→</span>
          </button>
        </div>
      </div>

      <!-- Right Exam Sidebar -->
      <div class="exam-sidebar">
        <!-- Timer Widget -->
        <div class="sidebar-card">
          <div class="timer-widget">
            <div class="timer-label">
              <span>⏱️ Thời gian:</span>
            </div>
            <div id="timer-val" class="timer-display">${timeStr}</div>
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

        <!-- Question Grid Palette -->
        <div class="sidebar-card">
          <div class="palette-header">
            <span class="palette-title">Danh sách ${totalQuestions} câu</span>
            <span class="palette-stats">Đã làm: ${answeredCount}/${totalQuestions}</span>
          </div>

          <div class="palette-grid ${totalQuestions > 30 ? 'palette-grid-50' : ''}">
            ${state.examQuestions.map((eq, idx) => {
              const ans = state.userAnswers[eq.id];
              const isCurrent = idx === state.currentExamIndex;
              const isAnswered = ans !== undefined;
              const isBm = Storage.isBookmarked(eq.id);

              let cls = 'palette-btn';
              if (isCurrent) cls += ' current';
              if (isAnswered) cls += ' answered';
              if (isBm) cls += ' bookmarked';
              if (eq.is_critical) cls += ' critical-indicator';

              if (state.isExamSubmitted) {
                const isCorrect = ans === eq.correct_option;
                if (isCorrect) {
                  cls += ' correct-mark';
                } else if (eq.is_critical) {
                  cls += ' critical-failed-mark';
                } else {
                  cls += ' incorrect-mark';
                }
              }

              return `
                <button class="${cls}" data-qindex="${idx}">
                  ${idx + 1}
                </button>
              `;
            }).join('')}
          </div>

          <div class="palette-legend">
            <div class="legend-item">
              <span class="legend-dot unanswered"></span>
              <span>Chưa làm</span>
            </div>
            <div class="legend-item">
              <span class="legend-dot answered"></span>
              <span>Đã chọn</span>
            </div>
            <div class="legend-item">
              <span class="legend-dot critical"></span>
              <span>Câu liệt</span>
            </div>
            <div class="legend-item">
              <span class="legend-dot bookmarked"></span>
              <span>Đã lưu ★</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  attachExamEvents();
}

function attachExamEvents() {
  // Option Clicks
  document.querySelectorAll('.option-item').forEach(btn => {
    btn.addEventListener('click', () => {
      const optNum = Number(btn.dataset.opt);
      selectExamOption(optNum);
    });
  });

  // Next / Prev buttons
  const prevBtn = document.getElementById('btn-prev-q');
  const nextBtn = document.getElementById('btn-next-q');
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (state.currentExamIndex > 0) {
        state.currentExamIndex--;
        renderExamView();
      }
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (state.currentExamIndex < state.examQuestions.length - 1) {
        state.currentExamIndex++;
      } else {
        state.currentExamIndex = 0;
      }
      renderExamView();
    });
  }

  // Question Grid jump buttons
  document.querySelectorAll('.palette-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      state.currentExamIndex = Number(btn.dataset.qindex);
      renderExamView();
    });
  });

  // Bookmark toggle
  const bmBtn = document.getElementById('btn-toggle-bookmark');
  if (bmBtn) {
    bmBtn.addEventListener('click', () => {
      const currentQ = state.examQuestions[state.currentExamIndex];
      Storage.toggleBookmark(currentQ.id);
      renderExamView();
    });
  }

  // Image zoom lightbox
  const imgWrap = document.getElementById('question-img-wrap');
  if (imgWrap) {
    imgWrap.addEventListener('click', () => {
      const currentQ = state.examQuestions[state.currentExamIndex];
      openLightbox(currentQ.image);
    });
  }

  // Submit test
  const submitBtn = document.getElementById('btn-submit-test');
  if (submitBtn) {
    submitBtn.addEventListener('click', submitExam);
  }

  // Retry exam
  const retryBtn = document.getElementById('btn-retry-exam');
  if (retryBtn) {
    retryBtn.addEventListener('click', () => startNewExam(state.examType));
  }
}

// ==========================================================================
// PRACTICE VIEW (CRITICAL 60, CHAPTER, MISTAKES, BOOKMARKS)
// ==========================================================================

function selectPracticeOption(optNum) {
  if (state.practiceQuestions.length === 0) return;
  const q = state.practiceQuestions[state.currentPracticeIndex];
  if (!q) return;

  state.practiceAnswers[q.id] = optNum;

  // Record mistake or correct in Storage
  if (optNum !== q.correct_option) {
    Storage.recordWrongQuestion(q.id);
  } else {
    Storage.recordCorrectQuestion(q.id);
  }

  renderCurrentPracticeMode();
}

function resetPracticeCurrentQuestion() {
  if (state.practiceQuestions.length === 0) return;
  const q = state.practiceQuestions[state.currentPracticeIndex];
  if (!q) return;

  delete state.practiceAnswers[q.id];
  renderCurrentPracticeMode();
}

function renderCurrentPracticeMode() {
  if (state.currentMode === 'chapter') {
    renderChapterView();
  } else if (state.currentMode === 'critical') {
    renderPracticeView('60 Câu Hỏi Điểm Liệt (Bắt Buộc Đúng)');
  } else if (state.currentMode === 'mistakes') {
    renderPracticeView('Danh Sách Câu Làm Sai Cần Ôn Lại');
  } else if (state.currentMode === 'bookmarks') {
    renderPracticeView('Câu Hỏi Đã Đánh Dấu Ghi Nhớ');
  }
}

function renderPracticeView(title, customHeader = '') {
  if (state.practiceQuestions.length === 0) {
    elements.appMain.innerHTML = `
      ${customHeader}
      <div class="empty-state" style="margin-top: 1rem;">
        <div class="empty-icon">📭</div>
        <h2>Chưa có câu hỏi nào trong danh sách này</h2>
        <p>Hãy làm bài thi hoặc ôn tập các chương để lưu câu hỏi vào đây nhé!</p>
        <button class="btn-nav btn-primary" id="btn-back-to-exam" style="margin-top: 1rem;">
          📝 Làm Đề Thi Thử 50 Câu
        </button>
      </div>
    `;
    const backBtn = document.getElementById('btn-back-to-exam');
    if (backBtn) backBtn.addEventListener('click', () => switchMode('exam'));
    attachChapterSelectEvent();
    return;
  }

  const q = state.practiceQuestions[state.currentPracticeIndex];
  const isBookmarked = Storage.isBookmarked(q.id);
  const total = state.practiceQuestions.length;

  const userAnswer = state.practiceAnswers[q.id];
  const isAnswered = userAnswer !== undefined;
  const isRevealed = state.showInstantAnswer || isAnswered;

  // Compute stats in current practice list
  let correctCount = 0;
  let wrongCount = 0;
  state.practiceQuestions.forEach(pq => {
    const ans = state.practiceAnswers[pq.id];
    if (ans !== undefined) {
      if (ans === pq.correct_option) correctCount++;
      else wrongCount++;
    }
  });
  const answeredCount = correctCount + wrongCount;

  // Feedback banner
  let feedbackHtml = '';
  if (isAnswered) {
    if (userAnswer === q.correct_option) {
      feedbackHtml = `
        <div class="practice-feedback correct">
          <span class="feedback-icon">🎉</span>
          <div class="feedback-text">
            <strong>Chính xác!</strong> Bạn đã chọn đúng đáp án <strong>#${q.correct_option}</strong>.
          </div>
        </div>
      `;
    } else {
      feedbackHtml = `
        <div class="practice-feedback incorrect">
          <span class="feedback-icon">❌</span>
          <div class="feedback-text">
            <strong>Chưa chính xác!</strong> Bạn đã chọn ý <strong>#${userAnswer}</strong>, đáp án đúng là ý <strong>#${q.correct_option}</strong>.
          </div>
        </div>
      `;
    }
  }

  elements.appMain.innerHTML = `
    ${customHeader}
    <div class="exam-layout" style="${customHeader ? 'margin-top: 1rem;' : ''}">
      <div class="question-card">
        <div class="question-header">
          <div class="question-meta">
            <span class="badge badge-index">${title}</span>
            <span class="badge badge-index">Câu ${state.currentPracticeIndex + 1} / ${total} (Mã: #${q.id})</span>
            <span class="badge badge-chapter">Chương ${q.chapter}</span>
            ${q.is_critical ? `<span class="badge badge-critical">⚠️ CÂU ĐIỂM LIỆT</span>` : ''}
          </div>
          <button class="btn-bookmark ${isBookmarked ? 'active' : ''}" id="btn-toggle-bookmark-prac">
            <span>${isBookmarked ? '★ Đã lưu' : '☆ Lưu câu này'}</span>
          </button>
        </div>

        <h2 class="question-title">${escapeHtml(q.question)}</h2>

        ${q.image ? `
          <div class="question-image-container" id="prac-img-wrap">
            <img src="${q.image}" alt="Hình câu ${q.id}" class="question-image" />
            <div class="zoom-hint">🔍 Phóng to</div>
          </div>
        ` : ''}

        <div class="options-list">
          ${q.options.map((optText, idx) => {
            const optNum = idx + 1;
            const isCorrectOption = optNum === q.correct_option;
            const isUserSelected = userAnswer === optNum;

            let optClass = 'option-item';
            let statusIconHtml = '';

            if (isRevealed) {
              if (isCorrectOption) {
                optClass += ' correct';
                statusIconHtml = `<span class="option-status-icon correct">✔️</span>`;
              } else if (isUserSelected && !isCorrectOption) {
                optClass += ' incorrect';
                statusIconHtml = `<span class="option-status-icon incorrect">❌</span>`;
              }
            } else if (isUserSelected) {
              optClass += ' selected';
            }

            return `
              <button class="${optClass}" data-pracopt="${optNum}">
                <span class="option-key">${optNum}</span>
                <span class="option-text">${escapeHtml(optText)}</span>
                ${statusIconHtml}
              </button>
            `;
          }).join('')}
        </div>

        ${isRevealed ? `
          <div class="explanation-box">
            ${feedbackHtml}
            <div class="explanation-title">
              <span>💡 Đáp án chuẩn & Lời khuyên chi tiết</span>
            </div>
            <div class="explanation-content">
              <strong>Đáp án đúng: Ý số ${q.correct_option}.</strong> ${q.explanation || (q.is_critical ? 'Lưu ý: Đây là câu hỏi điểm liệt (mất an toàn giao thông nghiêm trọng). Sai câu này trong kỳ thi sát hạch sẽ bị đánh giá TRƯỢT trực tiếp.' : 'Quy tắc chuẩn theo Bộ 600 câu hỏi sát hạch năm 2025.')}
            </div>
          </div>
        ` : `
          <div class="practice-hint-placeholder">
            <span>👉 Bấm chọn một đáp án ở trên để kiểm tra kết quả ngay lập tức</span>
          </div>
        `}

        <div class="question-controls">
          <button class="btn-nav" id="btn-prev-prac" ${state.currentPracticeIndex === 0 ? 'disabled' : ''}>
            ⬅️ Câu trước <span class="kbd">←</span>
          </button>

          <div style="display: flex; align-items: center; gap: 1rem; flex-wrap: wrap;">
            ${isAnswered ? `
              <button class="btn-nav btn-sm" id="btn-reset-prac" title="Chọn lại đáp án cho câu này">
                🔄 Chọn lại <span class="kbd">R</span>
              </button>
            ` : ''}

            <label style="display: flex; align-items: center; gap: 0.5rem; font-size: 0.875rem; cursor: pointer; user-select: none;">
              <input type="checkbox" id="chk-instant-ans" ${state.showInstantAnswer ? 'checked' : ''} />
              <span>👁️ Luôn hiện đáp án & giải thích</span>
            </label>
          </div>

          <button class="btn-nav btn-primary" id="btn-next-prac" ${state.currentPracticeIndex === total - 1 ? 'disabled' : ''}>
            Câu tiếp ➡️ <span class="kbd">→</span>
          </button>
        </div>
      </div>

      <!-- Practice Sidebar -->
      <div class="exam-sidebar">
        <div class="sidebar-card">
          <div class="palette-header">
            <span class="palette-title">Danh sách câu (${total})</span>
            <span class="palette-stats" style="font-size: 0.8125rem;">
              Đã làm: ${answeredCount}/${total}
              ${answeredCount > 0 ? `<br><span style="color: var(--success); font-weight: 700;">${correctCount} Đúng</span> • <span style="color: var(--danger); font-weight: 700;">${wrongCount} Sai</span>` : ''}
            </span>
          </div>
          <div class="palette-grid" style="max-height: 480px; overflow-y: auto; padding-right: 4px;">
            ${state.practiceQuestions.map((pq, idx) => {
              const isCurrent = idx === state.currentPracticeIndex;
              const ans = state.practiceAnswers[pq.id];
              const isAnsweredItem = ans !== undefined;

              let cls = 'palette-btn';
              if (isCurrent) cls += ' current';
              if (pq.is_critical) cls += ' critical-indicator';
              if (Storage.isBookmarked(pq.id)) cls += ' bookmarked';

              if (isAnsweredItem) {
                if (ans === pq.correct_option) {
                  cls += ' correct-mark';
                } else {
                  cls += ' incorrect-mark';
                }
              }

              return `
                <button class="${cls}" data-pracidx="${idx}">
                  ${idx + 1}
                </button>
              `;
            }).join('')}
          </div>

          <div class="palette-legend" style="margin-top: 0.75rem;">
            <div class="legend-item">
              <span class="legend-dot" style="background: var(--success); border-color: var(--success);"></span>
              <span>Làm đúng (${correctCount})</span>
            </div>
            <div class="legend-item">
              <span class="legend-dot" style="background: var(--danger); border-color: var(--danger);"></span>
              <span>Làm sai (${wrongCount})</span>
            </div>
            <div class="legend-item">
              <span class="legend-dot critical"></span>
              <span>Câu điểm liệt</span>
            </div>
            <div class="legend-item">
              <span class="legend-dot bookmarked"></span>
              <span>Đã lưu ★</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  // Attach Practice Events
  // Option clicks
  document.querySelectorAll('.option-item[data-pracopt]').forEach(btn => {
    btn.addEventListener('click', () => {
      const optNum = Number(btn.dataset.pracopt);
      selectPracticeOption(optNum);
    });
  });

  const resetBtn = document.getElementById('btn-reset-prac');
  if (resetBtn) {
    resetBtn.addEventListener('click', resetPracticeCurrentQuestion);
  }

  const prevBtn = document.getElementById('btn-prev-prac');
  const nextBtn = document.getElementById('btn-next-prac');
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (state.currentPracticeIndex > 0) {
        state.currentPracticeIndex--;
        renderCurrentPracticeMode();
      }
    });
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (state.currentPracticeIndex < state.practiceQuestions.length - 1) {
        state.currentPracticeIndex++;
        renderCurrentPracticeMode();
      }
    });
  }

  document.querySelectorAll('.palette-btn[data-pracidx]').forEach(btn => {
    btn.addEventListener('click', () => {
      state.currentPracticeIndex = Number(btn.dataset.pracidx);
      renderCurrentPracticeMode();
    });
  });

  const bmBtn = document.getElementById('btn-toggle-bookmark-prac');
  if (bmBtn) {
    bmBtn.addEventListener('click', () => {
      const curQ = state.practiceQuestions[state.currentPracticeIndex];
      Storage.toggleBookmark(curQ.id);
      renderCurrentPracticeMode();
    });
  }

  const chk = document.getElementById('chk-instant-ans');
  if (chk) {
    chk.addEventListener('change', (e) => {
      state.showInstantAnswer = e.target.checked;
      renderCurrentPracticeMode();
    });
  }

  const imgWrap = document.getElementById('prac-img-wrap');
  if (imgWrap) {
    imgWrap.addEventListener('click', () => {
      openLightbox(q.image);
    });
  }

  attachChapterSelectEvent();
}

function attachChapterSelectEvent() {
  const sel = document.getElementById('chapter-select');
  if (sel) {
    sel.addEventListener('change', (e) => {
      state.selectedChapter = Number(e.target.value);
      state.practiceQuestions = state.allQuestions.filter(q => q.chapter === state.selectedChapter);
      state.currentPracticeIndex = 0;
      renderChapterView();
    });
  }
}

function renderChapterView() {
  const chapters = [
    { id: 1, name: 'Chương 1: Quy định & Quy tắc chung (1 - 180)', count: 180 },
    { id: 2, name: 'Chương 2: Văn hóa & Đạo đức lái xe (181 - 205)', count: 25 },
    { id: 3, name: 'Chương 3: Kỹ thuật lái xe (206 - 263)', count: 58 },
    { id: 4, name: 'Chương 4: Cấu tạo & Sửa chữa (264 - 300)', count: 37 },
    { id: 5, name: 'Chương 5: Báo hiệu đường bộ (301 - 485)', count: 185 },
    { id: 6, name: 'Chương 6: Giải thế Sa hình (486 - 600)', count: 115 },
  ];

  const headerHtml = `
    <div class="filter-bar">
      <div style="font-weight: 700; font-size: 1.05rem; display: flex; align-items: center; gap: 0.5rem;">
        <span>📚 Chọn Chương Ôn Tập:</span>
      </div>
      <select id="chapter-select" class="filter-select" style="min-width: 340px;">
        ${chapters.map(ch => `
          <option value="${ch.id}" ${state.selectedChapter === ch.id ? 'selected' : ''}>
            ${ch.name}
          </option>
        `).join('')}
      </select>
    </div>
  `;

  state.practiceQuestions = state.allQuestions.filter(q => q.chapter === state.selectedChapter);
  const currentChapterObj = chapters.find(c => c.id === state.selectedChapter) || chapters[0];
  renderPracticeView(currentChapterObj.name.split(':')[0], headerHtml);
}

// ==========================================================================
// SEARCH & ALL 600 QUESTIONS VIEW
// ==========================================================================

function renderAllQuestionsView() {
  const query = state.searchQuery.toLowerCase().trim();
  let filtered = state.allQuestions.filter(q => {
    const matchesSearch = !query || q.question.toLowerCase().includes(query) || q.options.some(o => o.toLowerCase().includes(query)) || String(q.id).includes(query);
    
    if (!matchesSearch) return false;

    if (state.filterType === 'with_image') return !!q.image;
    if (state.filterType === 'critical') return q.is_critical;
    return true;
  });

  elements.appMain.innerHTML = `
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
        <option value="with_image" ${state.filterType === 'with_image' ? 'selected' : ''}>🖼️ Câu có hình ảnh (${state.allQuestions.filter(q => q.image).length} câu)</option>
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
            <button class="btn-bookmark ${Storage.isBookmarked(q.id) ? 'active' : ''}" data-bmid="${q.id}">
              <span>${Storage.isBookmarked(q.id) ? '★ Đã lưu' : '☆ Lưu'}</span>
            </button>
          </div>

          <h3 class="question-title" style="font-size: 1.05rem;">${escapeHtml(q.question)}</h3>

          ${q.image ? `
            <div class="question-image-container" style="max-height: 260px;" data-zoomimg="${q.image}">
              <img src="${q.image}" alt="Câu ${q.id}" class="question-image" style="max-height: 240px;" />
              <div class="zoom-hint">🔍 Phóng to</div>
            </div>
          ` : ''}

          <div class="options-list">
            ${q.options.map((opt, idx) => `
              <div class="option-item ${idx + 1 === q.correct_option ? 'correct' : ''}" style="padding: 0.75rem 1rem;">
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

  // Search input event
  const searchInp = document.getElementById('search-input');
  if (searchInp) {
    searchInp.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      renderAllQuestionsView();
    });
  }

  // Filter select
  const filterSel = document.getElementById('filter-type-select');
  if (filterSel) {
    filterSel.addEventListener('change', (e) => {
      state.filterType = e.target.value;
      renderAllQuestionsView();
    });
  }

  // Bookmark buttons
  document.querySelectorAll('[data-bmid]').forEach(btn => {
    btn.addEventListener('click', () => {
      const qid = Number(btn.dataset.bmid);
      Storage.toggleBookmark(qid);
      renderAllQuestionsView();
    });
  });

  // Image zoom
  document.querySelectorAll('[data-zoomimg]').forEach(wrap => {
    wrap.addEventListener('click', () => {
      openLightbox(wrap.dataset.zoomimg);
    });
  });
}

// ==========================================================================
// RESULT MODAL & LIGHTBOX
// ==========================================================================

function showResultModal() {
  if (!state.examResult) return;

  const res = state.examResult;
  const isPassed = res.passed;
  const preset = EXAM_PRESETS[state.examType] || EXAM_PRESETS.standard;

  let statusHtml = '';
  if (isPassed) {
    statusHtml = `
      <div class="result-status-badge passed">
        <span>🎉 ĐẠT (${preset.shortName.toUpperCase()})</span>
      </div>
      <p class="result-message">
        Chúc mừng! Bạn đã hoàn thành xuất sắc bài thi với <strong>${res.score}/${res.total}</strong> điểm! (Yêu cầu đạt tối thiểu ${res.passThreshold}/${res.total} điểm).
      </p>
    `;
  } else {
    let failReason = `Chưa đủ điểm đạt chuẩn (${res.score}/${res.total} - yêu cầu tối thiểu ${res.passThreshold}/${res.total} điểm).`;
    if (res.failedCritical) {
      failReason = `❌ <strong>RỚT TRỰC TIẾP DO SAI CÂU ĐIỂM LIỆT!</strong><br/>Bạn đã trả lời sai câu điểm liệt bắt buộc (Câu ${res.failedCriticalQuestions.map(q => q.id).join(', ')}).`;
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

  elements.resultModal.innerHTML = `
    <div class="modal-content">
      ${statusHtml}

      <div class="score-circle" style="border-color: ${isPassed ? '#10b981' : '#ef4444'}; box-shadow: 0 0 24px ${isPassed ? 'rgba(16, 185, 129, 0.4)' : 'rgba(239, 68, 68, 0.4)'};">
        <span class="score-num" style="color: ${isPassed ? '#10b981' : '#ef4444'};">${res.score}</span>
        <span class="score-total">/ ${res.total} ĐIỂM</span>
      </div>

      <div class="result-stats-grid">
        <div class="result-stat-box">
          <span class="result-stat-val" style="color: #10b981;">${res.score}</span>
          <span class="result-stat-lbl">Số câu đúng</span>
        </div>
        <div class="result-stat-box">
          <span class="result-stat-val" style="color: #ef4444;">${res.wrongCount}</span>
          <span class="result-stat-lbl">Số câu sai</span>
        </div>
        <div class="result-stat-box">
          <span class="result-stat-val" style="color: #94a3b8;">${res.unattemptedCount}</span>
          <span class="result-stat-lbl">Chưa làm</span>
        </div>
      </div>

      <div class="modal-actions">
        <button class="btn-nav btn-primary" id="btn-review-test">
          🔍 Xem Lại Bài Thi Chi Tiết
        </button>
        <button class="btn-nav" id="btn-new-exam-modal">
          🔄 Thi Đề Khác (Trộn ${res.total} câu mới)
        </button>
      </div>
    </div>
  `;

  elements.resultModal.classList.add('show');

  // Modal events
  document.getElementById('btn-review-test')?.addEventListener('click', () => {
    elements.resultModal.classList.remove('show');
    state.currentExamIndex = 0;
    renderExamView();
  });

  document.getElementById('btn-new-exam-modal')?.addEventListener('click', () => {
    elements.resultModal.classList.remove('show');
    startNewExam(state.examType);
  });
}

function openLightbox(imgSrc) {
  if (!imgSrc) return;
  elements.lightboxImg.src = imgSrc;
  elements.lightboxModal.classList.add('show');
}

function closeLightbox() {
  elements.lightboxModal.classList.remove('show');
}

// ==========================================================================
// EVENT LISTENERS & KEYBOARD SHORTCUTS
// ==========================================================================

function setupEventListeners() {
  elements.themeToggleBtn?.addEventListener('click', toggleTheme);

  elements.navTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      switchMode(tab.dataset.mode);
    });
  });

  elements.closeLightboxBtn?.addEventListener('click', closeLightbox);
  elements.lightboxModal?.addEventListener('click', (e) => {
    if (e.target === elements.lightboxModal) closeLightbox();
  });
}

function setupKeyboardShortcuts() {
  window.addEventListener('keydown', (e) => {
    // Ignore shortcuts when typing in search input
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') {
      return;
    }

    if (e.key === 'Escape') {
      closeLightbox();
      if (elements.resultModal.classList.contains('show')) {
        elements.resultModal.classList.remove('show');
      }
      return;
    }

    if (['exam', 'quick-exam'].includes(state.currentMode)) {
      // 1, 2, 3, 4 to select options
      if (['1', '2', '3', '4'].includes(e.key)) {
        const optNum = Number(e.key);
        const currentQ = state.examQuestions[state.currentExamIndex];
        if (currentQ && optNum <= currentQ.options.length) {
          selectExamOption(optNum);
        }
      }

      // Left / Right arrows or A / D
      if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
        if (state.currentExamIndex > 0) {
          state.currentExamIndex--;
          renderExamView();
        }
      } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
        if (state.currentExamIndex < state.examQuestions.length - 1) {
          state.currentExamIndex++;
          renderExamView();
        }
      }

      // Bookmark with B
      if (e.key.toLowerCase() === 'b') {
        const currentQ = state.examQuestions[state.currentExamIndex];
        if (currentQ) {
          Storage.toggleBookmark(currentQ.id);
          renderExamView();
        }
      }
    } else if (['chapter', 'critical', 'mistakes', 'bookmarks'].includes(state.currentMode)) {
      // Practice Modes shortcuts
      // 1, 2, 3, 4 to select options
      if (['1', '2', '3', '4'].includes(e.key)) {
        const optNum = Number(e.key);
        const currentQ = state.practiceQuestions[state.currentPracticeIndex];
        if (currentQ && optNum <= currentQ.options.length) {
          selectPracticeOption(optNum);
        }
      }

      // Left / Right arrows or A / D
      if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') {
        if (state.currentPracticeIndex > 0) {
          state.currentPracticeIndex--;
          renderCurrentPracticeMode();
        }
      } else if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') {
        if (state.currentPracticeIndex < state.practiceQuestions.length - 1) {
          state.currentPracticeIndex++;
          renderCurrentPracticeMode();
        }
      }

      // Bookmark with B
      if (e.key.toLowerCase() === 'b') {
        const currentQ = state.practiceQuestions[state.currentPracticeIndex];
        if (currentQ) {
          Storage.toggleBookmark(currentQ.id);
          renderCurrentPracticeMode();
        }
      }

      // Reset with R
      if (e.key.toLowerCase() === 'r') {
        resetPracticeCurrentQuestion();
      }
    }
  });
}

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Kickstart on DOM Load
document.addEventListener('DOMContentLoaded', initApp);
