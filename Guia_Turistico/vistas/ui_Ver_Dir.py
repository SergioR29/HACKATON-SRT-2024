# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ver_DirxHbGXS.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_dir(object):
    def setupUi(self, dir):
        if not dir.objectName():
            dir.setObjectName(u"dir")
        dir.resize(400, 39)
        self.label = QLabel(dir)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 381, 20))

        self.retranslateUi(dir)

        QMetaObject.connectSlotsByName(dir)
    # setupUi

    def retranslateUi(self, dir):
        dir.setWindowTitle(QCoreApplication.translate("dir", u"Direcci\u00f3n", None))
        self.label.setText("")
    # retranslateUi

