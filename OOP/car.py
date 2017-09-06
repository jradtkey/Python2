class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

car1 = Car(11000, 150, 'Full', 20000)
car2 = Car(5000, 100, 'Almost empty', 1000)
car3 = Car(9999, 120, 'Half Full', 10000)
car4 = Car(2000, 90, 'Empty', 30000)
car4 = Car(4000, 110, 'Kind of Full', 60000)
car5 = Car(80000, 200, 'Full', 300)
car6 = Car(8000, 90, 'Needs Gass', 21000)

print 'Car1'
car1.display_all()
print 'Car2'
car2.display_all()
print 'Car3'
car3.display_all()
print 'Car4'
car4.display_all()
print 'Car5'
car5.display_all()
print 'Car6'
car6.display_all()
