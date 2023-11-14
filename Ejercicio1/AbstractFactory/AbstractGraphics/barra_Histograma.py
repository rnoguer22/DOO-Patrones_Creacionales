from AbstractFactory.AbstractGraphics.abstractGraphics import AbstractGraphics
from LimpiezaDatos.limpiezaDatos import LimpiezaDatos
import matplotlib.pyplot as plt

limpieza = LimpiezaDatos('Ejercicio1/Datasets/activaciones_samur_2023.csv')
diferencia = limpieza.calcular_diferencia()

class GraficoBarras(AbstractGraphics):
    def create_graphic(self) -> str:
        # Crear el diagrama de barras
        plt.bar(range(50), diferencia[:50], color='b', alpha=0.5)
        plt.title('Diagrama de Barras de Diferencias de Tiempo')
        return "Barplot"


class GraficoHistograma(AbstractGraphics):
    def create_graphic(self) -> str:
        # Crear el histograma
        plt.hist([limpieza.df['Hora Intervención'], limpieza.df['Hora Solicitud']], bins=25, alpha=0.7)
        # Configuración adicional
        plt.xlabel('Diferencia de Tiempo (segundos)')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de Diferencias de Tiempo')
        return 'histograma'