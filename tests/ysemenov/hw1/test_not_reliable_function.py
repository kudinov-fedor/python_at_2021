import random
import pytest


def not_reliable():
    res = random.random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


@pytest.mark.parametrize("random_value, expected_output", [
    pytest.param(0.4, None, id="runtime error"),
    pytest.param(0.5, 0.5, id="equal to 0.5"),
    pytest.param(0.6, 0.6, id="equal to 0.6"),
])
def test_not_reliable(random_value, expected_output, mocker):
    mocker.patch.object(random, 'random', return_value=random_value)
    if expected_output is not None:
        assert not_reliable() == expected_output
    else:
        with pytest.raises(RuntimeError):
            not_reliable()
