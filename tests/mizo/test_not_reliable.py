import pytest
import random

"""
Cover with tests
"""


def not_reliable():
    res = random.random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


def test_not_reliable(mocker):
    mocker.patch.object(random, "random", return_value=0.5)
    assert not_reliable() == 0.5


def test_not_reliable_error(mocker):
    mocker.patch.object(random, "random", return_value=0.49)
    with pytest.raises(RuntimeError, match="Res is less than 0.5"):
        not_reliable()
