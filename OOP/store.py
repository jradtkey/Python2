class Store(object):
    def __init__(self, products, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        self.products.remove(product)
        return self

store1 = Store([], '24 N Blvd', 'Bob')
store1.add_product('Floss').add_product('Gum').remove_product('Floss')
print store1.products
print store1.location

store2 = Store([], '5454 27th ave', 'Stew')
store2.add_product('Stickers')
print store2.products
