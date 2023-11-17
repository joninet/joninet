from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QStatusBar, QToolBar)
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(480, 320)
        # Creamos la acción accion_info antes de usarla
        self.accion_info = QAction(QIcon(absPath("iconos/info.ico")), "&Info", self)
        self.accion_info.triggered.connect(self.mostrar_info)
        self.construir_menu()
        # construimos las herramientas
        self.construir_herramientas()

    def construir_menu(self):
        # Aquí puedes agregar más acciones de menú si es necesario
        pass

    def construir_herramientas(self):
        # Creamos una barra de herramientas
        herramientas = QToolBar("Barra de herramientas principal")
        # Podemos agregar la acción salir implícitamente
        herramientas.addAction(QIcon(absPath("iconos/new.ico")), "&Salir", self.close)
        # Añadimos la acción accion_info a la barra de herramientas
        herramientas.addAction(self.accion_info)
        # La añadimos a la ventana principal
        self.addToolBar(herramientas)

    def mostrar_info(self):
        dialogo = QMessageBox.information(
            self, "Diálogo informativo", "Esto es un texto informativo")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
