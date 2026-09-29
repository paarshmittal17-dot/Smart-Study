import unittest
from modules.analysis import grade, calculate_priority, priority_label

class TestAnalysis(unittest.TestCase):
    def test_grades(self):
        self.assertEqual(grade(95), "A+")
        self.assertEqual(grade(75), "B")
        self.assertEqual(grade(45), "F")

    def test_priority_labels(self):
        self.assertEqual(priority_label(70), "HIGH")
        self.assertEqual(priority_label(40), "MEDIUM")
        self.assertEqual(priority_label(20), "LOW")

    def test_weak_subject_gets_more_priority(self):
        weak = {"marks": 50, "difficulty": 3, "exam_days": 5, "attendance": 70}
        strong = {"marks": 90, "difficulty": 1, "exam_days": 60, "attendance": 90}
        self.assertGreater(calculate_priority(weak), calculate_priority(strong))

if __name__ == "__main__":
    unittest.main()
