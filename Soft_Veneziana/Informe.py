from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox ,QWidget, QGridLayout, QLabel, QComboBox, QPushButton, QDateEdit, QTableWidgetItem, QTableWidget
from PySide6.QtCore import Qt, QDate
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtGui import QPainter
from PySide6.QtPrintSupport import QPrintDialog, QPrinter

import sqlite3

class InInforme(QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.setWindowTitle("EasyPay - INFORMES")

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        centralWidget.setLayout(layout)


        # TITULO
        titulo = QLabel("   BUSQUEDA DE INFORMES")
        layout.addWidget(titulo, 0, 0)
       
        # ESPACIO
        espacio1 = QLabel()
        espacio1.setFixedSize(10, 10)
        layout.addWidget(espacio1, 1, 0)

        # Ingreso de Fecha Inicial
        self.tituloFechaInicial = QLabel("Fecha Desde")
        layout.addWidget(self.tituloFechaInicial, 2, 0)
        self.ingresoFechaInicial = QDateEdit()
        self.ingresoFechaInicial.setDate(QDate.currentDate())
        self.ingresoFechaInicial.setFixedSize(200, 30)
        layout.addWidget(self.ingresoFechaInicial, 3, 0)

        # Ingreso de Fecha Final
        self.tituloFechaFinal = QLabel("Fecha Hasta")
        layout.addWidget(self.tituloFechaFinal, 4, 0)
        self.ingresoFechaFinal = QDateEdit()
        self.ingresoFechaFinal.setDate(QDate.currentDate())
        self.ingresoFechaFinal.setFixedSize(200, 30)
        layout.addWidget(self.ingresoFechaFinal, 5, 0)

        # Título del Tipo de Pago
        self.tituloD = QLabel("Tipo de Movimiento")
        layout.addWidget(self.tituloD, 7, 0)

        # Combobox con las opciones
        self.tipoPagoCombo = QComboBox()
        self.tipoPagoCombo.addItems(["Pago", "Gasto", "Caja", "Todos"])
        self.tipoPagoCombo.setFixedSize(200, 30)
        layout.addWidget(self.tipoPagoCombo, 8, 0)

        # ESPACIO
        espacio3 = QLabel()
        espacio3.setFixedSize(10, 10)
        layout.addWidget(espacio3, 9, 0)

        # Botón Enviar
        self.botonEnviar = QPushButton("Enviar")
        self.botonEnviar.setDefault(True)
        self.botonEnviar.setFixedSize(200, 30)
        self.botonEnviar.clicked.connect(self.enviar)
        layout.addWidget(self.botonEnviar, 10, 0)

       
    
    def enviar(self):
        # Establece los criterios con que se va a filtrar
        cajaPagoGasto = self.tipoPagoCombo.currentText()
        fecha_inicial = self.ingresoFechaInicial.date()
        fecha_final = self.ingresoFechaFinal.date()        

        if fecha_final < fecha_inicial:
            dialogo = QMessageBox.information(self, 'MENSAJE','Se ingresó una fecha Final menor a la fecha Inicial. Intente Nuevamente')
            pass
        else:
            fecha_inicial_str = fecha_inicial.toString("yyyy-MM-dd")
            fecha_final = fecha_final.addDays(1) #se añade un día por el formate Fecha-hora de los resultados
            fecha_final_str = fecha_final.toString("yyyy-MM-dd")
        
            # Crear una nueva ventana para mostrar los resultados
            self.resultados_window = QMainWindow()
            self.resultados_window.setWindowTitle("Informe Obtenido")
            self.resultados_window.resize(1000,700)

            centralWidget = QWidget()
            self.resultados_window.setCentralWidget(centralWidget)
            layout = QGridLayout()
            centralWidget.setLayout(layout)

            self.botonImprimir = QPushButton("Imprimir")
            self.botonImprimir.setFixedSize(80, 30)
            self.botonImprimir.setStyleSheet(
                """
                QPushButton {
                    background-color: #0c4c80;
                    border-radius: 8px;
                    color: #fff;
                    font-family: 'Roboto';
                    font-size: 17px;
                }
                
                QPushButton:hover {
                    background-color: #1563a3; /* Cambia el color en el hover */
                }
                """
            )
            self.botonImprimir.clicked.connect(self.imprimir)
            layout.addWidget(self.botonImprimir)

            # Crear una tabla para mostrar los resultados
            table = QTableWidget()
            table.setColumnCount(6)  # Número de columnas
            table.setHorizontalHeaderLabels(["ID", "CajaPagoGasto", "Tipo", "Concepto" ,"Monto", "Fecha"])
            table.setColumnWidth(5, 200)

            conn = sqlite3.connect('EasyPay.db')
            cursor = conn.cursor()
            if cajaPagoGasto == "Todos":
            # Consulta SQL con filtro de fechas
                cursor.execute("SELECT id, CajaPagoGasto, tipo, concepto ,monto, fecha FROM caja WHERE fecha BETWEEN ? AND ?", (fecha_inicial_str, fecha_final_str))
            else:
            # Consulta SQL con filtro de PagoGasto y fechas
                cursor.execute("SELECT id, CajaPagoGasto, tipo, concepto, monto, fecha FROM caja WHERE CajaPagoGasto=? AND fecha BETWEEN ? AND ?", (cajaPagoGasto, fecha_inicial_str, fecha_final_str))



            # Agregar filas a la tabla con los datos de la base de datos
            row_count = 0
            for row in cursor:

                table.insertRow(row_count)
                for col in range(6):
                    item = QTableWidgetItem(str(row[col]))
                    table.setItem(row_count, col, item)
                row_count += 1

            layout.addWidget(table)

            self.resultados_window.show()

    def imprimir(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self.resultados_window)
        
        if dialog.exec() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            self.resultados_window.centralWidget().render(painter)