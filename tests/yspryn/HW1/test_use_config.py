import pytest
from tests.yspryn.HW1.use_config import if_debug_on, CONFIG


def test_if_debug_on():
    assert if_debug_on() is True


def test_if_debug_on_with_debug_false(monkeypatch):
    monkeypatch.setitem(CONFIG, "debug", False)
    assert if_debug_on() is False


def test_if_debug_on_debug_key_absent(monkeypatch):
    monkeypatch.delitem(CONFIG, "debug", raising=True)
    with pytest.raises(KeyError):
        if_debug_on()
