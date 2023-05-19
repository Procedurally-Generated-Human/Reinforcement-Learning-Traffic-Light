import numpy as np
from typing import List


class Simulator():
    
    def __init__(self, start:np.ndarray, accumulation:np.ndarray) -> None:
        self.start = start
        self.accumlation = accumulation
        self.cars = self.start
        self.counter = 0
    

    def update(self):
        added_cars = np.random.rand(4) < self.accumlation
        self.cars += added_cars
        self.counter += 1



