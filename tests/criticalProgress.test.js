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
import { questionService } from '../src/services/questionService.js';

test.beforeEach(() => {
  localStorage.clear();
  StorageService._cache.criticalProgress = null;
});

test('CriticalProgress - Default structure initializes correctly', () => {
  const prog = StorageService.getCriticalProgress();
  assert.equal(prog.lastIndex, 0);
  assert.deepEqual(prog.answers, {});
});

test('CriticalProgress - Save and retrieve critical answers and lastIndex', () => {
  const criticalList = questionService.getCriticalQuestions();
  assert.equal(criticalList.length, 60);

  const q1 = criticalList[0];
  const q2 = criticalList[1];

  StorageService.saveCriticalAnswer(q1.id, 2, 0);
  StorageService.saveCriticalAnswer(q2.id, 1, 1);

  const prog = StorageService.getCriticalProgress();
  assert.equal(prog.answers[q1.id], 2);
  assert.equal(prog.answers[q2.id], 1);
  assert.equal(prog.lastIndex, 1);

  // Clear cache to verify persistence in localStorage
  StorageService._cache.criticalProgress = null;
  const reloaded = StorageService.getCriticalProgress();
  assert.equal(reloaded.answers[q1.id], 2);
  assert.equal(reloaded.answers[q2.id], 1);
  assert.equal(reloaded.lastIndex, 1);
});

test('CriticalProgress - Save lastIndex independently', () => {
  StorageService.saveCriticalLastIndex(25);
  assert.equal(StorageService.getCriticalProgress().lastIndex, 25);

  StorageService._cache.criticalProgress = null;
  assert.equal(StorageService.getCriticalProgress().lastIndex, 25);
});

test('CriticalProgress - Remove single question answer', () => {
  const criticalList = questionService.getCriticalQuestions();
  const q1 = criticalList[0];
  const q2 = criticalList[1];

  StorageService.saveCriticalAnswer(q1.id, 1);
  StorageService.saveCriticalAnswer(q2.id, 2);

  assert.equal(StorageService.getCriticalProgress().answers[q1.id], 1);
  assert.equal(StorageService.getCriticalProgress().answers[q2.id], 2);

  StorageService.removeCriticalAnswer(q1.id);

  const updated = StorageService.getCriticalProgress();
  assert.equal(updated.answers[q1.id], undefined);
  assert.equal(updated.answers[q2.id], 2);
});

test('CriticalProgress - Reset critical progress', () => {
  const criticalList = questionService.getCriticalQuestions();
  StorageService.saveCriticalAnswer(criticalList[0].id, 1, 5);
  StorageService.saveCriticalAnswer(criticalList[1].id, 2, 6);

  StorageService.resetCriticalProgress();

  const resetProg = StorageService.getCriticalProgress();
  assert.deepEqual(resetProg.answers, {});
  assert.equal(resetProg.lastIndex, 0);

  // Check persistence
  StorageService._cache.criticalProgress = null;
  const reloaded = StorageService.getCriticalProgress();
  assert.deepEqual(reloaded.answers, {});
  assert.equal(reloaded.lastIndex, 0);
});

test('CriticalProgress - Calculate statistics correctly', () => {
  const criticalList = questionService.getCriticalQuestions();
  assert.equal(criticalList.length, 60);

  const q1 = criticalList[0];
  const q2 = criticalList[1];
  const q3 = criticalList[2];

  const correctOpt1 = Number(q1.correct_option);
  const wrongOpt2 = Number(q2.correct_option) === 1 ? 2 : 1;
  const correctOpt3 = Number(q3.correct_option);

  StorageService.saveCriticalAnswer(q1.id, correctOpt1);
  StorageService.saveCriticalAnswer(q2.id, wrongOpt2);
  StorageService.saveCriticalAnswer(q3.id, correctOpt3);

  const stats = StorageService.getCriticalStats(criticalList);
  assert.equal(stats.total, 60);
  assert.equal(stats.answered, 3);
  assert.equal(stats.correct, 2);
  assert.equal(stats.wrong, 1);
  assert.equal(stats.remaining, 57);
  assert.equal(stats.percent, 5); // Math.round(3 / 60 * 100) = 5%
  assert.equal(stats.isCompleted, false);
  assert.equal(stats.isAllCorrect, false);
});

