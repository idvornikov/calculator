from decimal import Decimal
from enum import Enum


class StateCode(str, Enum):
    UT = 'UT'
    NV = 'NV'
    TX = 'TX'
    AL = 'AL'
    CA = 'CA'


class OrderPrice(int, Enum):
    ONE_THOUSAND = 1000
    FIVE_THOUSAND = 5000
    SEVEN_THOUSAND = 7000
    TEN_THOUSAND = 10000
    FIFTY_THOUSAND = 50000


class Discount(int, Enum):
    THREE_PERCENT = 3
    FIVE_PERCENT = 5
    SEVEN_PERCENT = 7
    TEN_PERCENT = 10
    FIFTEEN_PERCENT = 15


TAXES = {
    StateCode.UT: Decimal(6.85),
    StateCode.NV: Decimal(8),
    StateCode.TX: Decimal(6.25),
    StateCode.AL: Decimal(4),
    StateCode.CA: Decimal(8.25),
}

DISCOUNTS = {
    OrderPrice.ONE_THOUSAND: Discount.THREE_PERCENT,
    OrderPrice.FIVE_THOUSAND: Discount.FIVE_PERCENT,
    OrderPrice.SEVEN_THOUSAND: Discount.SEVEN_PERCENT,
    OrderPrice.TEN_THOUSAND: Discount.TEN_PERCENT,
    OrderPrice.FIFTY_THOUSAND: Discount.FIFTEEN_PERCENT,
}
