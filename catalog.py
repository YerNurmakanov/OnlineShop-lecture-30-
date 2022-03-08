class ShopCatalog:

    __product_range = {}

    def __init__(self, item, price):
        self.item = item
        self.price = price
        if self.item and self.price:
            ShopCatalog.__product_range[self.item] = self.price

    @classmethod
    def get_product_range(cls):
        print('Product range:')
        return ShopCatalog.__product_range

    def add_item_to_product_range(self, item, price):
        if item and price:
            ShopCatalog.__product_range[item] = price

    def delete_item_from_product_range(self, item):
        del ShopCatalog.__product_range[item]





