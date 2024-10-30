import json

from ..Graphic import Graphic
from ..GraphicTyping import Color


class StatusDot(Graphic):
    def __init__(self, color: Color) -> None:
        self.__color = color
        self.__flash = False
        super().__init__()
        self.__notify()

    def flash(self):
        self.__flash = True
        self.__notify()

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, value: Color) -> None:
        self.__color = value
        self.__notify()


    def get_state(self) -> str:
        state = {"graphic": "StatusDot", "color": self.__color, "flash": self.__flash}
        self.__flash = False
        return json.dumps(state)

    def set_state(self, state: str) -> None:
        pass