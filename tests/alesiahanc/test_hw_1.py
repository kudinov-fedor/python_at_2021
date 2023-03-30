import pytest


@pytest.fixture
def mylist():
    return [1, 2, 10, 9, 8]


def test_mylist_edit(mylist):
    mylist[0] = 11
    assert mylist[0] == 11


def test_mylist_delete(mylist):
    del mylist[1]
    assert len(mylist) == 4
    assert mylist[1] == 10


def test_mylist_append(mylist):
    mylist.append(3)
    assert len(mylist) == 6
    assert mylist[5] == 3


def test_mylist_sort(mylist):
    mylist.sort()
    mylist_sorted = [1, 2, 8, 9, 10]
    assert mylist == mylist_sorted


def test_mylist_count(mylist):
    x = mylist.count(2)
    assert x == 1


def test_mylist_extend(mylist):
    ext = [3, 5]
    mylist.extend(ext)
    assert mylist == [1, 2, 10, 9, 8, 3, 5]


def test_mylist_index(mylist):
    x = mylist.index(9)
    assert x == 3


def test_mylist_insert(mylist):
    mylist.insert(0, 7)
    assert mylist == [7, 1, 2, 10, 9, 8]


def test_mylist_pop(mylist):
    mylist.pop(2)
    assert mylist == [1, 2, 9, 8]


def test_mylist_remove(mylist):
    mylist.remove(1)
    assert mylist == [2, 10, 9, 8]


def test_mylist_reverse(mylist):
    mylist.reverse()
    assert mylist == [8, 9, 10, 2, 1]


def test_mylist_length(mylist):
    assert len(mylist) == 5
