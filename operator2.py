import math

class Operator2:
    
    def __init__(self, a):
        self.a = a

    def normal_round(n):
        if n - math.floor(n) < 0.5:
            return math.floor(n)
        return math.ceil(n)

    # adding two objects
    def __add__(self, o):
        return max(self.a,o.a)
    
    # subtract from two objects
    def __sub__(self,o):
        return min(self.a,o.a)
    
    # multiply two objects
    def __mul__(self,o):
        return self.normal_round(self.a * o.a)
    
    # division between 2 objects
    def __truediv__(self,o):
        return self.normal_round(self.a / o.a)
    
    # power of object
    def __pow__(self,o):
        return self.a % o.a
