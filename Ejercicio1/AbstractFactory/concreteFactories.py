from AbstractFactory.abstractFactory import AbstractFactory
from AbstractFactory.AbstractGraphics.abstractGraphics import AbstractGraphics
from AbstractFactory.AbstractStatistics.abstractStatistics import AbstractStatistics
from AbstractFactory.AbstractGraphics.barra_Histograma import GraficoBarras, GraficoHistograma
from AbstractFactory.AbstractStatistics.media_Moda_Mediana import Mean, Mode, Median



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
