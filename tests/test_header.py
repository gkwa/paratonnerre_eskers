import datetime

from lib.header import HeaderEntry


def test_time():
    txt = " 19:12:01 up  1:00,  2 users,  load average: 0.17, 0.07, 0.36"
    entry = HeaderEntry.from_string(txt)
    assert entry.time == datetime.datetime.now().replace(
        hour=19, minute=12, second=1, microsecond=0
    )


def test_header_hours():
    txt = " 19:12:01 up  1:00,  2 users,  load average: 0.17, 0.07, 0.36"
    entry = HeaderEntry.from_string(txt)
    delta = datetime.timedelta(hours=1)
    assert entry.duration == delta


def test_header_minutes():
    txt = " 19:11:01 up 59 min,  2 users,  load average: 0.05, 0.03, 0.37"
    entry = HeaderEntry.from_string(txt)
    delta = datetime.timedelta(seconds=59 * 60)
    assert entry.duration == delta


def test_count_users():
    txt = " 19:12:01 up  1:00,  2 users,  load average: 0.17, 0.07, 0.36"
    entry = HeaderEntry.from_string(txt)
    assert entry.user_count == 2


def test_count_single_user():
    txt = " 19:12:01 up  1:00,  1 user,  load average: 0.17, 0.07, 0.36"
    entry = HeaderEntry.from_string(txt)
    assert entry.user_count == 1
