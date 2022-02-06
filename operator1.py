
class Operator1:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a
    
    # subtract from two objects
    def __sub__(self,o):
        return self.a - o.a
    
    # multiply two objects
    def __mul__(self,o):
        return self.a * o.a
    # division between 2 objects
    def __truediv__(self,o):
        return self.a / o.a
    
    # power of object
    def __pow__(self,o):
        return self.a ** o.a