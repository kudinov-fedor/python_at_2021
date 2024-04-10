import pytest
import tests.yspryn.HW1.not_reliable_function_2 as ysp
from tests.yspryn.HW1.not_reliable_function_2 import not_reliable, random


def test_not_reliable_function1(mocker):
    mocker.patch.object(ysp, 'random', return_value=0.5)
    assert not_reliable() == 0.5
    assert not_reliable() == 0.5
    assert not_reliable() == 0.5
    assert ysp.random.call_count == 3

def test_not_reliable_function2(mocker):
    mocker.patch.object(ysp, 'random', return_value=0.49)
    with pytest.raises(RuntimeError):
        not_reliable()