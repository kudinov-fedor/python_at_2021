import pytest
from tests.khrystynatk import hw1_khr_Not_reliable_function_2
from tests.khrystynatk.hw1_khr_Not_reliable_function_2 import not_reliable


@pytest.mark.parametrize("val", [
    0.5,
    0.6,
    0.7
])
def test_mock(mocker, val):
    mocker.patch.object(hw1_khr_Not_reliable_function_2, "random", return_value=val)
    assert not_reliable() == val
    assert hw1_khr_Not_reliable_function_2.random.call_count == 1


@pytest.mark.parametrize("val1", [
    [0.5, 0.6, 0.7],
    [0.55, 0.66, 0.77]
])
def test_side_values(mocker, val1):
    mocker.patch.object(hw1_khr_Not_reliable_function_2, "random", side_effect=val1)
    assert not_reliable() == val1[0]
    assert not_reliable() == val1[1]
    assert not_reliable() == val1[2]
    assert hw1_khr_Not_reliable_function_2.random.call_count == 3


@pytest.mark.parametrize("val2", [
    0,
    0.1,
    0.22,
    -1
])
def test_low_val(mocker, val2):
    mocker.patch.object(hw1_khr_Not_reliable_function_2, "random", return_value=val2)
    with pytest.raises(RuntimeError):
        not_reliable()
