from PySide6.QtWidgets import QApplication, QLabel, QWidget 

class Ventana(QWidget):
    def init(self):
        super().init()
        self.setWindowTitle("Ventana")
        self.etiqueta1 = QLabel("Hola mundo!", self)

if name == "main":
    app = QApplication([])
    ventana1 = Ventana()
    ventana1.show() 