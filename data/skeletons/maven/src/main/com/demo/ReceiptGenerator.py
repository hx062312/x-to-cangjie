from __future__ import annotations

# Imports Begin
from src.main.com.demo.ShoppingCart import *
from src.main.com.demo.DiscountService import *
from src.main.com.demo.CartItem import *
import io

# Imports End


class ReceiptGenerator:

    # Class Fields Begin
    __SEPARATOR: str = None
    # Class Fields End

    # Class Methods Begin
    def generateSummary(self, cart: ShoppingCart) -> str:
        pass

    def generate(self, cart: ShoppingCart) -> str:
        pass

    # Class Methods End
