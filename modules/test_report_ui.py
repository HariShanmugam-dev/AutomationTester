# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_report.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
from . icon_rc import *

class Ui_TestReport(object):
    def setupUi(self, TestReport):
        if not TestReport.objectName():
            TestReport.setObjectName(u"TestReport")
        TestReport.resize(510, 296)
        TestReport.setMaximumSize(QSize(600, 300))
        self.gridLayout_3 = QGridLayout(TestReport)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stylesheet = QWidget(TestReport)
        self.stylesheet.setObjectName(u"stylesheet")
        self.stylesheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"    /*background-color: #05151f; /* blue-charcoal 950 */\n"
"    background-color: #030A13;\n"
"    border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg {\n"
"    background-color: #0d597f; /* blue-charcoal 800 */\n"
"}\n"
"\n"
"QWidget {\n"
"    color: #bfe3fe; /* blue-charcoal 200 - light text on dark */\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#tabButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #05151f; /* blue-charcoal 950 - darker text for PushButton */\n"
"}\n"
"#tabButtons .QPushButton:hover {\n"
"    background-color: #0b6999; /* blue-charcoal 700 */\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#tabButtons .QPushButton"
                        ":pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}")
        self.gridLayout = QGridLayout(self.stylesheet)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.stylesheet)
        self.bgApp.setObjectName(u"bgApp")
        self.gridLayout_2 = QGridLayout(self.bgApp)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.bgApp)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.accept = QPushButton(self.widget)
        self.accept.setObjectName(u"accept")
        self.accept.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(191, 227, 254);/* Default background color */\n"
