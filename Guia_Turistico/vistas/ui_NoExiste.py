# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NoExisteBFwUOC.ui'
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

class Ui_Aviso(object):
    def setupUi(self, Aviso):
        if not Aviso.objectName():
            Aviso.setObjectName(u"Aviso")
        Aviso.resize(251, 108)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogError))
        Aviso.setWindowIcon(icon)
        self.label = QLabel(Aviso)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 0, 191, 51))
        self.label.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.Ok = QPushButton(Aviso)
        self.Ok.setObjectName(u"Ok")
        self.Ok.setGeometry(QRect(170, 80, 75, 24))

        self.retranslateUi(Aviso)
        self.Ok.clicked["bool"].connect(Aviso.close)

        QMetaObject.connectSlotsByName(Aviso)
    # setupUi

    def retranslateUi(self, Aviso):
        Aviso.setWindowTitle(QCoreApplication.translate("Aviso", u"Aviso", None))
        self.label.setText(QCoreApplication.translate("Aviso", u"El sitio no existe", None))
        self.Ok.setText(QCoreApplication.translate("Aviso", u"Ok", None))
    # retranslateUi

