import pytest
import faker
from pages.models import AddressInformation
from pages.models import UserData


@pytest.fixture()
def generate_user_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    title = fake.random_element(elements=('Mr', 'Mrs'))
    password = fake.password()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return UserData(name=name, email=email, title=title, password=password, date_of_birth=date_of_birth)


@pytest.fixture()
def generate_address_information_data():
    fake = faker.Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    address_2 = fake.address()
    countries = ['India', 'United States', 'Canada', 'Australia', 'Israel', 'New Zealand', 'Singapore']
    country = fake.random_element(countries)
    state = fake.state()
    city = fake.city()
    zipcode = fake.zipcode()
    mobile_number = fake.phone_number()
    street_address = fake.street_address()
    po_box = fake.random_number(digits=5)
    address = f"{street_address}, P.O. Box {po_box}, {company}"
    return AddressInformation(first_name=first_name, last_name=last_name, company=company, address_2=address_2,
                              country=country, state=state, city=city, zipcode=zipcode, mobile_number=mobile_number,
                              street_address=street_address, po_box=po_box, address=address)
