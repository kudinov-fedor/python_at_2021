import pytest


def test_my_func_1(session):
    print("Hello!")
    print(session)


def test_my_func_2(session):
    with pytest.raises(ZeroDivisionError):
        8 / 0


def test_my_func_3():
    x = [1, 2, 3]
    x_len = len(x)
    assert x_len == 3
