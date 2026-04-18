# ml_model.py
# Real ML layer for LearnWise
#
# Model 1 — K-Means Clustering
#   Input:  accuracy, avg_time, weakness_score per topic
#   Output: learning profile → "Struggling" / "Developing" / "Strong"
#
# Model 2 — Decision Tree Classifier
#   Input:  accuracy_so_far, avg_time_so_far, difficulty_encoded, topic_attempt_count
#   Output: recommended difficulty for next question (easy / medium / hard)

import numpy as np
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")


# ─── CLUSTER LABELS (ordered from worst to best) ───────────────────────────
CLUSTER_NAMES = ["Struggling", "Developing", "Strong"]

# ─── DIFFICULTY ENCODING ────────────────────────────────────────────────────
DIFFICULTY_MAP = {"easy": 0, "medium": 1, "hard": 2}
DIFFICULTY_REVERSE = {0: "easy", 1: "medium", 2: "hard"}


# ════════════════════════════════════════════════════════════
#  MODEL 1 — K-Means: Student Learning Profile
# ════════════════════════════════════════════════════════════

class StudentProfiler:
    """
    Clusters a student's topic-level performance into 3 learning profiles.
    Uses K-Means on [accuracy, avg_time_normalized, weakness_score].
    No hardcoded thresholds — model finds the boundaries itself.
    """

    def __init__(self, n_clusters=3):
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.fitted = False
        self._cluster_order = None  # maps cluster id → meaningful label index

    def fit_and_predict(self, metrics_df):
        """
        Takes the metrics DataFrame from model.py (after calculate_weakness)
        Returns the same df with 'profile' column added.
        """
        if len(metrics_df) < self.n_clusters:
            # Not enough data — assign profiles by weakness score directly
            metrics_df = metrics_df.copy()
            metrics_df['profile'] = metrics_df['weakness_score'].apply(
                lambda s: "Struggling" if s > 1.2 else ("Developing" if s > 0.7 else "Strong")
            )
            metrics_df['cluster_id'] = -1
            return metrics_df

        features = metrics_df[['accuracy', 'avg_time', 'weakness_score']].copy()

        # Normalize avg_time to same scale as accuracy (0-1 range approx)
        max_time = features['avg_time'].max()
        features['avg_time'] = features['avg_time'] / max_time if max_time > 0 else features['avg_time']

        # Fill any NaN with 0 to be safe
        features = features.fillna(0)

        self.model.fit(features)
        labels = self.model.labels_

        # Figure out which cluster = which profile
        # Higher weakness_score cluster = Struggling
        metrics_df = metrics_df.copy()
        metrics_df['cluster_id'] = labels

        cluster_avg_weakness = (
            metrics_df.groupby('cluster_id')['weakness_score'].mean()
            .sort_values()  # ascending: lowest weakness = Strong
        )

        # Map: lowest weakness → Strong (index 2), highest → Struggling (index 0)
        self._cluster_order = {}
        label_names = ["Strong", "Developing", "Struggling"]
        for rank, cid in enumerate(cluster_avg_weakness.index):
            self._cluster_order[cid] = label_names[rank]

        metrics_df['profile'] = metrics_df['cluster_id'].map(self._cluster_order)
        self.fitted = True
        return metrics_df

    def get_overall_profile(self, profiled_df):
        """Returns the student's dominant learning profile across all topics."""
        if 'profile' not in profiled_df.columns:
            return "Developing"
        counts = profiled_df['profile'].value_counts()
        return counts.idxmax()


# ════════════════════════════════════════════════════════════
#  MODEL 2 — Decision Tree: Adaptive Difficulty
# ════════════════════════════════════════════════════════════

class AdaptiveDifficulty:
    """
    Decides what difficulty the NEXT question should be.
    Trains a Decision Tree on session history.
    
    Features: [accuracy_so_far, avg_time_so_far, current_difficulty, streak]
    Target:   next_difficulty (easy=0, medium=1, hard=2)
    """

    def __init__(self):
        self.model = DecisionTreeClassifier(max_depth=4, random_state=42)
        self.fitted = False

    def _generate_training_data(self):
        """
        Synthetic but logically sound training data.
        In production this would come from real session history.
        Rules encoded:
          - High accuracy + fast time → increase difficulty
          - Low accuracy → decrease difficulty
          - Medium performance → stay same or go medium
        """
        np.random.seed(42)
        X, y = [], []

        # Strong performer → harder questions
        for _ in range(80):
            acc = np.random.uniform(0.75, 1.0)
            time = np.random.uniform(10, 35)
            curr_diff = np.random.choice([0, 1])
            streak = np.random.randint(2, 6)
            X.append([acc, time, curr_diff, streak])
            y.append(min(curr_diff + 1, 2))  # go harder

        # Average performer → stay medium
        for _ in range(80):
            acc = np.random.uniform(0.45, 0.75)
            time = np.random.uniform(30, 60)
            curr_diff = np.random.choice([0, 1, 2])
            streak = np.random.randint(0, 3)
            X.append([acc, time, curr_diff, streak])
            y.append(1)  # medium

        # Struggling → easier questions
        for _ in range(80):
            acc = np.random.uniform(0.0, 0.45)
            time = np.random.uniform(50, 120)
            curr_diff = np.random.choice([1, 2])
            streak = 0
            X.append([acc, time, curr_diff, streak])
            y.append(max(curr_diff - 1, 0))  # go easier

        return np.array(X), np.array(y)

    def train(self):
        X, y = self._generate_training_data()
        self.model.fit(X, y)
        self.fitted = True

    def predict_next_difficulty(self, accuracy_so_far, avg_time_so_far,
                                 current_difficulty="medium", correct_streak=0):
        """
        Returns: 'easy', 'medium', or 'hard'
        Call this after each answer to get next question's difficulty.
        """
        if not self.fitted:
            self.train()

        diff_encoded = DIFFICULTY_MAP.get(current_difficulty, 1)
        features = np.array([[accuracy_so_far, avg_time_so_far,
                               diff_encoded, correct_streak]])
        pred = self.model.predict(features)[0]
        return DIFFICULTY_REVERSE[pred]

    def get_difficulty_explanation(self, difficulty):
        explanations = {
            "easy":   "Taking it step by step — building your confidence.",
            "medium": "Balanced challenge — you're in the zone.",
            "hard":   "Pushing your limits — you're ready for this!"
        }
        return explanations.get(difficulty, "")


