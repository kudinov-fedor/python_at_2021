"""
Cover with tests
"""


from random import random


def not_reliable():
    tries = 1
    res = random()

    while res < 0.888:
        if tries > 10:
            raise RuntimeError("Its too much, total tries: {}".format(tries))

        res = random()
        tries += 1

    return res, tries
    
