from Prac_08.car import Car
from random import randint

class u_car(Car):

    def __init__(self, fuel, name, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self,distance):
        random_drive_distance = randint(0,100)
        if random_drive_distance >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven