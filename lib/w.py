from datetime import datetime

from pydantic import BaseModel

from lib.idle import IdleTime


class WhoEntry(BaseModel):
    USER: str
    TTY: str
    FROM: str
    LOGIN: datetime
    IDLE: IdleTime
    JCPU: str
    PCPU: str
    WHAT: str
    log_timestamp: datetime

    def __init__(self, **data):
        dt = data["log_timestamp"]
        d1 = datetime.strptime(data["LOGIN"], "%H:%M")
        dt = dt.replace(hour=d1.hour, minute=d1.minute, second=0, microsecond=0)
        data["IDLE"] = IdleTime(data["IDLE"])
        data["LOGIN"] = dt

        super().__init__(**data)

    def __str__(self):
        diff = self.log_timestamp - self.LOGIN
        return f"user={self.USER}, login_time={self.LOGIN}, login_duration={diff}, idle={self.IDLE}, idle_friendly={self.IDLE.idle_friendly()}"
