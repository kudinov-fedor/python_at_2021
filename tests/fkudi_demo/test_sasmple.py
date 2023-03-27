import pytest


def test_my_func(session):
    print("hi there")
    print(session)


def test_my_func_2(session):

    with pytest.raises(ZeroDivisionError):
        5 / 0
