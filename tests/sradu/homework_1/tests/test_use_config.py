import pytest
from tests.sradu.homework_1.use_config import if_debug_on, CONFIG


def test_is_debug_on_returns_original_value():
    assert if_debug_on() is True


def test_if_debug_on_returns_false(monkeypatch):
    monkeypatch.setitem(CONFIG, 'debug', False)
    assert if_debug_on() is False


def test_if_debug_on_raises_key_error(monkeypatch):
    monkeypatch.delitem(CONFIG, 'debug', raising=False)
    with pytest.raises(KeyError, match="debug"):
        if_debug_on()
