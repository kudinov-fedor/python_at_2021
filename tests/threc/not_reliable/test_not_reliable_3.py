import pytest

from tests.threc.not_reliable.not_reliable_function_3 import not_reliable
import tests.threc.not_reliable.not_reliable_function_3 as result


def test_not_releable_test1(mocker):
        mocker.patch.object(result, 'random', return_value=1)
        assert not_reliable() == (1, 1)

def test_not_releable_test2(mocker):
    mocker.patch.object(result, 'random', side_effect=[0.2, 0.3, 0.4, 0.55, 0.7, 0.8, 0.87, 1])
    assert not_reliable() == (1, 8)

def test_not_releable_error(mocker):
    mocker.patch.object(result, 'random', return_value=0.8)
    with pytest.raises(RuntimeError):
        not_reliable()