from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt



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
        # Crear el diagrama de barras
        plt.bar(range(50), diferencia[:50], color='b', alpha=0.5)
        plt.title('Diagrama de Barras de Diferencias de Tiempo')
        return "Barplot"


class GraficoHistograma(AbstractGraphics):
    def create_graphic(self) -> str:
        # Crear el histograma
        plt.hist([df['Hora Intervención'], df['Hora Solicitud']], bins=25, alpha=0.7)
        # Configuración adicional
        plt.xlabel('Diferencia de Tiempo (segundos)')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de Diferencias de Tiempo')
        plt.show()
        return 'histograma'

class AbstractStatistics(ABC):
    @abstractmethod
    def calculate_statistic(self) -> None:
        pass

    @abstractmethod
    def graphic(self, collaborator: AbstractGraphics) -> None:
        pass


class Mean(AbstractStatistics):
    def calculate_statistic(self) -> str:
        #Devuelve la media en minutos, redondeada a las centesimas
        return round(diferencia.mean().seconds/60, 2)

    def graphic(self, collaborator: AbstractGraphics) -> str:
        grafico = collaborator.create_graphic()
        plt.axhline(y=self.calculate_statistic(), color='r', linestyle='--', label='Mean')
        plt.savefig('Ejercicio1/Graficos/media_{}.png'.format(grafico))


class Mode(AbstractStatistics):
    def calculate_statistic(self) -> str:
        #Devuelve la moda en minutos, redondeada a las centesimas
        return round(diferencia.mode()[0].seconds/60, 2)

    def graphic(self, collaborator: AbstractGraphics) -> str:
        grafico = collaborator.create_graphic()
        plt.axhline(y=self.calculate_statistic(), color='r', linestyle='--', label='Mode')
        plt.savefig('Ejercicio1/Graficos/moda_{}.png'.format(grafico))
    
class Median(AbstractStatistics):
    def calculate_statistic(self) -> str:
        #Devuelve la mediana en minutos, redondeada a las centesimas   
        return round(diferencia.median().seconds/60, 2)

    def graphic(self, collaborator: AbstractGraphics) -> str:
        grafico = collaborator.create_graphic()
        plt.axhline(y=self.calculate_statistic(), color='r', linestyle='--', label='Median')
        plt.savefig('Ejercicio1/Graficos/mediana_{}.png'.format(grafico))


def client_code(factory: AbstractFactory) -> None:
    graphic = factory.create_graphic()
    statistic = factory.calculate_statistic()

    print(f"{statistic.calculate_statistic()}")
    print(f"{graphic.create_graphic()}")

if __name__ == "__main__":
 
    df = pd.read_csv('Ejercicio1/Datasets/filtrado_activaciones_samur_2023.csv', sep=';', encoding='UTF-8')
    df['Hora Intervención'] = pd.to_datetime(df['Hora Intervención'], format='%H:%M:%S')
    df['Hora Solicitud'] = pd.to_datetime(df['Hora Solicitud'], format='%H:%M:%S')
    #Calcula la diferencia entre la hora de solicitud y la hora de intervencion, ya que es lo unico que tiene sentido para una media
    diferencia = df['Hora Intervención'] - df['Hora Solicitud']

    plt.hist([df['Hora Intervención'], df['Hora Solicitud']], bins=25)
    plt.show()



    client_code(ConcreteFactory1())
    print("\n")
    client_code(ConcreteFactory2())        
    print("\n")
    client_code(ConcreteFactory3())    
    print("\n")
    client_code(ConcreteFactory4())    
    print("\n")
    client_code(ConcreteFactory5())    
    print("\n")
    client_code(ConcreteFactory6())   