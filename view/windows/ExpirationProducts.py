import sys
import os
from PyQt6.QtWidgets import QHBoxLayout,QTableWidget,QTableWidgetItem,QTableView,QHeaderView,QComboBox, QApplication, QWidget, QDateEdit, QLabel, QPushButton,QVBoxLayout,QLineEdit, QSpinBox, QMessageBox, QGridLayout, QScrollArea
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QPixmap, QFont
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from view.QSS.ExpirationProductsQSS import styleExpirationProduct

class ExpirationProduct(QWidget):
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
        self.setWindowTitle('Productos a vencer')
        # self.setGeometry(100, 100, 300, 650)  # Ajustar la geometría de la ventana
        self.setFixedSize( 1200, 810)
        self.generate_form()
        self.show()

    def generate_form(self):
        central_widget = QWidget()
       
        # Crear un layout vertical
        layout = QGridLayout(central_widget)
        
        image_label_product_expire = QLabel()
        pixmap = QPixmap(self.resource_path('../../Img/ico_productos_a vencer.png'))  # Ruta relativa de la imagen
        image_label_product_expire.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label_product_expire.setPixmap(pixmap)
        image_label_product_expire.setObjectName("image_see_sales") 
        
        layout.addWidget(image_label_product_expire,0,0,1,3)
      
        # Crear la tabla
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(100)  # Número de filas
        self.table_widget.setColumnCount(10)  # Número de columnas
        self.table_widget.setFixedSize(1180,450)
        self.table_widget.setObjectName('expire_products_table')
        # Llenar la tabla con datos de ejemplo
        for row in range(100):
            for column in range(10):
                item = QTableWidgetItem(f"Item {row},{column}")
                self.table_widget.setItem(row, column, item)
        
        # Crear una área de desplazamiento
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table_widget)
        scroll_area.setWidgetResizable(True)
        
        layout.addWidget(scroll_area,1,1)

        cant_expire_products=2
        label_cant_products=QLabel(f"CANTIDAD DE\n PRODUCTOS A VENCER: {cant_expire_products}")
        label_cant_products.setObjectName("label_cant_products")
        label_cant_products.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(label_cant_products,2,1)        

        self.setLayout(layout)
        
   
app = QApplication(sys.argv)
app.setStyleSheet(styleExpirationProduct())
window = ExpirationProduct()
window.show()
sys.exit(app.exec())