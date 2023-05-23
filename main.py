import numpy as np
from traffic_light import BaseTrafficLight, RRTrafficLight
from simulator import Simulator
from animator import Animator

traffic_paramaters = np.array([[0,5,10],[10,3,5],[5,7,10],[0,0,5]])

tf = RRTrafficLight(10)
sim = Simulator(traffic_paramaters, tf, 10)
ani = Animator(sim)
ani.setup()

#sim.update(100)

 