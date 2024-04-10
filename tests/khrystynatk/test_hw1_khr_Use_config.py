from tests.khrystynatk.hw1_khr_Use_config import if_debug_on
from tests.khrystynatk.hw1_khr_Use_config import CONFIG
import pytest


def test_original_val():
    assert if_debug_on()


def test_mocked_val(monkeypatch):
    monkeypatch.setitem(CONFIG, "debug", False)
    mocked_res = False
    assert if_debug_on() == mocked_res


def test_missing_key(monkeypatch):
    monkeypatch.delitem(CONFIG, "debug", raising=False)
    with pytest.raises(KeyError):
        _ = if_debug_on()
