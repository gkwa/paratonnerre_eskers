import logging
import pathlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

import monacelli_pylog_prefs.logger

from lib.header import HeaderEntry, TimestampHeader
from lib.w import WhoEntry

monacelli_pylog_prefs.logger.setup(
    filename=f"{pathlib.Path(__file__).stem}.log", stream_level=logging.DEBUG
)


@dataclass
class LogEntry:
    ts_header: TimestampHeader
    header: HeaderEntry
    content: List[WhoEntry] = field(init=False, default_factory=lambda: WhoEntry)

    @classmethod
    def content_from_list(cls, timestamp, who_header, lst) -> List[WhoEntry]:
        l3 = []
        l1 = [field.replace("@", "") for field in who_header.split()]
        for line in lst:
            l2 = line.split()
            dct = {key: value for key, value in zip(l1, l2)}
            dct["log_timestamp"] = timestamp
            who = WhoEntry(**dct)
            l3.append(who)
        return l3

    def user_list(self):
        return [line.split()[0] for line in self.content]

    def __str__(self):
        z = [str(p) for p in self.content]
        y = ", ".join(z)
        return f"{self.ts_header.dt} {y}"


def process_complete_entry(lines):
    if not lines:
        return None

    timestamp_header = lines[0]
    header = lines[1]
    who_header = lines[2]
    content = lines[3:]

    h1 = TimestampHeader.from_string(timestamp_header)
    h2 = HeaderEntry.from_string(header)
    l = LogEntry(h1, h2)
    l.content = LogEntry.content_from_list(h1.dt, who_header, content)
    return l


def process_file(path: Path):
    queue = []
    all_entries = []
    for line in path.read_text().splitlines():
        is_new = line.startswith("date: ")
        if is_new:
            entry = process_complete_entry(queue)
            all_entries.append(entry)
            logging.debug(entry)
            queue = []
        queue.append(line)
    return all_entries


def main():
    path = Path("wholog.log")
    entries = process_file(path)


if __name__ == "__main__":
    main()
