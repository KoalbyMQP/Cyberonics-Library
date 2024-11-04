from ..Graphic import Graphic
from ..GraphicState import GraphicState
from ..GraphicTyping import Color
from ... import DeviceProperty


class Switch(Graphic):
    def __init__(self, managed_property: DeviceProperty[bool], on_color=Color.SUCCESS, off_color=Color.DANGER) -> None:
        if not managed_property.mutable:
            raise ValueError("Managed property must be mutable")

        self.managed_property = managed_property
        self.__on_color = on_color
        self.__off_color = off_color
        super().__init__(managed_property)
        self.__notify()

    @property
    def on(self) -> bool:
        return self.managed_property.value

    @on.setter
    def on(self, value: bool) -> None:
        self.managed_property.value = value
        self.__notify()

    @property
    def on_color(self) -> Color:
        return self.__on_color

    @on_color.setter
    def on_color(self, value: Color) -> None:
        self.__on_color = value
        self.__notify()

    @property
    def off_color(self) -> Color:
        return self.__off_color

    @off_color.setter
    def off_color(self, value: Color) -> None:
        self.__off_color = value
        self.__notify()

    def get_state(self) -> GraphicState:
        return GraphicState("Switch", super().uuid, on=self.on, on_color=self.on_color, off_color=self.off_color)

    def set_state(self, state: GraphicState) -> None:
        on: bool = getattr(state, "on", None)
        if on is None:
            raise ValueError("Invalid state data. Missing key 'on'")
        if not isinstance(on, bool):
            raise ValueError("Invalid state data. 'on' must be a boolean")
        self.managed_property.value = on
        self.__notify()