import unittest
import tempfile
from pathlib import Path
from modules.student import Student
import modules.storage as storage

class TestStorage(unittest.TestCase):
    def test_save_and_load(self):
        with tempfile.TemporaryDirectory() as folder:
            old = storage.JSON_FILE
            storage.JSON_FILE = Path(folder) / "student.json"

            student = Student("Test Student", 1, 10)
            student.add_subject("Python", 80, 2, 10, 90)
            storage.save_student(student)
            loaded = storage.load_student()

            self.assertEqual(loaded.name, "Test Student")
            self.assertEqual(loaded.subjects[0]["name"], "Python")
            storage.JSON_FILE = old

if __name__ == "__main__":
    unittest.main()
