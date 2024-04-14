import pytest


"""
Create 2 tests
in 1: if_debug_on should return original value from CONFIG
in 2: if_debug_on should return False
After test ends, CONFIG should stay the same as it was no matter if test passes or fails.

Also test if 'debug' key is not present - KeyError will happen
"""



CONFIG = {
    "debug": True,
    "b": "abc",
    "c": 123
}


def if_debug_on():
    return CONFIG["debug"]


def test_return_original(mocker):
    print("this is firts test")
    assert if_debug_on() == CONFIG["debug"]


def test_return_false(mocker):
    mocker.patch.dict(CONFIG, {
        "debug": False,
        "b": "abc",
        "c": 123
    })
    assert if_debug_on() == False

