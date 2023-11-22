from PySide6.QtWidgets import QLabel

def funQlabel(layout, texto, fila, columna):
    nombre = QLabel(texto)

    nombre.update()
    layout.addWidget(nombre, fila, columna)

def funEspacio(layout, fila, columna):
    espacio = QLabel()
    espacio.setFixedSize(10, 10)
    layout.addWidget(espacio, fila, columna)