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
        self.LEARNING_RATE = 0.9
        self.DISCOUNT = 0.95
        self.EPISODES = 25000
        self.DIS_OS_SIZE = [10,10,10,10,4]
        self.q_table = np.random.uniform(low=-1, high=1, size=(self.DIS_OS_SIZE))

    def decide(self, counter:int, cars:np.ndarray) -> int:
        cars = tuple(cars)
        return np.argmax(self.q_table[cars])


class MFTrafficLight(BaseTrafficLight):

    def __init__(self) -> None:   
        super().__init__()
    
    def decide(self, counter: int, cars:np.ndarray) -> int:
        return np.argmax(cars)