from Prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, fuel, name, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if self.reliability > random_number:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven