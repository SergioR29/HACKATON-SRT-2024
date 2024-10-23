from PySide6.QtWidgets import *
from vistas.ui_NoEncontrado import Ui_No_Encontrado

class MiApp(QWidget, Ui_No_Encontrado):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

import sys  
 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    app.exec()