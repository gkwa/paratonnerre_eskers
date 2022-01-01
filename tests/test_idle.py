from lib.idle import IdleTime


def test_time():
    idle = IdleTime("8:13")
    assert str(idle.duration) == "0:08:13"
    idle = IdleTime("21.00s")
    assert str(idle.duration) == "0:00:21"
    idle = IdleTime("?xdm?")
    assert str(idle.duration) == "0:00:00"
