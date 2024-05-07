import pytest
from tests.vvashchu import not_reliable_function_3
from tests.vvashchu.not_reliable_function_3 import not_reliable


@pytest.mark.parametrize(
    ['values', 'res'],
    [
        [[0.888], (0.888, 1)],
        [[0.887, 0.888], (0.888, 2)],
        [[0.887] * 9 + [0.888], (0.888, 10)],
        [[0.887] * 10 + [0.888], (0.888, 11)],
    ],
)
def test_not_reliable(mocker, values, res):
    mocker.patch.object(not_reliable_function_3, 'random', side_effect=values)
    assert not_reliable() == res


def test_not_reliable_negative_scenario(mocker):
    mocker.patch.object(not_reliable_function_3, 'random', side_effect=([0.1] * 11))
    with pytest.raises(RuntimeError) as exc_info:
        not_reliable()
    assert str(exc_info.value) == 'Its too much, total tries: 11'
