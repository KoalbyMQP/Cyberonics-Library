from abc import ABC
from typing import Optional
from .Device import Device
from .Target import Target


class Robot(ABC):
    def __init__(self, devices: Optional[list[Device]], targets: Optional[list[Target]] = None):
        self.__devices = devices or []

    @property
    def devices(self) -> list[Device]:
        return self.__devices
