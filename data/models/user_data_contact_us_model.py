from dataclasses import dataclass


@dataclass
class UserDataContactUs:
    name: str
    email: str
    subject: str
    message: str
    file_path: str
