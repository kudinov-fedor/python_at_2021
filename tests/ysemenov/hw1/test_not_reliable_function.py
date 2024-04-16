
import random
import pytest


def not_reliable():
    res = random.random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


def test_not_reliable(mocker):
    # return 0.4
    mocker.patch.object(random, 'random', return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()

    # return 0.5
    mocker.patch.object(random, 'random', return_value=0.5)
    assert not_reliable() == 0.5

    # return 0.6
    mocker.patch.object(random, 'random', return_value=0.6)
    assert not_reliable() == 0.6
