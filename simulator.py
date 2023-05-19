import numpy as np
from typing import List


class Simulator():
    
    def __init__(self, start:np.ndarray, accumulation:np.ndarray) -> None:
        self.start = start
        self.accumlation = accumulation
        self.cars = self.start
        self.counter = 0
    

    def update(self):
        added_right_cars = np.random.randint(self.accumlation[0][0],self.accumlation[0][1]+1)
        added_up_cars = np.random.randint(self.accumlation[1][0],self.accumlation[1][1]+1)
        added_left_cars = np.random.randint(self.accumlation[2][0],self.accumlation[2][1]+1)
        added_down_cars = np.random.randint(self.accumlation[3][0],self.accumlation[3][1]+1)
        added_cars = np.array([added_right_cars, added_up_cars, added_left_cars, added_down_cars])
        self.cars += added_cars
        self.counter += 1



