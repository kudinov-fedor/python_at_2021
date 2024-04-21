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


def test_debug_original_state():
    assert if_debug_on() is True


def test_debug_off_state(monkeypatch):
    monkeypatch.setitem(CONFIG, "debug", False)
    assert if_debug_on() is False


def test_error(monkeypatch):
    monkeypatch.delitem(CONFIG, "debug")
    with pytest.raises(KeyError):
        if_debug_on()


