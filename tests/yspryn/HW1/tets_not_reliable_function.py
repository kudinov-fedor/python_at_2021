import pytest
import random
from tests.yspryn.HW1.not_reliable_function import not_reliable


def test_not_reliable_function(mocker):
    mocker.patch.object(random, 'random', return_value=0.5)
    assert not_reliable() == 0.5
    assert not_reliable() == 0.5
    assert not_reliable() == 0.5
    assert not_reliable() == 0.5

    assert random.random.call_count == 4


def test_not_reliable_function_low_value(mocker):
    mocker.patch.object(random, 'random', return_value=0.49)
    with pytest.raises(RuntimeError):
        not_reliable()


def test_not_reliable_function_side_effect(mocker):
    mocker.patch.object(random, 'random', side_effect=[0.5, 0.6, 0.74])
    assert not_reliable() == 0.5
    assert not_reliable() == 0.6
    assert not_reliable() == 0.74

    assert random.random.call_count == 3


def test_not_reliable_function_side_effect_error(mocker):
    mocker.patch.object(random, 'random', side_effect=RuntimeError)
    with pytest.raises(RuntimeError):
        not_reliable()
