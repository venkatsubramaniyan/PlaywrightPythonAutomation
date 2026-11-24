
PING = "/ping"
AUTH = "/auth"
BOOKING = "/booking"


def booking_by_id(booking_id: int) -> str:
    return f"{BOOKING}/{booking_id}"
