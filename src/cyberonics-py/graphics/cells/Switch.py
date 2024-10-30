import json
from collections.abc import Callable

from ..Graphic import Graphic
from ..GraphicTyping import Color


class Switch(Graphic):
    def __init__(self, on: bool, state_changed: Callable[[bool], []], on_color=Color.SUCCESS,
                 off_color=Color.DANGER) -> None:
        self.__on = on
        self.__on_color = on_color
        self.__off_color = off_color
        self.__state_changed = state_changed
        super().__init__()
        self.__notify()

    @property
    def on(self) -> bool:
        return self.__on

    @on.setter
    def on(self, value: bool) -> None:
        self.__on = value
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

    def get_state(self) -> str:
        state = {"graphic": "Switch", "on": self.__on, "on_color": self.__on_color, "off_color": self.__off_color}
        return json.dumps(state)

    def set_state(self, state: str) -> None:
        state_dict = json.loads(state)
        if "on" in state_dict:
            self.on = state_dict["on"]
            self.__state_changed(self.on)
        else:
            raise ValueError("Invalid state data")