from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
class Ui_Form2(object):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(400, 441)
        self.gridLayout = QGridLayout(Form2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.overpic1 = QLabel(Form2)
        self.overpic1.setObjectName(u"overpic1")
        self.overpic1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.overpic1, 2, 0, 1, 1)
        self.savepicbtn1 = QPushButton(Form2)
        self.savepicbtn1.setObjectName(u"savepicbtn1")
        self.savepicbtn1.setEnabled(False)
        self.gridLayout.addWidget(self.savepicbtn1, 3, 0, 1, 1)
        self.bigpic1btn = QPushButton(Form2)
        self.bigpic1btn.setObjectName(u"bigpic1btn")
        self.bigpic1btn.setEnabled(False)
        self.gridLayout.addWidget(self.bigpic1btn, 4, 0, 1, 1)
        self.choosemusic1btn = QPushButton(Form2)
        self.choosemusic1btn.setObjectName(u"choosemusic1btn")
        self.gridLayout.addWidget(self.choosemusic1btn, 1, 0, 1, 1)
        self.choosedmusic1 = QLabel(Form2)
        self.choosedmusic1.setObjectName(u"choosedmusic1")
        self.choosedmusic1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.choosedmusic1, 0, 0, 1, 1)
        self.intbtn = QPushButton(Form2)
        self.intbtn.setObjectName(u"intbtn")
        self.gridLayout.addWidget(self.intbtn, 5, 0, 1, 1)
        self.retranslateUi(Form2)
        QMetaObject.connectSlotsByName(Form2)
    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", u"\u9891\u8c31\u56fe\uff08Spectogram\uff09", None))
        self.overpic1.setText("")
        self.savepicbtn1.setText(QCoreApplication.translate("Form2", u"\u4fdd\u5b58\u9891\u8c31\u56fe\uff08Spectogram\uff09", None))
        self.bigpic1btn.setText(QCoreApplication.translate("Form2", u"\u653e\u5927\u9891\u8c31\u56fe\uff08Spectogram\uff09", None))
        self.choosemusic1btn.setText(QCoreApplication.translate("Form2", u"\u9009\u62e9\u97f3\u9891", None))
        self.choosedmusic1.setText("")
        self.intbtn.setText(QCoreApplication.translate("Form2", u"\u4ecb\u7ecd\u9891\u8c31\u56fe\uff08Spectogram\uff09", None))