import pandas as pd

class LecturaDatos:
    def __init__(self, csv):
        self.csv = csv
    
    #Lee el csv y lo devuelve como un dataframe
    def read_csv(self):
        data = pd.read_csv(self.csv, sep=';', encoding='UTF-8')
        return data
    
class LimpiezaDatos(LecturaDatos):
    def __init__(self, csv):
        super().__init__(csv)
        self.df = self.read_csv()

    #Copia el dataframe para no modificar el original
    def copia(self):
        self.df = self.df.copy()
        self.df.to_csv('Ejercicio1/Datasets/copy_activaciones_samur_2023.csv', sep=';', index=False)

    def limpieza_nulos(self):
        for column in self.df.columns:
            nan_values = self.df[column].isna().sum()
            if nan_values > 0: #Identificamos las columnas con valores nulos
                print(f'Columna {column} tiene {nan_values} valores nulos')
                #Si son < 10000, eliminamos las filas con valores nulos, ya que vamos a considerar que son pocos datos
                if nan_values < 10000:
                    self.df.dropna(subset=[column], inplace=True)
                else: #Si son > 10000, rellenamos los valores nulos con la media o 'Desconocido'
                    data_type = self.df[column].dtype
                    if data_type == 'int64' or data_type == 'float64':
                        #Si es de tipo numerico, rellenamos los valores nulos con la media de la columna
                        self.df[column].fillna(self.df[column].mean(), inplace=True)
                    else:
                        #Si es de tipo string, rellenamos los valores nulos con 'Desconocido'
                        self.df[column].fillna('Desconocido', inplace=True)
        return self.df
    
    #Eliminamos las filas duplicadas (aunque en este caso no hay)
    def limpieza_duplicados(self):
        self.df.drop_duplicates(inplace=True)
        return self.df
    
    #Esta funcion no tiene sentido, ya que la unica columna con valores numericos es la de 'Año'
    def limpieza_atipicos(self):
        pass
    
    #Guarda el dataframe en un csv
    def guardar(self):
        self.df.to_csv('Ejercicio1/Datasets/filtrado_activaciones_samur_2023.csv', sep=';', index=False)