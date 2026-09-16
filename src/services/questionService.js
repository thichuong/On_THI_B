/**
 * Question Service: Repository and indexer for the 600 questions dataset.
 */
import questionsData from '../data/questions.json' with { type: 'json' };

export const CHAPTERS = [
  { id: 1, name: 'Chương 1: Quy định & Quy tắc chung (1 - 180)', shortName: 'Chương 1', startId: 1, endId: 180, count: 180 },
  { id: 2, name: 'Chương 2: Văn hóa & Đạo đức lái xe (181 - 205)', shortName: 'Chương 2', startId: 181, endId: 205, count: 25 },
  { id: 3, name: 'Chương 3: Kỹ thuật lái xe (206 - 263)', shortName: 'Chương 3', startId: 206, endId: 263, count: 58 },
  { id: 4, name: 'Chương 4: Cấu tạo & Sửa chữa (264 - 300)', shortName: 'Chương 4', startId: 264, endId: 300, count: 37 },
  { id: 5, name: 'Chương 5: Báo hiệu đường bộ (301 - 485)', shortName: 'Chương 5', startId: 301, endId: 485, count: 185 },
  { id: 6, name: 'Chương 6: Giải thế Sa hình (486 - 600)', shortName: 'Chương 6', startId: 486, endId: 600, count: 115 }
];

class QuestionService {
  constructor() {
    this.questions = questionsData || [];
    this.byId = new Map();
    this.byChapter = new Map();
    this.criticalQuestions = [];
    this.questionsWithImages = [];

    this._indexData();
  }

  _indexData() {
    this.questions.forEach(q => {
      this.byId.set(q.id, q);

      if (!this.byChapter.has(q.chapter)) {
        this.byChapter.set(q.chapter, []);
      }
      this.byChapter.get(q.chapter).push(q);

      if (q.is_critical) {
        this.criticalQuestions.push(q);
      }

      if (q.image) {
        this.questionsWithImages.push(q);
      }
    });
  }

  getAll() {
    return this.questions;
  }

  getById(id) {
    return this.byId.get(Number(id)) || null;
  }

  getByIds(ids = []) {
    const idSet = new Set(ids.map(Number));
    return this.questions.filter(q => idSet.has(q.id));
  }

  getCriticalQuestions() {
    return this.criticalQuestions;
  }

  getQuestionsWithImages() {
    return this.questionsWithImages;
  }

  getByChapter(chapterId) {
    return this.byChapter.get(Number(chapterId)) || [];
  }

  getChapters() {
    return CHAPTERS;
  }

  getChapterInfo(chapterId) {
    return CHAPTERS.find(c => c.id === Number(chapterId)) || CHAPTERS[0];
  }

  /**
   * Search questions by query keyword and filter
   * @param {string} query
   * @param {'all' | 'critical' | 'with_image'} filterType
   * @returns {Array}
   */
  search(query = '', filterType = 'all') {
    const q = query.toLowerCase().trim();

    return this.questions.filter(item => {
      // Check query match
      if (q) {
        const matchesId = String(item.id).includes(q);
        const matchesQuestion = item.question.toLowerCase().includes(q);
        const matchesOptions = item.options.some(opt => opt.toLowerCase().includes(q));
        const matchesExplanation = item.explanation && item.explanation.toLowerCase().includes(q);

        if (!matchesId && !matchesQuestion && !matchesOptions && !matchesExplanation) {
          return false;
        }
      }

      // Check filter type
      if (filterType === 'critical') return item.is_critical;
      if (filterType === 'with_image') return !!item.image;

      return true;
    });
  }
}

export const questionService = new QuestionService();
