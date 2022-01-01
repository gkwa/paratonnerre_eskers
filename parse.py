import logging
import pathlib
from pathlib import Path

import monacelli_pylog_prefs.logger

from lib.header import HeaderEntry, TimestampHeader
from lib.log import LogEntry

monacelli_pylog_prefs.logger.setup(
    filename=f"{pathlib.Path(__file__).stem}.log", stream_level=logging.DEBUG
)


def process_complete_entry(lines):
    if not lines:
        return None

    timestamp_header = lines[0]
    header = lines[1]
    who_header = lines[2]
    content = lines[3:]

    h1 = TimestampHeader.from_string(timestamp_header)
    h2 = HeaderEntry.from_string(header)
    entry = LogEntry(h1, h2)
    entry.set_content(h1.dt, who_header, content)
    return entry


def process_file(path: Path):
    queue = []
    all_entries = []
    for line in path.read_text().splitlines():
        is_new = line.startswith("date: ")
        if is_new:
            entry = process_complete_entry(queue)
            all_entries.append(entry)
            queue = []
        queue.append(line)
    return all_entries


def main():
    path = Path("wholog.log")
    entries = process_file(path)
    for entry in entries:
        logging.debug(entry)


if __name__ == "__main__":
    main()
