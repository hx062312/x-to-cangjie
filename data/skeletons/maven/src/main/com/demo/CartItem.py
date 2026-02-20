from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class CartItem:

    # Class Fields Begin
    __price: float = None
    __quantity: int = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, o: typing.Any) -> bool:
        pass

    def getSubtotal(self) -> float:
        pass

    def getQuantity(self) -> int:
        pass

    def getPrice(self) -> float:
        pass

    def getName(self) -> str:
        pass

    def __init__(self, name: str, price: float, quantity: int) -> None:
        pass

    # Class Methods End
