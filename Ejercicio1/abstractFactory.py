from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd



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
        #Calcula la diferencia entre la hora de solicitud y la hora de intervencion, ya que es lo unico que tiene sentido para una media
        diferencia = df['Hora Intervención'] - df['Hora Solicitud']
        #Devuelve la media en minutos, redondeada a las centesimas
        return round(diferencia.mean().seconds/60, 2)

    def graphic(self, collaborator: AbstractGraphics) -> str:
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la media"


class Mode(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return df.mode()

    def graphic(self, collaborator: AbstractGraphics) -> str:
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la moda"
    
class Median(AbstractStatistics):
    def calculate_statistic(self) -> str:
        return df.median()

    def graphic(self, collaborator: AbstractGraphics) -> str:
        result = collaborator.create_graphic()
        return "Devolveria un grafico de la mediana"


def client_code(factory: AbstractFactory) -> None:
    graphic = factory.create_graphic()
    statistic = factory.calculate_statistic()

    print(f"{statistic.calculate_statistic()}")
    print(f"{statistic.graphic(graphic)}")
    print(f"{graphic.create_graphic()}")

if __name__ == "__main__":
 
    df = pd.read_csv('Ejercicio1/Datasets/filtrado_activaciones_samur_2023.csv', sep=';', encoding='UTF-8')
    df['Hora Intervención'] = pd.to_datetime(df['Hora Intervención'], format='%H:%M:%S')
    df['Hora Solicitud'] = pd.to_datetime(df['Hora Solicitud'], format='%H:%M:%S')


    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())
    print("\n")
    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory5())    