import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        ar=math.pi*math.pow(self.radius,2)
        print("area is",ar)