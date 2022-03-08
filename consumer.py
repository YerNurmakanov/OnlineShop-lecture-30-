import catalog


class Consumer:

    __consumer_id = 0
    __consumers = {}

    def __init__(self, name, surname):
        Consumer.__consumer_id += 1
        self.__consumer_id = Consumer.__consumer_id
        self.name = name
        self.surname = surname
        self.purchase_list = None
        if self.name and self.surname:
            Consumer.__consumers[self.__consumer_id] = f'{self.name} {self.surname}'

    def get_personal_info(self):
        print(f'{self.__consumer_id}: {self.name} {self.surname}')

    @classmethod
    def get_consumers(cls):
        return Consumer.__consumers


class Administrator:

    def track_consumers(self, consumers):
        print('Information about consumers:')
        for consumer in consumers:
            consumer.get_personal_info()
            if consumer.purchase_list:
                print(consumer.purchase_list)
            print('')

    def add_item_to_catalog(self, item, price):
        if item and price:
            catalog.ShopCatalog.add_item_to_product_range(self, item, price)





