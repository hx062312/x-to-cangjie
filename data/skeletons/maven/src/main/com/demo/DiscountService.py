from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class DiscountService:

    # Class Fields Begin
    __discountType: DiscountType = None
    __discountValue: float = None
    # Class Fields End

    # Class Methods Begin
    def reset(self) -> None:
        pass

    def hasDiscount(self) -> bool:
        pass

    def getDiscountDescription(self) -> str:
        pass

    def calculateDiscount(self, subtotal: float) -> float:
        pass

    def withDiscount(self, type_: DiscountType, value: float) -> DiscountService:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class DiscountType:

    # Class Fields Begin
    NONE: DiscountType = None
    VIP: DiscountType = None
    FIXED_AMOUNT: DiscountType = None
    PERCENTAGE: DiscountType = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End
