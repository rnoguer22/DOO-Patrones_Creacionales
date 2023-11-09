from abc import ABC, abstractmethod
from AbstractFactory.AbstractGraphics.abstractGraphics import AbstractGraphics


class AbstractStatistics(ABC):
    @abstractmethod
    def calculate_statistic(self) -> None:
        pass

    @abstractmethod
    def graphic(self, collaborator: AbstractGraphics) -> None:
        pass