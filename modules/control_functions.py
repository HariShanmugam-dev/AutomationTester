# ///////////////////////////////////////////////////////////////
from PySide6.QtGui import  QIcon
# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from . debug_log import *
from . controls import *
import time

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
        self.ui.deleteTestCase.clicked.connect(self.control.deleteTestCase)
        #Test Suite Connections
        self.ui.startTesting.clicked.connect(self.control.startTesting)
        self.ui.stopTesting.clicked.connect(self.control.stopTesting)
        self.ui.rerunTesting.clicked.connect(self.control.rerunTesting)
        self.ui.updateTestCase.clicked.connect(self.control.updateTestCase)
        #Home connections
        self.ui.button_closeWorkspace.clicked.connect(self.control.close_workspace)
        self.ui.button_openWorkspace.clicked.connect(self.control.open_workspace)
        self.ui.button_newWorkspace.clicked.connect(self.control.new_workspace)
        self.ui.button_newTestCase.clicked.connect(self.control.new_testCase)
        self.ui.button_loadTestCase.clicked.connect(self.control.load_testCase)
        #Recorder connections
        self.ui.button_recorder.clicked.connect(self.control.start_recorder)
        self.ui.recorder_save.clicked.connect(self.control.save_test_case)
        self.ui.recorder_cancel.clicked.connect(self.control.cancel_recording)
        self.ui.btn_save_settings.clicked.connect(self.control.save_settings)

        self.ui.lbl_connection_status.setVisible(False)

        #self.ui.connectPOS.clicked.connect(self.pipes.connectPOS)
        #self.ui.disconnectPOS.clicked.connect(self.pipes.disconnectPOS)

    def setHomeButtons(self):
        if self.control.workspacePath: #opened 
            self.ui.list_recents.clear()
            self.ui.recent_widget.setVisible(False)
            self.ui.button_openWorkspace.setVisible(False)
            self.ui.projectTitle.setText(self.control.workspaceManager.get_workspace_name())
            self.ui.button_closeWorkspace.setVisible(True)
        else:
            self.ui.button_openWorkspace.setVisible(True)
            self.ui.button_newTestCase.setVisible(True)
 
            self.ui.projectTitle.setVisible(False)
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
        self.ui.txt_projectName.setText(self.control.workspaceManager.get_workspace_name())
        self.ui.txt_projectLocationPath.setText(self.control.workspaceManager.get_workspace_path())
        self.ui.txt_projectLocationPath.setEnabled(False)
        self.ui.btn_findPath1.setEnabled(False)
        self.ui.txt_targetAppPath.setText(self.control.workspaceManager.get_target_application_path())
        self.ui.txt_cmdLineParams.setText(self.control.workspaceManager.get_cli_params())
        self.ui.txt_reportsPath.setText(self.control.workspaceManager.get_reports_path())
        self.ui.txt_setupScriptPath.setText(self.control.workspaceManager.get_setup_script_path())
        self.ui.txt_cleanupScriptPath.setText(self.control.workspaceManager.get_cleanup_script_path())
        self.ui.cb_autoconnect.setChecked(self.control.workspaceManager.get_auto_connect())
        self.ui.txt_screenshotTimer.setValue(self.control.workspaceManager.get_ss_timer())
        self.ui.cb_autoload.setChecked(self.control.workspaceManager.get_auto_load())
        self.ui.errorMessage.setVisible(False)

    def load_recent_files_to_list(self):
        """Load recent files from file and add to the QListWidget."""
        self.ui.list_recents.clear()
        self.ui.recent_widget.setVisible(True)

        recent_files = self.debug_log.read_recent_files()
        for file_info in recent_files:
            item_widget = QWidget()
            layout = QVBoxLayout()
            layout.setContentsMargins(5, 5, 5, 5)

            # Project name as clickable label
            project_label = ClickableLabel(f"{file_info['project_name']}")
            project_label.setStyleSheet("color: #0c84bd; font-size: 16px;")
            project_label.setCursor(Qt.PointingHandCursor)

            # Connect label click to open_project with file_path
            file_path = file_info['file_path']
            project_label.clicked.connect(lambda p=file_path: self.open_project(p))

            # Path as non-clickable label
            path_label = QLabel(f"{file_info['file_path']}")
            path_label.setStyleSheet("color: gray;font-size: 12px;")

            layout.addWidget(project_label)
            layout.addWidget(path_label)

            item_widget.setLayout(layout)

            list_item = QListWidgetItem()
            list_item.setSizeHint(item_widget.sizeHint())
            self.ui.list_recents.addItem(list_item)
            self.ui.list_recents.setItemWidget(list_item, item_widget)

    def open_project(self, file_path):
        """Open the selected project."""
        if self.control.open_workspace(file_path):
            self.ui.button_closeWorkspace.setVisible(True)
            self.ui.list_recents.clear()
            self.ui.recent_widget.setVisible(False)
            self.ui.button_openWorkspace.setVisible(False)
            self.ui.button_newTestCase.setVisible(True)
        else:
            ControlFunctions.load_recent_files_to_list(self)

    def close_application(self):
        # Close the application and perform any necessary cleanup.
        self.control.cleanup_application()
        self.close()
        
    def run_project(self, args):
        while True:
            if args.with_setup:
                if not self.control.run_setup_script():
                    break
            if args.output_report:
                self.control.set_html_reports_path(args.output_report)
            if args.run_project:
                self.control.startTesting(args.cli)
                break


class ClickableLabel(QLabel):
    clicked = Signal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()