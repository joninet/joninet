from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton,QMessageBox,QDialog, QDateEdit
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from datetime import datetime
import sqlite3
from FuncionesPyside import funQlabel, funEspacio
from Funciones_db import agregoIngreso

class InGastos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("Veneziana")
        #self.resize(300, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignLeft)
        centralWidget.setLayout(layout)


        # TITULO
        funQlabel(layout, "INGRESOS DE INSUMOS", 0, 0, tamTexto=13, colorTexto="#1e81b0")
        # Ingreso de Monto
        funQlabel(layout, "Codigo", 1, 0, tamTexto=12, colorTexto="#1e81b0")
        self.ingCodigo = QLineEdit()
        self.ingCodigo.setValidator(QIntValidator(999999, 999999))
        self.ingCodigo.setFixedSize(200, 30)
        layout.addWidget(self.ingCodigo, 2, 0)

        funQlabel(layout, "Descripcion", 1, 1)
        self.ingDesc = QLineEdit()
        self.ingDesc.setFixedSize(200, 30)
        layout.addWidget(self.ingDesc, 2, 1)

        funQlabel(layout, "Cantidad", 1, 2)
        self.ingCantidad = QLineEdit()
        self.ingCantidad.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ingCantidad.setFixedSize(200, 30)
        layout.addWidget(self.ingCantidad, 2, 2)

        funQlabel(layout, "Proveedor", 3, 0)
        self.ingProveedor = QComboBox()
        self.ingProveedor.addItems(["Efectivo", "Credito", "Debito", "Transferencia", "Debe", "Cheque"])
        self.ingProveedor.setFixedSize(200, 30)
        layout.addWidget(self.ingProveedor, 4, 0)

        funQlabel(layout, "Orden de Compra", 3, 1)
        self.ingOc = QLineEdit()
        self.ingOc.setValidator(QIntValidator(999999, 999999))
        self.ingOc.setFixedSize(200, 30)
        layout.addWidget(self.ingOc, 4, 1)

        funQlabel(layout, "Lote", 5, 0)
        self.ingLote = QLineEdit()
        self.ingLote.setFixedSize(200, 30)
        layout.addWidget(self.ingLote, 6, 0)

        funQlabel(layout, "Vencimiento", 5, 1)
        self.ingVto = QDateEdit()
        self.ingVto.setDate(QDate.currentDate())
        self.ingVto.setFixedSize(200, 30)
        layout.addWidget(self.ingVto, 6, 1)

        funQlabel(layout, "Estado", 5, 2)
        self.ingEstado = QComboBox()
        self.ingEstado.addItems(["Aprobado", "En Revision"])
        self.ingEstado.setFixedSize(200, 30)
        layout.addWidget(self.ingEstado, 6, 2)

        funEspacio(layout, 7, 0)

        # Botón Enviar
        self.botonEnviar = QPushButton("Enviar")
        self.botonEnviar.setDefault(True)
        self.botonEnviar.setFixedSize(200, 30)
        self.botonEnviar.clicked.connect(self.enviar)
        layout.addWidget(self.botonEnviar, 20, 0)

       
    def enviar(self):
        codigo=int(self.ingCodigo.text())
        desc=self.ingDesc.text()
        cant=float(self.ingCantidad.text())
        prov=self.ingProveedor.currentText() 
        oc=int(self.ingOc.text())
        lote=self.ingLote.text()
        vto=self.ingVto.text()
        estado=self.ingEstado.currentText()

        agregoIngreso(codigo, desc, cant, prov, oc, lote, vto, estado, False)

class ingEdGastos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("Veneziana")
        #self.resize(300, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignLeft)
        centralWidget.setLayout(layout)


        # TITULO
        funQlabel(layout, "EDITAR iNGRESOS", 0, 0, tamTexto=13, colorTexto="#1e81b0")
        # Ingreso de Monto
        funQlabel(layout, "iNGRESAR EL ID", 1, 0, tamTexto=12, colorTexto="#1e81b0")
        self.ingCodigo = QLineEdit()
        self.ingCodigo.setValidator(QIntValidator(999999, 999999))
        self.ingCodigo.setFixedSize(200, 30)
        layout.addWidget(self.ingCodigo, 2, 0)

class edGastos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("Veneziana")
        #self.resize(300, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignLeft)
        centralWidget.setLayout(layout)


        # TITULO
        funQlabel(layout, "EDITAR iNGRESOS", 0, 0, tamTexto=13, colorTexto="#1e81b0")
        # Ingreso de Monto
        funQlabel(layout, "iNGRESAR EL ID", 1, 0, tamTexto=12, colorTexto="#1e81b0")
        self.ingCodigo = QLineEdit()
        self.ingCodigo.setText("ingreso lo que quiero que diga")
        self.ingCodigo.setValidator(QIntValidator(999999, 999999))
        self.ingCodigo.setFixedSize(200, 30)
        layout.addWidget(self.ingCodigo, 2, 0)