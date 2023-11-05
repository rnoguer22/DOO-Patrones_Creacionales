import pandas as pd

class LecturaDatos:
    def __init__(self, csv):
        self.csv = csv
    
    def read_csv(self):
        data = pd.read_csv(self.csv, sep=';', encoding='UTF-8')
        return data
    
class LimpiezaDatos(LecturaDatos):
    def __init__(self, csv):
        super().__init__(csv)
        self.df = self.read_csv()

    def copia(self):
        self.df = self.df.copy()
        self.df.to_csv('Samur/copy_activaciones_samur_2023.csv', sep=';', index=False)

    def limpieza_nulos(self):
        for column in self.df.columns:
            nan_values = self.df[column].isna().sum()
            if nan_values > 0:
                print(f'Columna {column} tiene {nan_values} valores nulos')
                if nan_values < 10000:
                    self.df.dropna(subset=[column], inplace=True)
                else:
                    data_type = self.df[column].dtype
                    print(f'Columna {column} es de tipo {data_type}')
                    if data_type == 'int64' or data_type == 'float64':
                        self.df[column].fillna(self.df[column].mean(), inplace=True)
                    else:
                        self.df[column].fillna('Desconocido', inplace=True)
        return self.df
    
    def limpieza_duplicados(self):
        self.df.drop_duplicates(inplace=True)
        return self.df
    
    def guardar(self):
        self.df.to_csv('Samur/filtrado_activaciones_samur_2023.csv', sep=';', index=False)
    


dataCleaning = LimpiezaDatos('Samur/activaciones_samur_2023.csv')
dataCleaning.copia()
dataCleaning.limpieza()