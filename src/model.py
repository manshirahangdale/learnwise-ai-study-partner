import pandas as pd


# ---------------- LOAD DATA ----------------
def load_data(path):
    return pd.read_csv(path)


# ---------------- METRICS ----------------
def calculate_metrics(df):
    grouped = df.groupby(['subject', 'topic'])

    result = grouped.agg(
        total_questions=('correct', 'count'),
        correct_answers=('correct', 'sum'),
        avg_time=('time_taken', 'mean')
    ).reset_index()

    result['accuracy'] = result['correct_answers'] / result['total_questions']

    return result


# ---------------- WEAKNESS SCORE ----------------
def calculate_weakness(result):
    result['weakness_score'] = (1 - result['accuracy']) + (result['avg_time'] / 100)
    return result.sort_values(by='weakness_score', ascending=False)


# ---------------- RECOMMENDATIONS ----------------
def generate_recommendations(df):
    recommendations = []

    for _, row in df.iterrows():
        if row['weakness_score'] > 1.2:
            level = "HIGH PRIORITY"
            suggestion = f"Revise {row['topic']} in {row['subject']} immediately."
        elif row['weakness_score'] > 0.8:
            level = "MEDIUM PRIORITY"
            suggestion = f"Practice more questions on {row['topic']} in {row['subject']}."
        else:
            level = "LOW PRIORITY"
            suggestion = f"You are doing well in {row['topic']} ({row['subject']})."

        recommendations.append({
            "subject": row['subject'],
            "topic": row['topic'],
            "priority": level,
            "recommendation": suggestion
        })

    return recommendations


# ---------------- MAIN FUNCTION FOR UI ----------------
def get_recommendation_from_input(subject, topic, difficulty, correct, time_taken):
    new_data = pd.DataFrame([{
        "student_id": 1,
        "subject": subject,
        "topic": topic,
        "difficulty": difficulty,
        "correct": correct,
        "time_taken": time_taken,
        "attempt_no": 1
    }])

    df = pd.concat([new_data], ignore_index=True)
    metrics = calculate_metrics(df)
    weakness = calculate_weakness(metrics)
    recs = generate_recommendations(weakness)

    return recs
