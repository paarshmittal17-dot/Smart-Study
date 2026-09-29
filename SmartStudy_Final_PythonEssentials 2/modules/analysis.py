def calculate_priority(subject):
    # Lower marks, higher difficulty, closer exams and low attendance increase priority.
    marks_factor = 100 - subject["marks"]
    difficulty_factor = {1: 0, 2: 10, 3: 20}[subject["difficulty"]]

    if subject["exam_days"] <= 7:
        exam_factor = 20
    elif subject["exam_days"] <= 14:
        exam_factor = 12
    elif subject["exam_days"] <= 30:
        exam_factor = 6
    else:
        exam_factor = 0

    attendance_factor = 10 if subject["attendance"] < 75 else 0
    score = (marks_factor * 0.60) + difficulty_factor + exam_factor + attendance_factor
    return min(100, round(score, 2))

def priority_label(score):
    if score >= 60:
        return "HIGH"
    if score >= 35:
        return "MEDIUM"
    return "LOW"

def grade(marks):
    if marks >= 90: return "A+"
    if marks >= 80: return "A"
    if marks >= 70: return "B"
    if marks >= 60: return "C"
    if marks >= 50: return "D"
    return "F"

def analyze_subjects(subjects):
    results = []
    for subject in subjects:
        score = calculate_priority(subject)
        results.append({
            **subject,
            "priority_score": score,
            "priority": priority_label(score),
            "grade": grade(subject["marks"])
        })
    return sorted(results, key=lambda x: x["priority_score"], reverse=True)
