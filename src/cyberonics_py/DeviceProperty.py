from typing import TypeVar, Generic, Callable, Optional

T = TypeVar('T')
class DeviceProperty(Generic[T]):
    def __init__(self, value: T, set_value: Optional[Callable[[T], None]] = None):
        self.__value = value
        self.mutable = set_value is None
        self.__setter = set_value
        self.type = type(value)

    @property
    def value(self) -> T:
        return self.__value

    @value.setter
    def value(self, new_value: T | str) -> None:
        if not self.mutable:
            raise AttributeError("This property is read-only.")

        if isinstance(new_value, str):
            try:
                new_value = self.type(new_value)
            except ValueError:
                raise ValueError(f"Cannot convert '{new_value}' to {self.type.__name__}")
        else:
            self.__value = new_value
        self.__setter(new_value)