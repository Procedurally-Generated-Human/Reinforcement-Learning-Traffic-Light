import numpy as np

from simulator import Simulator


starting_cars = np.array([10,0,50,0])
accumulation = np.array([[0,1],[1,2],[0,3],[9,10]])
sim = Simulator(starting_cars, accumulation)

for i in range(20):
    sim.update()
    print(sim.cars)

