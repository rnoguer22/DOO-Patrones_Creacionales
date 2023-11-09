import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,QComboBox, QPushButton, QMessageBox, QTextEdit

class PizzeriaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.masas_disponibles = ["Fina", "Gruesa", "Rellena", "Calzone", "Siciliana", "Integral", "Sin gluten"]
        self.salsas_disponibles = ["Pesto", "Tomate", "Barbacoa", "Picante", "De ajo", "de queso", "Sin salsa"]
        self.quesos_disponibles = ["Mozarella", "Parmesano", "Cheddar", "Provolone", "Sin queso"]
        self.ingredientes_disponibles = ["Pepperoni", "Champiñones", "Jamon", "Aceitunas", "Cebolla", "Tomate natural"]
        self.cocciones_disponibles = ["Horno", "Parrilla", "Frito", "Cocido", "Crudo"]
        self.presentaciones_disponibles = ["Caja de cartón", "Gourmet"]
        self.maridajes_disponibles = ["Cerveza", "Vino", "Refresco", "Agua", "Jugo", "Ninguno"]

        self.seleccion = []

        self.init_gui()

    def init_gui(self):
        layout_vertical = QVBoxLayout()
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_horizontal3 = QHBoxLayout()

        label = QLabel("Selecciona tus ingredientes:")
        layout_horizontal1.addWidget(label)

        # Lista desplegable para seleccinar la masa
        box_masa = QComboBox(self)
        box_masa.addItems(self.masas_disponibles)
        layout_horizontal2.addWidget(box_masa)        
        
        # Lista desplegable para seleccinar la salsa
        box_salsa = QComboBox(self)
        box_salsa.addItems(self.salsas_disponibles)
        layout_horizontal2.addWidget(box_salsa)

        # Lista desplegable para seleccinar el queso
        box_queso = QComboBox(self)
        box_queso.addItems(self.quesos_disponibles)
        layout_horizontal2.addWidget(box_queso)

        # 3 Listas despegables para mostrar los ingredientes1, 2 y 3
        box_ingrediente1 = QComboBox(self)
        box_ingrediente1.addItems(self.ingredientes_disponibles)
        layout_horizontal2.addWidget(box_ingrediente1)

        box_ingrediente2 = QComboBox(self)
        box_ingrediente2.addItems(self.ingredientes_disponibles)
        layout_horizontal2.addWidget(box_ingrediente2)        
        
        box_ingrediente3 = QComboBox(self)
        box_ingrediente3.addItems(self.ingredientes_disponibles)
        layout_horizontal2.addWidget(box_ingrediente3)

        #Lista para agregar la coccion
        box_coccion = QComboBox(self)
        box_coccion.addItems(self.cocciones_disponibles)
        layout_horizontal2.addWidget(box_coccion)

        #Lista para agregar la presentacion
        box_presentacion = QComboBox(self)
        box_presentacion.addItems(self.presentaciones_disponibles)
        layout_horizontal2.addWidget(box_presentacion)

        #Lista para agregar el maridaje
        box_maridaje = QComboBox(self)
        box_maridaje.addItems(self.maridajes_disponibles)
        layout_horizontal2.addWidget(box_maridaje)

        # Botón para agregar ingredientes
        agregar_button = QPushButton("Agregar", self)
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente('Masa {}'.format(box_masa.currentText())))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente('Salsa {}'.format(box_salsa.currentText())))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente('Queso {}'.format(box_queso.currentText())))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(box_ingrediente1.currentText()))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(box_ingrediente2.currentText()))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(box_ingrediente3.currentText()))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(box_coccion.currentText()))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(box_presentacion.currentText()))
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(box_maridaje.currentText()))
        layout_horizontal2.addWidget(agregar_button)

        # Botón para mostrar la orden
        orden_button = QPushButton("Ver Orden", self)
        orden_button.clicked.connect(self.mostrar_orden)
        layout_horizontal3.addWidget(orden_button)

        # Área de texto para mostrar la orden
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setMinimumSize(400, 300) #Hacemos que el area de texto sea un poco mas grande
        layout_horizontal3.addWidget(self.text_area)

        layout_vertical.addLayout(layout_horizontal1)
        layout_vertical.addLayout(layout_horizontal2)
        layout_vertical.addLayout(layout_horizontal3)

        self.setLayout(layout_vertical)
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
            self.guardar_en_csv()

    def guardar_en_csv(self):
        with open('Ejercicio2/GUI/orden.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.seleccion)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = PizzeriaApp()
    sys.exit(app.exec_())