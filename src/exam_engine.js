/**
 * Exam Engine: Generates balanced mock exams with guaranteed critical questions,
 * handles shuffling, timer state, and official grading logic.
 */

export class ExamEngine {
  /**
   * Generates a 30-question mock test from the full dataset.
   * Guarantees at least 1-2 critical questions and balances topics across 6 chapters.
   *
   * @param {Array} allQuestions Full list of 600 questions
   * @param {Object} options Configuration options
   * @returns {Array} Array of 30 questions for the exam
   */
  static generate30QuestionExam(allQuestions, options = {}) {
    const {
      minCritical = 1,
      maxCritical = 2,
      shuffleQuestions = true,
      shuffleOptions = false
    } = options;

    // Filter into categories
    const criticalQuestions = allQuestions.filter(q => q.is_critical);
    const nonCriticalQuestions = allQuestions.filter(q => !q.is_critical);

    // Group non-critical by chapter
    const byChapter = {
      1: nonCriticalQuestions.filter(q => q.chapter === 1), // Luật & Quy tắc
      2: nonCriticalQuestions.filter(q => q.chapter === 2), // Văn hóa & Đạo đức
      3: nonCriticalQuestions.filter(q => q.chapter === 3), // Kỹ thuật lái xe
      4: nonCriticalQuestions.filter(q => q.chapter === 4), // Cấu tạo & Sửa chữa
      5: nonCriticalQuestions.filter(q => q.chapter === 5), // Biển báo
      6: nonCriticalQuestions.filter(q => q.chapter === 6), // Sa hình
    };

    // 1. Pick 1 or 2 critical questions randomly
    const criticalCount = Math.floor(Math.random() * (maxCritical - minCritical + 1)) + minCritical;
    const shuffledCritical = this.shuffleArray([...criticalQuestions]);
    const selectedCritical = shuffledCritical.slice(0, criticalCount);
    const selectedIds = new Set(selectedCritical.map(q => q.id));

    // 2. Desired distribution for remaining (30 - criticalCount) questions:
    // Chapter 1: ~7 questions
    // Chapter 2: ~1 question
    // Chapter 3: ~2 questions
    // Chapter 4: ~1 question
    // Chapter 5: ~10 questions
    // Chapter 6: ~8 questions
    // Total: 29 + 1 critical = 30
    const chapterQuotas = {
      1: 7 - (selectedCritical.filter(q => q.chapter === 1).length),
      2: 1,
      3: 2,
      4: 1,
      5: 10,
      6: 8
    };

    let selectedOthers = [];
    for (const [ch, quota] of Object.entries(chapterQuotas)) {
      const pool = byChapter[ch] || [];
      const available = pool.filter(q => !selectedIds.has(q.id));
      const shuffledPool = this.shuffleArray([...available]);
      const needed = Math.max(0, quota);
      const chosen = shuffledPool.slice(0, needed);
      chosen.forEach(q => {
        selectedOthers.push(q);
        selectedIds.add(q.id);
      });
    }

    // Fill any gap to ensure exact 30 questions
    let totalNeeded = 30 - (selectedCritical.length + selectedOthers.length);
    if (totalNeeded > 0) {
      const remainingPool = nonCriticalQuestions.filter(q => !selectedIds.has(q.id));
      const extra = this.shuffleArray([...remainingPool]).slice(0, totalNeeded);
      selectedOthers.push(...extra);
    }

    let examSet = [...selectedCritical, ...selectedOthers];

    // Guarantee exact 30 questions
    if (examSet.length > 30) {
      examSet = examSet.slice(0, 30);
    }

    // Shuffle the order of questions in the exam if enabled
    if (shuffleQuestions) {
      examSet = this.shuffleArray(examSet);
    }

    // Prepare questions (with clone so original is untouched)
    return examSet.map((q, index) => {
      const examQ = {
        ...q,
        examIndex: index + 1
      };

      if (shuffleOptions) {
        // Shuffle options and update correct_option index
        const originalCorrectText = q.options[q.correct_option - 1];
        const indexedOptions = q.options.map((opt, i) => ({ text: opt, isCorrect: i + 1 === q.correct_option }));
        const shuffled = this.shuffleArray(indexedOptions);
        examQ.options = shuffled.map(o => o.text);
        examQ.correct_option = shuffled.findIndex(o => o.isCorrect) + 1;
      }

      return examQ;
    });
  }

  /**
   * Grades the exam and determines PASS / FAIL with critical failure check.
   *
   * @param {Array} examQuestions 30 questions in the test
   * @param {Object} userAnswers Map of { [questionId]: selectedOptionIndex }
   * @param {number} passThreshold Minimum score to pass (default: 26 for 30 questions)
   * @returns {Object} Grading summary
   */
  static gradeExam(examQuestions, userAnswers, passThreshold = 26) {
    let correctCount = 0;
    let wrongCount = 0;
    let unattemptedCount = 0;
    let failedCritical = false;
    let failedCriticalQuestions = [];
    const wrongQuestionIds = [];
    const questionResults = [];

    examQuestions.forEach((q, index) => {
      const userAnswer = userAnswers[q.id];
      const isAnswered = userAnswer !== undefined && userAnswer !== null;
      const isCorrect = isAnswered && Number(userAnswer) === Number(q.correct_option);

      if (!isAnswered) {
        unattemptedCount++;
        wrongQuestionIds.push(q.id);
      } else if (isCorrect) {
        correctCount++;
      } else {
        wrongCount++;
        wrongQuestionIds.push(q.id);
      }

      if (!isCorrect && q.is_critical) {
        failedCritical = true;
        failedCriticalQuestions.push({
          id: q.id,
          question: q.question,
          userAnswer: isAnswered ? userAnswer : 'Chưa trả lời',
          correctAnswer: q.correct_option,
          correctText: q.options[q.correct_option - 1]
        });
      }

      questionResults.push({
        id: q.id,
        examIndex: index + 1,
        question: q.question,
        image: q.image,
        options: q.options,
        userAnswer: isAnswered ? Number(userAnswer) : null,
        correctAnswer: Number(q.correct_option),
        isCorrect,
        isCritical: q.is_critical,
        explanation: q.explanation || (q.is_critical ? 'Câu điểm liệt - bắt buộc trả lời đúng!' : '')
      });
    });

    const passed = (correctCount >= passThreshold) && !failedCritical;

    return {
      total: examQuestions.length,
      score: correctCount,
      wrongCount,
      unattemptedCount,
      passThreshold,
      passed,
      failedCritical,
      failedCriticalQuestions,
      wrongQuestionIds,
      questionResults,
      percentage: Math.round((correctCount / examQuestions.length) * 100)
    };
  }

  /**
   * Helper: Durstenfeld shuffle algorithm
   */
  static shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }
}
