# Traffic Light Simulator
This is a reinforcement learning project that simulates traffic lights in an intersection. The goal of the project is to optimize the timing of traffic lights to reduce congestion and improve traffic flow using reinforcement learning techniques and comparing it to other, more conventional methods.


## Methods
3 traffic light controlling algorithms have been implemented, These are:
- Reinforcement Learning: Q learning algorithim
- Round Robin: circulates the light in a counter clockwise rotation
- Greedy Algorithm: always services the direction with the highest load


# Usage
1- Clone repository
```
git clone https://github.com/Procedurally-Generated-Human/Reinforcement-Learning-Traffic-Light.git
```
2- Install requirements 
```
pip install -r requirements.txt
```
3- Creating and running a simulation
```
import numpy as np
from traffic_light import MFTrafficLight, RRTrafficLight, RLTrafficLight
from simulator import Simulator
from animator import Animator
from trainer import Trainer


#index 0: inital load | index 1: min increase rate | index 2: max increase rate
traffic_paramaters = np.array([[10,1,3],[15,1,1],[5,2,2],[20,3,3]])
decrease_rate = 5

traffic_light1 = RRTrafficLight(round_length=4)
sim = Simulator(traffic_paramaters, traffic_light1, decrease_rate)
sim.run(100)
```

4- Animating simulation
```

#index 0: inital load | index 1: min increase rate | index 2: max increase rate
traffic_paramaters = np.array([[10,1,3],[15,1,1],[5,2,2],[20,3,3]])
decrease_rate = 5

traffic_light1 = RRTrafficLight(round_length=4)
sim = Simulator(traffic_paramaters, traffic_light1, decrease_rate)

ani = Animator(sim)
ani.run()
```