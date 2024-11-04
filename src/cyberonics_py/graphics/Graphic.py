from abc import ABC, abstractmethod
from typing import Any, Optional

import uuid

from cyberonics_py import DeviceProperty
from cyberonics_py.graphics.GraphicState import GraphicState


class Graphic(ABC):
    def __init__(self, managed_property: Optional[DeviceProperty[Any]]):
        self.managed_property = managed_property
        self.__uuid = uuid.uuid4()
        super().__init__()


    @property
    def uuid(self) -> uuid.UUID:
        return self.__uuid


    # Called when the state of the graphic changes
    def __notify(self) -> None:
        pass

    @abstractmethod
    def get_state(self) -> GraphicState:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def set_state(self, state: GraphicState) -> None:
        raise NotImplementedError("Subclasses must implement this method")