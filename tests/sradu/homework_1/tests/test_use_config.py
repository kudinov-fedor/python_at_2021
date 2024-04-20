import pytest
from tests.sradu.homework_1.use_config import if_debug_on, CONFIG


@pytest.fixture(scope="function")
def restore_config():
    original_config = CONFIG.copy()
    yield
    CONFIG.update(original_config)


def test_is_debug_on_returns_original_value():
    assert if_debug_on() is True

def test_if_debug_on_returns_false(mocker):
    mocker.patch.dict(CONFIG, {'debug': False})
    assert  if_debug_on() is False

def test_if_debug_on_raises_key_error(mocker):
    mocker.patch.dict(CONFIG, {}, clear=True)
    with pytest.raises(KeyError):
        if_debug_on()
