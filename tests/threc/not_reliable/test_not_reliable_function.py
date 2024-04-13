from tests.threc.not_reliable.not_reliable_function import not_reliable
import pytest


def test_not_reliable_0_5(mocker):
    mocker.patch('random.random', return_value=0.5)
    assert not_reliable() == 0.5


def test_not_reliable_0_6(mocker):
    mocker.patch('random.random', return_value=0.6)
    assert not_reliable() == 0.6


def test_not_reliable_2(mocker):
    mocker.patch('random.random', return_value=2)
    assert not_reliable() == 2


def test_not_reliable_0(mocker):
    mocker.patch('random.random', return_value=0)
    with pytest.raises(RuntimeError):
        not_reliable()
