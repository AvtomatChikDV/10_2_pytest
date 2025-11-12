import pytest

from src.main import calculate_taxes


@pytest.mark.parametrize('prices, taxes, expected',
                         [([10, 40, 100], 10, [11, 44, 110.0])])
def test_calculate_taxes(prices, taxes, expected):
    assert (calculate_taxes(prices,taxes)) == expected


def test_calculate_zero_negativ():
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([-10, 10, 10, 0], 10)
    assert str(exc_info.value) == 'Неверная цена'

    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([10, 10, 10], -10)
    assert str(exc_info.value) == 'Неверный налоговый процент'

