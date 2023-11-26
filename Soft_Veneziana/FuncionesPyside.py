from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QColor, QFont

def funQlabel(layout, texto, fila, columna, tamTexto=12, colorTexto="#000000"):
    nombre = QLabel(texto)
    nombre.setFont(QFont("Roboto", tamTexto))
    nombre.setStyleSheet(f"color: {colorTexto}; text-align: left; font-size: {tamTexto}pt;")
    layout.addWidget(nombre, fila, columna)


def funEspacio(layout, fila, columna):
    espacio = QLabel()
    espacio.setFixedSize(10, 10)
    layout.addWidget(espacio, fila, columna)