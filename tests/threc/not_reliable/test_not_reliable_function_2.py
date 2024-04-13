import pytest

from tests.threc.not_reliable.not_reliable_function_2 import not_reliable
import tests.threc.not_reliable.not_reliable_function_2 as result


@pytest.mark.parametrize(["value"], [
    pytest.param(0.5),
    pytest.param(0.6),
    pytest.param(1)
])
def test_not_reliable_2(mocker, value):
    mocker.patch.object(result, 'random', return_value=value)
    assert not_reliable() == value
    assert not_reliable() == value
    assert not_reliable() == value


def test_not_reliable_2_0_4(mocker):
    mocker.patch.object(result, 'random', return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()
