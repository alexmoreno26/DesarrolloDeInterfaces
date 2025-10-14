# Actividad 14 de Octubre
- Alejandro Moreno
---
## Importacion
Importamos las clases QApplication, QLabel y QWidget del módulo QtWidgets
- from PySide6.QtWidgets import QApplication, QLabel, QWidget
---
## Creacion de clases
Ahora creamos 2 archivos diferentes llamados ventana.py e importador.py
- En ventana.py tenemos que tener la clase ventana creada  hereda de QWidget
  - Llamada al constructor de la superclase--->
        super().__init__()
  - Asignamos el título de la ventana--->
        self.setWindowTitle("Ventana")
  - Creamos una etiqueta con la ventana como elemento principal--->
        self.etiqueta1 = QLabel("¡Hola mundo!", self)
