from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QPushButton,QMessageBox,QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator, QDoubleValidator, QFont
from datetime import datetime
import sqlite3
from FuncionesPyside import funQlabel, funEspacio

class InGastos(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("EasyPay - GASTOS")
        #self.resize(300, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignLeft)
        centralWidget.setLayout(layout)


        # TITULO
        titulo = QLabel("INGRESO DE INSUMOS")
        layout.addWidget(titulo, 0, 0)
       
        # ESPACIO
        funEspacio(layout, 1, 0)
        # Ingreso de Monto
        funQlabel(layout, "Codigo", 2, 0)
        self.ingCodigo = QLineEdit()
        self.ingCodigo.setValidator(QIntValidator(999999, 999999))
        self.ingCodigo.setFixedSize(200, 30)
        layout.addWidget(self.ingCodigo, 3, 0)

        funQlabel(layout, "Descripcion", 2, 1)
        self.ingDesc = QLineEdit()
        self.ingDesc.setFixedSize(200, 30)
        layout.addWidget(self.ingDesc, 3, 1)

        funQlabel(layout, "Cantidad", 4, 0)
        self.ingCantidad = QLineEdit()
        self.ingCantidad.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.ingCantidad.setFixedSize(200, 30)
        layout.addWidget(self.ingCantidad, 5, 0)

        funQlabel(layout, "Proveedores", 4, 1)
        self.ingProveedor = QComboBox()
        self.ingProveedor.addItems(["Efectivo", "Credito", "Debito", "Transferencia", "Debe", "Cheque"])
        self.ingProveedor.setFixedSize(200, 30)
        layout.addWidget(self.ingProveedor, 5, 1)

        funQlabel(layout, "Orden de Compra", 10, 0)
        self.ingOc = QLineEdit()
        self.ingOc.setValidator(QIntValidator(999999, 999999))
        self.ingOc.setFixedSize(200, 30)
        layout.addWidget(self.ingOc, 11, 0)



        # Botón Enviar
        self.botonEnviar = QPushButton("Enviar")
        self.botonEnviar.setDefault(True)
        self.botonEnviar.setFixedSize(200, 30)
        self.botonEnviar.clicked.connect(self.enviar)
        layout.addWidget(self.botonEnviar, 20, 0)

       
    def enviar(self):
        try:
            monto = float(self.ingDesc.text())
            fecha = datetime.now()
            PagoGasto = 'Gasto'
            concepto = self.concepto.currentText()
            tipo = self.tipo.currentText()
            eliminado = False
            conn = sqlite3.connect("EasyPay.db")
            conn.execute(f"INSERT INTO caja (CajaPagoGasto,tipo,concepto,monto,fecha,eliminado) VALUES ('{PagoGasto}','{tipo}','{concepto}','{monto}','{fecha}','{eliminado}');")
            conn.commit()
            dialogo = QMessageBox.information(self, 'MENSAJE','SE INGRESARON LOS DATOS CORRECTAMENTE')
            conn.close()
            self.close()
        except:
            dialogo = QMessageBox.warning(self, 'MENSAJE', 'EL CAMPO MONTO NO PUEDE ESTAR VACIO')