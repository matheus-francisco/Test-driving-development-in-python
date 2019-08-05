"""
x Can create instance of Checkout class
x Can add item price
TODO

x Can add an item
- Can calculate the current total
- Can add multiple items and get correct total
- Can add discount rules
- Can add discount rules
- Can apply discount rules to the total
- Exception is throw for item added without a price
"""
import pytest
from functions.checkout import Checkout


@pytest.fixtures()
def checkout():
    checkout = Checkout()
    return checkout


def test_can_add_item_price(checkout):
    checkout.add_item_price("a", 1)


def test_can_add_item(checkout):
    checkout.add_item("a")


def test_can_calculate_total(checkout):
    checkout.add_item_price("a", 1)
    checkout.add_item("a")
    assert checkout.calculate_total() == 1
