import pytest

import tests.threc.hw_config.use_config
from tests.threc.hw_config.use_config import if_debug_on


def test_if_debug_on():
    assert if_debug_on()


def test_if_debug_off(monkeypatch):
    monkeypatch.setitem(tests.threc.hw_config.use_config.CONFIG, "debug", False)
    assert if_debug_on() is False


def test_if_debug_error(monkeypatch):
    monkeypatch.delitem(tests.threc.hw_config.use_config.CONFIG, "debug")
    with pytest.raises(KeyError):
        assert if_debug_on()