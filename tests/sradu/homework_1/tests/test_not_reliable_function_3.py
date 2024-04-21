import pytest
import tests.sradu.homework_1.not_reliable_function_3 as module


def test_not_reliable_success_first_try(mocker):
    mocker.patch.object(module, 'random', return_value=0.9)
    result, tries = module.not_reliable()
    assert result >= 0.888
    assert  tries == 1


def test_not_reliable_success_maximum_tries(mocker):
    sequence_of_returns = [0.1, 0.887, 0.0, 0.01, 0.1, 0.887, 0.0, 0.01, 0.01, 0.888]
    mocker.patch.object(module, 'random', side_effect=sequence_of_returns)
    result, tries = module.not_reliable()
    assert result >= 0.888
    assert tries == 10


def test_not_reliable_failure(mocker):
    sequence_of_returns = [0.1] * 11
    mocker.patch.object(module, 'random', side_effect=sequence_of_returns)
    with pytest.raises(RuntimeError, match="Its too much, total tries: 11"):
        module.not_reliable()
