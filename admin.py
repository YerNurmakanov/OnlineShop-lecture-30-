import consumer


class Administrator(consumer.Consumer):

    __admin_id = 0

    def __init__(self, name, surname):
        super().__init__(name, surname)
        Administrator.__admin_id += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            raise ValueError('Invalid data type!')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) == str:
            self.__surname = surname
        else:
            raise ValueError('Invalid data type!')

    def get_admin_personal_info(self):
        print(' Administrator personal information:')
        print(f'{self.__admin_id}: {self.name} {self.surname}')

    def track_consumers(self, consumers):
        print(' Information about consumers:')
        for consumer in consumers:
            consumer.get_personal_info()
            if consumer.purchase_list:
                print(consumer.purchase_list)
            print('')

    def track_catalogs(self, catalogs):
        print(' Information about catalogs and their product range:')
        for catalog in catalogs:
            print(catalog.get_catalog_info())
            print(catalog.product_range)
            print('')

    def add_item_to_catalog(self, item, price):
        if item and price:
            ShopCatalog.add_item_to_product_range(item, price)

    def delete_item_from_catalog(self, item):
        ShopCatalog.delete_item_from_product_range(item)




