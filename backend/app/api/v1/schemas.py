from decimal import Decimal

from pydantic import validator
from pydantic.main import BaseModel

from .constants import StateCode


class Order(BaseModel):
    count: int
    price: Decimal
    state_code: StateCode

    @validator('count', 'price')
    def non_negative_number(cls, value):
        if value <= 0:
            raise ValueError('must be greater than zero')
        return value
