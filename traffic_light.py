import numpy as np



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
