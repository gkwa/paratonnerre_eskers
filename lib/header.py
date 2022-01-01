import datetime
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta

import dateutil.parser
import humanize


@dataclass
class TimestampHeader:
    dt: datetime

    pat = re.compile(
        r"""
    ^date:\s+(?P<timestamp>\d+)
    \s+\#\s+
    (?P<date_str>.*)
    """,
        re.VERBOSE,
    )

    @classmethod
    def from_string(cls, _str):
        mo = cls.pat.search(_str)
        if not mo:
            raise ValueError(_str)
        x = mo.group("date_str")
        dt = dateutil.parser.parse(mo.group("date_str"))
        return cls(dt)


@dataclass
class HeaderEntry:
    user_count: int
    time: datetime = field(default_factory=lambda: datetime)
    uptime: timedelta = field(default_factory=lambda: timedelta)

    pat = re.compile(
        r"""
    (?P<time>\d{2}:\d{2}:\d{2})
    \s+up\s+
    (:?
    (?P<duration_minutes>\d+)\s+min
    |
    (?P<duration>(?P<hours>\d+):(?P<minutes>\d+))
    )
    \s*,\s*
    (?P<users>\d+)\s+users?
    """,
        re.VERBOSE,
    )

    def __str__(self):
        x1 = (
            f"count={self.user_count} {self.time} "
            f"up={humanize.naturaldelta(self.uptime)}"
        )
        return x1

    @classmethod
    def from_string(cls, _str):
        mo = cls.pat.search(_str)
        if not mo:
            raise ValueError(_str)

        time = dateutil.parser.parse(mo.group("time"))

        assert mo.group("duration_minutes") or mo.group("duration")

        if mo.group("duration_minutes"):
            assert mo.group("duration_minutes")
            duration = timedelta(seconds=int(mo.group("duration_minutes")) * 60)

        elif mo.group("duration"):
            hours = int(mo.group("hours"))
            minutes = mo.group("minutes")
            assert minutes is not None
            minutes = int(minutes)
            assert hours
            duration = timedelta(seconds=hours * 3600 + minutes * 60)

        user_count = int(mo.group("users"))
        return cls(user_count, time, duration)
