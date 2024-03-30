from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
class Ui_openmvForm(object):
    def setupUi(self, openmvForm):
        if not openmvForm.objectName():
            openmvForm.setObjectName(u"openmvForm")
        openmvForm.resize(400, 300)
        self.gridLayout = QGridLayout(openmvForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MvViewPiclab = QLabel(openmvForm)
        self.MvViewPiclab.setObjectName(u"MvViewPiclab")
        self.MvViewPiclab.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.MvViewPiclab, 0, 0, 1, 1)
        self.MvViewNamelab = QLabel(openmvForm)
        self.MvViewNamelab.setObjectName(u"MvViewNamelab")
        self.MvViewNamelab.setMaximumSize(QSize(16777215, 25))
        self.MvViewNamelab.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.MvViewNamelab, 1, 0, 1, 1)
        self.openMVbtn = QPushButton(openmvForm)
        self.openMVbtn.setObjectName(u"openMVbtn")
        self.openMVbtn.setEnabled(False)
        self.gridLayout.addWidget(self.openMVbtn, 2, 0, 1, 1)
        self.saveMVbtn = QPushButton(openmvForm)
        self.saveMVbtn.setObjectName(u"saveMVbtn")
        self.saveMVbtn.setEnabled(False)
        self.gridLayout.addWidget(self.saveMVbtn, 3, 0, 1, 1)
        self.retranslateUi(openmvForm)
        QMetaObject.connectSlotsByName(openmvForm)
    def retranslateUi(self, openmvForm):
        openmvForm.setWindowTitle(QCoreApplication.translate("openmvForm", u"MV\u5d4c\u5165\u97f3\u51c6\u53c2\u8003", None))
        self.MvViewPiclab.setText("")
        self.MvViewNamelab.setText("")
        self.openMVbtn.setText(QCoreApplication.translate("openmvForm", u"\u6253\u5f00MV\u89c6\u9891", None))
        self.saveMVbtn.setText(QCoreApplication.translate("openmvForm", u"\u4fdd\u5b58MV\u89c6\u9891", None))