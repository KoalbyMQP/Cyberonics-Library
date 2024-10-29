from abc import ABC, abstractmethod
from graphics.DeviceCell import DeviceCell
from DeviceProperty import DeviceProperty

class Device(ABC):
    def __init__(self, properties: [DeviceProperty], device_cell: DeviceCell):
        super().__init__()
        self.properties = properties
        self.device_cell = device_cell

    def get_state(self):
        return self.device_cell.graphics
