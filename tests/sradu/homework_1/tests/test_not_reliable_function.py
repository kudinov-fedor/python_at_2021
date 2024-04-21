import pytest
import random
from tests.sradu.homework_1.not_reliable_function import not_reliable


def test_not_reliable_success(mocker):
    mocker.patch.object(random, 'random', return_value=0.6)
    assert not_reliable() == 0.6


def test_not_reliable_failure(mocker):
    mocker.patch.object(random, 'random', return_value=0.4)
    with pytest.raises(RuntimeError, match=r"Res is less than 0.5:\s+0.4"):
        not_reliable()
