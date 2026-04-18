# student_profile.py
# Persists student name, selected domains/topics, and weak topics to remind them next session.
# Saves to data/student_profile.json

import json
import os

PROFILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'student_profile.json')


def load_profile():
    """Load existing student profile. Returns None if not found."""
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH, 'r') as f:
            return json.load(f)
    return None


def save_profile(name, selected_topics, weak_topics=None):
    """
    Save student profile.
    selected_topics: list of {domain, topic}
    weak_topics: list of {domain, topic, priority, advice} — persisted to remind next session
    """
    os.makedirs(os.path.dirname(PROFILE_PATH), exist_ok=True)
    profile = {
        "name": name,
        "selected_topics": selected_topics,
        "weak_topics": weak_topics or []
    }
    with open(PROFILE_PATH, 'w') as f:
        json.dump(profile, f, indent=2)
    return profile


def update_weak_topics(weak_topics):
    """Update only the weak topics in existing profile."""
    profile = load_profile()
    if profile:
        profile["weak_topics"] = weak_topics
        with open(PROFILE_PATH, 'w') as f:
            json.dump(profile, f, indent=2)


def clear_profile():
    if os.path.exists(PROFILE_PATH):
        os.remove(PROFILE_PATH)
