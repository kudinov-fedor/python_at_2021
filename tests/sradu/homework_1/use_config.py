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
