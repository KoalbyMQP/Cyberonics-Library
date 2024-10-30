import json
from collections.abc import Callable

from ..Graphic import Graphic
from ..GraphicTyping import Color


class Slider(Graphic):
    def __init__(self, value: float, min_value: float, max_value: float, step: float = 1, color: Color = Color.INFO) -> None:
        self.__value = value
        self.__min_value = min_value
        self.__max_value = max_value
        self.__step = step
        if min_value > max_value or value < min_value or value > max_value:
            raise ValueError("Invalid slider parameters")
        if step <= 0 or step > (max_value - min_value):
            raise ValueError("Invalid step value")
        self.__color = color
        super().__init__()
        self.__notify()

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float) -> None:
        self.__value = value
        self.__notify()

    @property
    def min_value(self) -> float:
        return self.__min_value

    @min_value.setter
    def min_value(self, min_value: float) -> None:
        self.__min_value = min_value
        self.__notify()

    @property
    def max_value(self) -> float:
        return self.__max_value

    @max_value.setter
    def max_value(self, max_value: float) -> None:
        self.__max_value = max_value
        self.__notify()

    @property
    def step(self) -> float:
        return self.__step

    @step.setter
    def step(self, step: float) -> None:
        self.__step = step
        self.__notify()

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, color: Color) -> None:
        self.__color = color
        self.__notify()

    def get_state(self) -> str:
        state = {"graphic": "Slider", "value": self.__value, "min_value": self.__min_value, "max_value": self.__max_value, "step": self.__step, "color": self.__color}
        return json.dumps(state)

    def set_state(self, state: str) -> None:
        state_dict = json.loads(state)
        if "value" in state_dict:
            if state_dict["value"] < self.__min_value or state_dict["value"] > self.__max_value:
                raise ValueError("Value out of bounds")
            self.value = state_dict["value"]
        else:
            raise ValueError("Invalid state data")