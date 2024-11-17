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
    def decode(state: dict[str, any]) -> 'GraphicState':
        graphic_type = state.pop('type')
        uuid_obj = UUID(state.pop('uuid'))
        return GraphicState(graphic_type, uuid_obj, **state)

    def __eq__(self, other):
        print("comparing")
        print(self.__dict__)
        print(other.__dict__)
        return self.__dict__ == other.__dict__