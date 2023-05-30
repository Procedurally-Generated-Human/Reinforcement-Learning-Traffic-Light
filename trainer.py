import copy

import numpy as np
from traffic_light import RLTrafficLight
from simulator import Simulator

class Trainer():

    def __init__(self, simulator) -> None:
        self.sim = simulator
        self.dd = copy.deepcopy(self.sim.traffic_paramaters)
        self.episodes = 50000

    def reset(self):
        self.temp = copy.deepcopy(self.dd)
        self.sim = Simulator(self.temp, self.sim.traffic_light, self.sim.decrease_rate)

    def run(self):
        epsilon = 0.8
        start_epsilon = 1
        end_epsilon = self.episodes // 2
        epsilon_decay = epsilon / (end_epsilon - start_epsilon)

        for episode in range(self.episodes):
            ss = 0
            done = False
            state = tuple(self.sim.cars)
            while not done and ss<1000:
                
                if np.random.random() > epsilon:
                    action = self.sim.traffic_light.decide(self.sim.counter, self.sim.cars)
                else:
                    action = np.random.randint(0, 4)
                new_state, reward, done = self.step()
                ss += reward
                if not done:
                    max_future_q = np.max(self.sim.traffic_light.q_table[new_state])
                    current_q = self.sim.traffic_light.q_table[new_state + (action, )]
                    new_q = (1 - self.sim.traffic_light.LEARNING_RATE) * current_q + self.sim.traffic_light.LEARNING_RATE * (reward + self.sim.traffic_light.DISCOUNT * max_future_q)
                    self.sim.traffic_light.q_table[state+(action, )] = new_q
                state = new_state
            self.reset()
            if end_epsilon >= episode >= start_epsilon:
                epsilon -= epsilon_decay
            print(ss)


    def step(self):
        self.sim.update()
        if np.any(self.sim.cars>=10):
            done = True
            reward = -1000
        else:
            done = False
            reward = self.sim.cars.sum()
        
        return tuple(self.sim.cars), reward, done
    
