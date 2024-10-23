# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NoEncontradoGPbzwd.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_No_Encontrado(object):
    def setupUi(self, No_Encontrado):
        if not No_Encontrado.objectName():
            No_Encontrado.setObjectName(u"No_Encontrado")
        No_Encontrado.resize(394, 115)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        No_Encontrado.setWindowIcon(icon)
        self.label = QLabel(No_Encontrado)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 10, 241, 51))
        self.label.setStyleSheet(u"font: 600 20pt \"Segoe UI\";")
        self.Ok = QPushButton(No_Encontrado)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setGeometry(QRect(310, 80, 75, 24))

        self.retranslateUi(No_Encontrado)
        self.Ok.clicked["bool"].connect(No_Encontrado.hide)

        QMetaObject.connectSlotsByName(No_Encontrado)
    # setupUi

    def retranslateUi(self, No_Encontrado):
        No_Encontrado.setWindowTitle(QCoreApplication.translate("No_Encontrado", u"Aviso", None))
        self.label.setText(QCoreApplication.translate("No_Encontrado", u"Sitio no encontrado", None))
        self.Ok.setText(QCoreApplication.translate("No_Encontrado", u"Ok", None))
    # retranslateUi

