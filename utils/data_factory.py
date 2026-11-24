
from datetime import timedelta
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


def generate_booking() -> dict:
    checkin = fake.future_date(end_date="+30d")
    checkout = checkin + timedelta(days=fake.random_int(min=1, max=10))

    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=1000),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat(),
        },
        "additionalneeds": fake.random_element(
            elements=("Breakfast", "Lunch", "Dinner")
        ),
    }
