

import pytest
from tests.ysemenov.hw1.not_reliable_function_2 import not_reliable


def test_not_reliable(mocker):
    # return 0.4
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_2.random', return_value=0.4)
    with pytest.raises(RuntimeError):
        not_reliable()

    # return 0.5
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_2.random', return_value=0.5)
    assert not_reliable() == 0.5

    # return 0.6
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_2.random', return_value=0.6)
    assert not_reliable() == 0.6
