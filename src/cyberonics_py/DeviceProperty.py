from typing import TypeVar, Generic, Callable, Optional

T = TypeVar('T')
class DeviceProperty(Generic[T]):
    def __init__(self, value: T, set_value: Optional[Callable[[T], None]] = None):
        self.value = value
        self.mutable = set_value is None
        self.__setter = set_value
        self.type = type(value)

    def get_value(self) -> T:
        return self.value

    def set_value(self, new_value: T | str) -> None:
        self.value = new_value
        if isinstance(new_value, str):
            try:
                new_value = self.type(new_value)
            except ValueError:
                raise ValueError(f"Cannot convert '{new_value}' to {self.type.__name__}")
        self.__setter(new_value)