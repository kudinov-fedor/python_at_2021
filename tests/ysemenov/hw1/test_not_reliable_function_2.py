import pytest
from tests.ysemenov.hw1.not_reliable_function_2 import not_reliable


@pytest.mark.parametrize("random_value, expected_output", [
    pytest.param(0.4, None, id="runtime error"),
    pytest.param(0.5, 0.5, id="equal to 0.5"),
    pytest.param(0.6, 0.6, id="equal to 0.6"),
])
def test_not_reliable(random_value, expected_output, mocker):
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_2.random', return_value=random_value)
    if expected_output is not None:
        assert not_reliable() == expected_output
    else:
        with pytest.raises(RuntimeError):
            not_reliable()
