from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
class Ui_tone(object):
    def setupUi(self, tone):
        if not tone.objectName():
            tone.setObjectName(u"tone")
        tone.resize(398, 168)
        self.gridLayout = QGridLayout(tone)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(tone)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QLabel(tone)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QLabel(tone)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QPushButton(tone)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QPushButton(tone)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.retranslateUi(tone)
        QMetaObject.connectSlotsByName(tone)
    def retranslateUi(self, tone):
        tone.setWindowTitle(QCoreApplication.translate("tone", u"tone", None))
        self.label.setText(QCoreApplication.translate("tone", u"<html><head/><body><p>\u8c03\u6027\u5c06\u88ab\u66f4\u6539\u4e3a</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("tone", u"\u8fd9\u548c\u8bc6\u522b\u7684\u8c03\u6027\u4e0d\u7b26", None))
        self.label_3.setText(QCoreApplication.translate("tone", u"\u5982\u679c\u60a8\u4e0d\u786e\u5b9a\u60a8\u6240\u9009\u62e9\u7684\u662f\u5426\u6b63\u786e\u5efa\u8bae\u7ef4\u6301", None))
        self.pushButton.setText(QCoreApplication.translate("tone", u"\u66f4\u6539\u8c03\u6027\uff0c\u6211\u786e\u5b9a\u6211\u7684\u9009\u62e9\u662f\u6b63\u786e\u7684", None))
        self.pushButton_2.setText(QCoreApplication.translate("tone", u"\u4fdd\u6301\u539f\u6709\u8c03\u6027", None))