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


# ------------------------------------------------------------------


# Test 1: if_debug_on returns original value from CONFIG
def test_if_debug_on():
    assert if_debug_on() is True


# Test 2: if_debug_on returns False
def test_if_debug_on_false_state(monkeypatch):
    monkeypatch.setitem(CONFIG, "debug", False)
    assert if_debug_on() is False


# Test 3: if 'debug' key is absent - KeyError is raised
def test_absent_key(monkeypatch):
    monkeypatch.delitem(CONFIG, "debug")
    with pytest.raises(KeyError):
        if_debug_on()
