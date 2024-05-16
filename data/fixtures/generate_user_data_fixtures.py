import pytest
import faker
from data.models.user_data_model import UserData


@pytest.fixture
def generate_user_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    title = fake.random_element(elements=('Mr', 'Mrs'))
    password = fake.password()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
    return UserData(name=name, email=email, title=title, password=password, date_of_birth=date_of_birth)

