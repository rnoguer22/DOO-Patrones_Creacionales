import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout,QComboBox, QPushButton, QMessageBox

class PizzeriaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.ingredientes_disponibles = ["Tomate", "Queso", "Pepperoni", "Champiñones", "Jamón", "Aceitunas", "Cebolla"]
        self.ingredientes_seleccionados = []

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        label = QLabel("Selecciona tus ingredientes:")
        layout.addWidget(label)

        # Lista desplegable para seleccionar ingredientes
        combo_box = QComboBox(self)
        combo_box.addItems(self.ingredientes_disponibles)
        layout.addWidget(combo_box)

        # Botón para agregar ingredientes
        agregar_button = QPushButton("Agregar Ingrediente", self)
        agregar_button.clicked.connect(lambda: self.agregar_ingrediente(combo_box.currentText()))
        layout.addWidget(agregar_button)

        # Botón para mostrar la orden
        orden_button = QPushButton("Ver Orden", self)
        orden_button.clicked.connect(self.mostrar_orden)
        layout.addWidget(orden_button)

        self.setLayout(layout)
        self.setWindowTitle("Pizzería App")
        self.show()

    def agregar_ingrediente(self, ingrediente):
        if ingrediente not in self.ingredientes_seleccionados:
            self.ingredientes_seleccionados.append(ingrediente)

    def mostrar_orden(self):
        if not self.ingredientes_seleccionados:
            QMessageBox.warning(self, "Advertencia", "Selecciona al menos un ingrediente.")
        else:
            orden = ", ".join(self.ingredientes_seleccionados)
            QMessageBox.information(self, "Tu Orden", f"Tu orden es: {orden}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = PizzeriaApp()
    sys.exit(app.exec_())