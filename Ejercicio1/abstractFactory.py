from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def create_graphic(self) -> AbstractGraphics:
        pass

    @abstractmethod
    def calculate_statistic(self) -> AbstractStatistics:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_graphic(self) -> AbstractGraphics:
        return GraficoBarras()

    def calculate_statistic(self) -> AbstractStatistics:
        return Mean()


class ConcreteFactory2(AbstractFactory):
    def create_graphic(self) -> AbstractGraphics:
        return GraficoBarras()

    def calculate_statistic(self) -> AbstractStatistics:
        return Mode()
    
class ConcreteFactory3(AbstractFactory):
    def create_graphic(self) -> AbstractGraphics:
        return GraficoBarras()

    def calculate_statistic(self) -> AbstractStatistics:
        return Median()
    
class ConcreteFactory4(AbstractFactory):
    def create_graphic(self) -> AbstractGraphics:
        return GraficoHistograma()

    def calculate_statistic(self) -> AbstractStatistics:
        return Mean()
    
class ConcreteFactory5(AbstractFactory):
    def create_graphic(self) -> AbstractGraphics:
        return GraficoHistograma()

    def calculate_statistic(self) -> AbstractStatistics:
        return Mode()
    
class ConcreteFactory6(AbstractFactory):
    def create_graphic(self) -> AbstractGraphics:
        return GraficoHistograma()

    def calculate_statistic(self) -> AbstractStatistics:
        return Median()


class AbstractGraphics(ABC):
    @abstractmethod
    def create_graphic(self) -> str:
        pass


class GraficoBarras(AbstractGraphics):
    def create_graphic(self) -> str:
        return "Devolveria un grafico de barras"


class GraficoHistograma(AbstractGraphics):
    def create_graphic(self) -> str:
        return "Devolveria un histograma"


class AbstractStatistics(ABC):
    @abstractmethod
    def calculate_statistic(self) -> None:
        pass

    @abstractmethod
    def graphic(self, collaborator: AbstractGraphics) -> None:
        pass


class Mean(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return "Devolveria la media"

    def graphic(self, collaborator: AbstractGraphics) -> str:
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la media"


class Mode(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return "Calcularia la moda"

    def graphic(self, collaborator: AbstractGraphics) -> str:
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la moda"
    
class Median(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return "Calcularia la mediana"

    def graphic(self, collaborator: AbstractGraphics) -> str:
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la mediana"


def client_code(factory: AbstractFactory) -> None:
    graphic = factory.create_graphic()
    statistic = factory.calculate_statistic()

    print(f"{statistic.graphic(graphic)}")
    print(f"{statistic.calculate_statistic()}")
    print(f"{graphic.create_graphic()}")

if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory6())
    print("\n")
    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory5())    