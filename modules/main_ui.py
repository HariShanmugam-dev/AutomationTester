# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QCommandLinkButton, QFormLayout,
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QScrollBar, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QVBoxLayout, QWidget)
from . icon_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 820)
        MainWindow.setMinimumSize(QSize(600, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"#home{\n"
"background-image:url(:/Icons/home_logo.png);\n"
"background-position: center center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"\n"
"QWidget {\n"
"    color: #bfe3fe; /* blue-charcoal 200 - light text on dark */\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"#filesList{\n"
" background-color: #05151f; /* blue-charcoal 950 */\n"
"   font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QTableWidgetItem:selected {\n"
"    background-color: rgb(191, 227, 254);/* Default background color */\n"
"    color: #05151f; /* Default text color */\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border: 1px solid #0b6999; /* blue-charcoal 700 */\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid #19a4de; /* blue-charcoal 500 */\n"
"    te"
                        "xt-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"#widget_2 .QPushButton {\n"
"    background-color: rgb(191, 227, 254);/* Default background color */\n"
"    color: #05151f; /* Default text color */\n"
"    border: none;\n"
"    border-radius: 12px; /* Set rounded corners */\n"
"    padding: 10px 20px; \n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"    background-color: #05151f; /* blue-charcoal 950 */\n"
"    border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg {\n"
"    background-color: #0d597f; /* blue-charcoal 800 */\n"
"}\n"
"#contentBottom {\n"
"    border-top: 3px solid #0d597f; /* blue-charcoal 800 */\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu "
                        "*/\n"
"#leftMenuBg {\n"
"    background-color: #0d597f; /* blue-charcoal 800 */\n"
"}\n"
"#topLogo {\n"
"	 border-image: url(:/Icons/Icon_logo.png) 0 0 0 0 stretch stretch; /* \u2705 Stretch and fit */\n"
"    background: none;  /* Remove the background-image to avoid conflicts */\n"
"    min-width:40px;   \n"
"    min-height: 40px;\n"
"    max-width: 40px;\n"
"    max-height: 40px;\n"
"}\n"
"#titleLeftApp {\n"
"    font: 12pt \"Segoe UI\";\n"
"}\n"
"#titleLeftDescription {\n"
"    font: 8pt \"Segoe UI\";\n"
"    color: #bfe3fe; /* blue-charcoal 200 */\n"
"}\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #05151f; /* blue-charcoal 950 - darker text for PushButton */\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"    background-color: #0b6999; /* blue-charcoal 70"
                        "0 */\n"
"}\n"
"\n"
"#topMenu .QPushButton:pressed {\n"
"    background-color:  rgb(191, 227, 254);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#pagesContainer .QPushButton {\n"
"    color: #05151f; /* blue-charcoal 950 - darker text for PushButton */\n"
"    text-align: center;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Bottom settings button */\n"
"#bottomMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #05151f; /* blue-charcoal 950 - darker text for PushButton */\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: #0b6999; /* blue-charcoal 700 */\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"    background-color: rgb(189, 147, 249);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar {\n"
"    background-color: #0d597"
                        "f; /* blue-charcoal 800 */\n"
"}\n"
"#bottomBar QLabel {\n"
"    font-size: 11px;\n"
"    color: #bfe3fe; /* blue-charcoal 200 */\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 2px;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: #0b6999; /* blue-charcoal 700 */\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #05151f;\n"
"}\n"
"#toggleButton:hover {\n"
"    background-color: #0b6999; /* blue-charcoal 700 */\n"
"}\n"
"#toggleButton:pressed {\n"
"     background-color: rgb(23, 26, 30);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #05151f; /* blue-charcoal 950 - darker text for PushButton */\n"
"}\n"
"#rightButtons .QPushButton:hover {\n"
"    backg"
                        "round-color: #0b6999; /* blue-charcoal 700 */\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#rightButtons .QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #0b6999; /* blue-charcoal 700 */\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #0c84bd; /* blue-charcoal 600 */\n"
"    min-width: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #0b6999; /* blue-charcoal 700 */\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollB"
                        "ar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #0b6999; /* blue-charcoal 700 */\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #0b6999; /* blue-charcoal 700 */\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #0c84bd; /* blue-charcoal 600 */\n"
"    min-height: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: #0b6999; /* blue-charcoal 700 */\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: "
                        "4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #0b6999; /* blue-charcoal 700 */\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color:rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color:  #0b6999; border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color:rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#extraReloadBtn { background-color:rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#ext"
                        "raReloadBtn:hover { background-color:  #0b6999; border-style: solid; border-radius: 4px; }\n"
"#extraReloadBtn:pressed { background-color:rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"#homeWidget .QLabel{\n"
"font: 20pt \"Segoe UI\";\n"
"}\n"
"#homeWidget .QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    color: #0c84bd; /* blue-charcoal 700 */\n"
"}\n"
"#homeWidget .QPushButton:hover {\n"
"    color: #bfe3fe;\n"
"}\n"
"\n"
"#homeWidget .QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.topLogoInfo)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(40, 40))
        self.topLogo.setMaximumSize(QSize(40, 40))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.topLogo)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/Icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/Icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_explorer = QPushButton(self.topMenu)
        self.btn_explorer.setObjectName(u"btn_explorer")
        sizePolicy.setHeightForWidth(self.btn_explorer.sizePolicy().hasHeightForWidth())
        self.btn_explorer.setSizePolicy(sizePolicy)
        self.btn_explorer.setMinimumSize(QSize(0, 45))
        self.btn_explorer.setFont(font)
        self.btn_explorer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_explorer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_explorer.setStyleSheet(u"background-image: url(:/Icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_explorer)

        self.btn_testsuite = QPushButton(self.topMenu)
        self.btn_testsuite.setObjectName(u"btn_testsuite")
        sizePolicy.setHeightForWidth(self.btn_testsuite.sizePolicy().hasHeightForWidth())
        self.btn_testsuite.setSizePolicy(sizePolicy)
        self.btn_testsuite.setMinimumSize(QSize(0, 45))
        self.btn_testsuite.setFont(font)
        self.btn_testsuite.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_testsuite.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_testsuite.setAutoFillBackground(False)
        self.btn_testsuite.setStyleSheet(u"background-image: url(:/Icons/icon_testtube.png);")
        self.btn_testsuite.setAutoRepeat(False)

        self.verticalLayout_8.addWidget(self.btn_testsuite)

        self.btn_reports = QPushButton(self.topMenu)
        self.btn_reports.setObjectName(u"btn_reports")
        sizePolicy.setHeightForWidth(self.btn_reports.sizePolicy().hasHeightForWidth())
        self.btn_reports.setSizePolicy(sizePolicy)
        self.btn_reports.setMinimumSize(QSize(0, 45))
        self.btn_reports.setFont(font)
        self.btn_reports.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_reports.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_reports.setStyleSheet(u"background-image: url(:/Icons/icon_reports.png);")

        self.verticalLayout_8.addWidget(self.btn_reports)

        self.btn_recorder = QPushButton(self.topMenu)
        self.btn_recorder.setObjectName(u"btn_recorder")
        sizePolicy.setHeightForWidth(self.btn_recorder.sizePolicy().hasHeightForWidth())
        self.btn_recorder.setSizePolicy(sizePolicy)
        self.btn_recorder.setMinimumSize(QSize(0, 45))
        self.btn_recorder.setFont(font)
        self.btn_recorder.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_recorder.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_recorder.setStyleSheet(u"background-image: url(:/Icons/icon_record.png);")

        self.verticalLayout_8.addWidget(self.btn_recorder)

        self.btn_edit = QPushButton(self.topMenu)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy)
        self.btn_edit.setMinimumSize(QSize(0, 45))
        self.btn_edit.setFont(font)
        self.btn_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_edit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_edit.setStyleSheet(u"background-image: url(:/Icons/icon_edit.png);")

        self.verticalLayout_8.addWidget(self.btn_edit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.bottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/Icons/icon_settings.png);")

        self.verticalLayout_7.addWidget(self.btn_settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setStyleSheet(u"color: rgb(191, 227, 254);\n"
"background-color: #030A13;\n"
"\n"
"")
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"background-image: url(:/Icons/cil-file.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"")
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.extraCloseColumnBtn.setStyleSheet(u" QPushButton{ background-color:rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
" QPushButton:hover { background-color:  #0b6999; border-style: solid; border-radius: 4px; }\n"
" QPushButton:pressed { background-color:rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon = QIcon()
        icon.addFile(u":/Icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setMinimumSize(QSize(0, 100))
        self.extraTopMenu.setStyleSheet(u"QListWidget::item {\n"
"    background-color: transparent; /* Make list items transparent by default */\n"
"    padding: 3px; /* Add some padding around list items */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #0b6999; /* Background color when selected */\n"
"    color: white; /* White text when selected */\n"
"    border-radius: 3px; /* Rounded corners like your hover button */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: rgba(255, 255, 255, 10); /* Light overlay on hover */\n"
"}")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.extraTopMenu)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.extraReloadBtn = QPushButton(self.extraTopMenu)
        self.extraReloadBtn.setObjectName(u"extraReloadBtn")
        self.extraReloadBtn.setMinimumSize(QSize(28, 28))
        self.extraReloadBtn.setMaximumSize(QSize(28, 28))
        self.extraReloadBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.extraReloadBtn.setStyleSheet(u" QPushButton{ background-color:rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
" QPushButton:hover { background-color:  #0b6999; border-style: solid; border-radius: 4px; }\n"
" QPushButton:pressed { background-color:rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/cil-reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraReloadBtn.setIcon(icon1)
        self.extraReloadBtn.setIconSize(QSize(20, 20))

        self.gridLayout_11.addWidget(self.extraReloadBtn, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(155, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.addTestCase = QPushButton(self.extraTopMenu)
        self.addTestCase.setObjectName(u"addTestCase")
        self.addTestCase.setMinimumSize(QSize(28, 28))
        self.addTestCase.setMaximumSize(QSize(28, 28))
        self.addTestCase.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addTestCase.setStyleSheet(u" QPushButton{ background-color:rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
" QPushButton:hover { background-color:  #0b6999; border-style: solid; border-radius: 4px; }\n"
" QPushButton:pressed { background-color:rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/cil-plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addTestCase.setIcon(icon2)
        self.addTestCase.setIconSize(QSize(20, 20))

        self.gridLayout_11.addWidget(self.addTestCase, 0, 2, 1, 1)

        self.addall_btn = QPushButton(self.extraTopMenu)
        self.addall_btn.setObjectName(u"addall_btn")
        self.addall_btn.setMaximumSize(QSize(100, 16777215))
        self.addall_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(191, 227, 254);/* Default background color */\n"
"    color: #05151f; /* Default text color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Set rounded corners */\n"
"    padding: 5px 7px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0b6999; /* Hover background color */\n"
"    border-radius: 5px; /* Set rounded corners */\n"
"}")

        self.gridLayout_11.addWidget(self.addall_btn, 0, 3, 1, 1)

        self.filesList = QListWidget(self.extraTopMenu)
        self.filesList.setObjectName(u"filesList")
        self.filesList.setDragEnabled(True)
        self.filesList.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.filesList.setDefaultDropAction(Qt.DropAction.CopyAction)

        self.gridLayout_11.addWidget(self.filesList, 1, 0, 1, 4)


        self.verticalLayout_12.addWidget(self.extraTopMenu)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.home)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_2 = QWidget(self.home)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.formLayout = QFormLayout(self.widget_4)
        self.formLayout.setObjectName(u"formLayout")
        self.labelHome = QLabel(self.widget_4)
        self.labelHome.setObjectName(u"labelHome")
        self.labelHome.setMinimumSize(QSize(0, 0))
        self.labelHome.setMaximumSize(QSize(100, 16777215))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelHome)

        self.labelWorkspacePath = QLabel(self.widget_4)
        self.labelWorkspacePath.setObjectName(u"labelWorkspacePath")
        sizePolicy1.setHeightForWidth(self.labelWorkspacePath.sizePolicy().hasHeightForWidth())
        self.labelWorkspacePath.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.labelWorkspacePath)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(0, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout_6.addWidget(self.widget_4, 0, 0, 1, 1)

        self.homeWidget = QWidget(self.widget_2)
        self.homeWidget.setObjectName(u"homeWidget")
        self.gridLayout_10 = QGridLayout(self.homeWidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.button_openWorkspace = QPushButton(self.homeWidget)
        self.button_openWorkspace.setObjectName(u"button_openWorkspace")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_openWorkspace.setIcon(icon5)

        self.gridLayout_10.addWidget(self.button_openWorkspace, 2, 0, 1, 1)

        self.label_2 = QLabel(self.homeWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_10.addWidget(self.label_2, 6, 0, 1, 1)

        self.button_newTestCase = QPushButton(self.homeWidget)
        self.button_newTestCase.setObjectName(u"button_newTestCase")
        self.button_newTestCase.setIcon(icon2)

        self.gridLayout_10.addWidget(self.button_newTestCase, 3, 0, 1, 1)

        self.button_loadTestCase = QPushButton(self.homeWidget)
        self.button_loadTestCase.setObjectName(u"button_loadTestCase")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/cil-file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_loadTestCase.setIcon(icon6)

        self.gridLayout_10.addWidget(self.button_loadTestCase, 4, 0, 1, 1)

        self.button_closeWorkspace = QPushButton(self.homeWidget)
        self.button_closeWorkspace.setObjectName(u"button_closeWorkspace")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/cil-folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_closeWorkspace.setIcon(icon7)

        self.gridLayout_10.addWidget(self.button_closeWorkspace, 5, 0, 1, 1)

        self.label_7 = QLabel(self.homeWidget)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_7.setFont(font2)

        self.gridLayout_10.addWidget(self.label_7, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.homeWidget, 1, 0, 1, 1)

        self.list_recents = QListView(self.widget_2)
        self.list_recents.setObjectName(u"list_recents")
        self.list_recents.setStyleSheet(u"background: transparent;")

        self.gridLayout_6.addWidget(self.list_recents, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.edit = QWidget()
        self.edit.setObjectName(u"edit")
        self.edit.setStyleSheet(u"background: transparent;")
        self.gridLayout_5 = QGridLayout(self.edit)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.topsection = QGridLayout()
        self.topsection.setObjectName(u"topsection")
        self.label_testcasedesc = QLabel(self.edit)
        self.label_testcasedesc.setObjectName(u"label_testcasedesc")
        self.label_testcasedesc.setMaximumSize(QSize(120, 50))

        self.topsection.addWidget(self.label_testcasedesc, 2, 0, 1, 1)

        self.testcasedesc = QLabel(self.edit)
        self.testcasedesc.setObjectName(u"testcasedesc")

        self.topsection.addWidget(self.testcasedesc, 2, 1, 1, 1)

        self.label_4 = QLabel(self.edit)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topsection.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_testcaseid = QLabel(self.edit)
        self.label_testcaseid.setObjectName(u"label_testcaseid")
        self.label_testcaseid.setMaximumSize(QSize(120, 50))

        self.topsection.addWidget(self.label_testcaseid, 1, 0, 1, 1)

        self.label_5 = QLabel(self.edit)
        self.label_5.setObjectName(u"label_5")

        self.topsection.addWidget(self.label_5, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.topsection, 0, 0, 1, 1)

        self.bodysection = QGridLayout()
        self.bodysection.setObjectName(u"bodysection")
        self.gv_expected = QGraphicsView(self.edit)
        self.gv_expected.setObjectName(u"gv_expected")

        self.bodysection.addWidget(self.gv_expected, 2, 0, 1, 1)

        self.labelexpected = QLabel(self.edit)
        self.labelexpected.setObjectName(u"labelexpected")
        self.labelexpected.setMaximumSize(QSize(16777215, 50))

        self.bodysection.addWidget(self.labelexpected, 0, 0, 1, 1)

        self.gv_actual = QGraphicsView(self.edit)
        self.gv_actual.setObjectName(u"gv_actual")

        self.bodysection.addWidget(self.gv_actual, 2, 1, 1, 1)

        self.labelactual = QLabel(self.edit)
        self.labelactual.setObjectName(u"labelactual")
        self.labelactual.setMaximumSize(QSize(16777215, 50))

        self.bodysection.addWidget(self.labelactual, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.bodysection, 1, 0, 1, 1)

        self.buttonsection = QHBoxLayout()
        self.buttonsection.setObjectName(u"buttonsection")
        self.edit_prevBtn = QPushButton(self.edit)
        self.edit_prevBtn.setObjectName(u"edit_prevBtn")
        self.edit_prevBtn.setMaximumSize(QSize(16777215, 50))
        self.edit_prevBtn.setStyleSheet(u"background-color: rgb(191, 227, 254);")

        self.buttonsection.addWidget(self.edit_prevBtn)

        self.edit_updatebtn = QPushButton(self.edit)
        self.edit_updatebtn.setObjectName(u"edit_updatebtn")
        self.edit_updatebtn.setMaximumSize(QSize(16777215, 50))
        self.edit_updatebtn.setStyleSheet(u"background-color: rgb(191, 227, 254);")

        self.buttonsection.addWidget(self.edit_updatebtn)

        self.edit_cancel = QPushButton(self.edit)
        self.edit_cancel.setObjectName(u"edit_cancel")
        self.edit_cancel.setMaximumSize(QSize(16777215, 50))
        self.edit_cancel.setStyleSheet(u"background-color: rgb(191, 227, 254);")

        self.buttonsection.addWidget(self.edit_cancel)

        self.edit_nextBtn = QPushButton(self.edit)
        self.edit_nextBtn.setObjectName(u"edit_nextBtn")
        self.edit_nextBtn.setMaximumSize(QSize(16777215, 50))
        self.edit_nextBtn.setStyleSheet(u"background-color: rgb(191, 227, 254);")

        self.buttonsection.addWidget(self.edit_nextBtn)


        self.gridLayout_5.addLayout(self.buttonsection, 2, 0, 1, 1)

        self.statussection = QHBoxLayout()
        self.statussection.setObjectName(u"statussection")
        self.labelstatus = QLabel(self.edit)
        self.labelstatus.setObjectName(u"labelstatus")
        self.labelstatus.setMaximumSize(QSize(100, 50))

        self.statussection.addWidget(self.labelstatus)

        self.status = QLabel(self.edit)
        self.status.setObjectName(u"status")

        self.statussection.addWidget(self.status)


        self.gridLayout_5.addLayout(self.statussection, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.edit)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"background: transparent;")
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setGeometry(QRect(10, 10, 298, 112))
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"color: white;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon8)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setGeometry(QRect(10, 132, 765, 150))
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon9)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setGeometry(QRect(10, 292, 818, 288))
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(191, 227, 254, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(191, 227, 254, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.widgets)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"background: transparent;\n"
"")
        self.gridLayout_8 = QGridLayout(self.settings)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_3 = QWidget(self.settings)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(600, 0))
        self.widget_3.setStyleSheet(u"\n"
"QGroupBox {\n"
"    border: 2px solid  #0d597f;\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"}\n"
"QPushButton {\n"
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
"}\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.widget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QSpinBox {\n"
"    background-color: #1c1c1c;\n"
"    border: 1px solid #1D9BF0;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.groupBox_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.title_ConnSettings = QLabel(self.groupBox_3)
        self.title_ConnSettings.setObjectName(u"title_ConnSettings")
        self.title_ConnSettings.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setFamilies([u"13 Segoe UI"])
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        self.title_ConnSettings.setFont(font5)
        self.title_ConnSettings.setStyleSheet(u"font: 15pt Bold \"Segoe UI\";\n"
"color: #0d597f;")

        self.gridLayout_16.addWidget(self.title_ConnSettings, 0, 0, 1, 2)

        self.lbl_connstatus = QLabel(self.groupBox_3)
        self.lbl_connstatus.setObjectName(u"lbl_connstatus")

        self.gridLayout_16.addWidget(self.lbl_connstatus, 1, 0, 1, 1)

        self.txt_connectionstatus = QLabel(self.groupBox_3)
        self.txt_connectionstatus.setObjectName(u"txt_connectionstatus")

        self.gridLayout_16.addWidget(self.txt_connectionstatus, 1, 1, 1, 1)

        self.lbl_lastConnTime = QLabel(self.groupBox_3)
        self.lbl_lastConnTime.setObjectName(u"lbl_lastConnTime")

        self.gridLayout_16.addWidget(self.lbl_lastConnTime, 2, 0, 1, 1)

        self.txt_lastConnectionTime = QLabel(self.groupBox_3)
        self.txt_lastConnectionTime.setObjectName(u"txt_lastConnectionTime")

        self.gridLayout_16.addWidget(self.txt_lastConnectionTime, 2, 1, 1, 1)

        self.connectPOS = QPushButton(self.groupBox_3)
        self.connectPOS.setObjectName(u"connectPOS")
        self.connectPOS.setMinimumSize(QSize(100, 0))
        self.connectPOS.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_16.addWidget(self.connectPOS, 3, 0, 1, 1)

        self.disconnectPOS = QPushButton(self.groupBox_3)
        self.disconnectPOS.setObjectName(u"disconnectPOS")
        self.disconnectPOS.setMinimumSize(QSize(100, 0))
        self.disconnectPOS.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_16.addWidget(self.disconnectPOS, 3, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(332, 38, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QSpinBox {\n"
"    background-color: #1c1c1c;\n"
"    border: 1px solid #1D9BF0;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gridLayout_12 = QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_12.addWidget(self.label_18, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"")
        self.spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinBox.setMaximum(1000)
        self.spinBox.setSingleStep(100)

        self.gridLayout_12.addWidget(self.spinBox, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_12.addWidget(self.label_16, 2, 2, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setFont(font5)
        self.label_17.setStyleSheet(u"font: 15pt Bold \"Segoe UI\";\n"
"color: #0d597f;")

        self.gridLayout_12.addWidget(self.label_17, 0, 0, 1, 3)

        self.saveTimer = QPushButton(self.groupBox_2)
        self.saveTimer.setObjectName(u"saveTimer")
        self.saveTimer.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_12.addWidget(self.saveTimer, 3, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_12.addWidget(self.label_15, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spinBox_2.setMaximum(30)

        self.gridLayout_12.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_12.addWidget(self.label_10, 1, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_2)


        self.gridLayout_8.addWidget(self.widget_3, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.label_13 = QLabel(self.settings)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 100))
        font6 = QFont()
        font6.setFamilies([u"13 Segoe UI"])
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"font: 20pt Bold \"Segoe UI\";")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_13, 1, 1, 1, 2)

        self.stackedWidget.addWidget(self.settings)
        self.recorder = QWidget()
        self.recorder.setObjectName(u"recorder")
        self.recorder.setStyleSheet(u"background: transparent;")
        self.verticalLayout_11 = QVBoxLayout(self.recorder)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.initialFrame = QFrame(self.recorder)
        self.initialFrame.setObjectName(u"initialFrame")
        self.initialFrame.setMaximumSize(QSize(16777215, 0))
        self.initialFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.initialFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.initialFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.recorderScreen = QWidget(self.initialFrame)
        self.recorderScreen.setObjectName(u"recorderScreen")
        self.recorderScreen.setMinimumSize(QSize(375, 0))
        self.recorderScreen.setStyleSheet(u"QLabel{\n"
"color: #bfe3fe; /* blue-charcoal 200 - light text on dark */\n"
"font: 30pt \"Segoe UI\";\n"
"}\n"
"\n"
"\n"
"#recorder_widget .QPushButton {\n"
"    border-image: url(:/Icons/reccorder.png) 0 0 0 0 stretch stretch; /* \u2705 Stretch and fit */\n"
"    background: none;  /* Remove the background-image to avoid conflicts */\n"
"    min-width: 75px;   \n"
"    min-height: 75px;\n"
"    max-width: 75px;\n"
"    max-height: 75px;\n"
"}\n"
"\n"
"#recorder_widget .QPushButton:hover {\n"
"    border-image: url(:/Icons/reccorder_hover.png) 0 0 0 0 stretch stretch; /* \u2705 Stretch hover image */\n"
"}\n"
"\n"
"\n"
"#recorder_restore_widget .QLabel{\n"
"font: 20pt \"Segoe UI\";\n"
"}\n"
"\n"
"#recorder_restore_widget .QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color:#0b6999;\n"
"}\n"
"\n"
"#recorder_restore_widget .QPushButton:pressed {\n"
"    border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"#recorder_restore_widget .QPushButton:hover {\n"
"    color: #0"
                        "c84bd; /* blue-charcoal 700 */\n"
"}\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.recorderScreen)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)

        self.recorder_widget = QWidget(self.recorderScreen)
        self.recorder_widget.setObjectName(u"recorder_widget")
        self.recorder_widget.setFont(font)
        self.recorder_widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.recorder_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.recorder_widget)
        self.label_8.setObjectName(u"label_8")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(30)
        font7.setBold(False)
        font7.setItalic(False)
        self.label_8.setFont(font7)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.button_recorder = QPushButton(self.recorder_widget)
        self.button_recorder.setObjectName(u"button_recorder")
        self.button_recorder.setFont(font)
        self.button_recorder.setStyleSheet(u"")
        self.button_recorder.setIconSize(QSize(75, 75))

        self.gridLayout_4.addWidget(self.button_recorder, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.recorder_widget)

        self.recorder_restore_widget = QWidget(self.recorderScreen)
        self.recorder_restore_widget.setObjectName(u"recorder_restore_widget")
        self.recorder_restore_widget.setStyleSheet(u"")
        self.gridLayout_13 = QGridLayout(self.recorder_restore_widget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.btn_play = QPushButton(self.recorder_restore_widget)
        self.btn_play.setObjectName(u"btn_play")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_play.setIcon(icon10)
        self.btn_play.setIconSize(QSize(50, 50))

        self.gridLayout_13.addWidget(self.btn_play, 2, 1, 1, 1)

        self.btn_save = QPushButton(self.recorder_restore_widget)
        self.btn_save.setObjectName(u"btn_save")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon11)
        self.btn_save.setIconSize(QSize(50, 50))

        self.gridLayout_13.addWidget(self.btn_save, 2, 2, 1, 1)

        self.btn_reset = QPushButton(self.recorder_restore_widget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setIcon(icon1)
        self.btn_reset.setIconSize(QSize(50, 50))

        self.gridLayout_13.addWidget(self.btn_reset, 2, 0, 1, 1)

        self.btn_start = QPushButton(self.recorder_restore_widget)
        self.btn_start.setObjectName(u"btn_start")
        icon12 = QIcon()
        icon12.addFile(u":/Icons/record_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start.setIcon(icon12)
        self.btn_start.setIconSize(QSize(100, 100))

        self.gridLayout_13.addWidget(self.btn_start, 1, 1, 1, 1)

        self.timer = QLabel(self.recorder_restore_widget)
        self.timer.setObjectName(u"timer")
        self.timer.setFont(font2)
        self.timer.setTextFormat(Qt.TextFormat.AutoText)
        self.timer.setScaledContents(False)
        self.timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_13.addWidget(self.timer, 3, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.recorder_restore_widget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.horizontalLayout_7.addWidget(self.recorderScreen)

        self.Instruction = QTextBrowser(self.initialFrame)
        self.Instruction.setObjectName(u"Instruction")

        self.horizontalLayout_7.addWidget(self.Instruction)


        self.verticalLayout_11.addWidget(self.initialFrame)

        self.finalFrame = QFrame(self.recorder)
        self.finalFrame.setObjectName(u"finalFrame")
        self.finalFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.finalFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.finalFrame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.recorder_save = QPushButton(self.finalFrame)
        self.recorder_save.setObjectName(u"recorder_save")
        self.recorder_save.setStyleSheet(u"QPushButton {\n"
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
"    color:  rgb(191, 227, 254);\n"
"}")

        self.gridLayout_9.addWidget(self.recorder_save, 3, 2, 1, 1)

        self.labelDescription = QLabel(self.finalFrame)
        self.labelDescription.setObjectName(u"labelDescription")
        self.labelDescription.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_9.addWidget(self.labelDescription, 0, 0, 1, 1)

        self.description = QLineEdit(self.finalFrame)
        self.description.setObjectName(u"description")
        self.description.setMinimumSize(QSize(0, 30))
        self.description.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_9.addWidget(self.description, 0, 1, 1, 1)

        self.recorder_cancel = QPushButton(self.finalFrame)
        self.recorder_cancel.setObjectName(u"recorder_cancel")
        self.recorder_cancel.setStyleSheet(u"QPushButton {\n"
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
"    color:  rgb(191, 227, 254);\n"
"}")

        self.gridLayout_9.addWidget(self.recorder_cancel, 3, 3, 1, 1)

        self.scrollAreaScreenshots = QScrollArea(self.finalFrame)
        self.scrollAreaScreenshots.setObjectName(u"scrollAreaScreenshots")
        self.scrollAreaScreenshots.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1003, 491))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy3)
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.widget = QWidget(self.scrollAreaWidgetContents_4)
        self.widget.setObjectName(u"widget")

        self.gridLayout_15.addWidget(self.widget, 0, 0, 1, 1)

        self.scrollAreaScreenshots.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_9.addWidget(self.scrollAreaScreenshots, 2, 0, 1, 4)

        self.listView = QListView(self.finalFrame)
        self.listView.setObjectName(u"listView")
        self.listView.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_9.addWidget(self.listView, 1, 0, 1, 4)


        self.verticalLayout_11.addWidget(self.finalFrame)

        self.stackedWidget.addWidget(self.recorder)
        self.reports = QWidget()
        self.reports.setObjectName(u"reports")
        self.reports.setStyleSheet(u"background: transparent;")
        self.gridLayout_3 = QGridLayout(self.reports)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.reports)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.reportsTable = QTableWidget(self.reports)
        if (self.reportsTable.columnCount() < 3):
            self.reportsTable.setColumnCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.reportsTable.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.reportsTable.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.reportsTable.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        if (self.reportsTable.rowCount() < 1):
            self.reportsTable.setRowCount(1)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font4);
        self.reportsTable.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.reportsTable.setItem(0, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.reportsTable.setItem(0, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.reportsTable.setItem(0, 2, __qtablewidgetitem30)
        self.reportsTable.setObjectName(u"reportsTable")
        sizePolicy3.setHeightForWidth(self.reportsTable.sizePolicy().hasHeightForWidth())
        self.reportsTable.setSizePolicy(sizePolicy3)
        self.reportsTable.setMinimumSize(QSize(600, 660))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.reportsTable.setPalette(palette1)
        self.reportsTable.setAcceptDrops(False)
        self.reportsTable.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(191, 227, 254);/* Default background color */\n"
"    color: #05151f; /* Default text color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Set rounded corners */\n"
"    padding: 2px 3px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0b6999; /* Hover background color */\n"
"    border-radius: 5px; /* Set rounded corners */\n"
"}")
        self.reportsTable.setFrameShape(QFrame.Shape.NoFrame)
        self.reportsTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.reportsTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.reportsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.reportsTable.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.reportsTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.reportsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.reportsTable.setShowGrid(True)
        self.reportsTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.reportsTable.setSortingEnabled(False)
        self.reportsTable.setRowCount(1)
        self.reportsTable.horizontalHeader().setVisible(False)
        self.reportsTable.horizontalHeader().setCascadingSectionResizes(True)
        self.reportsTable.horizontalHeader().setDefaultSectionSize(200)
        self.reportsTable.horizontalHeader().setStretchLastSection(False)
        self.reportsTable.verticalHeader().setVisible(False)
        self.reportsTable.verticalHeader().setCascadingSectionResizes(False)
        self.reportsTable.verticalHeader().setHighlightSections(False)
        self.reportsTable.verticalHeader().setProperty(u"showSortIndicator", False)
        self.reportsTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.reportsTable, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(416, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.reports)
        self.test_suite = QWidget()
        self.test_suite.setObjectName(u"test_suite")
        self.test_suite.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.test_suite)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.test_suite)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMaximumSize(QSize(850, 16777215))
        self.frame.setStyleSheet(u"QPushButton {\n"
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
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.startTesting = QPushButton(self.frame)
        self.startTesting.setObjectName(u"startTesting")
        self.startTesting.setEnabled(True)
        self.startTesting.setMaximumSize(QSize(150, 16777215))
        palette2 = QPalette()
        brush9 = QBrush(QColor(5, 21, 31, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        brush10 = QBrush(QColor(5, 21, 31, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        brush11 = QBrush(QColor(198, 217, 235, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        brush12 = QBrush(QColor(0, 0, 0, 92))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.startTesting.setPalette(palette2)
        self.startTesting.setStyleSheet(u"")
        self.startTesting.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.startTesting)

        self.stopTesting = QPushButton(self.frame)
        self.stopTesting.setObjectName(u"stopTesting")
        self.stopTesting.setEnabled(True)
        self.stopTesting.setMaximumSize(QSize(150, 16777215))
        icon13 = QIcon()
        icon13.addFile(u":/Icons/cil-media-stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stopTesting.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.stopTesting)

        self.rerunTesting = QPushButton(self.frame)
        self.rerunTesting.setObjectName(u"rerunTesting")
        self.rerunTesting.setEnabled(True)
        self.rerunTesting.setMaximumSize(QSize(150, 16777215))
        self.rerunTesting.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.rerunTesting)

        self.updateTestCase = QPushButton(self.frame)
        self.updateTestCase.setObjectName(u"updateTestCase")
        self.updateTestCase.setEnabled(False)
        self.updateTestCase.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_6.addWidget(self.updateTestCase)


        self.verticalLayout.addWidget(self.frame)

        self.label = QLabel(self.test_suite)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.test_suite_frame = QFrame(self.test_suite)
        self.test_suite_frame.setObjectName(u"test_suite_frame")
        self.test_suite_frame.setMinimumSize(QSize(0, 150))
        self.test_suite_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.test_suite_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.test_suite_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.testSuiteTable = QTableWidget(self.test_suite_frame)
        if (self.testSuiteTable.columnCount() < 8):
            self.testSuiteTable.setColumnCount(8)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.testSuiteTable.setHorizontalHeaderItem(7, __qtablewidgetitem38)
        if (self.testSuiteTable.rowCount() < 1):
            self.testSuiteTable.setRowCount(1)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font4);
        self.testSuiteTable.setVerticalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.testSuiteTable.setItem(0, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.testSuiteTable.setItem(0, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.testSuiteTable.setItem(0, 2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.testSuiteTable.setItem(0, 3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.testSuiteTable.setItem(0, 4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.testSuiteTable.setItem(0, 5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.testSuiteTable.setItem(0, 6, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.testSuiteTable.setItem(0, 7, __qtablewidgetitem47)
        self.testSuiteTable.setObjectName(u"testSuiteTable")
        sizePolicy3.setHeightForWidth(self.testSuiteTable.sizePolicy().hasHeightForWidth())
        self.testSuiteTable.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.testSuiteTable.setPalette(palette3)
        self.testSuiteTable.setAcceptDrops(False)
        self.testSuiteTable.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(191, 227, 254);/* Default background color */\n"
"    color: #05151f; /* Default text color */\n"
"    border: none;\n"
"    border-radius: 8px; /* Set rounded corners */\n"
"    padding: 2px 3px; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0b6999; /* Hover background color */\n"
"    border-radius: 8px; /* Set rounded corners */\n"
"}\n"
"\n"
"QTableWidgetItem:selected {\n"
"    \n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.testSuiteTable.setFrameShape(QFrame.Shape.NoFrame)
        self.testSuiteTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.testSuiteTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.testSuiteTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.testSuiteTable.setProperty(u"showDropIndicator", False)
        self.testSuiteTable.setDragDropOverwriteMode(False)
        self.testSuiteTable.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.testSuiteTable.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.testSuiteTable.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.testSuiteTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.testSuiteTable.setShowGrid(True)
        self.testSuiteTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.testSuiteTable.setSortingEnabled(False)
        self.testSuiteTable.setRowCount(1)
        self.testSuiteTable.horizontalHeader().setVisible(False)
        self.testSuiteTable.horizontalHeader().setCascadingSectionResizes(True)
        self.testSuiteTable.horizontalHeader().setDefaultSectionSize(200)
        self.testSuiteTable.horizontalHeader().setStretchLastSection(True)
        self.testSuiteTable.verticalHeader().setVisible(False)
        self.testSuiteTable.verticalHeader().setCascadingSectionResizes(False)
        self.testSuiteTable.verticalHeader().setHighlightSections(False)
        self.testSuiteTable.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_13.addWidget(self.testSuiteTable)


        self.verticalLayout.addWidget(self.test_suite_frame)

        self.stackedWidget.addWidget(self.test_suite)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_message = QLabel(self.bottomBar)
        self.label_message.setObjectName(u"label_message")

        self.horizontalLayout_5.addWidget(self.label_message)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_explorer.setText(QCoreApplication.translate("MainWindow", u"Explorer", None))
        self.btn_testsuite.setText(QCoreApplication.translate("MainWindow", u"Test Suite", None))
        self.btn_reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btn_recorder.setText(QCoreApplication.translate("MainWindow", u"Recorder", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Explorer", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
#if QT_CONFIG(tooltip)
        self.extraReloadBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reload", None))
#endif // QT_CONFIG(tooltip)
        self.extraReloadBtn.setText("")
#if QT_CONFIG(tooltip)
        self.addTestCase.setToolTip(QCoreApplication.translate("MainWindow", u"Add selected case", None))
#endif // QT_CONFIG(tooltip)
        self.addTestCase.setText("")
#if QT_CONFIG(tooltip)
        self.addall_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Add all test cases", None))
#endif // QT_CONFIG(tooltip)
        self.addall_btn.setText(QCoreApplication.translate("MainWindow", u"Add All", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Automation Testing", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelHome.setText(QCoreApplication.translate("MainWindow", u"Workspace:", None))
        self.labelWorkspacePath.setText(QCoreApplication.translate("MainWindow", u"workspacepathcd", None))
        self.button_openWorkspace.setText(QCoreApplication.translate("MainWindow", u"Open Workspace", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Recents", None))
        self.button_newTestCase.setText(QCoreApplication.translate("MainWindow", u"New Test Case", None))
        self.button_loadTestCase.setText(QCoreApplication.translate("MainWindow", u"Load Test case", None))
        self.button_closeWorkspace.setText(QCoreApplication.translate("MainWindow", u"Close Workspace", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_testcasedesc.setText(QCoreApplication.translate("MainWindow", u"Test Case Description", None))
        self.testcasedesc.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Test Case Editor", None))
        self.label_testcaseid.setText(QCoreApplication.translate("MainWindow", u"Test Case ID:", None))
        self.label_5.setText("")
        self.labelexpected.setText(QCoreApplication.translate("MainWindow", u"Expected", None))
        self.labelactual.setText(QCoreApplication.translate("MainWindow", u"Actual", None))
        self.edit_prevBtn.setText(QCoreApplication.translate("MainWindow", u"<<Prev", None))
        self.edit_updatebtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.edit_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.edit_nextBtn.setText(QCoreApplication.translate("MainWindow", u"Next >>", None))
        self.labelstatus.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Viewing 2 of 10 screenshots", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.groupBox_3.setTitle("")
        self.title_ConnSettings.setText(QCoreApplication.translate("MainWindow", u"Connection Settings", None))
        self.lbl_connstatus.setText(QCoreApplication.translate("MainWindow", u"Connections Status:", None))
        self.txt_connectionstatus.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.lbl_lastConnTime.setText(QCoreApplication.translate("MainWindow", u"Last Connected:", None))
        self.txt_lastConnectionTime.setText(QCoreApplication.translate("MainWindow", u"4: 03 PM", None))
#if QT_CONFIG(tooltip)
        self.connectPOS.setToolTip(QCoreApplication.translate("MainWindow", u"Connect POS", None))
#endif // QT_CONFIG(tooltip)
        self.connectPOS.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.disconnectPOS.setToolTip(QCoreApplication.translate("MainWindow", u"Disconnect POS", None))
#endif // QT_CONFIG(tooltip)
        self.disconnectPOS.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.groupBox_2.setTitle("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Screenshot timer", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"sec", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Timer Settings", None))
#if QT_CONFIG(tooltip)
        self.saveTimer.setToolTip(QCoreApplication.translate("MainWindow", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.saveTimer.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Testing Timer", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.button_recorder.setToolTip(QCoreApplication.translate("MainWindow", u"Start Recording", None))
#endif // QT_CONFIG(tooltip)
        self.button_recorder.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play.setToolTip(QCoreApplication.translate("MainWindow", u"Play ", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play.setText("")
#if QT_CONFIG(tooltip)
        self.btn_save.setToolTip(QCoreApplication.translate("MainWindow", u"Save test case", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save.setText("")
#if QT_CONFIG(tooltip)
        self.btn_reset.setToolTip(QCoreApplication.translate("MainWindow", u"Reset and start over", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset.setText("")
#if QT_CONFIG(tooltip)
        self.btn_start.setToolTip(QCoreApplication.translate("MainWindow", u"Start Recording", None))
#endif // QT_CONFIG(tooltip)
        self.btn_start.setText("")
        self.timer.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.Instruction.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Instructions for Using the Recorder</span></h3>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Start Recording:</span>\n"
""
                        "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click the <span style=\" font-weight:700;\">red circular button</span> to start recording.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The application will <span style=\" font-weight:700;\">track all mouse clicks and keyboard inputs</span>.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to include <span style=\" font-weight:700;\">barcode scanning</span>, make sure to enable it from the top left of recorder window before starting.</li></ul></li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:70"
                        "0;\">Stop Recording:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The <span style=\" font-weight:700;\">same button</span> turns into a <span style=\" font-weight:700;\">stop button</span> during recording.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click it to <span style=\" font-weight:700;\">stop the recording</span>.</li></ul></li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Playback:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0;"
                        " text-indent:0px;\">Use the <span style=\" font-weight:700;\">play button</span> to <span style=\" font-weight:700;\">review the recorded actions</span>.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This allows you to verify the correctness of the recorded steps.</li></ul></li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Save the Test Case:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Once satisfied with the recording, click the <span style=\" font-weight:700;\">save icon</span>.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This"
                        " will <span style=\" font-weight:700;\">save the recorded test case</span> for future use.</li></ul></li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Reset and Re-record:</span>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you want to start over, click the <span style=\" font-weight:700;\">reset button</span>.</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This will <span style=\" font-weight:700;\">clear the current recording</span> and let you start from scratch.</li></ul></li></ol></body></html>", None))
        self.recorder_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.labelDescription.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.description.setText("")
        self.description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.recorder_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Recent Test Reports", None))
        ___qtablewidgetitem24 = self.reportsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem25 = self.reportsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.reportsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.reportsTable.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.reportsTable.isSortingEnabled()
        self.reportsTable.setSortingEnabled(False)
        ___qtablewidgetitem28 = self.reportsTable.item(0, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"File name", None));
        ___qtablewidgetitem29 = self.reportsTable.item(0, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Generated on", None));
        ___qtablewidgetitem30 = self.reportsTable.item(0, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Edit", None));
        self.reportsTable.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.startTesting.setToolTip(QCoreApplication.translate("MainWindow", u"Start Testing", None))
#endif // QT_CONFIG(tooltip)
        self.startTesting.setText(QCoreApplication.translate("MainWindow", u"Start Testing", None))
#if QT_CONFIG(tooltip)
        self.stopTesting.setToolTip(QCoreApplication.translate("MainWindow", u"Stop Testing", None))
#endif // QT_CONFIG(tooltip)
        self.stopTesting.setText(QCoreApplication.translate("MainWindow", u"Stop Testing", None))
#if QT_CONFIG(tooltip)
        self.rerunTesting.setToolTip(QCoreApplication.translate("MainWindow", u"Rerun all test cases", None))
#endif // QT_CONFIG(tooltip)
        self.rerunTesting.setText(QCoreApplication.translate("MainWindow", u"Rerun Tests", None))
#if QT_CONFIG(tooltip)
        self.updateTestCase.setToolTip(QCoreApplication.translate("MainWindow", u"Update Failed test cases", None))
#endif // QT_CONFIG(tooltip)
        self.updateTestCase.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test Suite", None))
        ___qtablewidgetitem31 = self.testSuiteTable.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem32 = self.testSuiteTable.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem33 = self.testSuiteTable.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem34 = self.testSuiteTable.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem35 = self.testSuiteTable.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem36 = self.testSuiteTable.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem37 = self.testSuiteTable.horizontalHeaderItem(6)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem38 = self.testSuiteTable.horizontalHeaderItem(7)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem39 = self.testSuiteTable.verticalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.testSuiteTable.isSortingEnabled()
        self.testSuiteTable.setSortingEnabled(False)
        ___qtablewidgetitem40 = self.testSuiteTable.item(0, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem41 = self.testSuiteTable.item(0, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem42 = self.testSuiteTable.item(0, 2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Pre-Check", None));
        ___qtablewidgetitem43 = self.testSuiteTable.item(0, 3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        ___qtablewidgetitem44 = self.testSuiteTable.item(0, 4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem45 = self.testSuiteTable.item(0, 5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Tran. Number", None));
        ___qtablewidgetitem46 = self.testSuiteTable.item(0, 6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Time Elapsed", None));
        ___qtablewidgetitem47 = self.testSuiteTable.item(0, 7)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Error Message", None));
        self.testSuiteTable.setSortingEnabled(__sortingEnabled2)

        self.label_message.setText(QCoreApplication.translate("MainWindow", u"Happy Testing!!", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

