"""
x Can create instance of Checkout class
x Can add item price
TODO

- Can add an item
- Can calculate the current total
- Can add multiple items and get correct total
- Can add discount rules
- Can add discount rules
- Can apply discount rules to the total
- Exception is throw for item added without a price
"""
from functions.checkout import Checkout


def test_can_add_item_price():
    co = Checkout()
    co.add_item_price("a", 1)
