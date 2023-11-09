import pandas as pd
import matplotlib.pyplot as plt
from LimpiezaDatos.limpiezaDatos import LimpiezaDatos
from AbstractFactory.abstractFactory import AbstractFactory
from AbstractFactory.concreteFactories import (
                                        ConcreteFactory1, 
                                        ConcreteFactory2, 
                                        ConcreteFactory3, 
                                        ConcreteFactory4, 
                                        ConcreteFactory5, 
                                        ConcreteFactory6)
class Lanzador:
    def lanzar_limpieza(self):
        dataCleaning = LimpiezaDatos('Datasets/activaciones_samur_2023.csv')
        dataCleaning.limpieza_nulos()
        dataCleaning.limpieza_duplicados()
        dataCleaning.limpieza_atipicos()
        dataCleaning.guardar()
    
    def lanzar_abstractFactory(self):
        def client_code(factory: AbstractFactory) -> None:
            graphic = factory.create_graphic()
            statistic = factory.calculate_statistic()

            print(f"{statistic.calculate_statistic()}")
            print(f"{graphic.create_graphic()}")

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

    #Necesitamos la variable diferencia en otro directorio para calcular la media, moda y mediana
    def get_diferencia(self):
        return self.diferencia