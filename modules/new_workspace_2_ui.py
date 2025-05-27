# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_workspace_2.ui'
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
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)
import icon_rc

class Ui_newWorkspaceWindow(object):
    def setupUi(self, newWorkspaceWindow):
        if not newWorkspaceWindow.objectName():
            newWorkspaceWindow.setObjectName(u"newWorkspaceWindow")
        newWorkspaceWindow.setWindowModality(Qt.WindowModality.WindowModal)
        newWorkspaceWindow.resize(753, 500)
        newWorkspaceWindow.setMinimumSize(QSize(753, 500))
        self.gridLayout_3 = QGridLayout(newWorkspaceWindow)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(newWorkspaceWindow)
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

        self.winTtile = QFrame(self.contentTopBg)
        self.winTtile.setObjectName(u"winTtile")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winTtile.sizePolicy().hasHeightForWidth())
        self.winTtile.setSizePolicy(sizePolicy)
        self.winTtile.setMaximumSize(QSize(16777215, 45))
        self.winTtile.setFrameShape(QFrame.Shape.NoFrame)
        self.winTtile.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.winTtile)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.winTtile)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        self.title.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.title)


        self.gridLayout_2.addWidget(self.winTtile, 0, 0, 1, 1)

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
        self.lbl_testCaseId = QLabel(self.bgApp)
        self.lbl_testCaseId.setObjectName(u"lbl_testCaseId")
        self.lbl_testCaseId.setLineWidth(1)
        self.lbl_testCaseId.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_testCaseId, 0, 0, 1, 1)

        self.txt_projectName = QLineEdit(self.bgApp)
        self.txt_projectName.setObjectName(u"txt_projectName")
        self.txt_projectName.setMinimumSize(QSize(300, 30))
        self.txt_projectName.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_projectName, 0, 1, 1, 2)

        self.lbl_projectlocation = QLabel(self.bgApp)
        self.lbl_projectlocation.setObjectName(u"lbl_projectlocation")
        self.lbl_projectlocation.setLineWidth(1)
        self.lbl_projectlocation.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_projectlocation, 1, 0, 1, 1)

        self.txt_projectLocationPath = QLineEdit(self.bgApp)
        self.txt_projectLocationPath.setObjectName(u"txt_projectLocationPath")
        self.txt_projectLocationPath.setMinimumSize(QSize(400, 30))
        self.txt_projectLocationPath.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_projectLocationPath, 1, 1, 1, 2)

        self.btn_findPath1 = QPushButton(self.bgApp)
        self.btn_findPath1.setObjectName(u"btn_findPath1")
        self.btn_findPath1.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_findPath1.setFont(font1)
        self.btn_findPath1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_findPath1.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: white;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_findPath1.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_findPath1, 1, 3, 1, 1)

        self.lbl_tarAppPath = QLabel(self.bgApp)
        self.lbl_tarAppPath.setObjectName(u"lbl_tarAppPath")
        self.lbl_tarAppPath.setLineWidth(1)
        self.lbl_tarAppPath.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_tarAppPath, 2, 0, 1, 1)

        self.btn_findPath2 = QPushButton(self.bgApp)
        self.btn_findPath2.setObjectName(u"btn_findPath2")
        self.btn_findPath2.setMinimumSize(QSize(150, 30))
        self.btn_findPath2.setFont(font1)
        self.btn_findPath2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_findPath2.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: white;")
        self.btn_findPath2.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_findPath2, 2, 3, 1, 1)

        self.lbl_cmdLineParam = QLabel(self.bgApp)
        self.lbl_cmdLineParam.setObjectName(u"lbl_cmdLineParam")
        self.lbl_cmdLineParam.setLineWidth(1)
        self.lbl_cmdLineParam.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_cmdLineParam, 3, 0, 1, 1)

        self.lbl_reportsPath = QLabel(self.bgApp)
        self.lbl_reportsPath.setObjectName(u"lbl_reportsPath")
        self.lbl_reportsPath.setLineWidth(1)
        self.lbl_reportsPath.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_reportsPath, 4, 0, 1, 1)

        self.btn_findPath3 = QPushButton(self.bgApp)
        self.btn_findPath3.setObjectName(u"btn_findPath3")
        self.btn_findPath3.setMinimumSize(QSize(150, 30))
        self.btn_findPath3.setFont(font1)
        self.btn_findPath3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_findPath3.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: white;")
        self.btn_findPath3.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_findPath3, 4, 3, 1, 1)

        self.lbl_setupscriptPath = QLabel(self.bgApp)
        self.lbl_setupscriptPath.setObjectName(u"lbl_setupscriptPath")
        self.lbl_setupscriptPath.setLineWidth(1)
        self.lbl_setupscriptPath.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_setupscriptPath, 5, 0, 1, 1)

        self.btn_findPath4 = QPushButton(self.bgApp)
        self.btn_findPath4.setObjectName(u"btn_findPath4")
        self.btn_findPath4.setMinimumSize(QSize(150, 30))
        self.btn_findPath4.setFont(font1)
        self.btn_findPath4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_findPath4.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: white;")
        self.btn_findPath4.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_findPath4, 5, 3, 1, 1)

        self.lbl_cleanupscriptPath = QLabel(self.bgApp)
        self.lbl_cleanupscriptPath.setObjectName(u"lbl_cleanupscriptPath")
        self.lbl_cleanupscriptPath.setLineWidth(1)
        self.lbl_cleanupscriptPath.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_cleanupscriptPath, 6, 0, 1, 1)

        self.btn_findPath5 = QPushButton(self.bgApp)
        self.btn_findPath5.setObjectName(u"btn_findPath5")
        self.btn_findPath5.setMinimumSize(QSize(150, 30))
        self.btn_findPath5.setFont(font1)
        self.btn_findPath5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_findPath5.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: white;")
        self.btn_findPath5.setIcon(icon1)

        self.gridLayout.addWidget(self.btn_findPath5, 6, 3, 1, 1)

        self.lbl_screenshotSettings = QLabel(self.bgApp)
        self.lbl_screenshotSettings.setObjectName(u"lbl_screenshotSettings")

        self.gridLayout.addWidget(self.lbl_screenshotSettings, 7, 0, 1, 1)

        self.cb_autoconnect = QCheckBox(self.bgApp)
        self.cb_autoconnect.setObjectName(u"cb_autoconnect")
        self.cb_autoconnect.setAutoFillBackground(False)
        self.cb_autoconnect.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cb_autoconnect, 7, 1, 1, 1)

        self.lbl_screenshotTimer = QLabel(self.bgApp)
        self.lbl_screenshotTimer.setObjectName(u"lbl_screenshotTimer")

        self.gridLayout.addWidget(self.lbl_screenshotTimer, 8, 0, 1, 1)

        self.txt_screenshotTimer = QSpinBox(self.bgApp)
        self.txt_screenshotTimer.setObjectName(u"txt_screenshotTimer")
        self.txt_screenshotTimer.setStyleSheet(u"")
        self.txt_screenshotTimer.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.txt_screenshotTimer.setMaximum(1000)
        self.txt_screenshotTimer.setSingleStep(100)

        self.gridLayout.addWidget(self.txt_screenshotTimer, 8, 1, 1, 1)

        self.lbl_ms = QLabel(self.bgApp)
        self.lbl_ms.setObjectName(u"lbl_ms")

        self.gridLayout.addWidget(self.lbl_ms, 8, 2, 1, 1)

        self.cb_autoload = QCheckBox(self.bgApp)
        self.cb_autoload.setObjectName(u"cb_autoload")
        self.cb_autoload.setAutoFillBackground(False)
        self.cb_autoload.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cb_autoload, 9, 0, 1, 1)

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

        self.gridLayout.addWidget(self.dialogButtons, 10, 3, 1, 1)

        self.txt_targetAppPath = QLineEdit(self.bgApp)
        self.txt_targetAppPath.setObjectName(u"txt_targetAppPath")
        self.txt_targetAppPath.setMinimumSize(QSize(0, 30))
        self.txt_targetAppPath.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_targetAppPath, 2, 1, 1, 2)

        self.txt_cmdLineParams = QLineEdit(self.bgApp)
        self.txt_cmdLineParams.setObjectName(u"txt_cmdLineParams")
        self.txt_cmdLineParams.setMinimumSize(QSize(0, 30))
        self.txt_cmdLineParams.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_cmdLineParams, 3, 1, 1, 3)

        self.txt_reportsPath = QLineEdit(self.bgApp)
        self.txt_reportsPath.setObjectName(u"txt_reportsPath")
        self.txt_reportsPath.setMinimumSize(QSize(0, 30))
        self.txt_reportsPath.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_reportsPath, 4, 1, 1, 2)

        self.txt_setupScriptPath = QLineEdit(self.bgApp)
        self.txt_setupScriptPath.setObjectName(u"txt_setupScriptPath")
        self.txt_setupScriptPath.setMinimumSize(QSize(0, 30))
        self.txt_setupScriptPath.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_setupScriptPath, 5, 1, 1, 2)

        self.txt_cleanupScriptPath = QLineEdit(self.bgApp)
        self.txt_cleanupScriptPath.setObjectName(u"txt_cleanupScriptPath")
        self.txt_cleanupScriptPath.setMinimumSize(QSize(0, 30))
        self.txt_cleanupScriptPath.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.txt_cleanupScriptPath, 6, 1, 1, 2)

        self.errorMessage = QLabel(self.bgApp)
        self.errorMessage.setObjectName(u"errorMessage")

        self.gridLayout.addWidget(self.errorMessage, 10, 0, 1, 3)


        self.verticalLayout.addWidget(self.bgApp)


        self.gridLayout_2.addWidget(self.widget_3, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.contentTopBg, 0, 0, 1, 1)


        self.retranslateUi(newWorkspaceWindow)

        QMetaObject.connectSlotsByName(newWorkspaceWindow)
    # setupUi

    def retranslateUi(self, newWorkspaceWindow):
        newWorkspaceWindow.setWindowTitle(QCoreApplication.translate("newWorkspaceWindow", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("newWorkspaceWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.title.setText(QCoreApplication.translate("newWorkspaceWindow", u"New Workspace", None))
        self.lbl_testCaseId.setText(QCoreApplication.translate("newWorkspaceWindow", u"Workspace Name", None))
        self.txt_projectName.setText("")
        self.txt_projectName.setPlaceholderText(QCoreApplication.translate("newWorkspaceWindow", u"Required", None))
        self.lbl_projectlocation.setText(QCoreApplication.translate("newWorkspaceWindow", u"Location:", None))
        self.txt_projectLocationPath.setText("")
        self.txt_projectLocationPath.setPlaceholderText(QCoreApplication.translate("newWorkspaceWindow", u"Required", None))
        self.btn_findPath1.setText(QCoreApplication.translate("newWorkspaceWindow", u"Browse", None))
        self.lbl_tarAppPath.setText(QCoreApplication.translate("newWorkspaceWindow", u"Target Application Path:", None))
        self.btn_findPath2.setText(QCoreApplication.translate("newWorkspaceWindow", u"Browse", None))
        self.lbl_cmdLineParam.setText(QCoreApplication.translate("newWorkspaceWindow", u"Command Line paramter:", None))
        self.lbl_reportsPath.setText(QCoreApplication.translate("newWorkspaceWindow", u"Reports path:", None))
        self.btn_findPath3.setText(QCoreApplication.translate("newWorkspaceWindow", u"Browse", None))
        self.lbl_setupscriptPath.setText(QCoreApplication.translate("newWorkspaceWindow", u"Setup script path:", None))
        self.btn_findPath4.setText(QCoreApplication.translate("newWorkspaceWindow", u"Browse", None))
        self.lbl_cleanupscriptPath.setText(QCoreApplication.translate("newWorkspaceWindow", u"Clean-up script path:", None))
        self.btn_findPath5.setText(QCoreApplication.translate("newWorkspaceWindow", u"Browse", None))
        self.lbl_screenshotSettings.setText(QCoreApplication.translate("newWorkspaceWindow", u"Screenshot Settings:", None))
        self.cb_autoconnect.setText(QCoreApplication.translate("newWorkspaceWindow", u"Auto Connect POS", None))
        self.lbl_screenshotTimer.setText(QCoreApplication.translate("newWorkspaceWindow", u"Screenshot timer:", None))
#if QT_CONFIG(tooltip)
        self.txt_screenshotTimer.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbl_ms.setText(QCoreApplication.translate("newWorkspaceWindow", u"ms", None))
        self.cb_autoload.setText(QCoreApplication.translate("newWorkspaceWindow", u"Autoload", None))
        self.txt_targetAppPath.setText("")
        self.txt_targetAppPath.setPlaceholderText(QCoreApplication.translate("newWorkspaceWindow", u"Optional", None))
        self.txt_cmdLineParams.setText("")
        self.txt_cmdLineParams.setPlaceholderText(QCoreApplication.translate("newWorkspaceWindow", u"Optional", None))
        self.txt_reportsPath.setText("")
        self.txt_reportsPath.setPlaceholderText(QCoreApplication.translate("newWorkspaceWindow", u"Required", None))
        self.txt_setupScriptPath.setText("")
        self.txt_setupScriptPath.setPlaceholderText(QCoreApplication.translate("newWorkspaceWindow", u"Optional", None))
        self.txt_cleanupScriptPath.setText("")
        self.txt_cleanupScriptPath.setPlaceholderText(QCoreApplication.translate("newWorkspaceWindow", u"Optional", None))
        self.errorMessage.setText(QCoreApplication.translate("newWorkspaceWindow", u"This is a Error message line", None))
    # retranslateUi

