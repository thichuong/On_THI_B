import test from 'node:test';
import assert from 'node:assert/strict';

// Mock localStorage for Node.js environment before importing services
globalThis.localStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = String(v); },
  removeItem(k) { delete this.store[k]; },
  clear() { this.store = {}; }
};

import { QuestionCard } from '../src/components/QuestionCard.js';

test('QuestionCard - Render explanation with line breaks and pre-line structure', () => {
  const mockQuestion = {
    id: 486,
    question: 'Theo hướng mũi tên, xe nào chấp hành đúng quy tắc giao thông?',
    chapter: 6,
    chapter_name: 'Sa hình',
    options: ['Xe khách', 'Xe tải', 'Chỉ xe con'],
    correct_option: 3,
    is_critical: false,
    explanation: 'Dòng 1: Phân tích đèn tín hiệu:\n- Xe khách sai\n- Xe con đúng.\nDo đó chọn xe con.'
  };

  const html = QuestionCard.render({
    question: mockQuestion,
    currentIndex: 0,
    totalQuestions: 1,
    isSubmitted: true,
    isReviewMode: true
  });

  // Verify explanation box is rendered
  assert.ok(html.includes('class="explanation-box"'), 'Must contain explanation-box');
  
  // Verify correct answer is separated in its own container
  assert.ok(html.includes('class="explanation-correct-answer"'), 'Must contain explanation-correct-answer');
  assert.ok(html.includes('Đáp án đúng: Ý số 3.'), 'Must display correct option number');

  // Verify explanation text is inside .explanation-text and contains newlines
  assert.ok(html.includes('class="explanation-text"'), 'Must contain explanation-text container');
  assert.ok(html.includes('Dòng 1: Phân tích đèn tín hiệu:\n- Xe khách sai\n- Xe con đúng.\nDo đó chọn xe con.'), 'Must preserve \\n newlines in explanation-text');
});

test('QuestionCard - Escaping HTML in multi-line explanation', () => {
  const mockQuestion = {
    id: 999,
    question: 'Câu hỏi test ký tự đặc biệt',
    chapter: 1,
    options: ['A', 'B'],
    correct_option: 1,
    is_critical: false,
    explanation: 'Quy tắc ưu tiên:\nXe tải -> Máy kéo -> Rơ moóc\nĐiều kiện: Tốc độ < 50km/h & chiều cao > 2m'
  };

  const html = QuestionCard.render({
    question: mockQuestion,
    currentIndex: 0,
    totalQuestions: 1,
    isSubmitted: true,
    isReviewMode: true
  });

  assert.ok(html.includes('&lt; 50km/h'), 'Must escape < to &lt;');
  assert.ok(html.includes('&gt; 2m'), 'Must escape > to &gt;');
  assert.ok(html.includes('&amp;'), 'Must escape & to &amp;');
  assert.ok(html.includes('\n'), 'Must retain newlines in explanation-text');
});

test('QuestionCard - Does not render explanation when not revealed', () => {
  const mockQuestion = {
    id: 1,
    question: 'Câu hỏi chưa làm',
    chapter: 1,
    options: ['A', 'B'],
    correct_option: 1,
    is_critical: false,
    explanation: 'Lời giải thích câu 1'
  };

  const html = QuestionCard.render({
    question: mockQuestion,
    currentIndex: 0,
    totalQuestions: 1,
    isSubmitted: false,
    isReviewMode: false,
    isPractice: false,
    userAnswer: null
  });

  assert.ok(!html.includes('class="explanation-box"'), 'Must NOT contain explanation-box when hidden');
});

