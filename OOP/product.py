class Product(object):
    """docstring for Product."""
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def tax(self):
        return '{}'.format(self.price + self.price*.1)

    def rtrn(self):
        if reason == 'defective':
            self.status = "Defective"
            self.price = 0
            return self
        elif reason == 'in box':
            self.status = "For Sale"
            return self
        elif reason == "opened":
            self.status = "Used"
            self.price = self.price*.80
            return self

    def display_info(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.cost
        print self.status


prod1 = Product(100, "Ball", 2, "Fisher Price", 20)
reason = 'opened'
prod1.rtrn().display_info()
