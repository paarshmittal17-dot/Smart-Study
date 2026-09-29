import csv
import json
from pathlib import Path
from modules.student import Student

DATA_DIR = Path("data")
JSON_FILE = DATA_DIR / "student.json"
CSV_FILE = DATA_DIR / "smartstudy_report.csv"

def save_student(student):
    DATA_DIR.mkdir(exist_ok=True)
    data = {
        "name": student.name,
        "semester": student.semester,
        "available_hours": student.available_hours,
        "subjects": student.subjects
    }
    JSON_FILE.write_text(json.dumps(data, indent=4), encoding="utf-8")

def load_student():
    if not JSON_FILE.exists():
        return None
    try:
        data = json.loads(JSON_FILE.read_text(encoding="utf-8"))
        student = Student(data["name"], data["semester"], data["available_hours"])
        student.subjects = data["subjects"]
        return student
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Saved file is invalid or corrupted.")
        return None

def export_csv(student, analysis):
    DATA_DIR.mkdir(exist_ok=True)
    with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Student", "Semester", "Subject", "Marks", "Grade",
                         "Difficulty", "Exam Days", "Attendance", "Priority", "Priority Score"])
        for x in analysis:
            writer.writerow([
                student.name, student.semester, x["name"], x["marks"], x["grade"],
                x["difficulty"], x["exam_days"], x["attendance"],
                x["priority"], x["priority_score"]
            ])
