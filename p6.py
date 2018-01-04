# -*- coding: utf-8 -*-
# Created by Andrei Kisel

class Car:

    """Simple car class"""
    
    count = 0

    def __init__(self, color="black", wheels=5):
        """Constructor"""
        self.color = color
        self.wheels = wheels
        if self.color == "red":
            self.wheels = 4
        if self.wheels < 0:
            self.wheels = 5
        Car.count += 1

    def red_car(self):
        """Method for red car"""
        self.color = "red"
        self.wheels = 4

    def not_default_and_not_red_car(self, color, wheels):
        """Method for enother cars"""
        self.color = color
        self.wheels = wheels

    def diag(self):
        """Method for print out the color of the car and its wheels count"""
        print("This car is", self.color, "and has wheels", self.wheels)


obj1_cars_default = Car()
obj2_cars_default = Car("red")
obj3_cars_default = Car("red", 3)
obj4_cars_default = Car()
obj4_cars_default.red_car()
obj5_cars_default = Car("green", -2)
obj6_cars_default = Car("green", 2)


obj1_cars_default.diag()
obj2_cars_default.diag()
obj3_cars_default.diag()
obj4_cars_default.diag()
obj5_cars_default.diag()
obj6_cars_default.diag()

print("Value cars is", Car.count)
