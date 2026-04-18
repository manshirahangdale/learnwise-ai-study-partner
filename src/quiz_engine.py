# quiz_engine.py
# Manages one quiz session per topic.
# Uses AdaptiveDifficulty (Decision Tree) to pick next question difficulty.

import time
import random
from question_bank import get_questions, get_questions_by_difficulty
from ml_model import AdaptiveDifficulty, DIFFICULTY_MAP


class QuizSession:
    """
    One quiz session for a single (domain, topic) pair.

    Flow:
      1. session = QuizSession(domain, topic, n_questions=5)
      2. while session.has_next():
             q = session.current_question()
             session.start_timer()
             correct = session.submit_answer(user_answer)
      3. score, total, results = session.get_summary()
    """

    def __init__(self, domain, topic, n_questions=5):
        self.domain = domain
        self.topic = topic
        self.n_questions = n_questions

        self._adaptive = AdaptiveDifficulty()
        self._adaptive.train()  # train DT on synthetic data

        self._all_questions = get_questions(domain, topic)
        random.shuffle(self._all_questions)

        self._served = []        # questions asked so far
        self._results = []       # answer records
        self._start_time = None
        self._current_q = None
        self._current_difficulty = "easy"  # start easy
        self._correct_streak = 0

        # Load first question
        self._load_next_question()

    # ── INTERNAL ──────────────────────────────────────────────
    def _load_next_question(self):
        """Pick next question at the recommended difficulty."""
        if len(self._served) >= self.n_questions:
            self._current_q = None
            return

        # Get questions at recommended difficulty not yet seen
        candidates = [
            q for q in self._all_questions
            if q not in self._served and q['difficulty'] == self._current_difficulty
        ]

        # Fallback: if no questions at that difficulty, use any unseen
        if not candidates:
            candidates = [q for q in self._all_questions if q not in self._served]

        if not candidates:
            self._current_q = None
            return

        self._current_q = random.choice(candidates)
        self._served.append(self._current_q)

    def _update_difficulty(self, is_correct):
        """After each answer, ask the Decision Tree what to serve next."""
        total = len(self._results)
        if total == 0:
            return

        acc_so_far = sum(r['correct'] for r in self._results) / total
        avg_time_so_far = sum(r['time_taken'] for r in self._results) / total

        self._current_difficulty = self._adaptive.predict_next_difficulty(
            accuracy_so_far=acc_so_far,
            avg_time_so_far=avg_time_so_far,
            current_difficulty=self._current_difficulty,
            correct_streak=self._correct_streak
        )

    # ── PUBLIC API ────────────────────────────────────────────

    def has_next(self):
        return self._current_q is not None and len(self._served) <= self.n_questions

    def current_question(self):
        return self._current_q

    def current_difficulty(self):
        return self._current_difficulty

    def difficulty_explanation(self):
        return self._adaptive.get_difficulty_explanation(self._current_difficulty)

    def start_timer(self):
        self._start_time = time.time()

    def submit_answer(self, selected_option):
        """
        Submit user's answer. Returns True if correct.
        Internally updates adaptive difficulty for next question.
        """
        elapsed = round(time.time() - self._start_time, 2) if self._start_time else 30.0
        q = self._current_q
        is_correct = int(selected_option.strip() == q["answer"].strip())

        if is_correct:
            self._correct_streak += 1
        else:
            self._correct_streak = 0

        self._results.append({
            "subject":    self.domain,   # named 'subject' to match model.py
            "topic":      self.topic,
            "difficulty": q["difficulty"],
            "correct":    is_correct,
            "time_taken": elapsed,
        })

        self._update_difficulty(is_correct)
        self._load_next_question()
        return bool(is_correct)

    def get_summary(self):
        """Returns (score, total, results_list)"""
        score = sum(r['correct'] for r in self._results)
        return score, len(self._results), self._results

    def progress(self):
        """Returns (answered, total) for progress bar."""
        return len(self._results), self.n_questions

    def total_questions(self):
        return self.n_questions