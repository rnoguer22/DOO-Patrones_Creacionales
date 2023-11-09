from abc import ABC, abstractmethod

class AbstractGraphics(ABC):
    @abstractmethod
    def create_graphic(self) -> str:
        pass