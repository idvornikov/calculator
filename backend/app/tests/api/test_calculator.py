import pytest

from app.api.v1.constants import StateCode, DISCOUNTS, Discount
from app.api.v1.routers.calculator import get_discount_percent
from app.api.v1.schemas import Order


def test_get_state_code(client):
    response = client.get("/api/v1/calculator/state_code/")
    assert response.status_code == 200
    assert response.json() == StateCode.__members__


@pytest.mark.parametrize(
    'order_price,discount',
    (
        (999, 0),
        (1001, Discount.THREE_PERCENT),
        (5001, Discount.FIVE_PERCENT),
        (7001, Discount.SEVEN_PERCENT),
        (10001, Discount.TEN_PERCENT),
        (50001, Discount.FIFTEEN_PERCENT),
    ),
)
def test_get_discount_percent(order_price, discount):
    calculated_discount = get_discount_percent(order_price)
    assert calculated_discount == discount


@pytest.mark.parametrize(
    'data,result',
    (
        (
            {'price': 1, 'count': 1, 'state_code': StateCode.AL.value},
            {
                'raw_order_cost': 1,
                'discount': 0,
                'order_with_discount': 1,
                'taxes': 0.04,
                'final_order_cost': 1.04,
            },
        ),
    ),
)
def test_calculate_order_cost(client, data, result):
    response = client.post("/api/v1/calculator/", json=data)
    assert response.status_code == 200
    assert response.json() == result


def test_order_negative_number():
    with pytest.raises(ValueError):
        Order(count=1, price=-1, state_code=StateCode.AL.value).non_negative_number(-1)


def test_order_non_negative_number():
    order = Order(count=1, price=1, state_code=StateCode.AL.value)
    assert 1 == order.non_negative_number(1)
