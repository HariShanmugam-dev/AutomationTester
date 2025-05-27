
import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
#os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
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
        self.pipes = None
        global widgets
        widgets = self.ui
        self.block_keys = False  # Flag to block key events
        self.debug_log = DebugLogger()

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Automation Tester"
        description = f"Automation Tester V{APP_VERSION}"
        widgets.version.setText(f"v{APP_VERSION}")
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # Print system information
        self.debug_log.write_log(f"System Information:\n"
                                 f"OS: {platform.system()} {platform.release()}\n"
                                    f"Python Version: {platform.python_version()}\n"
                                    f"Architecture: {platform.architecture()[0]}\n"
                                    f"Machine: {platform.machine()}\n"
                                    f"Processor: {platform.processor()}\n")
        self.debug_log.write_log(f"Application Version: {APP_VERSION}\n")
        

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

        widgets.closeAppBtn.clicked.connect(lambda: ControlFunctions.close_application(self))

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        #self.show()

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        ControlFunctions.load_recent_files_to_list(self)
        ControlFunctions.setHomeButtons(self)
        


        """threading.Thread(target=self._monitor_connection,
                         args=(self.pipes,),
                         daemon=True).start()"""

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
            ControlFunctions.load_recent_files_to_list(self)
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
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        """if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')"""

    def open_project(self, file_path):
        """Open the selected project."""
        ControlFunctions.open_project(self,file_path)

    def _monitor_connection(self, server):
        server = AutoTestPipeServer()
        while True:
            status = '🟢 Connected' if server.is_connected() else '🔴 Not connected'
            self.ui.label_message.setText(f"POS Connection Status: {status}")
            print(f"POS connection status: {status}")
            time.sleep(5)

    def handle_cli_args(self, args):
        self.debug_log.write_log(f"CLI arguments received: {args}")
        if args.run_project:
            file_path = args.run_project
            if os.path.exists(file_path):
                self.open_project(file_path)
                ControlFunctions.run_project(self, args)
            else:
                print(f"Error: Project file '{file_path}' does not exist.")
                sys.exit(1)
            

def parse_args():
    parser = argparse.ArgumentParser(description="Automation Tester CLI")
    parser.add_argument("--run-project", type=str, help="Run specified .atest project file")
    parser.add_argument("--cli", action="store_true", help="Run in cli mode")
    parser.add_argument("--output-report", type=str, help="Output report path after test execution")
    parser.add_argument("--with-setup", action="store_true", help="Run setup and cleanup scripts before and after tests")
    args, unknown = parser.parse_known_args()

    # If no known args supplied — means normal GUI launch
    if not any(vars(args).values()):
        print("No CLI arguments supplied — starting in normal GUI mode.")
        return None

    print(f"CLI arguments detected: {args}")
    return args

if __name__ == "__main__":
    args = parse_args()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    window.show()
    if args is not None:
        window.handle_cli_args(args)
    # SHOW APP
    # ///////////////////////////////////////////////////////////////
    #if args is None or not args.headless:
    sys.exit(app.exec_())
