

import pytest
from tests.ysemenov.hw1.use_config import CONFIG, if_debug_on


def test_if_debug_on_true(mocker):
    """testing normal flow"""
    assert if_debug_on() == CONFIG["debug"]


def test_if_debug_on_false(mocker):
    """testing debug not on"""
    mocker.patch.dict(CONFIG, {
        "debug": False,
        "b": "abc",
        "c": 123
    })
    assert if_debug_on() is False


def test_if_debug_on_keyerror(mocker):
    """testing key error"""
    mocker.patch.dict(CONFIG, clear=True)
    with pytest.raises(KeyError):
        if_debug_on()
