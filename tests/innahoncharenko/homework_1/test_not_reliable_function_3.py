"""
Cover with tests
"""

import pytest
from random import random


def not_reliable():
    tries = 1
    res = random()

    while res < 0.888:
        if tries > 10:
            raise RuntimeError("Its too much, total tries: {}".format(tries))

        res = random()
        tries += 1

    return res, tries


@pytest.mark.parametrize(['values', 'expected_result'], [
    ([0.888], (0.888, 1)),
    ([0.887,0.888], (0.888, 2)),
    ([0.887] * 9 + [0.888], (0.888, 10)),
    ([0.887] * 10 + [0.888], (0.888, 11)),
])
def test_positive_non_reliable(mocker, values, expected_result):
    mocker.patch(__name__ + ".random", side_effect=values)
    assert not_reliable() == expected_result


def test_negative_non_reliable(mocker):
    mocker.patch(__name__ + ".random", side_effect=[0.887] * 11)
    with pytest.raises(RuntimeError):
        not_reliable()

