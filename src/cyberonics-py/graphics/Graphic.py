from abc import ABC, abstractmethod

class Graphic(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_state(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def set_state(self, state: str) -> None:
        raise NotImplementedError("Subclasses must implement this method")