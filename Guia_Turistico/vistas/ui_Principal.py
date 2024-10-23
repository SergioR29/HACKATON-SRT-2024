# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrincipalJsGBOX.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        MainWindow.setWindowIcon(icon)
        self.actionRefrescar = QAction(MainWindow)
        self.actionRefrescar.setObjectName(u"actionRefrescar")
        self.actionVer_Direcci_n = QAction(MainWindow)
        self.actionVer_Direcci_n.setObjectName(u"actionVer_Direcci_n")
        self.actionVer_Mapa = QAction(MainWindow)
        self.actionVer_Mapa.setObjectName(u"actionVer_Mapa")
        self.actionPartes = QAction(MainWindow)
        self.actionPartes.setObjectName(u"actionPartes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 35, 631, 111))
        self.label.setStyleSheet(u"font: 600 24pt \"Segoe UI\";")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(60, 150, 631, 64))
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(520, 250, 172, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuSitio = QMenu(self.menubar)
        self.menuSitio.setObjectName(u"menuSitio")
        self.menuMapa = QMenu(self.menubar)
        self.menuMapa.setObjectName(u"menuMapa")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSitio.menuAction())
        self.menubar.addAction(self.menuMapa.menuAction())
        self.menuSitio.addAction(self.actionVer_Direcci_n)
        self.menuSitio.addAction(self.actionPartes)
        self.menuMapa.addAction(self.actionRefrescar)
        self.menuMapa.addAction(self.actionVer_Mapa)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gu\u00eda Tur\u00edstico", None))
        self.actionRefrescar.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.actionVer_Direcci_n.setText(QCoreApplication.translate("MainWindow", u"Ver Direcci\u00f3n", None))
        self.actionVer_Mapa.setText(QCoreApplication.translate("MainWindow", u"Ver Mapa", None))
        self.actionPartes.setText(QCoreApplication.translate("MainWindow", u"Partes", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00bfA qu\u00e9 parte del sitio elegido quieres ir?", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.menuSitio.setTitle(QCoreApplication.translate("MainWindow", u"Sitio", None))
        self.menuMapa.setTitle(QCoreApplication.translate("MainWindow", u"Mapa", None))
    # retranslateUi

