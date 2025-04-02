from abc import ABC, abstractmethod
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from .Robot import Robot


class Target(ABC):

    def __init__(self, name: str, robot: 'Robot', shutdown_timeout: float = 0.5):
        self._name = name
        self.robot = robot
        self.shutdown_timeout = shutdown_timeout

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    async def run(self):
        pass

    @abstractmethod
    async def shutdown(self, beat: Callable[[], None]):
        pass