from abc import ABC, abstractmethod
from collections.abc import Callable
from Device import Device


class Robot(ABC):
    def __init__(self, devices: list[Device]):
        self.devices = devices
