
from faker import Faker

fake = Faker()


def generate_customer() -> dict:
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "telephone": fake.numerify("##########"),
        "password": fake.password(length=12),
    }
