from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Optional

from Device import Device


class Robot(ABC):
    def __init__(self, devices: Optional[list[Device]]):
        self.__devices = devices or []

    @property
    def devices(self) -> list[Device]:
        return self.__devices
