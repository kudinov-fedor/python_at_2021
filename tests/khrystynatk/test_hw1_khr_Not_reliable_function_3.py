import pytest
from tests.khrystynatk import hw1_khr_Not_reliable_function_3
from tests.khrystynatk.hw1_khr_Not_reliable_function_3 import not_reliable


@pytest.mark.parametrize("val1", [
    0.9,
    0.89,
    0.99
])
def test_one_try(mocker, val1):
    mocker.patch.object(hw1_khr_Not_reliable_function_3, "random", return_value=val1)
    assert not_reliable() == (val1, 1)


@pytest.mark.parametrize("val2", [
    [0.1, 0.887, 0.888],
    [0.05, 0.888, 0.1],
    [0.888, 0.1, 0.2]
])
def test_boundary(mocker, val2):
    mocker.patch.object(hw1_khr_Not_reliable_function_3, "random", side_effect=val2)
    assert not_reliable() == (0.888, val2.index(0.888) + 1)
    assert hw1_khr_Not_reliable_function_3.random.call_count == val2.index(0.888) + 1


def test_error(mocker):
    floats_list = [float(i) / 10 for i in range(1, 12)]
    mocker.patch.object(hw1_khr_Not_reliable_function_3, "random", side_effect=floats_list)
    with pytest.raises(RuntimeError):
        not_reliable()
