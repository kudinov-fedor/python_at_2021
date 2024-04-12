from random import random
import pytest
from tests.yana_pokulita import test_not_reliable_function_3_hw1


def not_reliable():
    tries = 1
    res = random()

    while res < 0.888:
        if tries > 10:
            raise RuntimeError("Its too much, total tries: {}".format(tries))

        res = random()
        tries += 1

    return res, tries


@pytest.mark.parametrize(
    ['values', 'res'],
    [
        [[0.888], (0.888, 1)],
        [[0.887, 0.888], (0.888, 2)],
        [[0.887] * 9 + [0.888], (0.888, 10)],
        [[0.887] * 10 + [0.888], (0.888, 11)],
    ],
)
def test_not_reliable(mocker, values, res):
    mocker.patch.object(test_not_reliable_function_3_hw1,'random', side_effect=values)
    assert not_reliable() == res


def test_not_reliable_negative_scenario(mocker):
    mocker.patch.object(test_not_reliable_function_3_hw1,'random', side_effect=([0.1] * 11))
    with pytest.raises(RuntimeError) as exc_info:
        not_reliable()
    assert str(exc_info.value) == 'Its too much, total tries: 11'
