import pytest
from collections import UserList


def test_my_func(session):
    print("hi there")
    print(session)


def test_my_func_2(session):

    with pytest.raises(ZeroDivisionError):
        5 / 0


def test_list_len(mocker):
    mocker.spy(UserList, "__len__")
    my_list = UserList()
    len(my_list)
    assert UserList.__len__.called
