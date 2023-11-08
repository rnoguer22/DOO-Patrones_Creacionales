import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout,QComboBox, QPushButton, QMessageBox, QTextEdit

class PizzeriaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.masas_disponibles = ["Fina", "Gruesa", "Rellena", "Calzone", "Siciliana", "Integral", "Sin gluten"]
        self.salsas_disponibles = ["Tomate", "Pesto", "Barbacoa", "Picante", "De ajo", "de queso", "Sin salsa"]
        self.ingredientes_disponibles = ["Tomate", "Queso", "Pepperoni", "Champiñones", "Jamón", "Aceitunas", "Cebolla"]

        self.seleccion = []

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        label = QLabel("Selecciona tus ingredientes:")
        layout.addWidget(label)

        # Lista desplegable para seleccinar la masa
        box_masa = QComboBox(self)
        box_masa.addItems(self.masas_disponibles)
        layout.addWidget(box_masa)        
        
        # Lista desplegable para seleccinar la salsa
        box_salsa = QComboBox(self)
        box_salsa.addItems(self.salsas_disponibles)
        layout.addWidget(box_salsa)

        # Lista desplegable para seleccionar la masa, salsa e ingredientes
        box_ingredientes = QComboBox(self)
        box_ingredientes.addItems(self.ingredientes_disponibles)
        layout.addWidget(box_ingredientes)

        # Botón para agregar ingredientes
        agregar_button = QPushButton("Agregar", self)
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente('Masa {}'.format(box_masa.currentText())))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente('Salsa {}'.format(box_salsa.currentText())))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(box_ingredientes.currentText()))
        layout.addWidget(agregar_button)

        # Botón para mostrar la orden
        orden_button = QPushButton("Ver Orden", self)
        orden_button.clicked.connect(self.mostrar_orden)
        layout.addWidget(orden_button)

        # Área de texto para mostrar la orden
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setMinimumSize(400, 300) #Hacemos que el area de texto sea un poco mas grande
        layout.addWidget(self.text_area)

        self.setLayout(layout)
        self.setWindowTitle("Pizzería App")
        self.show()

    def agregar_ingrediente(self, ingrediente):
        if ingrediente not in self.seleccion:
            self.seleccion.append(ingrediente)

    def mostrar_orden(self):
        if not self.seleccion:
            QMessageBox.warning(self, "Advertencia", "Selecciona al menos un ingrediente.")
        else:
            orden = ", ".join(self.seleccion)
            self.text_area.append(f"Tu orden es: {orden}")

            #Guardar en un archivo CSV
            self.guardar_en_csv(orden)

    def guardar_en_csv(self, orden):
        with open('Ejercicio2/GUI/orden.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([orden])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = PizzeriaApp()
    sys.exit(app.exec_())