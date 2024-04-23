import pytest


"""
Cover with tests
"""

import random


def not_reliable():
    res = random.random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


def test_less_than_0_5(mocker):
    mocker.patch.object(random, "random", return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()


@pytest.mark.parametrize("value, expected", [(0.6, 0.6), (0.5, 0.5)])
def test_positive_cases(mocker, value, expected):
    mocker.patch.object(random, "random", return_value=value)
    assert not_reliable() == expected