from abc import ABC
from typing import Optional
from .Device import Device
from .Target import Target


class Robot(ABC):
    def __init__(self, devices: Optional[list[Device]], targets: Optional[list[Target]] = None):
        self.__devices = devices or []
        self.__targets = {t.name: t for t in targets or []}

    @property
    def devices(self) -> list[Device]:
        return self.__devices

    @property
    def targets(self) -> list[Target]:
        return self.__targets.values()

    def run_target(self, withName: str):
        target = self.__targets.get(withName)
        if not target:
            raise Exception(f"Target {withName} not found")
        target.run()