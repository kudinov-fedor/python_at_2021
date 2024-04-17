import pytest
from tests.ysemenov.hw1.not_reliable_function_3 import not_reliable


@pytest.mark.parametrize("random_values, expected_result", [
    pytest.param([0.888] + [0.887] * 10, (0.888, 1), id="0.888 on first try"),
    pytest.param([0.887] * 10 + [0.888], (0.888, 11), id="0.888 on last try"),
])
def test_not_reliable_equal_or_larger(random_values, expected_result, mocker):
    # test 0.888 on first try and 0.888 on last try
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_3.random', side_effect=random_values)
    assert not_reliable() == expected_result


@pytest.mark.parametrize("random_values, tries", [
    pytest.param([0.887] * 11, 11, id="11 incorrect tries"),
])
def test_not_reliable_tries(random_values, tries, mocker):
    # test over 10 tries with a value less than 0.888
    mocker.patch('tests.ysemenov.hw1.not_reliable_function_3.random', side_effect=random_values)
    with pytest.raises(RuntimeError):
        not_reliable()
