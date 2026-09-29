import unittest
from modules.planner import allocate_hours, generate_daily_plan

class TestPlanner(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"name": "Python", "priority": "HIGH"},
            {"name": "Maths", "priority": "MEDIUM"},
            {"name": "English", "priority": "LOW"}
        ]

    def test_hours_sum(self):
        plan = allocate_hours(self.data, 10)
        self.assertEqual(sum(x["hours"] for x in plan), 10)

    def test_daily_plan_contains_all_subjects(self):
        schedule = generate_daily_plan(self.data, 10)
        names = {x["subject"] for sessions in schedule.values() for x in sessions}
        self.assertEqual(names, {"Python", "Maths", "English"})

if __name__ == "__main__":
    unittest.main()
