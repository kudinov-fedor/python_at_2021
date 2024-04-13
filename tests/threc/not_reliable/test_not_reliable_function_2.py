import pytest

from tests.threc.not_reliable.not_reliable_function_2 import not_reliable
import tests.threc.not_reliable.not_reliable_function_2 as result

def test_not_reliable_2_0_5(mocker):
    mocker.patch.object(result, 'random', return_value=0.5)
    assert not_reliable() == 0.5

def test_not_reliable_2_0_4(mocker):
    mocker.patch.object(result, 'random', return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()

def test_not_reliable_2_1(mocker):
    mocker.patch.object(result, 'random', return_value=1)
    assert not_reliable() == 1

def test_not_reliable_2_0_6(mocker):
    mocker.patch.object(result, 'random', return_value=0.6)
    assert not_reliable() == 0.6
