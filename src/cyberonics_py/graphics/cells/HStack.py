import uuid

from cyberonics_py.graphics import DeviceCell, Graphic
from cyberonics_py.graphics.GraphicState import GraphicState


class HStack(Graphic):
    def __init__(self, graphics: list[Graphic]):
        self.graphics = {graphic.uuid: graphic for graphic in graphics}
        super().__init__(None)

    def get_state(self):
        graphics = [graphic.get_state().encode() for graphic in self.graphics.values()]
        return GraphicState("HStack", super().uuid, graphics=graphics)

    def set_state(self, state):
        graphics: [GraphicState] = getattr(state, "graphics", None)
        if graphics is None:
            raise ValueError("Invalid state")
        for graphic_state in graphics:
            if graphic_state.uuid not in self.graphics:
                raise ValueError("Invalid state")
            self.graphics[graphic_state.uuid].set_state(graphic_state)
