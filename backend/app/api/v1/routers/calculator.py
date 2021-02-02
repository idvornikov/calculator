from decimal import Decimal
from typing import Dict

from fastapi import APIRouter

from ..constants import StateCode, OrderPrice, DISCOUNTS, TAXES
from ..schemas import Order

router = calculator_router = APIRouter()


def get_discount_percent(order_price):
    if order_price == 0 or order_price < OrderPrice.ONE_THOUSAND:
        return 0
    elif OrderPrice.ONE_THOUSAND <= order_price < OrderPrice.FIVE_THOUSAND:
        return DISCOUNTS[OrderPrice.ONE_THOUSAND]
    elif OrderPrice.FIVE_THOUSAND <= order_price < OrderPrice.SEVEN_THOUSAND:
        return DISCOUNTS[OrderPrice.FIVE_THOUSAND]
    elif OrderPrice.SEVEN_THOUSAND <= order_price < OrderPrice.TEN_THOUSAND:
        return DISCOUNTS[OrderPrice.SEVEN_THOUSAND]
    elif OrderPrice.TEN_THOUSAND <= order_price < OrderPrice.FIFTY_THOUSAND:
        return DISCOUNTS[OrderPrice.TEN_THOUSAND]
    else:
        return DISCOUNTS[OrderPrice.FIFTY_THOUSAND]


@router.post('/calculator/')
async def calculate_order_cost(order: Order) -> Dict[str, Decimal]:
    raw_order_cost = order.count * order.price
    discount_percent = get_discount_percent(raw_order_cost)
    discount = round(raw_order_cost * discount_percent / 100, 2)
    order_with_discount = raw_order_cost - discount
    taxes = round(order_with_discount * TAXES[order.state_code] / 100, 2)
    final_order_cost = order_with_discount + taxes
    return {
        'raw_order_cost': raw_order_cost,
        'discount': discount,
        'order_with_discount': order_with_discount,
        'taxes': taxes,
        'final_order_cost': final_order_cost,
    }


@router.get('/calculator/state_code/')
async def get_state_code() -> Dict[str, float]:
    return StateCode.__members__
