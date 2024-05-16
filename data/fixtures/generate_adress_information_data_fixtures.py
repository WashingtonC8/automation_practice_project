import pytest
import faker
from data.models.adress_information_data_model import AddressInformation


@pytest.fixture
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