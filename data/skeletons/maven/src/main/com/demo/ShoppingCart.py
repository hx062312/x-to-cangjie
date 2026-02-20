from __future__ import annotations

# Imports Begin
from src.main.com.demo.DiscountService import *
from src.main.com.demo.CartItem import *
import typing
from typing import *
import io

# Imports End


class ShoppingCart:

    # Class Fields Begin
    __items: List[CartItem] = None
    __discountService: DiscountService = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def clear(self) -> None:
        pass

    def hasDiscount(self) -> bool:
        pass

    def getDiscountService(self) -> DiscountService:
        pass

    def getTotal(self) -> float:
        pass

    def getDiscountAmount(self) -> float:
        pass

    def getSubtotal(self) -> float:
        pass

    def getItemCount(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def getItems(self) -> List[CartItem]:
        pass

    def removeItem(self, itemName: str) -> bool:
        pass

    def addItem(self, item: CartItem) -> None:
        pass

    @staticmethod
    def ShoppingCart1() -> ShoppingCart:
        pass

    def __init__(self, discountService: DiscountService) -> None:
        pass

    # Class Methods End
