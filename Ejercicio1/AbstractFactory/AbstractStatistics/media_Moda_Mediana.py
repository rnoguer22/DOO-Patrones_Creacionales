from AbstractFactory.AbstractStatistics.abstractStatistics import AbstractStatistics
from AbstractFactory.AbstractGraphics.abstractGraphics import AbstractGraphics
from LimpiezaDatos.limpiezaDatos import LimpiezaDatos
import matplotlib.pyplot as plt

limpieza = LimpiezaDatos('Ejercicio1/Datasets/activaciones_samur_2023.csv')
diferencia = limpieza.calcular_diferencia()

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