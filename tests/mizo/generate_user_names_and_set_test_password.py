import os


counter = 1
os.environ["LOGIN"] = "my varr"


def generate_next_username():
    global counter
    next_username = f"{os.environ['LOGIN']}{counter}"
    counter += 1
    return next_username


def set_test_password():
    return "apiP@ssw0rdTeest1"


def set_credentials():
    login = generate_next_username()
    password = set_test_password()
    return login, password
