import datetime
from dataclasses import dataclass


@dataclass
class UserData:
    name: str
    email: str
    title: str
    password: str
    date_of_birth: datetime
