from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
class Ui_Form1(object):
    def setupUi(self, Form1):
        if not Form1.objectName():
            Form1.setObjectName(u"Form1")
        Form1.resize(400, 441)
        self.gridLayout = QGridLayout(Form1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.choosedmusic1 = QLabel(Form1)
        self.choosedmusic1.setObjectName(u"choosedmusic1")
        self.choosedmusic1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.choosedmusic1, 0, 0, 1, 1)
        self.bigpic1btn = QPushButton(Form1)
        self.bigpic1btn.setObjectName(u"bigpic1btn")
        self.bigpic1btn.setEnabled(False)
        self.gridLayout.addWidget(self.bigpic1btn, 4, 0, 1, 1)
        self.savepicbtn1 = QPushButton(Form1)
        self.savepicbtn1.setObjectName(u"savepicbtn1")
        self.savepicbtn1.setEnabled(False)
        self.gridLayout.addWidget(self.savepicbtn1, 3, 0, 1, 1)
        self.choosemusic1btn = QPushButton(Form1)
        self.choosemusic1btn.setObjectName(u"choosemusic1btn")
        self.gridLayout.addWidget(self.choosemusic1btn, 1, 0, 1, 1)
        self.overpic1 = QLabel(Form1)
        self.overpic1.setObjectName(u"overpic1")
        self.overpic1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.overpic1, 2, 0, 1, 1)
        self.intbtn = QPushButton(Form1)
        self.intbtn.setObjectName(u"intbtn")
        self.gridLayout.addWidget(self.intbtn, 5, 0, 1, 1)
        self.retranslateUi(Form1)
        QMetaObject.connectSlotsByName(Form1)
    def retranslateUi(self, Form1):
        Form1.setWindowTitle(QCoreApplication.translate("Form1", u"\u6ce2\u5f62\u56fe", None))
        self.choosedmusic1.setText("")
        self.bigpic1btn.setText(QCoreApplication.translate("Form1", u"\u653e\u5927\u6ce2\u5f62\u56fe", None))
        self.savepicbtn1.setText(QCoreApplication.translate("Form1", u"\u4fdd\u5b58\u6ce2\u5f62\u56fe", None))
        self.choosemusic1btn.setText(QCoreApplication.translate("Form1", u"\u9009\u62e9\u97f3\u9891", None))
        self.overpic1.setText("")
        self.intbtn.setText(QCoreApplication.translate("Form1", u"\u4ecb\u7ecd\u6ce2\u5f62\u56fe", None))