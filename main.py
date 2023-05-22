import numpy as np
from traffic_light import BaseTrafficLight, RRTrafficLight
from simulator import Simulator


starting_cars = np.array([110,100,100,100])
accumulation = np.array([[0,1],[1,2],[0,3],[9,10]])

traffic_paramaters = np.array([[0,5,10],[10,3,5],[5,7,10],[0,0,5]])

tf = RRTrafficLight(10)
sim = Simulator(traffic_paramaters, tf, 10)

for i in range(100):
    sim.update()
    print(sim.cars)

