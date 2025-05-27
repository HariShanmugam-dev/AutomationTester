# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recorder.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . icon_rc import *

class Ui_RecorderWindow(object):
    def setupUi(self, RecorderWindow):
        if not RecorderWindow.objectName():
            RecorderWindow.setObjectName(u"RecorderWindow")
        RecorderWindow.resize(258, 322)
        RecorderWindow.setStyleSheet(u"color: #bfe3fe; /* blue-charcoal 200 - light text on dark */\n"
"background-color: #030A13; /* blue-charcoal 950 */")
        self.verticalLayout_2 = QVBoxLayout(RecorderWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_frame = QWidget(RecorderWindow)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 30))
        self.top_frame.setStyleSheet(u"\n"
"QToolButton:hover {\n"
"    background-color:transparent; /* blue-charcoal 700 */\n"
" border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(141, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.rightButtons = QFrame(self.top_frame)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setStyleSheet(u"QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:transparent; /* blue-charcoal 700 */\n"
" border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  transparent;\n"
"     border: 20px solid #0c84bd; /* blue-charcoal 600 */\n"
"}")
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.recorder = QFrame(RecorderWindow)
        self.recorder.setObjectName(u"recorder")
        self.recorder.setAutoFillBackground(False)
        self.recorder.setStyleSheet(u"/*border: none;*/\n"
"\n"
"\n"
"")
        self.vboxLayout = QVBoxLayout(self.recorder)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.recorder)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_grid = QGridLayout()
        self.btn_grid.setSpacing(0)
        self.btn_grid.setObjectName(u"btn_grid")
        self.btn_play = QPushButton(self.widget)
        self.btn_play.setObjectName(u"btn_play")
        self.btn_play.setStyleSheet(u"QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:transparent; /* blue-charcoal 700 */\n"
" border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  transparent;\n"
"     border: 2px solid #0c84bd; /* blue-charcoal 600 */\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_play.setIcon(icon3)
        self.btn_play.setIconSize(QSize(50, 50))

        self.btn_grid.addWidget(self.btn_play, 1, 1, 1, 1)

        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:transparent; /* blue-charcoal 700 */\n"
" border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  transparent;\n"
"     border: 2px solid #0c84bd; /* blue-charcoal 600 */\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon4)
        self.btn_save.setIconSize(QSize(50, 50))

        self.btn_grid.addWidget(self.btn_save, 1, 2, 1, 1)

        self.btn_reset = QPushButton(self.widget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setStyleSheet(u"QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:transparent; /* blue-charcoal 700 */\n"
" border: 1px solid #0c84bd; /* blue-charcoal 600 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  transparent;\n"
"     border: 2px solid #0c84bd; /* blue-charcoal 600 */\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/cil-reload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reset.setIcon(icon5)
        self.btn_reset.setIconSize(QSize(50, 50))

        self.btn_grid.addWidget(self.btn_reset, 1, 0, 1, 1)

        self.btn_start = QPushButton(self.widget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:transparent; /* blue-charcoal 700 */\n"
" border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  transparent;\n"
"     border: 2px solid #0c84bd; /* blue-charcoal 600 */\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/record_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start.setIcon(icon6)
        self.btn_start.setIconSize(QSize(100, 100))

        self.btn_grid.addWidget(self.btn_start, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.btn_grid)

        self.lbl_timer = QLabel(self.widget)
        self.lbl_timer.setObjectName(u"lbl_timer")
        sizePolicy.setHeightForWidth(self.lbl_timer.sizePolicy().hasHeightForWidth())
        self.lbl_timer.setSizePolicy(sizePolicy)
        self.lbl_timer.setMinimumSize(QSize(50, 30))
        self.lbl_timer.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(25)
        font1.setBold(False)
        font1.setItalic(False)
        self.lbl_timer.setFont(font1)
        self.lbl_timer.setTextFormat(Qt.TextFormat.AutoText)
        self.lbl_timer.setScaledContents(False)
        self.lbl_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_timer)

        self.lbl_message = QLabel(self.widget)
        self.lbl_message.setObjectName(u"lbl_message")
        self.lbl_message.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.lbl_message.setFont(font2)
        self.lbl_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_message)


        self.vboxLayout.addWidget(self.widget)


        self.verticalLayout_2.addWidget(self.recorder)

        QWidget.setTabOrder(self.minimizeAppBtn, self.closeAppBtn)

        self.retranslateUi(RecorderWindow)

        QMetaObject.connectSlotsByName(RecorderWindow)
    # setupUi

    def retranslateUi(self, RecorderWindow):
        RecorderWindow.setWindowTitle(QCoreApplication.translate("RecorderWindow", u"Recorder", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("RecorderWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("RecorderWindow", u"Restore", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("RecorderWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.btn_play.setToolTip(QCoreApplication.translate("RecorderWindow", u"Play ", None))
#endif // QT_CONFIG(tooltip)
        self.btn_play.setText("")
#if QT_CONFIG(tooltip)
        self.btn_save.setToolTip(QCoreApplication.translate("RecorderWindow", u"Save test case", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save.setText("")
#if QT_CONFIG(tooltip)
        self.btn_reset.setToolTip(QCoreApplication.translate("RecorderWindow", u"Reset and start over", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset.setText("")
#if QT_CONFIG(tooltip)
        self.btn_start.setToolTip(QCoreApplication.translate("RecorderWindow", u"Start Recording", None))
#endif // QT_CONFIG(tooltip)
        self.btn_start.setText("")
        self.lbl_timer.setText(QCoreApplication.translate("RecorderWindow", u"00:00", None))
        self.lbl_message.setText(QCoreApplication.translate("RecorderWindow", u"Start Recording!", None))
    # retranslateUi

