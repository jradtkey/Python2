class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print 'Health is: {}'.format(self.health)
        return self

class Dog(Animal):
    def setHealth(self):
        self.health = 150
        return self

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def setHealth(self):
        self.health = 170
        return self

    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print "I am a dragon. Health: {}".format(self.health)

class Ape(Animal):
    def setIntelligence(self):
        self.intelligence = 10
        return self

animal1 = Animal('Galaxy', 20)
animal1.walk().walk().walk().run().run().display_health()
dog1 = Dog('Rex', 0)
dog1.setHealth().walk().walk().walk().run().run().pet().display_health()
dragon1 = Dragon('Shrek', 0)
dragon1.setHealth().fly().display_health()
ape1 = Ape('George', 200)
ape1.walk().display_health()
