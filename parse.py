import logging
import pathlib
from pathlib import Path

import monacelli_pylog_prefs.logger

from lib.log import LogEntry

monacelli_pylog_prefs.logger.setup(
    filename=f"{pathlib.Path(__file__).stem}.log", stream_level=logging.DEBUG
)


def process_file(path: Path):
    queue = []
    for line in path.read_text().splitlines():
        is_new = line.startswith("date: ")
        if is_new:
            if entry := LogEntry.from_lines(queue):
                yield entry
            queue = []
        queue.append(line)


def main():
    path = Path("wholog.log")
    for entry in process_file(path):
        logging.debug(entry)

if __name__ == "__main__":
    main()
