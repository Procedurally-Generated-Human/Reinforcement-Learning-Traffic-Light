import numpy as np
import torch.nn as nn


class BaseTrafficLight:

    def __init__(self) -> None:
        pass

    def decide(self, counter:int, cars:np.ndarray) -> int:
        return 3
    


class RRTrafficLight(BaseTrafficLight):

    def __init__(self, round_length) -> None:
        self.round_length = round_length

    def decide(self, counter:int, cars:np.ndarray) -> int:
        return (counter//self.round_length) % 4


class RLTrafficLight(BaseTrafficLight):

    def __init__(self) -> None:
        super().__init__()
    
    def setup_network(self):
        self.network = nn.Sequential(
            nn.Linear(4, 12),
            nn.ReLU(),
            nn.Linear(12, 4),
            nn.ReLU(),
            nn.Linear(4, 1),
            nn.Sigmoid())
