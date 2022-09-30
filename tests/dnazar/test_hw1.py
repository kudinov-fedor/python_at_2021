import random
import pytest


@pytest.fixture()
def get_num():
    return random.randint(-100, 100)


def test_append(get_num):
    my_list = [1, 2, 3]
    my_list.append(get_num)
    assert get_num in my_list


def test_random_equals_fifty(get_num):
    if get_num != 50:
        pytest.skip("Random returns always different numbers")
    assert get_num == 50


@pytest.mark.xfail
def test_fail_hash():
    my_first_str = 'Test'
    my_second_str = 'Test '
    assert hash(my_first_str) == hash(my_second_str)


@pytest.mark.parametrize("param1, param2, res", [
    (-13, 2, 1),
    (0, 9, 0),
    (7, 5, 2),
])
def test_module(param1, param2, res):
    assert param1 % param2 == res
