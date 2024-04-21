import pytest
from random import random
from tests.mariana_petrushanska import test_not_reliable_function_3


def not_reliable():
    tries = 1
    res = random()

    while res < 0.888:
        if tries > 10:
            raise RuntimeError("Its too much, total tries: {}".format(tries))

        res = random()
        tries += 1

    return res, tries


# Test possible positive cases
@pytest.mark.parametrize(["value", "expected_result"], [
    pytest.param([0.888], (0.888, 1), id="res = 0.888"),
    pytest.param([0.889], (0.889, 1), id="res > 0.888"),
    pytest.param([0.5, 0.887, 0.888], (0.888, 3), id="final res = 0.888"),
    pytest.param([0.2, 0.5, 0.887, 0.889], (0.889, 4), id="final res > 0.888"),
    pytest.param([0.887] * 9 + [0.888], (0.888, 10), id="tries = 10"),
    pytest.param([0.5] * 8 + [1.5], (1.5, 9), id="tries < 10")
])
def test_not_reliable_positive_cases(mocker, value, expected_result):
    mocker.patch.object(test_not_reliable_function_3, "random", side_effect=value)
    assert not_reliable() == expected_result


# Test possible negative case
def test_not_reliable_negative_case(mocker):
    mocker.patch.object(test_not_reliable_function_3, "random", side_effect=([0.887] * 11))
    with pytest.raises(RuntimeError):
        not_reliable()
    assert test_not_reliable_function_3.random.call_count == 11


# Test when error occurs
def test_not_reliable_error(mocker):
    mocker.patch.object(test_not_reliable_function_3, "random", side_effect=[RuntimeError])
    with pytest.raises(RuntimeError):
        not_reliable()
