
import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
#os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
import ctypes
#ctypes.windll.shcore.SetProcessDpiAwareness(0)

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

#Version Number
# ///////////////////////////////////////////////////////////////
APP_VERSION = "1.0.0"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pipes = AutoTestPipeServer()
        global widgets
        widgets = self.ui

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Automation Tester"
        description = f"Automation Tester V{APP_VERSION}"
        widgets.version.setText(f"v{APP_VERSION}")
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        UIFunctions.enable_windows_snap(self)
        self.recorder_screen_state = False
        self.testsuite_Screen_state = False
        
        # SET signals and slot connections
        # ///////////////////////////////////////////////////////////////
        ControlFunctions.setup_connections(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        #widgets.btn_explorer.clicked.connect(self.buttonClick)
        widgets.btn_testsuite.clicked.connect(self.buttonClick)
        widgets.btn_reports.clicked.connect(self.buttonClick)
        widgets.btn_recorder.clicked.connect(self.buttonClick)
        widgets.btn_edit.clicked.connect(self.buttonClick)
        widgets.btn_settings.clicked.connect(self.buttonClick)
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.btn_explorer.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        ControlFunctions.setHomeButtons(self)

    # BUTTONS CLICK
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        """Handle button clicks and switch pages without reconnecting signals."""
        btn = self.sender()
        btnName = btn.objectName()

        # PAGE SWITCHING LOGIC
        if btnName == "btn_edit":
            widgets.stackedWidget.setCurrentWidget(widgets.edit)

        elif btnName == "btn_recorder":
            widgets.stackedWidget.setCurrentWidget(widgets.recorder)
            ControlFunctions.setRecButtons(self)   # Only update visibility, no signals

        elif btnName == "btn_reports":
            widgets.stackedWidget.setCurrentWidget(widgets.reports)

        elif btnName == "btn_testsuite":
            widgets.stackedWidget.setCurrentWidget(widgets.test_suite)
            ControlFunctions.setTestSuiteButton(self)  # Only update states

        elif btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            ControlFunctions.setHomeButtons(self)
        
        elif btnName == "btn_settings":
            widgets.stackedWidget.setCurrentWidget(widgets.settings)
            ControlFunctions.setSettingsButton(self)
            
        # Update button styles
        UIFunctions.resetStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        """if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')"""



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
