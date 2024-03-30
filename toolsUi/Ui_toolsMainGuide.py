from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)
class Ui_toolsMainGuide(object):
    def setupUi(self, toolsMainGuide):
        if not toolsMainGuide.objectName():
            toolsMainGuide.setObjectName(u"toolsMainGuide")
        toolsMainGuide.resize(409, 345)
        self.gridLayout = QGridLayout(toolsMainGuide)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolsbtn1 = QPushButton(toolsMainGuide)
        self.toolsbtn1.setObjectName(u"toolsbtn1")
        self.toolsbtn1.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(10)
        self.toolsbtn1.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn1, 0, 0, 1, 1)
        self.toolsbtn2 = QPushButton(toolsMainGuide)
        self.toolsbtn2.setObjectName(u"toolsbtn2")
        self.toolsbtn2.setMinimumSize(QSize(0, 50))
        self.toolsbtn2.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn2, 0, 1, 1, 1)
        self.toolsbtn3 = QPushButton(toolsMainGuide)
        self.toolsbtn3.setObjectName(u"toolsbtn3")
        self.toolsbtn3.setMinimumSize(QSize(0, 50))
        self.toolsbtn3.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn3, 1, 0, 1, 1)
        self.toolsbtn4 = QPushButton(toolsMainGuide)
        self.toolsbtn4.setObjectName(u"toolsbtn4")
        self.toolsbtn4.setMinimumSize(QSize(0, 50))
        self.toolsbtn4.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn4, 1, 1, 1, 1)
        self.toolsbtn5 = QPushButton(toolsMainGuide)
        self.toolsbtn5.setObjectName(u"toolsbtn5")
        self.toolsbtn5.setMinimumSize(QSize(0, 50))
        self.toolsbtn5.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn5, 2, 0, 1, 1)
        self.toolsbtn6 = QPushButton(toolsMainGuide)
        self.toolsbtn6.setObjectName(u"toolsbtn6")
        self.toolsbtn6.setMinimumSize(QSize(0, 50))
        self.toolsbtn6.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn6, 2, 1, 1, 1)
        self.toolsbtn7 = QPushButton(toolsMainGuide)
        self.toolsbtn7.setObjectName(u"toolsbtn7")
        self.toolsbtn7.setMinimumSize(QSize(0, 50))
        self.toolsbtn7.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn7, 3, 0, 1, 1)
        self.toolsbtn8 = QPushButton(toolsMainGuide)
        self.toolsbtn8.setObjectName(u"toolsbtn8")
        self.toolsbtn8.setMinimumSize(QSize(0, 50))
        self.toolsbtn8.setFont(font)
        self.gridLayout.addWidget(self.toolsbtn8, 3, 1, 1, 1)
        self.retranslateUi(toolsMainGuide)
        QMetaObject.connectSlotsByName(toolsMainGuide)
    def retranslateUi(self, toolsMainGuide):
        toolsMainGuide.setWindowTitle(QCoreApplication.translate("toolsMainGuide", u"\u97f3\u9891\u5206\u6790\u5c0f\u5de5\u5177", None))
        self.toolsbtn1.setText(QCoreApplication.translate("toolsMainGuide", u"\u6ce2\u5f62\u56fe", None))
        self.toolsbtn2.setText(QCoreApplication.translate("toolsMainGuide", u"\u9891\u8c31\u56fe\n"
"Spectogram", None))
        self.toolsbtn3.setText(QCoreApplication.translate("toolsMainGuide", u"\u6885\u5c14\u9891\u7387\u5012\u8c31\u7cfb\u6570\n"
"MFCC", None))
        self.toolsbtn4.setText(QCoreApplication.translate("toolsMainGuide", u"\u8fc7\u96f6\u7387\n"
"zero-crossing rate\uff0cZCR", None))
        self.toolsbtn5.setText(QCoreApplication.translate("toolsMainGuide", u"\u9891\u8c31\u8d28\u5fc3\n"
"Spectral Centroid", None))
        self.toolsbtn6.setText(QCoreApplication.translate("toolsMainGuide", u"\u9891\u8c31\u5e26\u5bbd\n"
"Spectral Bandwidth", None))
        self.toolsbtn7.setText(QCoreApplication.translate("toolsMainGuide", u"\u9891\u8c31\u6eda\u964d", None))
        self.toolsbtn8.setText(QCoreApplication.translate("toolsMainGuide", u"\u8272\u5ea6\u7279\u5f81\n"
"Chroma Feature", None))