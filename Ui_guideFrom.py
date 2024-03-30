from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
class Ui_guideFrom(object):
    def setupUi(self, guideFrom):
        if not guideFrom.objectName():
            guideFrom.setObjectName(u"guideFrom")
        guideFrom.resize(292, 370)
        self.verticalLayout = QVBoxLayout(guideFrom)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.maintoolbtn = QPushButton(guideFrom)
        self.maintoolbtn.setObjectName(u"maintoolbtn")
        self.maintoolbtn.setMinimumSize(QSize(20, 60))
        self.maintoolbtn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(15)
        self.maintoolbtn.setFont(font)
        self.verticalLayout.addWidget(self.maintoolbtn)
        self.toolsbtn = QPushButton(guideFrom)
        self.toolsbtn.setObjectName(u"toolsbtn")
        self.toolsbtn.setMinimumSize(QSize(0, 60))
        self.toolsbtn.setFont(font)
        self.verticalLayout.addWidget(self.toolsbtn)
        self.batetoolbtn = QPushButton(guideFrom)
        self.batetoolbtn.setObjectName(u"batetoolbtn")
        self.batetoolbtn.setMinimumSize(QSize(0, 60))
        self.batetoolbtn.setFont(font)
        self.verticalLayout.addWidget(self.batetoolbtn)
        self.helpbtn = QPushButton(guideFrom)
        self.helpbtn.setObjectName(u"helpbtn")
        self.helpbtn.setMinimumSize(QSize(0, 60))
        self.helpbtn.setFont(font)
        self.verticalLayout.addWidget(self.helpbtn)
        self.themebtn = QPushButton(guideFrom)
        self.themebtn.setObjectName(u"themebtn")
        self.verticalLayout.addWidget(self.themebtn)
        self.retranslateUi(guideFrom)
        QMetaObject.connectSlotsByName(guideFrom)
    def retranslateUi(self, guideFrom):
        guideFrom.setWindowTitle(QCoreApplication.translate("guideFrom", u"\u5de5\u5177\u7bb1", None))
        self.maintoolbtn.setText(QCoreApplication.translate("guideFrom", u"\u751f\u6210\u97f3\u51c6\u5206\u6790\u89c6\u9891", None))
        self.toolsbtn.setText(QCoreApplication.translate("guideFrom", u"\u97f3\u9891\u5206\u6790\u5c0f\u5de5\u5177", None))
        self.batetoolbtn.setText(QCoreApplication.translate("guideFrom", u"\u66f4\u591a\u5c0f\u5de5\u5177(bate\u6d4b\u8bd5)", None))
        self.helpbtn.setText(QCoreApplication.translate("guideFrom", u"\u6253\u5f00\u5e2e\u52a9\u6587\u6863", None))
        self.themebtn.setText(QCoreApplication.translate("guideFrom", u"\u4e3b\u9898\u8bbe\u7f6e", None))