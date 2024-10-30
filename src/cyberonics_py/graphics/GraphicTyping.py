from enum import Enum

class TextAlignment(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

class Color(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    LIGHT = "light"
    BACKGROUND = "background"
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning"
    INFO = "info"