class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        if self.miles > 5:
            self.miles -= 5
        else:
            self.miles = 0

bike1 = Bike(150, "15mph", 0)
bike2 = Bike(300, "25mph", 0)
bike3 = Bike(250, "20mph", 0)

for value in range(0,3):
    bike1.ride()
bike1.reverse()
bike1.displayInfo()

for value in range(0,2):
    bike2.ride()
    bike2.reverse()
bike2.displayInfo()

for value in range(0,3):
    bike3.reverse()
bike3.displayInfo()
