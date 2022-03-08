import catalog
import order
import consumer


c1 = consumer.Consumer('Jack', 'Sparrow')
c2 = consumer.Consumer('Micky', 'Mouse')
c2.purchase_list = order.ConsumerOrder('Pencil', 20)
c2.purchase_list = order.ConsumerOrder('Shirt', 250)
print(c2.purchase_list)

my_catalog = catalog.ShopCatalog('bread', 25)
my_catalog.add_item_to_product_range('brush', 42)
print(my_catalog.get_product_range())

admin = consumer.Administrator()
admin.track_consumers([c1, c2])

admin.add_item_to_catalog('Pepsi', 25)
admin.add_item_to_catalog('HotDog', 40)
print(my_catalog.get_product_range())