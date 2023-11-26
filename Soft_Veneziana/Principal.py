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

    def menuHerramientas(self):
        self.accion_info = QAction(QIcon(absPath("Iconos_estilos/new.ico")), "&Nuevo Ingreso", self)
        self.accion_info.triggered.connect(lambda: self.mostrarVentana(InGastos))
        herramientas = QToolBar("Barra de herramientas principal")
        herramientas.addAction(self.accion_info)
        self.addToolBar(herramientas)

    def mostrarVentana(self, conexion):
        self.ventana2 = conexion()
        self.setCentralWidget(self.ventana2)


    def crearSubmenu(self, nombreMenu, nombreVariable, titulo, nombreConexion):
        nombreVariable = QAction(titulo, self)
        nombreVariable.triggered.connect(lambda: self.mostrarVentana(nombreConexion))
        nombreMenu.addAction(nombreVariable)
    


if __name__ == "__main__":
    
    app = QApplication([])
    
    # Importamos el archivo QSS
    with open('Soft_Veneziana/estilo.qss', 'r') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)

    window = MainWindow()
    window.show()

    app.exec()
