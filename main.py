import numpy as np
from traffic_light import MFTrafficLight, RRTrafficLight, RLTrafficLight
from simulator import Simulator
from animator import Animator
from trainer import Trainer

traffic_paramaters = np.array([[10,1,3],[15,1,1],[5,2,2],[20,3,3]])
decrease_rate = np.array([1,5,0,2])

tf = RRTrafficLight(4)
sim = Simulator(traffic_paramaters, tf, decrease_rate)

ani = Animator(sim)

ani.run()