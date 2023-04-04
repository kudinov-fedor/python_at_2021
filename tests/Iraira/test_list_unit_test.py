# Tests can relate to list:
# String representation and formatting
# Get length
# Usage of + and * operators
# Objects conversion from list and to list (str, bool, tuple, dict, set)
# Usage of list methods (append, extend. etc.)
# Usage in conditions
# Usage for loops
# Interaction with built-in functions (zip, enumerate, map etc.) --

import pytest


@pytest.fixture
def list_unit_test():
    return ['a', 'b', 'c', 5, 'e', 'f', 'g']


def get_length(listItem):
    return len(listItem)


def show_result(map_object):
    for item in map_object:
        print(item)


def test_get_length(list_unit_test):
    assert get_length(list_unit_test) == 7


def test_append_elem(list_unit_test):
    list_unit_test.append(1)
    assert list_unit_test[7] == 1


def test_remove_elem(list_unit_test):
    list_unit_test.remove('c')
    assert list_unit_test[2] == 'd'


def test_add_elem(list_unit_test):
    result = list_unit_test[3] + 1
    assert result == 6


def test_find_item():
    item_list = ["laundry detergent", "eggs", "bread", "milk", "apples"]
    # assert "meat" not in item_list
    for item in item_list:
        if item == "meat":
            raise AssertionError("Meat should not be in list")


def test_list_to_string():
    words = ["hello", "world", "hola", "mundi"]
    capital_words = list(map(str.upper, words))
    assert capital_words == ['HELLO', 'WORLD', 'HOLA', 'MUNDI']


def test_match_pet_owner():
    pet = ['buttons', 'mochi', 'willy', 'kali']
    human = ['Tom', 'Crissy', 'Mike', 'Susan']
    list_to_zip = list(zip(pet, human))
    assert list_to_zip == [('buttons', 'Tom'), ('mochi', 'Crissy'), ('willy', 'Mike'), ('kali', 'Susan')]
