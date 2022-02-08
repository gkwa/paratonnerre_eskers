import re
from dataclasses import dataclass, field
from datetime import timedelta

import humanize


@dataclass
class IdleTime:
    input_str: str
    duration: timedelta = field(init=False)
    xdm: bool = False

    p1 = re.compile(
        r"""
        (:?
        (?P<hours>\d+)
        :
        )?
        (?P<minutes>\d+)
        :
        (?P<seconds>\d+)
        """,
        re.VERBOSE,
    )

    p2 = re.compile(
        r"""
    .*xdm.*
    """,
        re.VERBOSE,
    )

    p3 = re.compile(
        r"""
    (?P<seconds>\d+\.\d+)s
    """,
        re.VERBOSE,
    )

    p4 = re.compile(
        r"""
    (?P<minutes>\d+)
    :
    (?P<seconds>\d+)
    """,
        re.VERBOSE,
    )

    def idle_friendly(self):
        return humanize.naturaldelta(self.duration)

    def __str__(self):
        return str(self.duration)

    def __post_init__(self):
        td = timedelta(seconds=0)

        if mo := self.p1.search(self.input_str):
            td = timedelta(
                hours=int(mo.group("hours") or 0),
                minutes=int(mo.group("minutes")),
                seconds=int(mo.group("seconds")),
            )

        elif mo := self.p2.search(self.input_str):
            self.xdm = True

        elif mo := self.p4.search(self.input_str):
            td = timedelta(
                minutes=int(mo.group("minutes")),
                seconds=int(mo.group("seconds")),
            )
        elif mo := self.p3.search(self.input_str):
            td = timedelta(seconds=float(mo.group("seconds")))

        self.duration = td
