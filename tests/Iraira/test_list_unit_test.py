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
def listUnitTest():
    return ['a', 'b', 'c', 5, 'e', 'f', 'g']


@pytest.fixture
def listToZip():
    pet = ['buttons', 'mochi', 'willy', 'kali']
    human = ['Tom', 'Crissy', 'Mike', 'Susan']
    return list(zip(pet, human))


def getLength(listItem):
    return len(listItem)


def show_result(map_object):
    for item in map_object:
        print(item)


def test_getLength(listUnitTest):
    assert getLength(listUnitTest) == 7


def test_appendElem(listUnitTest):
    listUnitTest.append(1)
    assert listUnitTest[7] == 1


def test_removeElem(listUnitTest):
    listUnitTest.remove('c')
    assert listUnitTest[2] == 'd'


def test_addElem(listUnitTest):
    result = listUnitTest[3] + 1
    assert result == 6


def test_findItem():
    itemList = ["laundry detergent", "eggs", "bread", "milk", "apple"]
    for item in itemList:
        if item == "meat":
            print("Item is added to shopping list")
            break
        else:
            print("Item not in shopping list")


def test_listToString():
    words = ["hello", "world", "hola", "mundi"]
    capitalWords = list(map(str.upper, words))
    assert capitalWords == ['HELLO', 'WORLD', 'HOLA', 'MUNDI']


def test_matchPetOwner(listToZip):
    assert listToZip == [('buttons', 'Tom'), ('mochi', 'Crissy'), ('willy', 'Mike'), ('kali', 'Susan')]
