"""
Cover with tests
"""

import random


def not_reliable():
    res = random.random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res


def test_res_more_0_5(mocker):
    mocker.patch('random.random', return_value=0.6)
    res = not_reliable()
    assert res == 0.6
