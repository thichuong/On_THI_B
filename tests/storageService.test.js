import test from 'node:test';
import assert from 'node:assert/strict';

// Mock localStorage for Node.js environment
globalThis.localStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = String(v); },
  removeItem(k) { delete this.store[k]; },
  clear() { this.store = {}; }
};

import { StorageService } from '../src/services/storageService.js';

test.beforeEach(() => {
  localStorage.clear();
});

test('StorageService - Record and retrieve wrong questions', () => {
  StorageService.recordWrongQuestion(101);
  StorageService.recordWrongQuestion(102);
  StorageService.recordWrongQuestion(101); // wrong twice

  const wrongMap = StorageService.getWrongQuestions();
  assert.equal(wrongMap[101], 2);
  assert.equal(wrongMap[102], 1);

  const ids = StorageService.getWrongQuestionIds();
  assert.ok(ids.includes(101));
  assert.ok(ids.includes(102));
});

test('StorageService - Remove wrong question (removeWrongQuestion)', () => {
  StorageService.recordWrongQuestion(55);
  StorageService.recordWrongQuestion(77);

  const removed = StorageService.removeWrongQuestion(55);
  assert.equal(removed, true, 'Should return true when existing question is removed');

  const wrongMap = StorageService.getWrongQuestions();
  assert.equal(wrongMap[55], undefined, 'Question 55 must no longer be in wrong questions');
  assert.equal(wrongMap[77], 1, 'Question 77 must remain');

  const removedAgain = StorageService.removeWrongQuestion(55);
  assert.equal(removedAgain, false, 'Removing non-existent question should return false');
});

test('StorageService - Record correct question (recordCorrectQuestion decrements & deletes)', () => {
  StorageService.recordWrongQuestion(99); // count = 1
  StorageService.recordCorrectQuestion(99); // decrements to 0 -> should delete

  const wrongMap = StorageService.getWrongQuestions();
  assert.equal(wrongMap[99], undefined);
});

test('StorageService - Exam Cycle tracking and status', () => {
  StorageService.resetExamCycle('standard');
  let status = StorageService.getCycleStatus('standard', 600);
  assert.equal(status.seenCount, 0);
  assert.equal(status.remainingCount, 600);

  // Add 50 questions
  const first50 = Array.from({ length: 50 }, (_, i) => i + 1);
  StorageService.addSeenExamQuestionIds('standard', first50);

  status = StorageService.getCycleStatus('standard', 600);
  assert.equal(status.seenCount, 50);
  assert.equal(status.remainingCount, 550);

  // Reset cycle
  StorageService.resetExamCycle('standard');
  status = StorageService.getCycleStatus('standard', 600);
  assert.equal(status.seenCount, 0);
  assert.equal(status.remainingCount, 600);
});

test('StorageService - Bookmarks toggle', () => {
  assert.equal(StorageService.isBookmarked(1), false);

  const marked = StorageService.toggleBookmark(1);
  assert.equal(marked, true);
  assert.equal(StorageService.isBookmarked(1), true);

  const unmarked = StorageService.toggleBookmark(1);
  assert.equal(unmarked, false);
  assert.equal(StorageService.isBookmarked(1), false);
});

