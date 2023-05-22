import numpy as np
from typing import List
from traffic_light import BaseTrafficLight

class Simulator():
    
    def __init__(self, start:np.ndarray, accumulation:np.ndarray, traffic_light:BaseTrafficLight) -> None:
        self.start = start
        self.accumlation = accumulation
        self.traffic_light = traffic_light
        self.cars = self.start
        self.counter = 0
    

    def add_new_cars(self):
        added_right_cars = np.random.randint(self.accumlation[0][0],self.accumlation[0][1]+1)
        added_up_cars = np.random.randint(self.accumlation[1][0],self.accumlation[1][1]+1)
        added_left_cars = np.random.randint(self.accumlation[2][0],self.accumlation[2][1]+1)
        added_down_cars = np.random.randint(self.accumlation[3][0],self.accumlation[3][1]+1)
        added_cars = np.array([added_right_cars, added_up_cars, added_left_cars, added_down_cars])
        self.cars += added_cars


    def move_cars(self):
        current_light = self.traffic_light.decide(self.counter, self.cars)
        self.cars[current_light] = max(self.cars[current_light] - 10,0)


    def update(self):
        self.add_new_cars()
        self.move_cars()
        self.counter += 1




