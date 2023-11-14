from tests.mizo.constants import base_username

counter = 1

def generate_next_username():
    global counter
    next_username = f"{base_username}{counter}"
    counter += 1
    return next_username


def set_test_password():
    return "apiP@ssw0rdTeest1"
