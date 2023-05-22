import numpy as np
from traffic_light import BaseTrafficLight, RRTrafficLight
from simulator import Simulator


starting_cars = np.array([110,100,100,100])
#accumulation = np.array([[0,1],[1,2],[0,3],[9,10]])
accumulation = np.array([[0,0],[0,0],[0,0],[0,0]])
tf = RRTrafficLight(10)
sim = Simulator(starting_cars, accumulation, tf)

for i in range(100):
    sim.update()
    print(sim.cars)

