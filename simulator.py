import copy
import numpy as np
from typing import List
from traffic_light import BaseTrafficLight


class Simulator():
    
    def __init__(self, traffic_paramaters:np.ndarray, traffic_light:BaseTrafficLight, decrease_rate:np.ndarray) -> None:
        self.traffic_paramaters = traffic_paramaters
        self.cars = traffic_paramaters[:,0]
        self.accumlation = traffic_paramaters[:,1:]
        self.traffic_light = traffic_light
        self.decrease_rate = decrease_rate
        self.counter = 0
        self.added_cars = np.zeros(4)
    

    def add_new_cars(self):
        self.added_right_cars = np.random.randint(self.accumlation[0][0],self.accumlation[0][1]+1)
        self.added_up_cars = np.random.randint(self.accumlation[1][0],self.accumlation[1][1]+1)
        self.added_left_cars = np.random.randint(self.accumlation[2][0],self.accumlation[2][1]+1)
        self.added_down_cars = np.random.randint(self.accumlation[3][0],self.accumlation[3][1]+1)
        self.added_cars = np.array([self.added_right_cars, self.added_up_cars, self.added_left_cars, self.added_down_cars])
        self.cars += self.added_cars

    def move_cars(self):
            self.cars[self.current_light] = max(self.cars[self.current_light] - self.decrease_rate, 0)

    def update(self):
            self.current_light = self.traffic_light.decide(self.counter, self.cars)
            print(self.counter, self.cars, self.current_light)
            self.add_new_cars()
            self.move_cars()
            self.counter += 1


    def run(self, i):
        print("--------")
        while self.counter <= i:
            for i in range(i):
                try:
                    self.update()
                except IndexError:
                     print(i)
                     break
            

    def numbers(self):
        Number = [0, 0, 0, 0]
        Number = self.added_cars
        return(Number)

