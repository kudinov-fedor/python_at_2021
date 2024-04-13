"""
Cover with tests
"""


from random import random


def not_reliable():
    res = random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res

def test_not_reliable_2_0_3(mocker):
    mocker.patch(res, 'random.random', return_value=0.3)
    res = not_reliable()
    assert res == 0.3
