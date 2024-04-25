import pytest
import faker
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture()
def generate_user_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    title = fake.random_element(elements=('Mr', 'Mrs'))
    password = fake.password()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
    day_of_birth = fake.random_int(min=1, max=28)
    month_of_birth = fake.random_int(min=1, max=12)
    year_of_birth = fake.random_int(min=1900, max=2021)
    return {"name": name, "email": email, "title": title, "password": password, "day_of_birth": day_of_birth,
            "month_of_birth": month_of_birth, "year_of_birth": year_of_birth, "date_of_birth": date_of_birth}


@pytest.fixture()
def generate_address_information_data():
    fake = faker.Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    company = fake.company()
    address2 = fake.address()
    country = fake.country()
    state = fake.state()
    city = fake.city()
    zipcode = fake.zipcode()
    mobile_number = fake.phone_number()
    street_address = fake.street_address()
    po_box = fake.random_number(digits=5)
    address = f"{street_address}, P.O. Box {po_box}, {company}"
    return first_name, last_name, company, address2, country, state, city, zipcode, mobile_number, address
