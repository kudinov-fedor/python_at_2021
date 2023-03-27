import pytest


@pytest.mark.parametrize(["data", "expected_len"], [
    ([1, 2, 3], 3),
    ([], 0)
])
def test_my_func_data_driven(data, expected_len):  # AAA
    x = data  # arrange
    x_len = len(x)  # act
    assert x_len == expected_len  # assert


def test_my_func_4():  # AAA
    x = []  # arrange
    x_len = len(x)  # act
    assert x_len == 0  # assert
