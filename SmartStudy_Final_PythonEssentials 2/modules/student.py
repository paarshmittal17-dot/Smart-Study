class Student:
    """Stores student profile and subject records."""

    def __init__(self, name, semester, available_hours):
        self.name = name
        self.semester = semester
        self.available_hours = available_hours
        self.subjects = []

    def add_subject(self, name, marks, difficulty, exam_days, attendance):
        self.subjects.append({
            "name": name,
            "marks": marks,
            "difficulty": difficulty,
            "exam_days": exam_days,
            "attendance": attendance
        })
