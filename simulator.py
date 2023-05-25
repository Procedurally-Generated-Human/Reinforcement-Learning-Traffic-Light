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
        self.added_cars = np.zeros(4)
        self.current_light = 5
    

    def add_new_cars(self):
        self.added_right_cars = np.random.randint(self.accumlation[0][0],self.accumlation[0][1]+1)
        self.added_up_cars = np.random.randint(self.accumlation[1][0],self.accumlation[1][1]+1)
        self.added_left_cars = np.random.randint(self.accumlation[2][0],self.accumlation[2][1]+1)
        self.added_down_cars = np.random.randint(self.accumlation[3][0],self.accumlation[3][1]+1)
        self.added_cars = np.array([self.added_right_cars, self.added_up_cars, self.added_left_cars, self.added_down_cars])
        self.cars += self.added_cars


    def update(self):
            change = False
            self.add_new_cars()
            if self.current_light != self.traffic_light.decide(self.counter, self.cars) and self.counter!=0:
                change = True
            self.current_light = self.traffic_light.decide(self.counter, self.cars)
            if not change:
                self.cars[self.current_light] = max(self.cars[self.current_light] - self.decrease_rate,0)
            self.counter += 1
            print(self.cars)
    

    def run(self, i):
        while self.counter <= i:
            for i in range(i):
                self.update()
        print(self.counter)
            

    def numbers(self):
        Number = [0, 0, 0, 0]
        Number = self.added_cars
        return(Number)
    

    def train_rl(self):
        pass