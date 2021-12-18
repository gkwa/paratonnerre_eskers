import argparse
from datetime import datetime

import humanfriendly
import humanize
from dateutil.parser import parse

parser = argparse.ArgumentParser()
parser.add_argument("--timestamp", required=True, help="timestamp")
args = parser.parse_args()

# past = parse(" 16:50:01 ")
past = parse(args.timestamp)
duration = datetime.now() - past

print(f"timestamp: {args.timestamp}")
print(f"seconds since timestamp: {int(duration.total_seconds())}")
print(f"minutes since timestamp: {int(duration.total_seconds()/60)}")
print(f"hours since timestamp: {int(duration.total_seconds()/3600)}")
print(
    f"friendly1 since timestamp: {humanfriendly.format_timespan(duration.total_seconds())}"
)
print(f"friendly2 since timestamp: {humanize.naturaldelta(duration)}")
