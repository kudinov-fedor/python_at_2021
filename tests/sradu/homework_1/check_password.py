import re


def check_password(word):
    has_lowercase = bool(re.search('[a-z]', word))
    has_uppercase = bool(re.search('[A-Z]', word))
    has_numbers = bool(re.search('[0-9]', word))
    has_symbols = bool(re.search(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]', word))

    length_valid = 8 <= len(word) <= 30

    return all([has_lowercase,
                has_uppercase,
                has_numbers,
                has_symbols,
                length_valid])


assert check_password("Psswrd1!") is True
assert check_password("Psswr1!") is False  # less than 8 characters
assert check_password("psswrd1!") is False  # no uppercase letter
assert check_password("PSSWRD1!") is False  # no lowercase letter
assert check_password("Psswrdd!") is False  # no number
assert check_password("Psswrdd1") is False  # no symbol
assert check_password("Psswrd111111111111111111111111!") is False  # more than 30 characters

print("All checks passed")
