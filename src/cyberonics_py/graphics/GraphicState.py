import json
from uuid import UUID, uuid4



class GraphicState:
    def __init__(self, graphic_type: str, uuid: uuid4, **kwargs):
        self.type = graphic_type
        self.uuid = uuid
        self.__dict__.update(kwargs)

    def encode(self):
        state_dict = self.__dict__.copy()
        state_dict['uuid'] = str(self.uuid)
        return json.dumps(state_dict)

    @staticmethod
    def decode(state_str) -> 'GraphicState':
        state_dict = json.loads(state_str)
        graphic_type = state_dict.pop('type')
        uuid_obj = UUID(state_dict.pop('uuid'))
        return GraphicState(graphic_type, uuid_obj, **state_dict)