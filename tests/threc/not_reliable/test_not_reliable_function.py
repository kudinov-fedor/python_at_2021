from tests.threc.not_reliable.not_reliable_function import not_reliable
import pytest


@pytest.mark.parametrize("value", [0.5, 0.6, 2])
def test_not_reliable(mocker, value):
    mocker.patch('random.random', return_value=value)
    assert not_reliable() == value
    assert not_reliable() == value
    assert not_reliable() == value


def test_not_reliable_error(mocker):
    mocker.patch('random.random', return_value=0)
    with pytest.raises(RuntimeError):
        not_reliable()
