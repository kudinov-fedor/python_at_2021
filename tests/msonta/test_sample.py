import pytest
import random


def add(a, b):
    return a + b


def test_sample():
    pass


@pytest.mark.xfail
def test_fail():
    assert 1 == 2


@pytest.mark.xfail
def test_pass():
    assert 1 == 1


@pytest.mark.parametrize("a, b, expected",[
    (1, 1, 2),
    (2, 2, 4),
    pytest.param("1", "2", 0, marks=pytest.mark.skipif(reason="AssertionError"))])
def test_sum(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, expected", [
    ("hello", 5),
    ("pytest", 6),
    (0, TypeError),
    (0.1, TypeError),
    (None, TypeError),
    (["test", "selenium", "pytest"], 3),
    ([1, 2, 3, 4, 5], 5)

])
def test_len(a, expected):
    try:
        length = len(a)
    except Exception as e:
        assert isinstance(e, expected)
    else:
        assert length == expected


@pytest.mark.parametrize("a, expected", [
    ("pytest", ["p", "y", "t", "e", "s", "t"]),
    ("", []),
    ([1, 2, 3], [1, 2, 3]),
    (5, TypeError),
    (0, TypeError),
    (0.1, TypeError),
    (None, TypeError)
])
def test_list(a, expected):
    try:
        res = list(a)
    except Exception as e:
        assert isinstance(e, expected)
    else:
        assert res == expected


@pytest.fixture
def random_list():
    res = random.sample(range(10), 6)
    return res


def test_list_len(random_list):
    assert len(random_list) == 6
