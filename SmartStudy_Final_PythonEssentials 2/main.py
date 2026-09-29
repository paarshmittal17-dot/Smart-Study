from modules.student import Student
from modules.validation import get_non_empty, get_float, get_int
from modules.analysis import analyze_subjects
from modules.planner import generate_daily_plan
from modules.storage import save_student, load_student, export_csv

def create_student():
    print("\n--- CREATE STUDENT PROFILE ---")
    name = get_non_empty("Student name: ")
    semester = get_int("Semester (1-8): ", 1, 8)
    hours = get_float("Available study hours per week: ", 1, 168)
    student = Student(name, semester, hours)
    count = get_int("Number of subjects: ", 1, 20)

    for i in range(count):
        print(f"\nSubject {i+1}")
        subject = get_non_empty("Subject name: ")
        marks = get_float("Marks percentage (0-100): ", 0, 100)
        difficulty = get_int("Difficulty (1 Easy, 2 Medium, 3 Hard): ", 1, 3)
        days = get_int("Days until exam (0-365): ", 0, 365)
        attendance = get_float("Attendance percentage (0-100): ", 0, 100)
        student.add_subject(subject, marks, difficulty, days, attendance)
    return student

def show_student(student):
    analysis = analyze_subjects(student.subjects)
    print("\n" + "="*72)
    print("SMARTSTUDY REPORT")
    print("="*72)
    print(f"Student: {student.name} | Semester: {student.semester}")
    print(f"Available study time: {student.available_hours} hours/week")
    average = sum(x["marks"] for x in analysis) / len(analysis)
    print(f"Overall average: {average:.2f}%")
    print(f"Strongest subject: {min(analysis, key=lambda x: x['priority_score'])['name']}")
    print(f"Highest-priority subject: {max(analysis, key=lambda x: x['priority_score'])['name']}")

    print("\n--- Subject Analysis ---")
    for x in analysis:
        print(f"{x['name']:<18} Marks: {x['marks']:>5.1f}% | "
              f"Grade: {x['grade']:<2} | Priority: {x['priority']:<6} | "
              f"Score: {x['priority_score']:>5.1f}")

    daily = generate_daily_plan(analysis, student.available_hours)
    print("\n--- Weekly Study Plan ---")
    for day, sessions in daily.items():
        print(f"\n{day}:")
        if not sessions:
            print("  Revision / Break")
        for session in sessions:
            print(f"  {session['subject']:<18} {session['hours']:.1f} hour(s)")

    return analysis, daily

def main():
    student = None

    while True:
        print("\n" + "="*55)
        print(" SMARTSTUDY - PERSONALIZED STUDY TIME OPTIMIZER")
        print("="*55)
        print("1. Create new student profile")
        print("2. View current analysis")
        print("3. Update a subject")
        print("4. Delete a subject")
        print("5. Save student data")
        print("6. Load saved student")
        print("7. Export report to CSV")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            student = create_student()
            show_student(student)

        elif choice == "2":
            if student:
                show_student(student)
            else:
                print("Create or load a student first.")

        elif choice == "3":
            if not student:
                print("Create or load a student first.")
                continue
            for i, s in enumerate(student.subjects, 1):
                print(f"{i}. {s['name']}")
            n = get_int("Subject number to update: ", 1, len(student.subjects))
            s = student.subjects[n-1]
            s["marks"] = get_float("New marks %: ", 0, 100)
            s["difficulty"] = get_int("New difficulty (1-3): ", 1, 3)
            s["exam_days"] = get_int("New exam days: ", 0, 365)
            s["attendance"] = get_float("New attendance %: ", 0, 100)
            print("Subject updated.")

        elif choice == "4":
            if not student:
                print("Create or load a student first.")
                continue
            for i, s in enumerate(student.subjects, 1):
                print(f"{i}. {s['name']}")
            n = get_int("Subject number to delete: ", 1, len(student.subjects))
            removed = student.subjects.pop(n-1)
            print(f"Deleted {removed['name']}.")

        elif choice == "5":
            if student:
                save_student(student)
                print("Student data saved.")
            else:
                print("Nothing to save.")

        elif choice == "6":
            student = load_student()
            print("Student loaded." if student else "No valid saved student found.")

        elif choice == "7":
            if student:
                analysis = analyze_subjects(student.subjects)
                export_csv(student, analysis)
                print("CSV report exported to data/smartstudy_report.csv")
            else:
                print("Create or load a student first.")

        elif choice == "8":
            print("Thank you for using SmartStudy!")
            break
        else:
            print("Invalid option. Choose 1-8.")

if __name__ == "__main__":
    main()
