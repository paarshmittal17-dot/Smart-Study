# SmartStudy — Personalized Study Time Optimizer

## Python Essentials — VITyarthi Evaluated Course Project

SmartStudy is a menu-driven Python application for students who have limited study time and multiple subjects. It analyzes marks, difficulty , attendance and exam urgency, then recommends how study time should be distributed.

## Why Python?

The solution is implemented using Python fundamentals and standard-library modules. It demonstrates variables, conditions, loops, functions, lists, dictionaries, classes, modules, exception handling, JSON file handling, CSV export and unit testing. Python's standard library provides built-in support for modules, file formats and `unittest`, so no external package is required for the core application. 

## Features
1. Student profile creation
2. Subject data entry and validation
3. Grade calculation
4. Priority-score calculation
5. Strong/weak subject identification
6. Weekly study-hour allocation
7. Daily study-plan generation
8. Update subject records
9. Delete subject records
10. Save/load JSON data
11. CSV report export
12. Automated unit tests

## Priority Algorithm

Priority is calculated from four factors:

- Marks: 60% influence
- Difficulty: Easy 0, Medium 10, Hard 20
- Exam urgency: up to 20 points
- Attendance below 75%: 10 points

Priority labels:

- 60–100: HIGH
- 35–59: MEDIUM
- 0–34: LOW

## Project Structure

```text
SmartStudy/
├── main.py
├── modules/
│   ├── __init__.py
│   ├── student.py
│   ├── validation.py
│   ├── analysis.py
│   ├── planner.py
│   └── storage.py
├── tests/
│   ├── __init__.py
│   ├── test_analysis.py
│   ├── test_planner.py
│   └── test_storage.py
├── data/
├── README.md
├── statement.md
└── requirements.txt
```

## Run

```bash
python3 main.py
```


## Test

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## CSV Output

Choose option 7 from the program menu. The report is saved to:

```text
data/smartstudy_report.csv
```
