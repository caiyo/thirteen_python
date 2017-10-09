from enum import Enum


class BaseEnum(Enum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