# ════════════════════════════════════════════════════════════
#  ROADMAP GENERATOR
# ════════════════════════════════════════════════════════════

RESOURCES = {
    "Machine Learning": {
        "Supervised Learning":  {"book": "Hands-On ML – Aurélien Géron", "link": "https://scikit-learn.org/stable/supervised_learning.html", "days": 5},
        "Neural Networks":      {"book": "Deep Learning – Goodfellow et al.", "link": "https://www.deeplearningbook.org", "days": 7},
        "Model Evaluation":     {"book": "Introduction to Statistical Learning", "link": "https://developers.google.com/machine-learning/crash-course", "days": 3},
    },
    "Web Development": {
        "HTML & CSS":   {"book": "MDN Web Docs", "link": "https://developer.mozilla.org/en-US/docs/Learn", "days": 3},
        "JavaScript":   {"book": "You Don't Know JS – Kyle Simpson", "link": "https://javascript.info", "days": 6},
        "React":        {"book": "React Docs (official)", "link": "https://react.dev/learn", "days": 5},
    },
    "Data Structures & Algorithms": {
        "Arrays & Strings":     {"book": "CLRS – Introduction to Algorithms", "link": "https://neetcode.io", "days": 4},
        "Trees & Graphs":       {"book": "CLRS – Introduction to Algorithms", "link": "https://visualgo.net", "days": 5},
        "Dynamic Programming":  {"book": "Dynamic Programming for Coding Interviews", "link": "https://leetcode.com/tag/dynamic-programming", "days": 7},
    },
    "Database Systems": {
        "SQL":              {"book": "Learning SQL – Alan Beaulieu", "link": "https://sqlzoo.net", "days": 4},
        "Database Design":  {"book": "Database Design for Mere Mortals", "link": "https://www.lucidchart.com/pages/er-diagrams", "days": 3},
    },
    "Operating Systems": {
        "Processes & Threads":  {"book": "Operating System Concepts – Silberschatz", "link": "https://pages.cs.wisc.edu/~remzi/OSTEP", "days": 5},
        "Memory Management":    {"book": "Operating System Concepts – Silberschatz", "link": "https://pages.cs.wisc.edu/~remzi/OSTEP/vm-intro.pdf", "days": 4},
    },
    "Computer Networks": {
        "Network Basics":   {"book": "Computer Networks – Tanenbaum", "link": "https://www.cloudflare.com/learning/network-layer/what-is-a-network", "days": 4},
        "Security":         {"book": "The Web Application Hacker's Handbook", "link": "https://owasp.org/www-project-top-ten", "days": 5},
    },
    "Mathematics": {
        "Linear Algebra":           {"book": "Linear Algebra – Gilbert Strang (MIT OCW)", "link": "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010", "days": 6},
        "Probability & Statistics": {"book": "Statistics – Freedman, Pisani, Purves", "link": "https://seeing-theory.brown.edu", "days": 5},
    },
    "Software Engineering": {
        "Design Patterns":  {"book": "Design Patterns – Gang of Four", "link": "https://refactoring.guru/design-patterns", "days": 5},
        "Version Control":  {"book": "Pro Git – Scott Chacon", "link": "https://learngitbranching.js.org", "days": 2},
    },
}

DEFAULT_RESOURCE = {"book": "Search on Google Scholar", "link": "https://scholar.google.com", "days": 4}


def generate_roadmap(profiled_df):
    """
    Takes profiled_df (output of StudentProfiler.fit_and_predict)
    Returns a list of roadmap items ordered by priority.

    Each item:
    {
        domain, topic, priority, weakness_score, profile,
        days_to_spend, resource_book, resource_link, advice
    }
    """
    roadmap = []

    priority_map = {
        "Struggling":  ("🔴 HIGH",   "Revise fundamentals immediately before moving forward."),
        "Developing":  ("🟡 MEDIUM", "Practice more problems and revisit core concepts."),
        "Strong":      ("🟢 LOW",    "You're solid here. Quick revision before exams is enough."),
    }

    for _, row in profiled_df.iterrows():
        domain = row['subject']   # 'subject' col from model.py = domain
        topic = row['topic']
        profile = row.get('profile', 'Developing')

        priority_label, advice = priority_map.get(profile, ("🟡 MEDIUM", "Keep practicing."))

        res = RESOURCES.get(domain, {}).get(topic, DEFAULT_RESOURCE)

        roadmap.append({
            "domain":          domain,
            "topic":           topic,
            "priority":        priority_label,
            "weakness_score":  round(row['weakness_score'], 3),
            "profile":         profile,
            "days_to_spend":   res["days"],
            "resource_book":   res["book"],
            "resource_link":   res["link"],
            "advice":          advice,
        })

    # Sort: Struggling first, then Developing, then Strong
    order = {"🔴 HIGH": 0, "🟡 MEDIUM": 1, "🟢 LOW": 2}
    roadmap.sort(key=lambda x: order.get(x['priority'], 1))

    return roadmap
