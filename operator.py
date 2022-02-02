import math
 
class A:
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
        return A.normal_round(self.a * o.a)
    
    # division between 2 objects
    def __truediv__(self,o):
        return A.normal_round(self.a / o.a)
    
    # power of object
    def __pow__(self,o):
        return self.a % o.a
    
    
ob1 = A(5)
ob2 = A(2)
ob3 = A(8)
ob4 = A(4)
ob5 = A(2)
ob6 = A(2.24)
ob7 = A(2)
ob8 = A(2.25)
 
print(ob1 + ob2)
print(ob3 + ob4)
print()
print(ob1 - ob2)
print(ob3 - ob4)
print()
print(ob5 * ob6)
print(ob7 * ob8)
print()
print(ob1 / ob2)
print(ob3 / ob4)
print()
print(ob1 ** ob2)
print(ob3 ** ob4)

# print(1+3)