import pytest
from parametrization import Parametrization


@pytest.mark.parametrize(["data", "expected_len"],
                         [([1, 2, 3], 3),
                          ([1, 2, 3, 4], 4),
                          ([], 0)])
def test_my_func_1(data, expected_len):
    data_len = len(data)
    assert data_len == expected_len


@Parametrization.autodetect_parameters()
@Parametrization.case(name="TestA", data=[1, 2, 3], expected_len=3)
@Parametrization.case(name="TestB", data=[1, 2, 3, 4], expected_len=4)
@Parametrization.case(name="TestC", data=[], expected_len=0)
def test_my_func_2(data, expected_len):
    data_len = len(data)
    assert data_len == expected_len


@pytest.mark.parametrize(["data", "expected_len"],
                         [([1, 2, 3], 3),
                          ([1, 2, 3, 4], 4),
                          ([], 0)], ids=['TestA', 'TestB', 'TestC'])
def test_my_func_3(data, expected_len):
    data_len = len(data)
    assert data_len == expected_len
