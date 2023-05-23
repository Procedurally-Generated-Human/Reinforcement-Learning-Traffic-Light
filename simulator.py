import numpy as np
from typing import List
from traffic_light import BaseTrafficLight


class Simulator():
    
    def __init__(self, traffic_paramaters:np.ndarray, traffic_light:BaseTrafficLight, decrease_rate=10) -> None:
        self.cars = traffic_paramaters[:,0]
        self.accumlation = traffic_paramaters[:,1:]
        self.traffic_light = traffic_light
        self.decrease_rate = decrease_rate
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
        self.cars[current_light] = max(self.cars[current_light] - self.decrease_rate,0)


    def update(self, steps:int):
        for i in range(steps):
            self.add_new_cars()
            self.move_cars()
            self.counter += 1
            print(self.cars)




