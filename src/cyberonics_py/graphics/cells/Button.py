import json
from collections.abc import Callable

from ..Graphic import Graphic
from ..GraphicTyping import Color


class Button(Graphic):
    def __init__(self, text: str, onclick: Callable, text_color: Color = Color.PRIMARY, background_color: Color = Color.BACKGROUND) -> None:
        self.__text = text
        self.__on_click = onclick
        self.__text_color = text_color
        self.__background_color = background_color
        super().__init__()
        self.__notify()

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value: str) -> None:
        self.__text = value
        self.__notify()

    @property
    def text_color(self) -> Color:
        return self.__text_color

    @text_color.setter
    def text_color(self, value: Color) -> None:
        self.__text_color = value
        self.__notify()

    @property
    def background_color(self) -> Color:
        return self.__background_color

    @background_color.setter
    def background_color(self, value: Color) -> None:
        self.__background_color = value
        self.__notify()

    def get_state(self) -> str:
        state = {"graphic": "Button", "text": self.text, "text_color": self.text_color, "background_color": self.background_color}
        return json.dumps(state)

    def set_state(self, state: str) -> None:
        state_dict = json.loads(state)
        if "pressed" in state_dict:
            if state_dict["pressed"]:
                self.__on_click()
        else:
            raise ValueError("Invalid state data")