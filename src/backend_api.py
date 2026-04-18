# backend_api.py
# ─────────────────────────────────────────────────────────
# THE ONLY FILE YOUR TEAMMATE NEEDS TO IMPORT.
# She calls these functions from the Tkinter UI.
# No pandas, no sklearn, no ML knowledge required on her end.
# ─────────────────────────────────────────────────────────

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from model import calculate_metrics, calculate_weakness
from ml_model import StudentProfiler, generate_roadmap
from quiz_engine import QuizSession
from question_bank import get_domains, get_topics, get_questions
from student_profile import load_profile, save_profile, update_weak_topics


# ════════════════════════════════════════════════════════════
#  1. STUDENT PROFILE
# ════════════════════════════════════════════════════════════

def register_student(name, selected_topics):
    """
    Call on first launch / registration.

    selected_topics: list of dicts → [{"domain": "ML", "topic": "Neural Networks"}, ...]
    Returns: profile dict
    """
    return save_profile(name, selected_topics)


def get_student_profile():
    """
    Returns existing profile or None.
    UI uses this to decide: show Login screen vs Home screen.
    """
    return load_profile()


def get_available_domains():
    """Returns list of all available domains (for topic selection screen)."""
    return get_domains()


def get_available_topics(domain):
    """Returns list of topics for a given domain."""
    return get_topics(domain)


# ════════════════════════════════════════════════════════════
#  2. QUIZ SESSION
# ════════════════════════════════════════════════════════════

def start_quiz(domain, topic, n_questions=5):
    """
    Creates and returns a QuizSession object.
    UI holds this object for the duration of the quiz.

    Usage:
        session = start_quiz("Machine Learning", "Neural Networks")
        while session.has_next():
            q = session.current_question()
            # show q['q'], q['options'], q['difficulty']
            session.start_timer()
            correct = session.submit_answer(user_pick)
        score, total, results = session.get_summary()
    """
    return QuizSession(domain, topic, n_questions)


def get_current_question(session):
    """
    Returns current question dict:
    {
        'q': question text,
        'options': [list of 4 options],
        'answer': correct answer,
        'difficulty': 'easy'/'medium'/'hard'
    }
    """
    return session.current_question()


def submit_answer(session, selected_option):
    """
    Submit user's selected option.
    Returns: True if correct, False if wrong.
    Also internally updates adaptive difficulty.
    """
    return session.submit_answer(selected_option)


def get_quiz_progress(session):
    """Returns (answered, total) tuple for progress bar."""
    return session.progress()


def get_difficulty_status(session):
    """
    Returns current difficulty and a motivational message.
    UI can show this as a small tag next to the question.
    """
    return {
        "difficulty": session.current_difficulty(),
        "message":    session.difficulty_explanation()
    }


# ════════════════════════════════════════════════════════════
#  3. ANALYSIS & ROADMAP
# ════════════════════════════════════════════════════════════

def analyse_and_get_roadmap(all_session_results):
    """
    Call this after ALL quiz sessions are done (one per topic).

    all_session_results: flat list of result dicts from multiple sessions
        Each dict: {subject, topic, difficulty, correct, time_taken}

    Returns:
    {
        "overall_profile": "Struggling" / "Developing" / "Strong",
        "roadmap": [
            {
                domain, topic, priority, weakness_score, profile,
                days_to_spend, resource_book, resource_link, advice
            },
            ...
        ]
    }
    """
    df = pd.DataFrame(all_session_results)

    # Run your existing model.py pipeline
    metrics = calculate_metrics(df)
    weakness = calculate_weakness(metrics)

    # Run ML clustering
    profiler = StudentProfiler()
    profiled = profiler.fit_and_predict(weakness)
    overall = profiler.get_overall_profile(profiled)

    # Generate full roadmap
    roadmap = generate_roadmap(profiled)

    # Persist weak topics to profile
    weak = [
        {"domain": r["domain"], "topic": r["topic"],
         "priority": r["priority"], "advice": r["advice"]}
        for r in roadmap if "HIGH" in r["priority"] or "MEDIUM" in r["priority"]
    ]
    update_weak_topics(weak)

    return {
        "overall_profile": overall,
        "roadmap": roadmap
    }


def get_weak_topic_reminders():
    """
    Returns weak topics saved from last session.
    UI shows these on the home screen as reminders.
    Returns: list of {domain, topic, priority, advice}
    """
    profile = load_profile()
    if profile:
        return profile.get("weak_topics", [])
    return []


# ════════════════════════════════════════════════════════════
#  4. QUICK TEST — run this file directly to verify
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 55)
    print("  LearnWise Backend — Integration Test")
    print("=" * 55)

    # Step 1: Register
    profile = register_student("Manshi", [
        {"domain": "Machine Learning", "topic": "Neural Networks"},
        {"domain": "Data Structures & Algorithms", "topic": "Dynamic Programming"},
        {"domain": "Mathematics", "topic": "Probability & Statistics"},
    ])
    print(f"\n✅ Student registered: {profile['name']}")
    print(f"   Topics: {[t['topic'] for t in profile['selected_topics']]}")

    # Step 2: Simulate quiz sessions
    all_results = []
    test_topics = [
        ("Machine Learning", "Neural Networks"),
        ("Data Structures & Algorithms", "Dynamic Programming"),
        ("Mathematics", "Probability & Statistics"),
    ]

    import random
    for domain, topic in test_topics:
        session = start_quiz(domain, topic, n_questions=5)
        print(f"\n📝 Quiz: {domain} → {topic}")

        while session.has_next():
            q = get_current_question(session)
            session.start_timer()

            # Simulate answer (random for test)
            pick = random.choice(q['options'])
            correct = submit_answer(session, pick)
            answered, total = get_quiz_progress(session)
            status = get_difficulty_status(session)
            print(f"   Q{answered}/{total} [{q['difficulty']}] → {'✓' if correct else '✗'} | Next: {status['difficulty']}")

        score, total, results = session.get_summary()
        all_results.extend(results)
        print(f"   Score: {score}/{total}")

    # Step 3: Analyse
    print("\n🤖 Running ML analysis...")
    output = analyse_and_get_roadmap(all_results)

    print(f"\n🎓 Overall Learning Profile: {output['overall_profile']}")
    print("\n📍 Your Personalized Roadmap:")
    print("-" * 55)
    for item in output['roadmap']:
        print(f"\n{item['priority']}  {item['domain']} → {item['topic']}")
        print(f"   Profile:  {item['profile']}")
        print(f"   Weakness: {item['weakness_score']}")
        print(f"   Spend:    {item['days_to_spend']} days")
        print(f"   Book:     {item['resource_book']}")
        print(f"   Link:     {item['resource_link']}")
        print(f"   Advice:   {item['advice']}")

    # Step 4: Reminders
    reminders = get_weak_topic_reminders()
    print(f"\n🔔 Reminders saved for next session: {len(reminders)} weak topics")
    for r in reminders:
        print(f"   → {r['topic']} ({r['priority']})")