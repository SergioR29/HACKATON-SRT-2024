from PySide6.QtWidgets import *
from vistas.ui_Principal import Ui_MainWindow

class MiApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

import sys  
 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    app.exec() 