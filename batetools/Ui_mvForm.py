from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
class Ui_mvForm(object):
    def setupUi(self, mvForm):
        if not mvForm.objectName():
            mvForm.setObjectName(u"mvForm")
        mvForm.resize(400, 300)
        self.gridLayout = QGridLayout(mvForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MvViewPiclab = QLabel(mvForm)
        self.MvViewPiclab.setObjectName(u"MvViewPiclab")
        self.MvViewPiclab.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.MvViewPiclab, 0, 0, 1, 1)
        self.MvViewNamelab = QLabel(mvForm)
        self.MvViewNamelab.setObjectName(u"MvViewNamelab")
        self.MvViewNamelab.setMaximumSize(QSize(16777215, 25))
        self.MvViewNamelab.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.MvViewNamelab, 1, 0, 1, 1)
        self.selMVbtn = QPushButton(mvForm)
        self.selMVbtn.setObjectName(u"selMVbtn")
        self.gridLayout.addWidget(self.selMVbtn, 2, 0, 1, 1)
        self.starbtn = QPushButton(mvForm)
        self.starbtn.setObjectName(u"starbtn")
        self.starbtn.setEnabled(False)
        self.gridLayout.addWidget(self.starbtn, 3, 0, 1, 1)
        self.retranslateUi(mvForm)
        QMetaObject.connectSlotsByName(mvForm)
    def retranslateUi(self, mvForm):
        mvForm.setWindowTitle(QCoreApplication.translate("mvForm", u"MV\u5d4c\u5165\u97f3\u51c6\u53c2\u8003", None))
        self.MvViewPiclab.setText("")
        self.MvViewNamelab.setText("")
        self.selMVbtn.setText(QCoreApplication.translate("mvForm", u"\u9009\u62e9MV\u89c6\u9891", None))
        self.starbtn.setText(QCoreApplication.translate("mvForm", u"\u5f00\u59cb\u5206\u6790", None))