"    color: #05151f; /* Default text color */\n"
"    border: none;\n"
"    border-radius: 12px; /* Set rounded corners */\n"
"    padding: 10px 20px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0b6999; /* Hover background color */\n"
"    border-radius: 12px; /* Set rounded corners */\n"
"}")

        self.gridLayout_4.addWidget(self.accept, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 4, 2, 1, 1)

        self.lbl_reports = QLabel(self.widget)
        self.lbl_reports.setObjectName(u"lbl_reports")
        font = QFont()
        font.setPointSize(15)
        self.lbl_reports.setFont(font)
        self.lbl_reports.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_reports, 3, 0, 1, 3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(550, 200))
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_TestReport = QLabel(self.widget_2)
        self.lbl_TestReport.setObjectName(u"lbl_TestReport")
        self.lbl_TestReport.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_TestReport.sizePolicy().hasHeightForWidth())
        self.lbl_TestReport.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.lbl_TestReport.setFont(font1)
        self.lbl_TestReport.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_TestReport)

        self.lbl_elapsedTime = QLabel(self.widget_2)
        self.lbl_elapsedTime.setObjectName(u"lbl_elapsedTime")
        sizePolicy.setHeightForWidth(self.lbl_elapsedTime.sizePolicy().hasHeightForWidth())
        self.lbl_elapsedTime.setSizePolicy(sizePolicy)
        self.lbl_elapsedTime.setMaximumSize(QSize(150, 16777215))
        self.lbl_elapsedTime.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_elapsedTime)

        self.txt_elapsedTime = QLabel(self.widget_2)
        self.txt_elapsedTime.setObjectName(u"txt_elapsedTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_elapsedTime.sizePolicy().hasHeightForWidth())
        self.txt_elapsedTime.setSizePolicy(sizePolicy1)
        self.txt_elapsedTime.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txt_elapsedTime)

        self.lbl_testFailed = QLabel(self.widget_2)
        self.lbl_testFailed.setObjectName(u"lbl_testFailed")
        self.lbl_testFailed.setMaximumSize(QSize(150, 16777215))
        self.lbl_testFailed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_testFailed)

        self.txt_Failed = QLabel(self.widget_2)
        self.txt_Failed.setObjectName(u"txt_Failed")
        sizePolicy.setHeightForWidth(self.txt_Failed.sizePolicy().hasHeightForWidth())
        self.txt_Failed.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txt_Failed)

        self.lbl_testPassed = QLabel(self.widget_2)
        self.lbl_testPassed.setObjectName(u"lbl_testPassed")
        self.lbl_testPassed.setMaximumSize(QSize(150, 16777215))
        self.lbl_testPassed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_testPassed)

        self.txt_Passed = QLabel(self.widget_2)
        self.txt_Passed.setObjectName(u"txt_Passed")
        sizePolicy.setHeightForWidth(self.txt_Passed.sizePolicy().hasHeightForWidth())
        self.txt_Passed.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txt_Passed)

        self.lbl_testBlocked = QLabel(self.widget_2)
        self.lbl_testBlocked.setObjectName(u"lbl_testBlocked")
        self.lbl_testBlocked.setMaximumSize(QSize(150, 16777215))
        self.lbl_testBlocked.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lbl_testBlocked)

        self.txt_Blocked = QLabel(self.widget_2)
        self.txt_Blocked.setObjectName(u"txt_Blocked")
        sizePolicy.setHeightForWidth(self.txt_Blocked.sizePolicy().hasHeightForWidth())
        self.txt_Blocked.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.txt_Blocked)


        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 2, 3)


        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.bgApp, 1, 0, 1, 1)

        self.contentTopBg = QFrame(self.stylesheet)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.winTtile = QFrame(self.contentTopBg)
        self.winTtile.setObjectName(u"winTtile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.winTtile.sizePolicy().hasHeightForWidth())
        self.winTtile.setSizePolicy(sizePolicy2)
        self.winTtile.setFrameShape(QFrame.Shape.NoFrame)
        self.winTtile.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.winTtile)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.winTtile)
        self.title.setObjectName(u"title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy3)
        self.title.setMaximumSize(QSize(16777215, 45))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.title.setFont(font2)
        self.title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.title)


        self.horizontalLayout_4.addWidget(self.winTtile)

        self.tabButtons = QFrame(self.contentTopBg)
        self.tabButtons.setObjectName(u"tabButtons")
        self.tabButtons.setMinimumSize(QSize(0, 28))
        self.tabButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.tabButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.tabButtons)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.tabButtons)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(28, 28))
        self.minimizeBtn.setMaximumSize(QSize(28, 28))
        self.minimizeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeBtn.setIcon(icon)
        self.minimizeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.closeBtn = QPushButton(self.tabButtons)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(28, 28))
        self.closeBtn.setMaximumSize(QSize(28, 28))
        self.closeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_4.addWidget(self.tabButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.contentTopBg, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.stylesheet, 0, 0, 1, 1)


        self.retranslateUi(TestReport)
        self.minimizeBtn.clicked.connect(TestReport.showMinimized)
        self.closeBtn.clicked.connect(TestReport.close)
        self.accept.clicked.connect(TestReport.close)

        QMetaObject.connectSlotsByName(TestReport)
    # setupUi

    def retranslateUi(self, TestReport):
        TestReport.setWindowTitle(QCoreApplication.translate("TestReport", u"Form", None))
        self.accept.setText(QCoreApplication.translate("TestReport", u"Accept", None))
        self.lbl_reports.setText(QCoreApplication.translate("TestReport", u"Test reports can be accessed on Reports tab", None))
        self.lbl_TestReport.setText(QCoreApplication.translate("TestReport", u"Detailed Test Report", None))
        self.lbl_elapsedTime.setText(QCoreApplication.translate("TestReport", u"Time Elapsed:", None))
        self.txt_elapsedTime.setText(QCoreApplication.translate("TestReport", u"HH:MM:SS", None))
        self.lbl_testFailed.setText(QCoreApplication.translate("TestReport", u"Test cases Failed:", None))
        self.txt_Failed.setText(QCoreApplication.translate("TestReport", u"None", None))
        self.lbl_testPassed.setText(QCoreApplication.translate("TestReport", u"Test cases Passed:", None))
        self.txt_Passed.setText(QCoreApplication.translate("TestReport", u"None", None))
        self.lbl_testBlocked.setText(QCoreApplication.translate("TestReport", u"Test cases Blocked:", None))
        self.txt_Blocked.setText(QCoreApplication.translate("TestReport", u"None", None))
        self.title.setText(QCoreApplication.translate("TestReport", u"Testing Completed", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("TestReport", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("TestReport", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
    # retranslateUi

