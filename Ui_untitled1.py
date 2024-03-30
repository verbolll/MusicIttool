
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(176, 234)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.selectsong = QLabel(Form)
        self.selectsong.setObjectName(u"selectsong")
        self.selectsong.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.selectsong, 0, 0, 1, 1)

        self.selectButton = QPushButton(Form)
        self.selectButton.setObjectName(u"selectButton")

        self.gridLayout.addWidget(self.selectButton, 1, 0, 1, 1)

        self.loading = QLabel(Form)
        self.loading.setObjectName(u"loading")
        font = QFont()
        font.setPointSize(20)
        self.loading.setFont(font)
        self.loading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.loading, 2, 0, 1, 1)

        self.doButton = QPushButton(Form)
        self.doButton.setObjectName(u"doButton")

        self.gridLayout.addWidget(self.doButton, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.selectsong.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u8981\u5206\u6790\u7684\u97f3\u9891", None))
        self.selectButton.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u97f3\u4e50", None))
        self.loading.setText("")
        self.doButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5206\u6790", None))

