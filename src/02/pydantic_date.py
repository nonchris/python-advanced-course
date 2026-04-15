from datetime import date, datetime, time, timedelta
import time as t
from pydantic import BaseModel


class Model(BaseModel):
    d: datetime = None
    dt: datetime = None
    t: time = None
    td: timedelta = None


m = Model(
    d=t.time(),
    dt='2032-04-23T10:20:30.400+02:30',
    t=time(4, 8, 16),
    td='P3DT12H30M5S',
)

print(m.model_dump())