"""Classes for holding Schedule information."""

from datetime import datetime, timedelta
from typing import Optional
import re

from attr import dataclass

WEEK_PREFIX = 'Week: '
WEEK_REGEX = r'\d{1,2}/\d{1,2}/\d{4}'
DAY_PREFIXES = ('Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri')
TIME_FORMATS = ['%I:%M%p', '%I%p']
TIME_REGEX = r'\d{1,2}(:\d{2})?\s*[ap]\.?m\.?'

class Schedule:
    """Processes and stores information regarding a work schedule from text."""

    def __init__(self, text: str):
        self.error = None
        self.text = text
        self.save_week()
        if self.error is not None:
            return
        self.save_days()

    def save_week(self):
        """Parses this Schedule's text to determine the week this Schedule is for."""
        match = re.search(WEEK_PREFIX + WEEK_REGEX, self.text)
        if match is None:
            self.error = f'Could not find "{WEEK_PREFIX}M/D/Y" in input.'
            return
        self.week = datetime.strptime(match.group(), f'{WEEK_PREFIX}%m/%d/%Y')

    def save_days(self):
        """Parses the days from this Schedule's text to find beginning and end times for shifts."""
        # set up the dates first without worry about schedule bc the Week date is
        # the cleanest to parse
        days = [self.week + timedelta(days=x) for x in range(7)]
        times = [
            self.parse_times(line)
            for line in self.text
            if line.strip().startswith(DAY_PREFIXES)
        ]
        if len(times) != 7:
            self.error = 'Did not find 7 days of schedules.'

        self.days = [
            ScheduleDay(day, begin, end)
            for day, (begin, end)
            in zip(days, times)
        ]

    def parse_times(self, line: str):
        """Parses beginning and end schedule times from a single line of Schedule text."""
        if 'Not Scheduled' in line:
            return None, None
        begin, end = [
            self.parse_time(part, line)
            for part
            in re.sub('|'.join(DAY_PREFIXES), '', line).split('-')
        ]
        return begin, end

    def parse_time(self, time_str: str, whole_line: str) -> Optional[datetime]:
        """Parses a single time based on the format usually seen in the Schedule text."""
        time_str = time_str.strip().replace(' ', '').replace('.', '')
        for time_format in TIME_FORMATS:
            try:
                return datetime.strptime(time_str, time_format)
            except ValueError:
                pass
        # if we're still here, we couldn't parse any time formats
        self.error = f'Could not parse {time_str} into a time using a known format ({whole_line})'
        return None

    def __str__(self):
        if self.error is not None:
            return self.error

        s = f'Week: {self.week:%m/%d/%Y}\n'
        for day in self.days:
            s += f'{day.day:%m/%d/%Y}: '
            if day.begin is None:
                s += 'Not Scheduled\n'
                continue
            s += f'{day.begin} - {day.end}\n'
        return s

@dataclass
class ScheduleDay:
    """Holds the begin and end time for each Schedule day"""
    day: datetime
    begin: Optional[datetime] = None
    end: Optional[datetime] = None
