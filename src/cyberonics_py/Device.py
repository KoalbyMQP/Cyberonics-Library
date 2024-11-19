import json
from abc import ABC
from .graphics.GraphicCell import GraphicCell
from .DeviceProperty import DeviceProperty
from typing import Optional, Callable
from uuid import uuid5, NAMESPACE_DNS

from .graphics.GraphicState import GraphicState


class Device(ABC):
    def __init__(self, identifier, properties: [DeviceProperty], graphic_cell: Optional[GraphicCell] = None):
        super().__init__()
        self.__properties = properties
        for p in properties:
            p.add_listener(self.__property_updated)
        if graphic_cell is None:
            self.device_cell = GraphicCell([])
        self.device_cell = graphic_cell
        self.__listeners = []
        self.__uuid = uuid5(NAMESPACE_DNS, identifier)

    @property
    def uuid(self) -> uuid5:
        return self.__uuid

    def get_state(self) -> dict[str, any]:
        states = [graphic.get_state() for graphic in self.device_cell.graphics]
        return {str(state.uuid): state.encode() for state in states}

    def set_state(self, state: dict[str, any] or str) -> None:
        if type(state) == str:
            state: dict[str, any] = json.loads(state)
        for graphic in self.device_cell.graphics:
            try:
                graphic_state = GraphicState.decode(state[str(graphic.uuid)])
                graphic.set_state(graphic_state)
            except KeyError:
                print(state)
                print("graphics: ", [g.uuid for g in self.device_cell.graphics])
                print("state: ", [k for k in state.keys()])
                raise ValueError("Invalid state")

    """
    Adds a listener and returns its ID. This id can be passed to `free_listener` to remove the listener.
    """
    def add_listener(self, listener: Callable[['Device'], None]) -> int:
        self.__listeners.append(listener)
        return len(self.__listeners)

    """
    Removes a listener by its ID.
    """
    def free_listener(self, listener_id: int) -> None:
        if len(self.__listeners) < listener_id or listener_id < 1:
            raise ValueError("Invalid listener ID")
        self.__listeners.pop(listener_id - 1)

    def __property_updated(self, _):
        for listener in self.__listeners:
            listener(self)