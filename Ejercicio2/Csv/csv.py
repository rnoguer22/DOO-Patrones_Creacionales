import csv

class Csv:
    def __init__(self, path):
        self.path = path
    
    def guardar_en_csv(self, datos):
        with open(self.path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(datos)