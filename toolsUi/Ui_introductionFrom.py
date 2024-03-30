from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)
class Ui_introductionFrom(object):
    def setupUi(self, introductionFrom):
        if not introductionFrom.objectName():
            introductionFrom.setObjectName(u"introductionFrom")
        introductionFrom.resize(400, 300)
        self.gridLayout = QGridLayout(introductionFrom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(introductionFrom)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.retranslateUi(introductionFrom)
        QMetaObject.connectSlotsByName(introductionFrom)
    def retranslateUi(self, introductionFrom):
        introductionFrom.setWindowTitle(QCoreApplication.translate("introductionFrom", u"\u7b80\u4ecb", None))
        self.label.setText("")