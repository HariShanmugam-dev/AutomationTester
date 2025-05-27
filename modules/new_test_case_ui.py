# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_test_case.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
from . icon_rc import *

class Ui_newTestCaseWindow(object):
    def setupUi(self, newTestCaseWindow):
        if not newTestCaseWindow.objectName():
            newTestCaseWindow.setObjectName(u"newTestCaseWindow")
        newTestCaseWindow.resize(658, 500)
        newTestCaseWindow.setMinimumSize(QSize(658, 500))
        newTestCaseWindow.setMaximumSize(QSize(658, 500))
        self.gridLayout_3 = QGridLayout(newTestCaseWindow)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(newTestCaseWindow)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setStyleSheet(u"#contentTopBg {\n"
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
"#tabButtons .QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    border: 1px solid  #bfe3fe;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 1px solid #0b6999;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 10px solid #0b6999;\n"
"	bor"
                        "der: 1px solid #0b6999;	\n"
"	background-image: url(:/Icons/cil-check-alt.png);\n"
"}")
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.contentTopBg)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabButtons = QFrame(self.contentTopBg)
        self.tabButtons.setObjectName(u"tabButtons")
        self.tabButtons.setMinimumSize(QSize(0, 28))
        self.tabButtons.setMaximumSize(QSize(16777215, 45))
        self.tabButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.tabButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.tabButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeBtn = QPushButton(self.tabButtons)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(28, 28))
        self.closeBtn.setMaximumSize(QSize(28, 28))
        self.closeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon)
        self.closeBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.closeBtn)


        self.gridLayout_2.addWidget(self.tabButtons, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.contentTopBg)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"background-color: #05151f; /* blue-charcoal 950 */\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.bgApp = QFrame(self.widget_3)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"background-color: transparent;")
        self.bgApp.setFrameShape(QFrame.Shape.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.bgApp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_priority = QComboBox(self.bgApp)
        self.cb_priority.addItem("")
        self.cb_priority.addItem("")
        self.cb_priority.addItem("")
        self.cb_priority.setObjectName(u"cb_priority")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.cb_priority.setFont(font)
        self.cb_priority.setAutoFillBackground(False)
        self.cb_priority.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_priority.setIconSize(QSize(16, 16))
        self.cb_priority.setFrame(True)

        self.gridLayout.addWidget(self.cb_priority, 6, 1, 1, 1)

        self.txt_testCaseId = QLineEdit(self.bgApp)
        self.txt_testCaseId.setObjectName(u"txt_testCaseId")
        self.txt_testCaseId.setMinimumSize(QSize(300, 30))
        self.txt_testCaseId.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_testCaseId, 0, 1, 1, 2)

        self.txt_screenshotTimer = QSpinBox(self.bgApp)
        self.txt_screenshotTimer.setObjectName(u"txt_screenshotTimer")
        self.txt_screenshotTimer.setStyleSheet(u"")
        self.txt_screenshotTimer.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.txt_screenshotTimer.setMaximum(1000)
        self.txt_screenshotTimer.setSingleStep(100)

        self.gridLayout.addWidget(self.txt_screenshotTimer, 5, 1, 1, 1)

        self.lbl_description = QLabel(self.bgApp)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setLineWidth(1)
        self.lbl_description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_description, 1, 0, 1, 1)

        self.btn_findPath = QPushButton(self.bgApp)
        self.btn_findPath.setObjectName(u"btn_findPath")
        self.btn_findPath.setMinimumSize(QSize(150, 30))
        self.btn_findPath.setFont(font)
        self.btn_findPath.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_findPath.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_findPath.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_findPath, 2, 3, 1, 1)

        self.lbl_screenshotTimer = QLabel(self.bgApp)
        self.lbl_screenshotTimer.setObjectName(u"lbl_screenshotTimer")

        self.gridLayout.addWidget(self.lbl_screenshotTimer, 5, 0, 1, 1)

        self.lbl_priority = QLabel(self.bgApp)
        self.lbl_priority.setObjectName(u"lbl_priority")

        self.gridLayout.addWidget(self.lbl_priority, 6, 0, 1, 1)

        self.lbl_cmdLineParam = QLabel(self.bgApp)
        self.lbl_cmdLineParam.setObjectName(u"lbl_cmdLineParam")
        self.lbl_cmdLineParam.setLineWidth(1)
        self.lbl_cmdLineParam.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_cmdLineParam, 3, 0, 1, 1)

        self.cb_autoConnect = QCheckBox(self.bgApp)
        self.cb_autoConnect.setObjectName(u"cb_autoConnect")
        self.cb_autoConnect.setAutoFillBackground(False)
        self.cb_autoConnect.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cb_autoConnect, 4, 0, 1, 1)

        self.lbl_ms = QLabel(self.bgApp)
        self.lbl_ms.setObjectName(u"lbl_ms")

        self.gridLayout.addWidget(self.lbl_ms, 5, 2, 1, 1)

        self.lbl_testCaseId = QLabel(self.bgApp)
        self.lbl_testCaseId.setObjectName(u"lbl_testCaseId")
        self.lbl_testCaseId.setLineWidth(1)
        self.lbl_testCaseId.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_testCaseId, 0, 0, 1, 1)

        self.lbl_tarAppPath = QLabel(self.bgApp)
        self.lbl_tarAppPath.setObjectName(u"lbl_tarAppPath")
        self.lbl_tarAppPath.setLineWidth(1)
        self.lbl_tarAppPath.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_tarAppPath, 2, 0, 1, 1)

        self.txt_description = QLineEdit(self.bgApp)
        self.txt_description.setObjectName(u"txt_description")
        self.txt_description.setMinimumSize(QSize(0, 30))
        self.txt_description.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_description, 1, 1, 1, 2)

        self.txt_targetAppPath = QLineEdit(self.bgApp)
        self.txt_targetAppPath.setObjectName(u"txt_targetAppPath")
        self.txt_targetAppPath.setMinimumSize(QSize(0, 30))
        self.txt_targetAppPath.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_targetAppPath, 2, 1, 1, 2)

        self.txt_cmdLineParams = QLineEdit(self.bgApp)
        self.txt_cmdLineParams.setObjectName(u"txt_cmdLineParams")
        self.txt_cmdLineParams.setMinimumSize(QSize(0, 30))
        self.txt_cmdLineParams.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_cmdLineParams, 3, 1, 1, 2)

        self.dialogButtons = QDialogButtonBox(self.bgApp)
        self.dialogButtons.setObjectName(u"dialogButtons")
        self.dialogButtons.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(191, 227, 254); /* Default background color */\n"
