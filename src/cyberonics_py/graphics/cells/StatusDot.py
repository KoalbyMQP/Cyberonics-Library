from ..Graphic import Graphic
from ..GraphicState import GraphicState
from ..GraphicTyping import Color


class StatusDot(Graphic):
    def __init__(self, color: Color) -> None:
        self.__color = color
        self.__flash = False
        super().__init__(None)
        super()._notify()

    def flash(self):
        self.__flash = True
        super()._notify()
        self.__flash = False

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, value: Color) -> None:
        self.__color = value
        super()._notify()


    def get_state(self) -> GraphicState:
        return GraphicState("StatusDot", super().uuid, color=self.__color, flash=self.__flash)

    def set_state(self, state: GraphicState) -> None:
        raise ValueError("StatusDot cannot by set by the client")