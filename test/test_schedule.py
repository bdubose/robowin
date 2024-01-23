"""Tests for Schedule classes"""

from datetime import datetime
import unittest

from schedule import Schedule

GOOD_SCHEDULE = r'''
¢) Week: 1/20/2024
Total Net Scheduled: 28.25 hrs

Sat Not Scheduled
1/20

Sun 10 a.m. - 3:45 p.m.
1/21

Mon 2p.m.- 6 p.m.
1/22

Tue 1p.m.- 7:15 p.m.
1/23

Wed 12:30 p.m. - 6:30 p.m.
1/24

Thu 10 a.m. - 7 p.m.
1/25

Fri Not Scheduled

1/26
'''

MISSING_DAYS = r'''
¢) Week: 1/20/2024
Total Net Scheduled: 28.25 hrs

Sat Not Scheduled
1/20

Sun 10 a.m. - 3:45 p.m.
1/21

Mon 2p.m.- 6 p.m.
1/22

Tue 1p.m.- 7:15 p.m.
1/23

Wed 12:30 p.m. - 6:30 p.m.
1/24
'''

class TestSchedule(unittest.TestCase):
    """Tests for Schedule class"""

    def setUp(self):
        """Initalizes good Schedule"""
        self.schedule = Schedule(GOOD_SCHEDULE)

    def test_no_errors(self):
        """Tests basic Schedule parsing without issues."""
        self.assertIsNone(self.schedule.error)

    def test_week_not_found(self):
        """Tests Schedule parsing when it cannot find the week."""
        schedule = Schedule('')
        self.assertEqual('Could not find "Week: M/D/Y" in input.', schedule.error)

    def test_week_found(self):
        """Tests if the week is found correctly."""
        week = datetime.fromisoformat('2024-01-20 00:00')
        self.assertEqual(week, self.schedule.week)

    def test_seven_days(self):
        """Tests if 7 days are found."""
        self.assertEqual(7, len(self.schedule.days))

    def test_seven_days_not_found(self):
        """Tests for correct failure for not having 7 days"""
        schedule = Schedule(MISSING_DAYS)
        self.assertRegex(schedule.error, 'Did not find 7 days of schedules. Found:.*')
