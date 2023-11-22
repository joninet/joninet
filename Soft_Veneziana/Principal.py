from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar, QLabel, QToolBar
from PySide6.QtGui import QAction, QFont, QIcon
from Informe import InInforme
from pathlib import Path
import sqlite3
from Ingreso_Insumo import InGastos

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EasyPay - PRINCIPAL")
        self.resize(700, 400)
        self.menuCompleto()
        self.menuHerramientas()

    def menuCompleto(self):
        menu = self.menuBar()
        
        #menu caja
        menuCaja = menu.addMenu("Nuevo  |")
        self.crearSubmenu(menuCaja,"arqueoCaja","Aqueo de Caja",InInforme)
        self.crearSubmenu(menuCaja,"cierreCaja","Cierre de Caja",InInforme)
        

        #menu pagos
        menuPagos = menu.addMenu("Pago  |")
        self.crearSubmenu(menuPagos,"ingresarPagos","Ingresar",InInforme)
        self.crearSubmenu(menuPagos,"editarPagos","Editar",InInforme)

        self.setStatusBar(QStatusBar(self))

        self.etiqueta_estado_caja = QLabel("Estado Caja: CERRADO", self)
        self.etiqueta_estado_caja.setGeometry(10, 20, 300, 30)
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)  # Cambia el tamaño de la fuente a 14 puntos
        self.etiqueta_estado_caja.setFont(font)

    def menuHerramientas(self):
        self.accion_info = QAction(QIcon(absPath("iconos/new.ico")), "&Nuevo Ingreso", self)
        self.accion_info.triggered.connect(lambda: self.mostrarVentana(InGastos))
        herramientas = QToolBar("Barra de herramientas principal")
        herramientas.addAction(self.accion_info)
        self.addToolBar(herramientas)

    def mostrarVentana(self, conexion):
        self.ventana2 = conexion()
        if self.accion_info.triggered:
            self.ventana2.show()

    def crearSubmenu(self, nombreMenu, nombreVariable, titulo, nombreConexion):
        nombreVariable = QAction(titulo, self)
        nombreVariable.triggered.connect(lambda: self.mostrarVentana(nombreConexion))
        nombreMenu.addAction(nombreVariable)
    


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
