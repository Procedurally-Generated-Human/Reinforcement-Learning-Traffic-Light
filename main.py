import numpy as np
from traffic_light import MFTrafficLight, RRTrafficLight, RLTrafficLight
from simulator import Simulator
from animator import Animator
from trainer import Trainer

#index 0: inital load | index 1: min increase rate | index 2: max increase rate
traffic_paramaters = np.array([[10,1,3],[15,1,1],[5,2,2],[20,3,3]])
decrease_rate = 5

traffic_light1 = MFTrafficLight()
sim = Simulator(traffic_paramaters, traffic_light1, decrease_rate)

ani = Animator(sim)
ani.run()