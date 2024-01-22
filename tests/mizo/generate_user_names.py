from tests.mizo.constants import BASE_LOGIN

counter = 1


def generate_next_username():
    global counter
    next_username = f"{BASE_LOGIN}{counter}"
    counter += 1
    return next_username
