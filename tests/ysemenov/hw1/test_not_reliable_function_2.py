import pytest
from tests.ysemenov.hw1.not_reliable_function_2 import not_reliable
from tests.ysemenov.hw1 import not_reliable_function_2 as module


@pytest.mark.parametrize("random_value, expected_output", [
    pytest.param(0.5, 0.5, id="equal to 0.5"),
    pytest.param(0.6, 0.6, id="equal to 0.6"),
])
def test_not_reliable_positive(random_value, expected_output, mocker):
    mocker.patch.object(module, 'random', return_value=random_value)
    assert not_reliable() == expected_output


@pytest.mark.parametrize("random_value, expected_output", [
    pytest.param(0.4, None, id="runtime error"),
])
def test_not_reliable_negative(random_value, expected_output, mocker):
    mocker.patch.object(module, 'random', return_value=random_value)
    with pytest.raises(RuntimeError):
        not_reliable()
