import json

class GraphicState:
    def __init__(self, graphic_type, uuid, **kwargs):
        self.type = graphic_type
        self.uuid = uuid
        self.__dict__.update(kwargs)

    def encode(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def decode(state_str):
        state_dict = json.loads(state_str)
        graphic_type = state_dict.pop('type')
        uuid = state_dict.pop('uuid')
        return GraphicState(graphic_type, uuid, **state_dict)