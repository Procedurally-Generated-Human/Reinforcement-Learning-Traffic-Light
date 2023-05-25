import numpy as np
from traffic_light import MFTrafficLight, RRTrafficLight
from simulator import Simulator
from animator import Animator

traffic_paramaters = np.array([[50,1,1],[50,1,1],[50,1,1],[50,1,1]])

tf = MFTrafficLight()
sim = Simulator(traffic_paramaters, tf, 10)
sim.run(30)