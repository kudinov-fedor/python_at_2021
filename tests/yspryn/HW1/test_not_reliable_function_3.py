import pytest
import tests.yspryn.HW1.not_reliable_function_3 as ysp
from tests.yspryn.HW1.not_reliable_function_3 import not_reliable


def test_not_reliable_function_test1(mocker):
    mocker.patch.object(ysp, 'random', return_value=0.9)
    assert not_reliable() == (0.9, 1)


def test_not_reliable_function_test2(mocker):
    mocker.patch.object(ysp, 'random', side_effect=[0.4, 0.3, 0.2, 0.25, 0.6, 1])
    assert not_reliable() == (1, 6)
    assert ysp.random.call_count == 6


def test_not_reliable_function_test3(mocker):
    mocker.patch.object(ysp, 'random', side_effect=[0.1, 0.15, 0.14, 0.2, 0.33, 0.49, 0.887, 0.1, 0.62, 0.8, 0.77])
    with pytest.raises(RuntimeError):
        not_reliable()
    assert ysp.random.call_count == 11
