from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QDialog, QDateEdit
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from datetime import datetime
import sqlite3
from FuncionesPyside import funQlabel, funEspacio
from Funciones_db import agregoIngreso, buscarId

class ingEditarId(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Veneziana")

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignLeft)
        centralWidget.setLayout(layout)

        # TITULO
        funQlabel(layout, "EDITAR INGRESOS", 0, 0, tamTexto=13, colorTexto="#1e81b0")

        # Ingreso de ID
        funQlabel(layout, "INGRESAR EL ID", 1, 0, tamTexto=12, colorTexto="#1e81b0")
        self.ingCodigo = QLineEdit()
        self.ingCodigo.setValidator(QIntValidator(999999, 999999))
        self.ingCodigo.setFixedSize(200, 30)
        layout.addWidget(self.ingCodigo, 2, 0)

        # Botón Enviar
        self.botonEnviar = QPushButton("Enviar")
        self.botonEnviar.setDefault(True)
        self.botonEnviar.setFixedSize(200, 30)

        # Etiqueta para mostrar el resultado
        self.resultadoLabel = QLabel()
        self.resultadoLabel.setFixedHeight(30)

        # Conectar el botón Enviar a la función buscarYMostrarResultado
        self.botonEnviar.clicked.connect(self.buscarYMostrarResultado)

        # Añadir los widgets al layout
        layout.addWidget(self.botonEnviar, 3, 0)
        layout.addWidget(self.resultadoLabel, 4, 0)

    def buscarYMostrarResultado(self):
        layout = self.centralWidget().layout()
        idBuscado = int(self.ingCodigo.text())
        resultado = buscarId(idBuscado)
        if resultado:
            # ... código existente ...
            idT, fechatT, codT, descT, cantT, provT, ocT, loteT, vtoT, estadoT, eliminadoT = resultado
            # Convierte codT a cadena antes de establecer el texto
            self.ingCodigo.setText(str(codT))

            funQlabel(layout, "EDITAR INGRESOS", 0, 0, tamTexto=13, colorTexto="#1e81b0")
            # Ingreso de Monto
            funQlabel(layout, "Codigo", 1, 0, tamTexto=12, colorTexto="#1e81b0")
            self.ingCodigo = QLineEdit()
            self.ingCodigo.setText(codT)
            self.ingCodigo.setValidator(QIntValidator(999999, 999999))
            self.ingCodigo.setFixedSize(200, 30)
            layout.addWidget(self.ingCodigo, 2, 0)

            funQlabel(layout, "Descripcion", 1, 1)
            self.ingDesc = QLineEdit()
            self.ingDesc.setText(descT)
            self.ingDesc.setFixedSize(200, 30)
            layout.addWidget(self.ingDesc, 2, 1)

            funQlabel(layout, "Cantidad", 1, 2)
            self.ingCantidad = QLineEdit()
            self.ingCantidad.setText(cantT)
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
            self.ingOc.setText(ocT)
            self.ingOc.setValidator(QIntValidator(999999, 999999))
            self.ingOc.setFixedSize(200, 30)
            layout.addWidget(self.ingOc, 4, 1)

            funQlabel(layout, "Lote", 5, 0)
            self.ingLote = QLineEdit()
            self.ingLote.setText(loteT)
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
            
        else:
            self.resultadoLabel.setText("ID no encontrado")

    def on_btnEnviar_clicked(self):
        # Obtener los datos del formulario
        id = self.ingCodigo.text()
        codigo = self.ingCodigo.text()
        descripcion = self.ingDesc.text()
        cantidad = self.ingCantidad.text()
        proveedor = self.ingProveedor.currentText()
        oc = self.ingOc.text()
        lote = self.ingLote.text()
        vto = self.ingVto.date()
        estado = self.ingEstado.currentText()

        # Actualizar los datos en la base de datos
        agregoIngreso(id, codigo, descripcion, cantidad, proveedor, oc, lote, vto, estado)

        # Mostrar un mensaje de confirmación
        QMessageBox.information(self, "Información", "Los datos se actualizaron correctamente.")

        # Limpiar los campos del formulario
        self.ingCodigo.setText("")
        self.ingDesc.setText("")
        self.ingCantidad.setText("")
        self.ingProveedor.setCurrentIndex(0)
        self.ingOc.setText("")
        self.ingLote.setText("")
        self.ingVto.setDate(QDate.currentDate())
        self.ingEstado.setCurrentIndex(0)

