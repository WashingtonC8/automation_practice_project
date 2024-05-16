import datetime
from dataclasses import dataclass


@dataclass
class AddressInformation:
    first_name: str
    last_name: str
    company: str
    address_2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str
    street_address: str
    po_box: int
    address: str


@dataclass
class UserData:
    name: str
    email: str
    title: str
    password: str
    date_of_birth: datetime
