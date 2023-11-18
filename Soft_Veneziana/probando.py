from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton,QMessageBox,QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from datetime import datetime
import sqlite3
from Informe import InInforme
from FuncionesPyside import funQlabel, funEspacio

class VentanaEmergentePagos(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mensaje")
        layout = QGridLayout()
        self.setLayout(layout)

        textoInformativo = QLabel("Para hacer modificaciones, debe conocer el ID.")
        layout.addWidget(textoInformativo, 0, 0, 1, 2)

        boton_conocer_id = QPushButton("Buscar ID")
        boton_conocer_id.clicked.connect(self.mostrar_id)
        layout.addWidget(boton_conocer_id, 1, 0)

        boton_aceptar = QPushButton("Editar")
        boton_aceptar.clicked.connect(self.abrir_edit_pagos)
        layout.addWidget(boton_aceptar, 1, 1)

    def mostrar_id(self):
        self.ventana2 = InInforme()
        self.ventana2.show()
        self.accept()

    def abrir_edit_pagos(self):
        self.ventana2 = EditPagos()
        self.ventana2.show()
        self.accept()

class InPagos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("EasyPay - PAGOS")

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        centralWidget.setLayout(layout)

        # TITULO
        titulo = QLabel("          INGRESAR PAGOS")
        layout.addWidget(titulo, 0, 0)
        # ESPACIO
        funEspacio(layout, 1, 0)
        # Ingreso de Monto
        self.tituloMonto = QLabel("Monto")
        layout.addWidget(self.tituloMonto, 2, 0)
        self.ingresoMonto = QLineEdit()
        self.ingresoMonto.setValidator(QDoubleValidator(0.00, 9999999999.99, 2))
        self.ingresoMonto.setFixedSize(200, 30)
        layout.addWidget(self.ingresoMonto, 3, 0)

        # Título del Tipo de Pago
        funQlabel(layout, "Tipo de Pago", 5, 0)
        # Combobox con las opciones
        self.tipoPagoCombo = QComboBox()
        self.tipoPagoCombo.addItems(["Efectivo", "Credito", "Debito", "Transferencia", "Debe", "Cheque"])
        self.tipoPagoCombo.setFixedSize(200, 30)
        layout.addWidget(self.tipoPagoCombo, 6, 0)
        # ESPACIO
        funEspacio(layout, 7, 0)
        # Botón Enviar
        self.botonEnviar = QPushButton("Enviar")
        self.botonEnviar.setDefault(True)
        self.botonEnviar.setFixedSize(200, 30)
        self.botonEnviar.clicked.connect(self.enviar)
        layout.addWidget(self.botonEnviar, 8, 0)

       

    def enviar(self):
        try:
            fecha = datetime.now()
            PagoGasto = 'Pago'
            concepto = "Venta"
            tipo = self.tipoPagoCombo.currentText()
            monto = float(self.ingresoMonto.text())
            eliminado = False
            conn = sqlite3.connect("EasyPay.db")
            conn.execute(f"INSERT INTO caja (CajaPagoGasto,tipo,concepto,monto,fecha,eliminado) VALUES ('{PagoGasto}','{tipo}','{concepto}','{monto}','{fecha}','{eliminado}');")
            conn.commit()
            dialogo = QMessageBox.information(self, 'MENSAJE','SE INGRESARON LOS DATOS CORRECTAMENTE')
            conn.close()
            self.close()
        except:
            dialogo = QMessageBox.warning(self, 'MENSAJE', 'EL CAMPO MONTO NO PUEDE ESTAR VACIO')
            
class EditPagos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("EasyPay - PAGOS")

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        centralWidget.setLayout(layout)

        # TITULO
        titulo = QLabel("            EDITAR PAGOS")
        layout.addWidget(titulo, 0, 0)
        # ESPACIO
        funEspacio(layout, 11, 0)

        # Ingreso de ID (editar)
        self.tituloEditar = QLabel("ID")
        layout.addWidget(self.tituloEditar, 12, 0)
        self.ingresoIdEditar = QLineEdit()
        self.ingresoIdEditar.setValidator(QIntValidator(0, 100))
        self.ingresoIdEditar.setFixedSize(200, 30)
        layout.addWidget(self.ingresoIdEditar, 13, 0)

        # Ingreso de monto (editar)
        self.tituloMontoEditar = QLabel("Monto")
        layout.addWidget(self.tituloMontoEditar, 14, 0)
        self.ingresoMontoEditar = QLineEdit()
        self.ingresoMontoEditar.setValidator(QDoubleValidator(0.00, 9999999999.99, 2))
        self.ingresoMontoEditar.setFixedSize(200, 30)
        layout.addWidget(self.ingresoMontoEditar, 15, 0)

        # Tipo de Pago (editar)
        self.tituloDeditar = QLabel("Tipo de Pago")
        layout.addWidget(self.tituloDeditar, 16, 0)
        self.tipoEditar = QComboBox()
        self.tipoEditar.addItems(["Efectivo", "Credito", "Debito", "Transferencia", "Debe", "Cheque"])
        self.tipoEditar.setFixedSize(200, 30)
        layout.addWidget(self.tipoEditar, 17, 0)

        # Botón Enviar (editar)
        self.botonEnviarEditar = QPushButton("Enviar")
        self.botonEnviarEditar.setDefault(True)
        self.botonEnviarEditar.setFixedSize(200, 30)
        self.botonEnviarEditar.clicked.connect(self.enviar)
        layout.addWidget(self.botonEnviarEditar, 18, 0)

    def enviar(self):
        try:
            conn = sqlite3.connect("EasyPay.db")
            cursor = conn.cursor()
            registro_id = int(self.ingresoIdEditar.text())
            registro_CajaPagoGasto = 'Pago'
            nuevoMonto = float(self.ingresoMontoEditar.text())
            nuevoTipo = self.tipoEditar.currentText()       
            nuevoConcepto = "Venta"
            cursor.execute("UPDATE caja SET monto = ?, concepto = ?, tipo = ? WHERE id = ? AND CajaPagoGasto = ?", (nuevoMonto, nuevoConcepto, nuevoTipo, registro_id, registro_CajaPagoGasto))
            conn.commit()
            if cursor.rowcount == 1:
                dialogo = QMessageBox.information(self, 'MENSAJE','SE ACTUALIZO CORRECTAMENTE REGISTRO')
                self.close()
            else:
                dialogo = QMessageBox.warning(self, 'MENSAJE', 'NO SE ENCONTRO REGISTRO, VUELVA A INTENTARLO')
            conn.close()
        except:
            dialogo = QMessageBox.warning(self, 'MENSAJE', 'EL CAMPO MONTO/ID NO PUEDE ESTAR VACIO')