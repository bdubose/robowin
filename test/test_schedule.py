import unittest

from schedule import Schedule

class TestSchedule(unittest.TestCase):
    def test_happy_path(self):
        schedule = Schedule('')
        self.assertIsNone(schedule.error)

    def test_week_not_found(self):
        schedule = Schedule('')
        self.assertEqual(schedule.error, 'Could not find "Week: M/D/Y" in input.')