# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IniciodiusFB.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Inicio(object):
    def setupUi(self, Inicio):
        if not Inicio.objectName():
            Inicio.setObjectName(u"Inicio")
        Inicio.resize(299, 188)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AppointmentNew))
        Inicio.setWindowIcon(icon)
        self.label = QLabel(Inicio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 131, 21))
        self.label.setStyleSheet(u"font: 700 9pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(Inicio)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 80, 241, 21))
        self.Aceptar = QPushButton(Inicio)
        self.Aceptar.setObjectName(u"Aceptar")
        self.Aceptar.setGeometry(QRect(170, 150, 75, 24))
        self.Ninguno = QPushButton(Inicio)
        self.Ninguno.setObjectName(u"Ninguno")
        self.Ninguno.setGeometry(QRect(40, 150, 75, 24))

        self.retranslateUi(Inicio)
        self.Aceptar.clicked["bool"].connect(Inicio.hide)
        self.Ninguno.clicked["bool"].connect(Inicio.hide)

        QMetaObject.connectSlotsByName(Inicio)
    # setupUi

    def retranslateUi(self, Inicio):
        Inicio.setWindowTitle(QCoreApplication.translate("Inicio", u"Inicio", None))
        self.label.setText(QCoreApplication.translate("Inicio", u"\u00bfA qu\u00e9 sitio quieres ir?:", None))
        self.Aceptar.setText(QCoreApplication.translate("Inicio", u"Aceptar", None))
        self.Ninguno.setText(QCoreApplication.translate("Inicio", u"Ninguno", None))
    # retranslateUi

