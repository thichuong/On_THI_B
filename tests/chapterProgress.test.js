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
  StorageService._cache.chapterProgress = null;
});

test('ChapterProgress - Default structure initializes all 6 chapters', () => {
  const allProg = StorageService.getAllChapterProgress();
  assert.equal(allProg.lastActiveChapter, 1);
  assert.ok(allProg.chapters, 'chapters object must exist');

  for (let ch = 1; ch <= 6; ch++) {
    const chProg = StorageService.getChapterProgress(ch);
    assert.equal(chProg.lastIndex, 0);
    assert.deepEqual(chProg.answers, {});
  }
});

test('ChapterProgress - Active chapter persistence', () => {
  assert.equal(StorageService.getActiveChapter(), 1);

  StorageService.saveActiveChapter(4);
  assert.equal(StorageService.getActiveChapter(), 4);

  // Re-reading from clean cache confirms localStorage persistence
  StorageService._cache.chapterProgress = null;
  assert.equal(StorageService.getActiveChapter(), 4);
});

test('ChapterProgress - Save and retrieve chapter answers and lastIndex', () => {
  StorageService.saveChapterAnswer(1, 10, 2, 5);
  StorageService.saveChapterAnswer(1, 11, 3, 6);

  const progCh1 = StorageService.getChapterProgress(1);
  assert.equal(progCh1.answers[10], 2);
  assert.equal(progCh1.answers[11], 3);
  assert.equal(progCh1.lastIndex, 6);

  // Ensure persisted in localStorage
  StorageService._cache.chapterProgress = null;
  const reloaded = StorageService.getChapterProgress(1);
  assert.equal(reloaded.answers[10], 2);
  assert.equal(reloaded.answers[11], 3);
  assert.equal(reloaded.lastIndex, 6);
});

test('ChapterProgress - Remove single question answer', () => {
  StorageService.saveChapterAnswer(2, 185, 1);
  StorageService.saveChapterAnswer(2, 186, 2);

  assert.equal(StorageService.getChapterProgress(2).answers[185], 1);
  assert.equal(StorageService.getChapterProgress(2).answers[186], 2);

  StorageService.removeChapterAnswer(2, 185);

  const updated = StorageService.getChapterProgress(2);
  assert.equal(updated.answers[185], undefined);
  assert.equal(updated.answers[186], 2);
});

test('ChapterProgress - Chapter independence and resetting single chapter', () => {
  // Populate Chapter 1
  StorageService.saveChapterAnswer(1, 1, 1, 3);
  StorageService.saveChapterAnswer(1, 2, 2, 3);

  // Populate Chapter 3
  StorageService.saveChapterAnswer(3, 210, 4, 8);

  // Reset Chapter 1 only
  StorageService.resetChapterProgress(1);

  const ch1 = StorageService.getChapterProgress(1);
  assert.deepEqual(ch1.answers, {});
  assert.equal(ch1.lastIndex, 0);

  // Chapter 3 must be untouched
  const ch3 = StorageService.getChapterProgress(3);
  assert.equal(ch3.answers[210], 4);
  assert.equal(ch3.lastIndex, 8);
});

test('ChapterProgress - Calculate chapter statistics correctly', () => {
  // Chapter 2 has 25 questions (IDs 181 - 205)
  const ch2Questions = questionService.getByChapter(2);
  assert.equal(ch2Questions.length, 25);

  const q1 = ch2Questions[0];
  const q2 = ch2Questions[1];

  // Answer q1 correctly, answer q2 incorrectly
  const correctOpt = Number(q1.correct_option);
  const wrongOpt = correctOpt === 1 ? 2 : 1;

  StorageService.saveChapterAnswer(2, q1.id, correctOpt);
  StorageService.saveChapterAnswer(2, q2.id, wrongOpt);

  const stats = StorageService.getChapterStats(2, ch2Questions);
  assert.equal(stats.total, 25);
  assert.equal(stats.answered, 2);
  assert.equal(stats.correct, 1);
  assert.equal(stats.wrong, 1);
  assert.equal(stats.remaining, 23);
  assert.equal(stats.percent, 8); // Math.round(2 / 25 * 100) = 8%
});

