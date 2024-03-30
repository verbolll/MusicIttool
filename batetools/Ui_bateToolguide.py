# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bateToolguide.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_bateToolguide(object):
    def setupUi(self, bateToolguide):
        if not bateToolguide.objectName():
            bateToolguide.setObjectName(u"bateToolguide")
        bateToolguide.resize(280, 338)
        self.gridLayout = QGridLayout(bateToolguide)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(bateToolguide)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.mvbtn = QPushButton(bateToolguide)
        self.mvbtn.setObjectName(u"mvbtn")
        self.mvbtn.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.mvbtn, 1, 0, 1, 1)


        self.retranslateUi(bateToolguide)

        QMetaObject.connectSlotsByName(bateToolguide)
    # setupUi

    def retranslateUi(self, bateToolguide):
        bateToolguide.setWindowTitle(QCoreApplication.translate("bateToolguide", u"\u5c0f\u5de5\u5177(bate\u6d4b\u8bd5)", None))
        self.pushButton.setText(QCoreApplication.translate("bateToolguide", u"\u591a\u97f3\u9891\u5206\u79bb", None))
        self.mvbtn.setText(QCoreApplication.translate("bateToolguide", u"MV\u5d4c\u5165\u97f3\u51c6\u53c2\u8003", None))
    # retranslateUi

