from abc import ABC, abstractmethod
from graphics.DeviceCell import DeviceCell
from DeviceProperty import DeviceProperty
from typing import Optional, Dict, Any


class Device(ABC):
    def __init__(self, properties: [DeviceProperty], device_cell: Optional[DeviceCell] = None):
        super().__init__()
        self.properties = properties
        if device_cell is None:
            self.device_cell = DeviceCell([])
        self.device_cell = device_cell

    def get_state(self) -> Dict[str, Any]:
        states = [graphic.get_state() for graphic in self.device_cell.graphics]
        return {state.uuid: state.encode() for state in states}

