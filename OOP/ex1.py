### Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance
# of the line.


class Line:

    def __init__(self, coordinate1: tuple, coordinate2: tuple):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

    def slope(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return (y2 - y1)/(x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


#### Fill in the class

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * self.radius ** 2

    def surface_area(self):
        top = 3.14 * self.radius ** 2
        return (2 * top) + (2 * 3.14 * self.radius * self.height)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
