import pytest
import random


"""
Cover with tests
"""

import random


def not_reliable():
    res = random.random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


# Test lower value
def test_not_reliable_lower_value(mocker):
    mocker.patch.object(random, "random", return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()


# Test equal value
def test_not_reliable_equal_value(mocker):
    mocker.patch.object(random, "random", return_value=0.5)
    assert not_reliable() == 0.5
    assert not_reliable() == 0.5
    assert not_reliable() == 0.5

    assert random.random.call_count == 3


# Test higher values
def test_not_reliable_higher_values(mocker):
    mocker.patch.object(random, "random", side_effect=[0.6, 0.9, 1])
    assert not_reliable() == 0.6
    assert not_reliable() == 0.9
    assert not_reliable() == 1

    assert random.random.call_count == 3


# Test when error occurs
def test_not_reliable_error(mocker):
    mocker.patch.object(random, "random", side_effect=[RuntimeError])
    with pytest.raises(RuntimeError):
        not_reliable()
