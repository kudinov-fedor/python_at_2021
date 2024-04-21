import pytest
import tests.sradu.homework_1.not_reliable_function_2 as module


def test_not_reliable_success(mocker):
    mocker.patch.object(module, 'random', return_value=0.5)
    result = module.not_reliable()
    assert result == 0.5


def test_not_reliable_failure(mocker):
    mocker.patch.object(module, 'random', return_value=0.49)
    with pytest.raises(RuntimeError, match=r"Res is less than 0.5:\s+0.49"):
        module.not_reliable()