"    color: #05151f; /* Default text color */\n"
"    border: none;\n"
"    border-radius: 12px; /* Rounded corners */\n"
"    padding: 5px 10px; /* More padding for a modern look */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0b6999; /* Hover background color */\n"
"    color: rgb(191, 227, 254);\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #094f73; /* Darker blue for pressed state */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #c6d9eb; /* Lighter greyed-out background */\n"
"    color: #7aa9d6; /* Dimmed text color */\n"
"    border: none;\n"
"    opacity: 0.6;\n"
"}")
        self.dialogButtons.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.dialogButtons, 8, 3, 1, 1)

        self.errorMessage = QLabel(self.bgApp)
        self.errorMessage.setObjectName(u"errorMessage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorMessage.sizePolicy().hasHeightForWidth())
        self.errorMessage.setSizePolicy(sizePolicy)
        self.errorMessage.setWordWrap(True)

        self.gridLayout.addWidget(self.errorMessage, 8, 0, 1, 3)


        self.verticalLayout.addWidget(self.bgApp)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 2)

        self.winTtile = QFrame(self.contentTopBg)
        self.winTtile.setObjectName(u"winTtile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.winTtile.sizePolicy().hasHeightForWidth())
        self.winTtile.setSizePolicy(sizePolicy1)
        self.winTtile.setMaximumSize(QSize(16777215, 45))
        self.winTtile.setFrameShape(QFrame.Shape.NoFrame)
        self.winTtile.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.winTtile)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.winTtile)
        self.title.setObjectName(u"title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy2)
        self.title.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.title.setFont(font1)
        self.title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.title)


        self.gridLayout_2.addWidget(self.winTtile, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.contentTopBg, 0, 0, 1, 1)


        self.retranslateUi(newTestCaseWindow)

        QMetaObject.connectSlotsByName(newTestCaseWindow)
    # setupUi

    def retranslateUi(self, newTestCaseWindow):
        newTestCaseWindow.setWindowTitle(QCoreApplication.translate("newTestCaseWindow", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("newTestCaseWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.cb_priority.setItemText(0, QCoreApplication.translate("newTestCaseWindow", u"LOW", None))
        self.cb_priority.setItemText(1, QCoreApplication.translate("newTestCaseWindow", u"MED", None))
        self.cb_priority.setItemText(2, QCoreApplication.translate("newTestCaseWindow", u"HIGH", None))

        self.txt_testCaseId.setText("")
        self.txt_testCaseId.setPlaceholderText(QCoreApplication.translate("newTestCaseWindow", u"Type here", None))
#if QT_CONFIG(tooltip)
        self.txt_screenshotTimer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_description.setText(QCoreApplication.translate("newTestCaseWindow", u"Description:", None))
        self.btn_findPath.setText(QCoreApplication.translate("newTestCaseWindow", u"Browse", None))
        self.lbl_screenshotTimer.setText(QCoreApplication.translate("newTestCaseWindow", u"Screenshot timer:", None))
        self.lbl_priority.setText(QCoreApplication.translate("newTestCaseWindow", u"Priority:", None))
        self.lbl_cmdLineParam.setText(QCoreApplication.translate("newTestCaseWindow", u"Command Line paramters:", None))
        self.cb_autoConnect.setText(QCoreApplication.translate("newTestCaseWindow", u"Auto Connect POS", None))
        self.lbl_ms.setText(QCoreApplication.translate("newTestCaseWindow", u"ms", None))
        self.lbl_testCaseId.setText(QCoreApplication.translate("newTestCaseWindow", u"Test Case ID:", None))
        self.lbl_tarAppPath.setText(QCoreApplication.translate("newTestCaseWindow", u"Target Application Path:", None))
        self.txt_description.setText("")
        self.txt_description.setPlaceholderText(QCoreApplication.translate("newTestCaseWindow", u"Type here", None))
        self.txt_targetAppPath.setText("")
        self.txt_targetAppPath.setPlaceholderText(QCoreApplication.translate("newTestCaseWindow", u"Type here", None))
        self.txt_cmdLineParams.setText("")
        self.txt_cmdLineParams.setPlaceholderText(QCoreApplication.translate("newTestCaseWindow", u"Type here", None))
        self.errorMessage.setText(QCoreApplication.translate("newTestCaseWindow", u"This is a Error message line", None))
        self.title.setText(QCoreApplication.translate("newTestCaseWindow", u"New Test Case", None))
    # retranslateUi

