class Checkout:
    class Discount:
        def __init__(self, nbr_items, price):
            self.nbr_items = nbr_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.prices[item] * cnt
        return total

    def add_discount(self, item, nbr_of_items, price):
        discount = self.Discount(nbr_of_items, price)
        self.discounts[item] = discount
