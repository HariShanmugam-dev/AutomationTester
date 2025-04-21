# ///////////////////////////////////////////////////////////////
from PySide6.QtGui import  QIcon
# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from . debug_log import *
from . controls import *


# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False

class ControlFunctions:

    def __init__(self, main_window):
        self.main_window = main_window  # Store MainWindow instance

    def setup_connections(self):
        self.control = Control(self)
        #Explorer connections
        self.ui.addall_btn.clicked.connect(self.control.load_alltestCase)
        self.ui.addTestCase.clicked.connect(self.control.addTestCase)
        self.ui.extraReloadBtn.clicked.connect(self.control.reloadWorkspace)
        #Test Suite Connections
        self.ui.startTesting.clicked.connect(self.control.startTesting)
        self.ui.stopTesting.clicked.connect(self.control.stopTesting)
        self.ui.rerunTesting.clicked.connect(self.control.rerunTesting)
        self.ui.updateTestCase.clicked.connect(self.control.updateTestCase)
        #Home connections
        self.ui.button_closeWorkspace.clicked.connect(self.control.close_workspace)
        self.ui.button_openWorkspace.clicked.connect(self.control.open_workspace)
        self.ui.button_newTestCase.clicked.connect(self.control.new_testCase)
        self.ui.button_loadTestCase.clicked.connect(self.control.load_testCase)
        #Recorder connections
        self.ui.button_recorder.clicked.connect(self.control.start_recorder)
        self.ui.recorder_save.clicked.connect(self.control.save_test_case)
        self.ui.recorder_cancel.clicked.connect(self.control.cancel_recording)

        self.ui.connectPOS.clicked.connect(self.pipes.connectPOS)
        self.ui.disconnectPOS.clicked.connect(self.pipes.disconnectPOS)

    def setHomeButtons(self):
        if self.control.workspacePath: #opened 
            self.ui.button_openWorkspace.setVisible(False)
            self.ui.labelWorkspacePath.setVisible(True)
            self.ui.button_closeWorkspace.setVisible(True)
        else:
            self.ui.button_openWorkspace.setVisible(True)
            self.ui.button_newTestCase.setVisible(True)
            self.ui.labelHome.setVisible(False)
            self.ui.labelWorkspacePath.setVisible(False)
            self.ui.button_closeWorkspace.setVisible(False)

    def setRecButtons(self):
        self.ui.initialFrame.setVisible(True);
        self.ui.finalFrame.setVisible(False);
        self.ui.recorder_restore_widget.setVisible(False);
        
    def setTestSuiteButton(self):
        if self.ui.testSuiteTable.rowCount() > 1:
            self.ui.startTesting.setEnabled(True)
            self.ui.stopTesting.setEnabled(False)
            self.ui.rerunTesting.setEnabled(False)
        else:
            self.ui.startTesting.setEnabled(False)
            self.ui.stopTesting.setEnabled(False)
            self.ui.rerunTesting.setEnabled(False)


    def setSettingsButton(self):
        if self.pipes.is_connected:
            self.ui.connectPOS.setEnabled(True)
            self.ui.disconnectPOS.setEnabled(False)
            self.ui.txtConnectionstatus.setText("Disconnected")
            self.ui.txtConnectionstatus.setStyleSheet("color: red;")
            self.ui.txtlastConnectionTime.setText("N/A")
        else:
            self.ui.connectPOS.setEnabled(False)
            self.ui.disconnectPOS.setEnabled(True)
            self.ui.txtConnectionstatus.setText("Connected")
            self.ui.txtConnectionstatus.setStyleSheet("color: green;")
            self.ui.txtlastConnectionTime.setText("N/A")
