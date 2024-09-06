
import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

from PyQt6.QtGui import QPixmap
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.SalesMenuQSS import styleSalesMenuQSS
from controller.ControllerSell import optionSell

class SalesMenu(QWidget):
    def resource_path(self, relative_path):
        """Obtiene la ruta absoluta al recurso, trabajando para dev y para PyInstaller"""
        try:
            # PyInstaller crea una carpeta temporal y almacena el path en _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Formulario de Producto')
        self.setFixedHeight(730)
        self.setFixedWidth(650)
        self.generate_form()
        self.show()

    def generate_form(self):
      layout = QVBoxLayout()

      image_label_sales_menu = QLabel()
      pixmap = QPixmap(self.resource_path('../../Img/ico_menu_ventas.png'))  # Ruta relativa de la imagen
      image_label_sales_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)
      image_label_sales_menu.setPixmap(pixmap)
      image_label_sales_menu.setObjectName("image_sales_menu") 

      label_title_sales_menu = QLabel("Escoja el tipo de caja que necesita")
      label_title_sales_menu.setObjectName("title_sales_menu")
      label_title_sales_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)

      self.type_sell_combo_box = QComboBox()
      options = optionSell()
      self.type_sell_combo_box.addItem("Escoja una opcion")
      self.type_sell_combo_box.addItems(options)
      self.type_sell_combo_box.model().item(0).setEnabled(False)

      btn_sell = QPushButton("IR A CAJA")
      btn_sell.setObjectName("btn_sell")
    #   btn_sell.clicked.connect(lambda: self.show_cash_register(self.type_sell_combo_box.currentText()))

      layout.addWidget(image_label_sales_menu)
      layout.addWidget(label_title_sales_menu)
      layout.addWidget(self.type_sell_combo_box)
      layout.addWidget(btn_sell)

      self.setLayout(layout)
    
    # def show_cash_register(self, type_sale):
    #     if self.cash_register_window:
    #         self.cash_register_window.close()
    #     app = CashRegister(type_sale)
    #     app.show()


app = QApplication(sys.argv)
app.setStyleSheet(styleSalesMenuQSS())
window = SalesMenu()
sys.exit(app.exec())
