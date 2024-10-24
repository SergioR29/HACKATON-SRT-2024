from PySide6.QtWidgets import *
from vistas.ui_Ver_Dir import Ui_dir

class MiApp(QWidget, Ui_dir):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
import sys  
 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    app.exec() 