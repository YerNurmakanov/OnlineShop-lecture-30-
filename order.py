
class ConsumerOrder:

    __items_ordered = {}

    def __init__(self, item, price):
        self.item = item
        self.price = price
        if self.item and self.price:
            ConsumerOrder.__items_ordered[self.item] = self.price

    def __str__(self):
        return f'{ConsumerOrder.__items_ordered}'







