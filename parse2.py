import re
from datetime import datetime

import dateutil.parser
import humanize
import pytz
import humanfriendly


from abc import ABC, abstractmethod
import datetime
from dataclasses import dataclass
from pathlib import Path
from typing import List

from lib.header import HeaderEntry

@dataclass
class LogEntry:
    header: HeaderEntry
    who_header: List[str]
    content: List[str]

    def user_list(self):
        return [line.split()[0] for line in self.content]

    def __str__(self):
        ts1 = humanfriendly.format_timespan(self.header.duration.total_seconds())
        ts2 = humanize.naturaldelta(self.header.duration)
        ts_relative_now = humanize.naturaldelta(datetime.datetime.now() - self.header.time)
        return f"relative time: {ts_relative_now}, {self.header=}, entry_count: {len(self.content)}, uptime1: {ts1}, uptime2:{ts2}, {self.content}"

def process_complete_entry(lines):
    if not lines:
        return None

    header = lines[0]
    who_header = lines[1]
    content = lines[2:]

    h = HeaderEntry.from_string(header)
    l = LogEntry(h, who_header, content)
    return l


def process_file(path: Path):
    queue = []
    for line in path.read_text().splitlines():
        is_new = line.startswith(" ")
        if is_new:
            entry = process_complete_entry(queue)
            print(entry)
            queue = []
        queue.append(line)


def main():
    path = Path("who.log")
    process_file(path)


if __name__ == "__main__":
    main()
