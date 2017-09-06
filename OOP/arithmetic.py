class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *x):
        for num in x:
            if isinstance(num, list) or isinstance(num, tuple):
                for value in num:
                    #print value
                    self.total += value
                    #print self.total
            else:
                #print num
                self.total += num
                #print self.total
        return self

    def subtract(self, *x):
        for num in x:
            if isinstance(num, list):
                for value in num:
                    #print value
                    self.total -= value
                    #print self.total
            else:
                #print num
                self.total -= num
                #print self.total
        return self

md = MathDojo()
print mds.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).total
