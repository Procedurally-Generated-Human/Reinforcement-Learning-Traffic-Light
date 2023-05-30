import numpy as np
from traffic_light import MFTrafficLight, RRTrafficLight, RLTrafficLight
from simulator import Simulator
from animator import Animator
from trainer import Trainer

traffic_paramaters = np.array([[2,1,1],[1,1,1],[0,1,1],[3,1,1]])

tf = RLTrafficLight()
sim = Simulator(traffic_paramaters, tf, 5)
trainer = Trainer(sim)
trainer.run()

traffic_paramaters2 = np.array([[2,1,1],[1,1,1],[0,1,1],[3,1,1]])
sim2 = Simulator(traffic_paramaters2, tf)
sim2.run(10000)
print(sim2.counter)

traffic_paramaters3 = np.array([[2,1,1],[1,1,1],[0,1,1],[3,1,1]])
sim3 = Simulator(traffic_paramaters3, tf, 5)
ani = Animator(sim3)
ani.run()

