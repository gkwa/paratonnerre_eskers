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

    """
    date: 1640987148 # Fri Dec 31 20:45:48 UTC 2021
     20:45:48 up 19 min,  2 users,  load average: 0.00, 0.03, 0.05
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    centos   :0       :0               20:28   ?xdm?  58.24s  0.16s /usr/libexec/gnome-session-binary
    root     pts/0    71-213-102-53.mn 20:28    4.00s  0.08s  0.00s /bin/bash /opt/paratonnerre_eskers/wholog.sh
    date: 1640987161 # Fri Dec 31 20:46:01 UTC 2021
    """
        
    """
    date: 1640987148 # Fri Dec 31 20:45:48 UTC 2021
     20:45:48 up 19 min,  2 users,  load average: 0.00, 0.03, 0.05
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    centos   :0       :0               20:28   ?xdm?  58.24s  0.16s /usr/libexec/gnome-session-binary
    root     pts/0    71-213-102-53.mn 20:28    4.00s  0.08s  0.00s /bin/bash /opt/paratonnerre_eskers/wholog.sh
    date: 1640987161 # Fri Dec 31 20:46:01 UTC 2021
    """

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
            if entry := process_complete_entry(queue):
                all_entries.append(entry)
            queue = []
        queue.append(line)
    return all_entries


def main():
    path = Path("wholog.log")
    entries = process_file(path)
    for entry in entries:
        logging.debug(entry.header)
        logging.debug(entry)


if __name__ == "__main__":
    main()
