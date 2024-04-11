"""
Cover with tests
"""


from random import random


def not_reliable():
    res = random()
    if res < 0.5:
        raise RuntimeError("Res is less than 0.5:  {}".format(res))
    return res
    
