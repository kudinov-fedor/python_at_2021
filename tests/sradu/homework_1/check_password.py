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
