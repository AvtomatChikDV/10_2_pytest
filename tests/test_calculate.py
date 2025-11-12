import pytest

from src.main import calculate_taxes
from src.main import calculate_tax

@pytest.fixture()
def prices():
    return [100, 200, 300]


@pytest.mark.parametrize('tax_rate, expected',
                         [( 10, [110, 220, 330]),
                          ( 20, [120, 240, 360])])
def test_calculate_taxes(prices, tax_rate, expected):
    assert (calculate_taxes(prices,tax_rate)) == expected


def test_calculate_zero_negativ(prices):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([-10, 10, 10, 0], 10)
    assert str(exc_info.value) == 'Неверная цена'

    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(prices, -10)
    assert str(exc_info.value) == 'Неверный налоговый процент'


@pytest.mark.parametrize('price, tax_rate, expected',[(100, 10, 110),
                                                          (50, 5, 52.5)])
def test_calculate_tax(price, tax_rate, expected):
    assert (calculate_tax(price,tax_rate)) == expected

@pytest.mark.parametrize('price',[(-1),
                                   (0)])
def test_calculate_tax_price_negative(price):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, 1)

def test_calculate_tax_tax_rate_negative():
        with pytest.raises(ValueError) as exc_info:
            calculate_tax(1, -1)

@pytest.mark.parametrize('discount, point',[("1", 1),
                                   (1, " ")])
def test_calculate_tax_type_invalid(discount, point):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(1, 1, discount, point)





