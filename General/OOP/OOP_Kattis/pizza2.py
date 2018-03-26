from math import pi


class Pizza(object):
    def __init__(self, base_radius, crust_radius):
        self.base = base_radius
        self.crust = crust_radius

    def get_base_area(self):
        return pi * (self.base) ** 2

    def get_cheese_area(self):
        cheese_radius = self.base - self.crust
        return pi * (cheese_radius) ** 2

    def get_percentage(self, total_area, cheese_area):
        return (cheese_area * 100.0) / total_area


R, C = map(int, input().split())
pizza = Pizza(R, C)
total_area = pizza.get_base_area()
cheese_area = pizza.get_cheese_area()
percentage = pizza.get_percentage(total_area, cheese_area)
print(percentage)
