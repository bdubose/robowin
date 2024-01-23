"""Tests for Schedule classes"""

import unittest

from schedule import Schedule

class TestSchedule(unittest.TestCase):
    """Tests for Schedule class"""
    def test_happy_path(self):
        """Tests basic Schedule parsing without issues."""
        # todo: provide actual good Schedule text
        schedule = Schedule('')
        self.assertIsNone(schedule.error)

    def test_week_not_found(self):
        """Tests Schedule parsing when it cannot find the week."""
        schedule = Schedule('')
        self.assertEqual(schedule.error, 'Could not find "Week: M/D/Y" in input.')
