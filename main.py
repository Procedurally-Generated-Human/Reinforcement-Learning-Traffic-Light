import numpy as np

from simulator import Simulator


starting_cars = np.array([10,0,50,0])
accumulation = np.array([0.1,0.3,0.5,2])
sim = Simulator(starting_cars, accumulation)

for i in range(20):
    sim.update()
    print(sim.cars)

