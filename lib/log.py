from dataclasses import dataclass, field
from typing import List

from lib.header import HeaderEntry, TimestampHeader
from lib.w import WhoEntry


@dataclass
class LogEntry:
    ts_header: TimestampHeader
    header: HeaderEntry
    content: List[WhoEntry] = field(init=False, default_factory=lambda: WhoEntry)

    @classmethod
    def from_lines(cls, lines):
        if not lines:
            return None

        """
        date: 1640987148 # Fri Dec 31 20:45:48 UTC 2021
         20:45:48 up 19 min,  2 users,  load average: 0.00, 0.03, 0.05
        USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
        centos   :0       :0               20:28   ?xdm?  58.24s  0.16s /usr/libexec/gnome-session-binary
        root     pts/0    71-213-102-53.mn 20:28    4.00s  0.08s  0.00s /bin/bash /opt/paratonnerre_eskers/wholog.sh
        """

        timestamp_header = lines[0]
        header = lines[1]
        who_header = lines[2]
        content = lines[3:]

        h1 = TimestampHeader.from_string(timestamp_header)
        h2 = HeaderEntry.from_string(header)
        entry = cls(h1, h2)
        entry.set_content(h1.dt, who_header, content)
        return entry

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
        if self.content:
            z = [str(p) for p in self.content]
            y = ", ".join(z)
            p1 = f"{self.ts_header.dt} {y}"
            p2 = f"{y}"
            return p2
        return "no one logged in"
