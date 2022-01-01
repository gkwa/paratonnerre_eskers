from dataclasses import dataclass, field
from typing import List

from lib.header import HeaderEntry, TimestampHeader
from lib.w import WhoEntry


@dataclass
class LogEntry:
    ts_header: TimestampHeader
    header: HeaderEntry
    content: List[WhoEntry] = field(init=False, default_factory=lambda: WhoEntry)

    def set_content(self, timestamp, who_header, lst) -> List[WhoEntry]:
        l3 = []
        l1 = [field.replace("@", "") for field in who_header.split()]
        for line in lst:
            l2 = line.split()
            dct = {key: value for key, value in zip(l1, l2)}
            dct["log_timestamp"] = timestamp
            who = WhoEntry(**dct)
            l3.append(who)
        self.content = l3

    def __str__(self):
        z = [str(p) for p in self.content]
        y = ", ".join(z)
        p1 = f"{self.ts_header.dt} {y}"
        p2 = f"{y}"
        return p2
