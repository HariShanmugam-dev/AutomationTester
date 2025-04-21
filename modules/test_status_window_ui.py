# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_status_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)
import icon_rc

class Ui_TestStatus(object):
    def setupUi(self, TestStatus):
        if not TestStatus.objectName():
            TestStatus.setObjectName(u"TestStatus")
        TestStatus.resize(283, 70)
        TestStatus.setMinimumSize(QSize(283, 70))
        TestStatus.setMaximumSize(QSize(283, 70))
        self.gridLayout = QGridLayout(TestStatus)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stylesheet = QWidget(TestStatus)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"    /*background-color: #05151f; /* blue-charcoal 950 */\n"
"    background-color: #030A13;\n"
"    border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"\n"
"\n"
"QWidget {\n"
"    color: #bfe3fe; /* blue-charcoal 200 - light text on dark */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #0d597f;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #bfe3fe; /* blue-charcoal 950 - darker text for PushButton */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #0b6999; /* blue-charcoal 700 */\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.stylesheet)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.stylesheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.Shape.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.bgApp)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.test_stopBtn = QPushButton(self.bgApp)
        self.test_stopBtn.setObjectName(u"test_stopBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_stopBtn.sizePolicy().hasHeightForWidth())
        self.test_stopBtn.setSizePolicy(sizePolicy)
        self.test_stopBtn.setMaximumSize(QSize(60, 20))
        icon = QIcon()
        icon.addFile(u":/Icons/cil-media-stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.test_stopBtn.setIcon(icon)

        self.gridLayout_2.addWidget(self.test_stopBtn, 0, 0, 1, 1)

        self.test_pauseBtn = QPushButton(self.bgApp)
        self.test_pauseBtn.setObjectName(u"test_pauseBtn")
        self.test_pauseBtn.setMaximumSize(QSize(60, 20))

        self.gridLayout_2.addWidget(self.test_pauseBtn, 0, 1, 1, 1)

        self.test_playBtn = QPushButton(self.bgApp)
        self.test_playBtn.setObjectName(u"test_playBtn")
        self.test_playBtn.setMaximumSize(QSize(60, 20))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.test_playBtn.setIcon(icon1)

        self.gridLayout_2.addWidget(self.test_playBtn, 0, 2, 1, 1)

        self.label = QLabel(self.bgApp)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 3)


        self.gridLayout_3.addWidget(self.bgApp, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.stylesheet, 0, 0, 1, 1)


        self.retranslateUi(TestStatus)

        QMetaObject.connectSlotsByName(TestStatus)
    # setupUi

    def retranslateUi(self, TestStatus):
        TestStatus.setWindowTitle(QCoreApplication.translate("TestStatus", u"Form", None))
        self.test_stopBtn.setText(QCoreApplication.translate("TestStatus", u"Stop", None))
        self.test_pauseBtn.setText(QCoreApplication.translate("TestStatus", u"Pause", None))
        self.test_playBtn.setText(QCoreApplication.translate("TestStatus", u"Play", None))
        self.label.setText(QCoreApplication.translate("TestStatus", u"Testing Calculator .....", None))
    # retranslateUi

