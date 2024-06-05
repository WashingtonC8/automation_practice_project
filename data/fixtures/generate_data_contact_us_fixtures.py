import os
import tempfile
from data.models.user_data_contact_us_model import UserDataContactUs
import pytest
import faker


@pytest.fixture()
def generate_user_data_contact_us():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    subject = fake.subject()
    message = fake.text()
    random_text = fake.text()
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt')
    temp_file.write(random_text)
    temp_file.close()
    file_path = temp_file.name
    return UserDataContactUs(name=name, email=email, subject=subject, message=message, file_path=file_path)