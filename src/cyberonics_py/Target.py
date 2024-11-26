from abc import ABC, abstractmethod
from .Robot import Robot


class Target(ABC):

    def __init__(self, robot: Robot):
        self.robot = robot

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def shutdown(self, beat: ):