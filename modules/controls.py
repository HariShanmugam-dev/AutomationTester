from main import *
from . debug_log import *
from . test_case import TestCaseManager, TestCase,WorkspaceManager, TestCaseConfig
from . recorder import *
from PySide6 import QtWidgets as qtw
from textwrap import dedent
import webbrowser
from . testing_functions import *
from . report_functions import *

from threading import Thread
import time
import threading
import subprocess
from PIL.ImageQt import ImageQt
from PIL import Image
from pathlib import Path

def get_test_case_id():
    return datetime.today().strftime('%Y%m%d%H%M')

class Control(QObject):

    generate_report = Signal()
    def __init__(self, MainWindow):
        super().__init__()
        self.debug_log = DebugLogger()
        self.workspacePath = ""
        self.test_manager = TestCaseManager()
        self.workspaceManager = WorkspaceManager()
        self.new_workspace_window = None
        self.Main = MainWindow
        self.recorder = None
        self.pipes = AutoTestPipeServer()
        self.cli_active = False

        self.control_definitions()
        self.validation_failed_img = {}
        self.disable_control_buttons()
        self.connection_stop_flag = threading.Event()
        self.html_report_path = ""

    def get_workspace(self):
        if self.workspacePath:
             return self.workspacePath
        else:
            m = dedent("Workspace not found. Please first select a workspace.")
            QMessageBox.critical(self.Main, "Error", str(m))
            self.open_workspace()
            return None
         
    def set_workspace(self, path,reset = False):
        if (path == "" and reset) or os.path.exists(path):
            self.workspacePath = path
            self.Main.ui.projectTitle.setText(self.workspaceManager.get_workspace_name())
            self.Main.ui.projectTitle.setVisible(True)
            self.Main.ui.button_closeWorkspace.setVisible(True)
            self.Main.ui.button_newWorkspace.setVisible(False)
            self.Main.ui.button_openWorkspace.setVisible(False)
            self.enable_control_buttons()
            self.Main.ui.recent_widget.setVisible(False)
            return True
        return False
         
    def disable_control_buttons(self):
        self.Main.ui.btn_explorer.setVisible(False)
        self.Main.ui.btn_recorder.setVisible(False)
        self.Main.ui.btn_testsuite.setVisible(False)
        self.Main.ui.btn_reports.setVisible(False)
        self.Main.ui.btn_settings.setVisible(False)

    def enable_control_buttons(self):
        self.Main.ui.btn_explorer.setVisible(True)
        self.Main.ui.btn_recorder.setVisible(True)
        self.Main.ui.btn_testsuite.setVisible(True)
        self.Main.ui.btn_reports.setVisible(True)
        self.Main.ui.btn_settings.setVisible(True)

    def new_workspace(self):
        self.debug_log.write_log("clicked new_project()")
        self.new_workspace_window = NewWorkspaceWindow(self.workspaceManager,self.Main)
        self.new_workspace_window.workspace_created.connect(self.set_workspace)
        self.new_workspace_window.show()

    def open_workspace(self,filepath = ""):
        try:
            self.debug_log.write_log("clicked Open_workspace()")
            self.new_workspace_window = NewWorkspaceWindow(self.workspaceManager,self.Main)
            if self.new_workspace_window.open_workspace(filepath):
                if self.set_workspace(self.workspaceManager.get_workspace_path()):
                    for tc_config in self.workspaceManager.testCases:
                        pathname = os.path.join(self.get_workspace()+"/testcases",f"{tc_config.test_case_id}.json")
                        testcaseFileHandler = TestCase(tc_config)
                        testcaseFileHandler.load_test_case(pathname)
                        test_case_id = self.test_manager.add_test_case(testcaseFileHandler)
                        if test_case_id:
                            self.update_explorer(test_case_id)
                    self.debug_log.write_log(f"Workpace set: {self.get_workspace()}")
                    self.fetch_reports()
    
                    if self.workspaceManager.get_auto_load():
                        self.Main.ui.addall_btn.click()
                    if self.workspaceManager.get_auto_connect():
                        self.Main.ui.lbl_connection_status.setVisible(True)
                        self.connect_application()
                    return True
                else:
                    self.debug_log.write_log("Workpace Not set/ Not found")
                    QMessageBox.critical(self, "Error", "Workspace file not found.")
                    self.debug_log.delete_recent_file(filepath)
            return False
        except Exception as e:
                self.debug_log.write_log(str(e))
                m = dedent("Unkown error occured while Opening workspace. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))

    def update_explorer(self, test_case_id):
        try:
            test_case = self.test_manager.get_test_case(test_case_id)
            if test_case:
                item = QListWidgetItem(QIcon(u":/Icons/cil-file.png"), test_case.description)
                item = self.Main.ui.filesList.addItem(item)
                # Store ID as internal data
                self.Main.ui.filesList.item(self.Main.ui.filesList.count() - 1).setData(Qt.UserRole, test_case.test_case_id)
        except Exception as e:
                self.debug_log.write_log(str(e))
                m = dedent("Unkown error occured while loading script. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))
    def close_workspace(self):
        try:
            self.set_workspace("",True) #reset
            self.disable_control_buttons()
            self.workspaceManager.clear()
            self.Main.ui.projectTitle.setText("")
            self.Main.ui.projectTitle.setVisible(False)
            self.Main.ui.button_closeWorkspace.setVisible(False)
            self.Main.ui.button_newTestCase.setVisible(True)
            self.Main.ui.button_openWorkspace.setVisible(True)
            self.Main.ui.button_newWorkspace.setVisible(True)
            self.test_manager = TestCaseManager()
            self.Main.ui.filesList.clear()
            row_count = self.Main.ui.reportsTable.rowCount()

            # Remove all rows except the header
            for row in range(row_count - 1, 0, -1):
                self.Main.ui.reportsTable.removeRow(row)
            row_count = self.Main.ui.testSuiteTable.rowCount()

            # Remove all rows except the header
            for row in range(row_count - 1, 0, -1):
                self.Main.ui.testSuiteTable.removeRow(row)
            self.debug_log.write_log("clicked close_workspace()")
            self.testsuite_Screen_state = False
            self.Main.ui.btn_home.click()
            self.Main.ui.lbl_connection_status.setVisible(False)
        except Exception as e:
                self.debug_log.write_log(str(e))
                m = dedent("Unkown error occured while closing workspace. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))
    def new_testCase(self):
         self.Main.ui.btn_recorder.click()
    def load_testCase(self):
        self.debug_log.write_log("clicked action_load_script")
        workspacepath = self.get_workspace()
        if workspacepath:
            try:
                file_path, _ = QFileDialog.getOpenFileName(None,"Select JSON File",filter="JSON Files (*.json)")
                if file_path != "" and file_path.endswith(".json"):

                    pathname = os.path.join(workspacepath,"testcases")
                    tmp_filepath = os.path.join(pathname,os.path.basename(file_path))
                    if(not os.path.exists(tmp_filepath)):
                        shutil.copy2(file_path, pathname)
                    else:
                        m = dedent("Test Case already exists in the workspace.")
                        QMessageBox.critical(self.Main, "Error", str(m))
                        self.debug_log.write_log(str(m))
                        return
                    
                    tc_config = TestCaseConfig("",
                                            "",
                                            self.workspaceManager.get_target_application_path(),
                                            self.workspaceManager.get_cli_params(),
                                            self.workspaceManager.get_ss_timer(),
                                            self.workspaceManager.get_auto_connect(),
                                            0,
                                            self.workspaceManager.get_assets_path(),
                                            None)
                    testcaseFileHandler = TestCase(tc_config, [])
                    testcaseFileHandler.load_test_case(tmp_filepath)

                    # Copy assets to the workspace
                    assetpath = testcaseFileHandler.asset_path
                    for asset in testcaseFileHandler.asset_ids:
                        filepath = os.path.join(assetpath, asset)
                        if os.path.exists(filepath):
                            shutil.copy2(filepath, self.workspaceManager.get_assets_path())

                    test_case_id = self.test_manager.add_test_case(testcaseFileHandler)
                    if test_case_id:
                        self.update_explorer(test_case_id)
                        tc_config.test_case_id = test_case_id
                        tc_config.description = testcaseFileHandler.description
                        tc_config.priority = testcaseFileHandler.priority
                        tc_config.asset_ids = testcaseFileHandler.asset_ids
                        self.workspaceManager.add_test_case(tc_config)
                        self.workspaceManager.update_to_file()
            except Exception as e:
                self.debug_log.write_log(str(e))
                m = dedent("Unkown error occured while loading script. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))
    
    def load_alltestCase(self):
        if self.Main.ui.filesList.count() > 0:
            for i in range(self.Main.ui.filesList.count()):
                item = self.Main.ui.filesList.item(i)
                test_case_id = item.data(Qt.UserRole)
                test_case = self.test_manager.get_test_case(test_case_id)
                self.populate_test_suite_table(test_case,test_case_id)
            self.Main.ui.startTesting.setEnabled(True)
            self.Main.ui.stopTesting.setEnabled(False)
            self.Main.ui.rerunTesting.setEnabled(False)
        else:
            QMessageBox.critical(self.Main, "Error", "No test cases found in the workspace")

    def addTestCase(self):
        item = self.Main.ui.filesList.currentItem()
        if item:
            test_case_id = item.data(Qt.UserRole)
            if test_case_id is not None:
                test_case = self.test_manager.get_test_case(test_case_id)
                self.populate_test_suite_table(test_case,test_case_id)
        else:
            QMessageBox.critical(self.Main, "Error", "Please select a test case to load")
        self.Main.ui.startTesting.setEnabled(True)
        self.Main.ui.stopTesting.setEnabled(False)
        self.Main.ui.rerunTesting.setEnabled(False)

    def deleteTestCase(self):
        try:
            item = self.Main.ui.filesList.currentItem()
            if item:
                # Confirm before deletion
                reply = QMessageBox.question(
                    self.Main,
                    "Delete Test Case",
                    "Are you sure you want to delete this test case?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.No
                )

                if reply == QMessageBox.Yes:
                    test_case_id = item.data(Qt.UserRole)
                    if test_case_id is not None:
                        success,message = self.workspaceManager.delete_test_case(test_case_id)
                        if success:
                            self.Main.ui.filesList.takeItem(self.Main.ui.filesList.row(item))
                            row = self.find_row_by_test_case_id(test_case_id)
                            if row != -1:
                                self.offload_test_case(row, test_case_id)
                            self.debug_log.write_log(f"Test case {test_case_id} deleted successfully.")
                        if message:
                            QMessageBox.critical(self.Main, "Error", message)
                            return
            else:
                QMessageBox.critical(self.Main, "Error", "Please select a test case to delete")
        except Exception as e:
            self.debug_log.write_log(str(e))
            m = dedent("Unkown error occured while deleting test case. Please try again.")
            QMessageBox.critical(self.Main, "Error", str(m))

        
    def find_row_by_test_case_id(self, test_case_id):
        """Finds the row index for a given test_case_id."""
        for row in range(self.Main.ui.testSuiteTable.rowCount()):
            item = self.Main.ui.testSuiteTable.item(row, 0)
            if item and item.text() == test_case_id:
                return row
        return -1
    def populate_test_suite_table(self, TestCase, test_case_id = 0):
        """Parses and populates the table with test cases from the recorder."""
        if not test_case_id:
            test_case_id = self.test_manager.add_test_case(TestCase)
        
        if self.find_row_by_test_case_id(test_case_id) != -1:
            print("Test already added")
            return 
        
        self.test_manager.load_test_case(test_case_id, True)

        test_case = self.test_manager.get_test_case(test_case_id)

        row_count = self.Main.ui.testSuiteTable.rowCount()
        self.Main.ui.testSuiteTable.insertRow(row_count)

        self.Main.ui.testSuiteTable.setItem(row_count, 0, qtw.QTableWidgetItem(str(test_case_id)))

        # Description as text, but clickable
        description_item = qtw.QTableWidgetItem(test_case.description)
        description_item.setFlags(description_item.flags() | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)  # Make it selectable and enabled
        self.Main.ui.testSuiteTable.setItem(row_count, 1, description_item)


        # Status Column
        status_item = qtw.QTableWidgetItem(test_case.status)
        self.Main.ui.testSuiteTable.setItem(row_count, 4, status_item)

        delete_button = qtw.QPushButton("Remove")
        #delete_button.setIcon(QIcon("Icon\\delete.png"))
        delete_button.setToolTip("Remove Test Case")
        delete_button.clicked.connect(lambda _, row=row_count, test_case_id=test_case_id: self.offload_test_case(row, test_case_id))


        button_widget = qtw.QWidget()
        layout = qtw.QHBoxLayout(button_widget)
        layout.addWidget(delete_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        self.Main.ui.testSuiteTable.setCellWidget(row_count, 3, button_widget)
    def offload_test_case(self, row, test_case_id):
        """Deletes a test case from the table and the TestCaseManager."""
        self.Main.ui.testSuiteTable.removeRow(row)
        self.test_manager.load_test_case(test_case_id, False)
        # ✅ Update row numbers for remaining test cases
        for new_row in range(row, self.Main.ui.testSuiteTable.rowCount()):
            delete_button_widget = self.Main.ui.testSuiteTable.cellWidget(new_row, 3)  # Get the button widget
            
            if delete_button_widget:
                delete_button = delete_button_widget.findChild(qtw.QPushButton)  # Find the button inside the widget
                if delete_button:
                    # ✅ Update the button's lambda function with the new row number
                    delete_button.clicked.disconnect()  # Remove old connection
                    new_test_case_id = int(self.Main.ui.testSuiteTable.item(new_row, 0).text())  # Get new test case ID
                    delete_button.clicked.connect(lambda _, r=new_row, t=new_test_case_id: self.offload_test_case(r, t))
        if self.Main.ui.testSuiteTable.rowCount() == 1:
            self.Main.ui.startTesting.setEnabled(False)
            self.Main.ui.stopTesting.setEnabled(False)
            self.Main.ui.rerunTesting.setEnabled(False)
    def startTesting(self,cli = False):
        self.testsuite_Screen_state = True
        self.cli_active = cli

        dialog = StartTestingDialog()
        result = dialog.exec()

        if result == qtw.QDialog.Accepted:
            self.debug_log.write_log("User clicked Proceed. Start Testing!")
        else:
            self.debug_log.write_log("Testing Aborted")
            return

        self.debug_log.write_log("Testing Started")
        self.show_message("Testing Started")
        #update the test cases
        #for test_case in self.test_manager.get_loaded_test_cases():
        #    self.test_manager.update_test_case_status(test_case.test_case_id, "Pending")
        #    row = self.find_row_by_test_case_id(test_case.test_case_id)
        #    item = self.Main.ui.testSuiteTable.item(row, 4)
        #    item.setBackground(QBrush(QColor(255,255,255)))
        #    item.setForeground(QBrush(QColor(191, 227, 254)))
        #    if row != -1:
        #        self.Main.ui.testSuiteTable.setItem(row, 2, qtw.QTableWidgetItem("Pending")) #clear pre check
        #        self.Main.ui.testSuiteTable.setItem(row, 4, qtw.QTableWidgetItem("Pending")) #clear status
        #self.Main.ui.startTesting.setEnabled(False)
        #self.Main.ui.stopTesting.setEnabled(True)

        test_cases = []
        for row in range(self.Main.ui.testSuiteTable.rowCount()):
            if row > 0:
                item = self.Main.ui.testSuiteTable.item(row, 4)
                item.setBackground(QBrush(QColor(255,255,255)))
                item.setForeground(QBrush(QColor(191, 227, 254)))
                item = self.Main.ui.testSuiteTable.item(row, 0)
                self.Main.ui.testSuiteTable.setItem(row, 2, qtw.QTableWidgetItem("Pending")) #clear pre check
                self.Main.ui.testSuiteTable.setItem(row, 4, qtw.QTableWidgetItem("Pending")) #clear status
                if item:
                    test_cases.append(item.text())
        self.Main.ui.startTesting.setEnabled(False)
        self.Main.ui.stopTesting.setEnabled(True)

        #create report thread - in parallel
        self.report_worker = ReportingManager(self.workspaceManager.get_reports_path())
        self.report_thread = qtc.QThread()
        self.report_worker.moveToThread(self.report_thread)
        self.report_worker.finished.connect(self.update_test_report)
        self.generate_report.connect(self.report_worker.finalize_report)
        if self.cli_active:
            self.report_worker.finished.connect(self.run_cleanup_script)
        self.report_worker.finished.connect(self.report_thread.quit)
        self.report_worker.finished.connect(self.report_worker.deleteLater)
        self.report_thread.finished.connect(self.report_thread.deleteLater)
        
        
        # Create a testing thread in parallel
        self.testingthread = qtc.QThread()
        self.testingworker = TestingManager(self.test_manager, self.report_worker, self.workspaceManager, test_cases, self.pipes)
        self.testingworker.moveToThread(self.testingthread)
        # Connect signals and slots
        self.mutex.lock()
        self.testingthread.started.connect(self.testingworker.run)
        self.testingworker.finished.connect(self.testingthread.quit)
        self.testingworker.finished.connect(self.testingworker.deleteLater)
        self.testingthread.finished.connect(self.testingthread.deleteLater)
        self.mutex.unlock()

        #start the keyboard listener for kill switch
        self.listener_stop_flag.clear()  # Clear the stop flag
        self.listener_thread = threading.Thread(target=self.start_listener , args=(self.listener_stop_flag,))
        self.listener_thread.start()


        self.testingworker.finished.connect(self.update_test_reports)
        self.testingworker.stopped.connect(self.test_stopped)
        self.testingworker.progress.connect(self.update_test_case_status)
        self.testingworker.precheck.connect(self.update_pre_check_status)
        self.testingworker.time_elapsed.connect(self.update_time_elapsed)
        self.testingworker.log.connect(self.log_message)
        self.testingworker.error.connect(self.update_error)
        self.testingworker.failedscreens.connect(self.update_failed_screens)

        # Start the thread
        self.testingthread.start()

        # Disable the start button and enable the stop button
        self.testingthread.finished.connect(lambda: self.Main.ui.startTesting.setEnabled(False))
        self.testingthread.finished.connect(lambda: self.Main.ui.stopTesting.setEnabled(False))
        self.testingthread.finished.connect(lambda: setattr(self, 'testingthread', None))

    def start_listener(self,stop_flag):
        def on_press(key):
            try:
                if key == keyboard.Key.esc:
                    str = "ESC Key detected - STOP Requested"
                    self.debug_log.write_log(str)
                    print(str)
                    self.stopTesting()
                    return False
            except AttributeError:
                pass

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()
        
        while not stop_flag.is_set():
            time.sleep(0.1)

        if self.listener.running:
            self.listener.stop()

    def update_test_report(self,report_file_path):
        if report_file_path == "":
            return
        file_name = os.path.basename(report_file_path)
        if os.path.exists(report_file_path):
            #self.log.display_log_message("Test Report generated")
            print("Test Report generated")
            self.add_report(report_file_path,file_name)
            self.Main.ui.rerunTesting.setEnabled(True)
        else:
            #self.log.display_log_message("Test Report Not found")
            print("Test Report Not found")
            self.Main.ui.rerunTesting.setEnabled(True)

    def update_error(self, test_case_id, message):
        #self.log.display_log_message(f"Error: TC({test_case_id}) -{message}")
        print(f"Error: TC({test_case_id}) -{message}")
        row = self.find_row_by_test_case_id(test_case_id)
        if row != -1:
            self.Main.ui.testSuiteTable.setItem(row, 7, qtw.QTableWidgetItem(message))

    def update_pre_check_status(self, test_case_id, status):
        #self.log.display_log_message(f"Test case {test_case_id} - Precheck - {status}")
        print(f"Test case {test_case_id} - Precheck - {status}")
        row = self.find_row_by_test_case_id(test_case_id)
        if row != -1:
            self.Main.ui.testSuiteTable.setItem(row, 2, qtw.QTableWidgetItem(status))
        
    def update_time_elapsed(self, test_case_id, time):
        #self.log.display_log_message(f"Test case {test_case_id} - Time Elapsed - {time}")
        print(f"Test case {test_case_id} - Time Elapsed - {time}")
        row = self.find_row_by_test_case_id(test_case_id)
        if row != -1:
            self.Main.ui.testSuiteTable.setItem(row, 6, qtw.QTableWidgetItem(time))
    def update_failed_screens(self, test_case_id, index, current_screen):
        filepath = os.path.join(self.workspaceManager.get_assets_path(), f"{test_case_id}{index:04d}.png")
        if(os.path.exists(filepath)):
            self.store_failed_screenshots(test_case_id,filepath,current_screen)
        else:    
            print("Screenshot not found");
        print(f"Test case {test_case_id} - Failed Screen {index} - {filepath}")

    def log_message(self, test_case_id, message):
        #self.log.display_log_message(f"Test case {test_case_id} - {message}")
        print(f"Test case {test_case_id} - {message}")
        
    def update_test_case_status(self, test_case_id, status):
        """Updates the status of a test case in the table."""
        self.test_manager.update_test_case_status(test_case_id,status)
        #self.log.display_log_message(f"Test case {test_case_id} - {status}")
        print(f"Test case {test_case_id} - {status}")
        row = self.find_row_by_test_case_id(test_case_id)
        if row != -1:
            self.Main.ui.testSuiteTable.setItem(row, 4, qtw.QTableWidgetItem(status))
            item = self.Main.ui.testSuiteTable.item(row, 4)
            if status == "Passed":
                item.setBackground(QBrush(QColor(92,250,203)))
                item.setForeground(QBrush(QColor(5, 21, 3)))
            elif status == "Failed":
                item.setBackground(QBrush(QColor(250,92,100)))
                item.setForeground(QBrush(QColor(5, 21, 3)))

        print("In update test case")

    def test_stopped(self):
        self.show_message("Testing Stopped")
        QMessageBox.critical(self.Main, "Testing Stopped", "ESC Key detected \nPlease click Re-runtests to start again.")
        """reply = qtw.QMessageBox.question(self, "Testing Stopped", "Do you want to prepare a report for the completed test cases?",
                                            qtw.QMessageBox.Yes | qtw.QMessageBox.No, qtw.QMessageBox.No)
            
        if reply == qtw.QMessageBox.No :
            self.report_worker.stop()
            if not self.headless:
                self.reports_window.show()
            self.Main.ui.rerunTesting.setEnabled(True)
        else:
            #self.log.display_log_message("Preparing report. Please wait.......")
            str = f"Preparing report. Please wait......."
            self.debug_log.write_log(str)
            print(str)
            self.show_message(str)
            self.update_test_reports()"""
        #self.listener.stop()
    def update_test_reports(self):
        if self.listener_thread and self.listener_thread.is_alive():
            self.listener_stop_flag.set()  # Signal the thread to stop
        self.generate_report.emit()
        retry = 0
        while self.report_worker.reportReady == False and retry < 5:
            retry+=1
            qtw.QApplication.processEvents()
            time.sleep(5)
            

        if self.report_worker.reportReady == True:
           self.test_report = self.report_worker.report
        else:
            self.reports_window.show()
            self.Main.ui.rerunTesting.setEnabled(True)
            return
            
        if self.cli_active:
            self.generate_html_report(self.test_report)
            print("skipping report display in CLI mode")
        else:
            self.reports_window.load_report(self.test_report)
            self.reports_window.show()
                

    def stopTesting(self):
        print("pressed stop testing")
        self.debug_log.write_log("Testing Stopped")
        self.Main.ui.label_message.setText("")
        self.Main.ui.rerunTesting.setEnabled(True)
        self.Main.ui.startTesting.setEnabled(False)
        self.Main.ui.stopTesting.setEnabled(False)
        if self.testingworker:
            self.testingworker.stop()
            print("stopped worker")
        if self.testingthread:
            self.testingthread.quit()
            self.testingthread.wait()
            print("stopped thread")
        else:
            print("testingthread already stopped or deleted")
        if self.listener_thread and self.listener_thread.is_alive():
            self.listener.stop()
            self.listener_stop_flag.set()  # Signal the thread to stop

    def rerunTesting(self):
        print("Pressed Rerun testing")
        for test_case in self.test_manager.get_loaded_test_cases():
            self.test_manager.update_test_case_status(test_case.test_case_id, "Pending")
            row = self.find_row_by_test_case_id(test_case.test_case_id)
            item = self.Main.ui.testSuiteTable.item(row, 4)
            item.setBackground(QBrush(QColor(255,255,255)))
            item.setForeground(QBrush(QColor(191, 227, 254)))
            if row != -1:
                self.Main.ui.testSuiteTable.setItem(row, 2, qtw.QTableWidgetItem("Pending")) #clear pre check
                self.Main.ui.testSuiteTable.setItem(row, 4, qtw.QTableWidgetItem("Pending")) #clear status
                self.Main.ui.testSuiteTable.setItem(row, 7, qtw.QTableWidgetItem("")) #clear error
        self.debug_log.write_log("Re-running Tests")
        self.startTesting()
        self.Main.ui.startTesting.setEnabled(False)
        self.Main.ui.stopTesting.setEnabled(True)
    def updateTestCase(self):
        print("Pressed update test case")
        item = self.Main.ui.testSuiteTable.currentItem()
        if item:
            test_case_id = self.Main.ui.testSuiteTable.item(item.row(), 0).text()
            test_case = self.test_manager.get_test_case(test_case_id)
            if test_case:
                editor = ScreenshotEditor(self.Main,self.validation_failed_img,test_case_id,test_case.description)
                self.Main.ui.btn_edit.click()
        else:
            QMessageBox.critical(self.Main, "Error", "Please select a test case to update")
    def start_recorder(self):
        self.currTestCase = TestCaseConfig(get_test_case_id(),
                                           "",
                                           self.workspaceManager.get_target_application_path(),
                                           self.workspaceManager.get_cli_params(),
                                           self.workspaceManager.get_ss_timer(),
                                           self.workspaceManager.get_auto_connect(),
                                           0,
                                           self.workspaceManager.get_assets_path(),
                                           None)
        self.window = NewTestCaseWindow(self.currTestCase)
        result, self.currTestCase = self.window.show_new_test_case()
        if result:
            self.recorder = Recorder(self.Main,self,self.currTestCase)
            self.recorder.show()
            self.recorder.raise_()
            self.recorder.activateWindow()

    def cancel_recording(self):
        self.Main.ui.initialFrame.setEnabled(True)
        self.Main.ui.initialFrame.setVisible(True)
        self.Main.ui.finalFrame.setEnabled(False)
        self.Main.ui.finalFrame.setVisible(False)
        self.recorder = None
    def save_settings(self):
        self.debug_log.write_log("clicked save on Settings")

        if not self.get_workspace():
            self.debug_log.write_log("Workspace not found. Please first select a workspace.")
            return False

        # Validate fields
        if not self.Main.ui.txt_projectName.text().strip():
            self.Main.ui.errorMessage.setText("Project Name cannot be empty.")
            self.Main.ui.errorMessage.setVisible(True)
            return False

        if len(self.Main.ui.txt_projectName.text()) > 100:
            self.Main.ui.errorMessage.setText("Project Name cannot exceed 100 characters.")
            self.Main.ui.errorMessage.setVisible(True)
            return False

        if not self.Main.ui.txt_projectLocationPath.text().strip():
            self.Main.ui.errorMessage.setText("Project Location cannot be empty.")
            self.Main.ui.errorMessage.setVisible(True)
            return False

        if self.Main.ui.txt_targetAppPath.text().strip() and not self.Main.ui.txt_targetAppPath.text().strip().lower().endswith(".exe"):
            self.Main.ui.errorMessage.setText("Target application must be a .exe file.")
            self.Main.ui.errorMessage.setVisible(True)
            return False

        if not self.Main.ui.txt_reportsPath.text().strip():
            self.Main.ui.errorMessage.setText("Reports path cannot be empty.")
            self.Main.ui.errorMessage.setVisible(True)
            return False

        self.workspaceManager.set_target_application_path(self.Main.ui.txt_targetAppPath.text())
        self.workspaceManager.set_cli_params(self.Main.ui.txt_cmdLineParams.text())
        self.workspaceManager.set_setup_script_path(self.Main.ui.txt_setupScriptPath.text())
        self.workspaceManager.set_cleanup_script_path(self.Main.ui.txt_cleanupScriptPath.text())
        self.workspaceManager.set_auto_connect(self.Main.ui.cb_autoconnect.isChecked())
        self.workspaceManager.set_ss_timer(self.Main.ui.txt_screenshotTimer.value())  # 60 minutes session timeout
        self.workspaceManager.set_auto_load(self.Main.ui.cb_autoload.isChecked())
        result, message = self.workspaceManager.rename_workspace(self.Main.ui.txt_projectName.text())
        if result:
            QMessageBox.information(self.Main, "Settings", message)
        else:
            QMessageBox.critical(self.Main, "Settings", message)
            return
        
        filepath = os.path.join(self.workspaceManager.get_workspace_path(),f"{self.workspaceManager.get_workspace_name()}.atest")
        self.close_workspace()
        self.open_workspace(filepath)

        return True
    def save_test_case(self):
        self.debug_log.write_log("clicked save on Recorder")
        if self.get_workspace():
            try:
                self.Main.recorder_screen_state = False
                description = self.Main.ui.description.text()
                self.Main.ui.initialFrame.setEnabled(True)
                self.Main.ui.initialFrame.setVisible(True)
                self.Main.ui.finalFrame.setEnabled(False)
                self.Main.ui.finalFrame.setVisible(False)
                self.recorder.record_ctrl.testcase.update_test_case(self.recorder.record_ctrl.temp_file,
                                                                    TestCaseDescription=description)
                #self.recorder.record_ctrl.testcase.update_test_case(self.recorder.record_ctrl.temp_file,description)
                self.populate_test_suite_table(self.recorder.record_ctrl.testcase)
                test_case_id = self.recorder.record_ctrl.testcase.test_case_id
                self.workspaceManager.add_test_case(self.currTestCase)
                #test_case = self.test_manager.get_test_case(test_case_id)
                #src = os.path.normpath(get_temp_file_path(test_case_id))
                #dest = os.path.normpath(self.get_workspace() + "/testcases")
                shutil.copy2(get_temp_file_path(test_case_id), self.get_workspace() + "/testcases")

                #src = os.path.normpath(get_screenshot_path(test_case_id))
                #dest = os.path.normpath(self.workspaceManager.get_assets_path())
                shutil.copytree(get_screenshot_path(test_case_id),self.workspaceManager.get_assets_path(), dirs_exist_ok=True)
                shutil.rmtree(get_test_case_path(test_case_id))  # Delete the source directory
                self.update_explorer(test_case_id)
            except Exception as e:
                print(str(e))
                m = dedent("Unkown error occured while loading script. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))


    def fetch_reports(self):
        if self.get_workspace():
            try:
                reports_folder_path = self.workspaceManager.get_reports_path()
                for file in os.listdir(reports_folder_path):
                    if file.endswith(".pdf"):
                        # Get file details
                        pathname = os.path.join(reports_folder_path, file)
                        self.add_report(pathname,file)
            except:
                m = dedent("Unkown error occured while loading reports. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))
    
    def add_report(self,filepath,filename):
        # Get file details
        try:
            file_date = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%Y-%m-%d %H:%M:%S")

            header = self.Main.ui.reportsTable.horizontalHeader()
            header.setSectionResizeMode(0, QHeaderView.Stretch)    # First column stretches
            header.setSectionResizeMode(1, QHeaderView.Stretch)  # Second column auto-fits content
            header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # Third column auto-fits content
            # Insert row into the table
            row_count = self.Main.ui.reportsTable.rowCount()
            self.Main.ui.reportsTable.insertRow(row_count)

            # Add filename
            self.Main.ui.reportsTable.setItem(row_count, 0, QTableWidgetItem(filename))
                            
            # Add generated on date
            self.Main.ui.reportsTable.setItem(row_count, 1, QTableWidgetItem(file_date))

            # Add Edit buttons (View and Delete)
            btn_widget = QWidget()
            btn_layout = QHBoxLayout(btn_widget)
            btn_layout.setContentsMargins(0, 0, 0, 0)

            # View button
            view_btn = QPushButton("View")
            view_btn.setFixedSize(70, 20) 
            view_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
            view_btn.clicked.connect(lambda _, path=filepath: self.view_pdf(path))
            btn_layout.addWidget(view_btn)

            btn_layout.addSpacing(10)  # <-- this adds space between buttons

            # Delete button
            del_btn = QPushButton("Delete")
            del_btn.setFixedSize(70, 20) 
            del_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  
            del_btn.clicked.connect(lambda _, row=row_count: self.delete_report(row))
            btn_layout.addWidget(del_btn)

            self.Main.ui.reportsTable.setCellWidget(row_count, 2, btn_widget)
        except:
            m = dedent("Unkown error occured saving reports")
            QMessageBox.critical(self.Main, "Error", str(m))

    def delete_report(self, row):
        #Delete a report and reindex the buttons.
        try:
            # Confirm before deletion
            reply = QMessageBox.question(
                self.Main,
                "Delete Report",
                "Are you sure you want to delete this report?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # Remove the row from the table
                self.Main.ui.reportsTable.removeRow(row)

                # Reindex the remaining buttons
                row_count = self.Main.ui.reportsTable.rowCount()
                
                for i in range(row, row_count):
                    widget = self.Main.ui.reportsTable.cellWidget(i, 2)
                    layout = widget.layout()

                    # Disconnect existing signals to avoid duplicates
                    for j in range(layout.count()):
                        btn = layout.itemAt(j).widget()
                        if isinstance(btn, QPushButton):
                            btn.clicked.disconnect()

                    # Reconnect with the updated row index
                    layout.itemAt(0).widget().clicked.connect(
                        lambda _, path=self.get_workspace() + '/' + self.Main.ui.reportsTable.item(i, 0).text(): 
                        self.view_pdf(path)
                    )
                    layout.itemAt(1).widget().clicked.connect(
                        lambda _, r=i: self.delete_report(r)
                    )

        except Exception as e:
            QMessageBox.critical(self.Main, "Error", f"Failed to delete report: {str(e)}")

    def view_pdf(self, filepath):
        #Open the PDF report in the default PDF viewer.
        try:
            if os.path.exists(filepath):
                webbrowser.open(filepath)
            else:
                QMessageBox.warning(self.Main, "File Not Found", f"Could not find the file:\n{filepath}")
        except Exception as e:
            QMessageBox.critical(self.Main, "Error", f"Failed to open PDF: {str(e)}")

    def control_definitions(self):
        # Create and start the thread
        self.testingthread = None
        self.testingworker = None
        self.report_worker = None
        self.report_thread = None
        self.listener_thread = None
        self.listener_stop_flag = threading.Event()
        self.listener = None

        self.Main.ui.testSuiteTable.setColumnWidth(0, 100)
        self.Main.ui.testSuiteTable.setColumnWidth(1, 250)
        self.Main.ui.testSuiteTable.setColumnWidth(2, 100)
        self.Main.ui.testSuiteTable.setColumnWidth(3, 60)
        self.Main.ui.testSuiteTable.setColumnWidth(4, 100)
        self.Main.ui.testSuiteTable.setColumnWidth(5, 100)
        self.Main.ui.testSuiteTable.setColumnWidth(6, 100)
        self.Main.ui.testSuiteTable.setColumnWidth(7, 250)
        header = self.Main.ui.testSuiteTable.horizontalHeader()
        header.setSectionResizeMode(qtw.QHeaderView.ResizeMode.Fixed)

        self.reports_window = TestingCompleteDialog()
        self.mutex = QMutex()

        
    def connect_application(self):
        def _monitor_connection(server):
            server.connectPOS()
            while True and not self.connection_stop_flag.is_set():
                self.show_message("")
                status = '🟢 Connected' if server.is_connected() else '🔴 Not connected'
                self.Main.ui.lbl_connection_status.setText(f"Application connection status: {status}")
                print(f"[AUTOTEST] Application connection status: {status}")
                time.sleep(5)

        self.show_message("Attempting to connect target application")
        threading.Thread(target=_monitor_connection,
                         args=(self.pipes,),
                         daemon=True).start()
    def store_failed_screenshots(self,test_case_id,imagepath,actual_image):
        #self.validation_failed_img[test_case_id] = [expected_image,actual_image]
        """Store screenshots in order for the same test case ID."""
        if test_case_id not in self.validation_failed_img:
            self.validation_failed_img[test_case_id] = []
        
        # Append the new screenshot pair in order
        self.validation_failed_img[test_case_id].append((imagepath, actual_image))

    def get_failed_screenshots(self, test_case_id):
        return self.validation_failed_img.get(test_case_id, [])
    
    def show_message(self, message):
        """Display a message box with the given message."""
        self.Main.ui.label_message.setText(message)

    def cleanup_application(self):
        """Close the application."""
        self.connection_stop_flag.set()
        if self.pipes.is_connected:
            self.pipes.disconnectPOS()
        self.stopTesting()
        self.cancel_recording()

    def set_html_reports_path(self, path=""):
        """Set the reports path."""
        if not path:
            path = self.workspaceManager.get_reports_path()
        if not path.endswith(".html"):
            path = os.path.dirname(path)
            self.html_report_path = os.path.join(path, "TestReport.html")
        else:
            self.html_report_path = path

    def generate_html_report(self, report):
        summary = report["execution_summary"]

        html_content = f"""
        <html>
        <head>
            <title>Automation Testing Summary Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px; }}
                h1 {{ color: #333; }}
                p {{ font-size: 16px; }}
                .summary-table {{
                    border-collapse: collapse;
                    width: 50%;
                }}
                .summary-table th, .summary-table td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: left;
                }}
                .summary-table th {{
                    background-color: #eee;
                }}
            </style>
        </head>
        <body>
            <h1>AUTOTEST Summary</h1>
            <table class="summary-table">
                <tr><th>Total Test Cases</th><td>{summary['total']}</td></tr>
                <tr><th>Passed</th><td>{summary['passed']}</td></tr>
                <tr><th>Failed</th><td>{summary['failed']}</td></tr>
                <tr><th>Blocked</th><td>{summary['blocked']}</td></tr>
                <tr><th>Start Time</th><td>{summary['start_time']}</td></tr>
                <tr><th>End Time</th><td>{summary['end_time']}</td></tr>
                <tr><th>Total Execution Time</th><td>{summary['total_execution_time']}</td></tr>
                <tr><th>Report ID</th><td>{summary['report_id']}</td></tr>
            </table>
        </body>
        </html>
        """

        with open(self.html_report_path, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f"HTML summary report created: {self.html_report_path}")

    def run_setup_script(self):
        """Run the setup script if it exists."""
        setup_script_path = self.workspaceManager.get_setup_script_path()
        if os.path.exists(setup_script_path):
            try:
                subprocess.run([setup_script_path], check=True)
                str = "Setup script executed successfully"
                self.debug_log.write_log(str)
                print(str)
                return True
            except subprocess.CalledProcessError as e:
                str = f"Error executing setup script: {e}"
                self.debug_log.write_log(str)
                print(str)
                return False
        else:
            str = "No setup script found."
            self.debug_log.write_log(str)
            print(str)
            return True

    def run_cleanup_script(self):
        """Run the cleanup script if it exists."""
        cleanup_script_path = self.workspaceManager.get_cleanup_script_path()
        if os.path.exists(cleanup_script_path):
            try:
                subprocess.run([cleanup_script_path], check=True)
                str = "Cleanup script executed successfully"
                self.debug_log.write_log(str)
                print(str)

            except subprocess.CalledProcessError as e:
                str = f"Error executing cleanup script: {e}"
                self.debug_log.write_log(str)
                print(str)
                return False
        else:
            str = "No cleanup script found."
            self.debug_log.write_log(str)
            print(str)
            
        if self.cli_active:
            self.cleanup_application()
            self.Main.close()

class ScreenshotEditor(QObject):
    def __init__(self, MainWindow, screenshots, test_case_id, test_case_description):
        super().__init__()

        # Initialize variables
        self.screenshots = screenshots.get(test_case_id, [])
        self.test_case_id = test_case_id
        self.test_case_description = test_case_description

        # Navigation index
        self.current_index = 0
        self.Main = MainWindow
        self.Main.ui.edit_prevBtn.clicked.connect(self.prev_screenshot)
        self.Main.ui.edit_nextBtn.clicked.connect(self.next_screenshot)
        self.Main.ui.edit_updatebtn.clicked.connect(self.update_screenshot)
        self.Main.ui.edit_cancel.clicked.connect(self.close_editor)

        # Initialize UI with data
        self.load_screenshots()

    def load_screenshots(self):
        """Load and display current screenshots."""
        if not self.screenshots:
            QMessageBox.information(self.Main, "No Screenshots", "No screenshots available for this test case.")
            self.Main.ui.status.setText("No screenshots found.")
            return

        if self.current_index < 0 or self.current_index >= len(self.screenshots):
            return

        # Load current expected and actual images
        imagepath, actual_img = self.screenshots[self.current_index]

        # Display the images in the QGraphicsView
        self.display_expected_image(self.Main.ui.gv_expected, imagepath)
        self.display_actual_image(self.Main.ui.gv_actual, actual_img)

        # Update labels
        self.Main.ui.status.setText(f"Viewing {self.current_index + 1} of {len(self.screenshots)}")
        self.Main.ui.testcaseid.setText(self.test_case_id)
        self.Main.ui.testcasedesc.setText(self.test_case_description)

    def display_expected_image(self, graphics_view, image_path):
        """Display an image in the specified QGraphicsView."""
        scene = QGraphicsScene()
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            QMessageBox.warning(self.Main, "Image Load Error", f"Failed to load image: {image_path}")
            return

        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)

        # Adjust the scene to fit the image properly
        graphics_view.setScene(scene)
        graphics_view.fitInView(item)

    def display_actual_image(self, graphics_view, image):
        """Display a numpy array in the specified QGraphicsView."""
        scene = QGraphicsScene()

        try:
            pil_image = Image.fromarray(image).convert("RGBA")
            qimage = ImageQt(pil_image)
            pixmap = QPixmap.fromImage(qimage)
        except Exception as e:
            QMessageBox.warning(self.Main, "Image Conversion Error", f"Failed to convert NumPy image: {e}")
            return

        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        graphics_view.setScene(scene)
        graphics_view.fitInView(item)
        #graphics_view.fitInView(item, Qt.AspectRatioMode.KeepAspectRatio)

    def prev_screenshot(self):
        """Navigate to the previous screenshot."""
        if self.current_index > 0:
            self.current_index -= 1
            self.load_screenshots()

    def next_screenshot(self):
        """Navigate to the next screenshot."""
        if self.current_index < len(self.screenshots) - 1:
            self.current_index += 1
            self.load_screenshots()

    def update_screenshot(self):
        """Replace the actual screenshot with the expected."""
        if not self.screenshots:
            QMessageBox.warning(self.Main, "No Screenshots", "No screenshots to update.")
            return

        if 0 <= self.current_index < len(self.screenshots):
            image_path, _ = self.screenshots[self.current_index]

            # Replace actual with expected
            self.screenshots[self.current_index] = (image_path, image_path)

            QMessageBox.information(self.Main, "Screenshot Updated", "Actual screenshot replaced with expected.")
            
            # Reload the current screenshot pair
            self.load_screenshots()

    def close_editor(self):
        """Clear the editor without closing the application."""
        # Clear the QGraphicsViews
        self.Main.ui.gv_expected.setScene(QGraphicsScene())  # Clear expected image
        self.Main.ui.gv_actual.setScene(QGraphicsScene())    # Clear actual image

        # Reset labels
        self.Main.ui.labelstatus.setText("Editor Cleared.")
        self.Main.ui.label_testcaseid.setText("Test Case ID: N/A")
        self.Main.ui.testcasedesc.setText("No Description")

        # Reset navigation index
        self.current_index = 0

        # Display a message
        QMessageBox.information(self.Main, "Editor Cleared", "All screenshots have been cleared.")


class NewWorkspaceWindow(QWidget, Ui_newWorkspaceWindow):
    workspace_created = Signal(str)  # str for projectPath
    def __init__(self, wsmanager,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setup_connections()
        self.wsmanager = wsmanager
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint| Qt.FramelessWindowHint)
        self.errorMessage.setVisible(False)
        self.projectPath = ""
        self.debug_log = DebugLogger()
    

    def center_on_parent(self):
        if self.parent():
            parent_rect = self.parent().frameGeometry()
            parent_screen = self.parent().screen().availableGeometry()

            # Center relative to the parent window within its own screen
            x = parent_rect.center().x() - self.width() // 2
            y = parent_rect.center().y() - self.height() // 2

            # Constrain to available screen geometry
            x = max(parent_screen.left(), min(x, parent_screen.right() - self.width()))
            y = max(parent_screen.top(), min(y, parent_screen.bottom() - self.height()))

            self.move(x, y)

    def setup_connections(self):
        self.btn_findPath1.clicked.connect(lambda: self.browse_folder(self.txt_projectLocationPath))
        self.btn_findPath2.clicked.connect(lambda: self.browse_file(self.txt_targetAppPath, "exe"))
        self.btn_findPath3.clicked.connect(lambda: self.browse_folder(self.txt_reportsPath))
        self.btn_findPath4.clicked.connect(lambda: self.browse_file(self.txt_setupScriptPath))
        self.btn_findPath5.clicked.connect(lambda: self.browse_file(self.txt_cleanupScriptPath))

        self.cb_autoconnect.toggled.connect(self.toggle_screenshot_timer)

        # Connect the DialogButtonBox
        self.dialogButtons.accepted.connect(self.save_settings)  # OK clicked
        self.dialogButtons.rejected.connect(self.close_settings)        # Cancel clicked
        self.closeBtn.clicked.connect(self.close_settings)  # Close button clicked

    def close_settings(self):
        # Close the window
        self.close()
    def browse_folder(self, target_widget):
        path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if target_widget == self.txt_projectLocationPath and path:
            self.projectPath = os.path.join(path, self.txt_projectName.text().strip())
            self.projectPath = os.path.normpath(self.projectPath)  # Normalize the path
            reportsPath = os.path.join(self.projectPath, "reports")
            reportsPath = os.path.normpath(reportsPath)  # Normalize the path
            self.txt_reportsPath.setText(reportsPath)
        if path:
            target_widget.setText(path)

    def browse_file(self, target_widget, file_extension=None):
        if file_extension:
            filter_str = f"{file_extension.upper()} Files (*.{file_extension})"
        else:
            filter_str = "All Files (*)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", filter=filter_str)

        if file_path:
            target_widget.setText(file_path)

    def toggle_screenshot_timer(self):
        is_checked = self.cb_autoconnect.isChecked()
        if(is_checked):
            self.txt_screenshotTimer.setValue(0)
        self.txt_screenshotTimer.setDisabled(is_checked)

    def validate_inputs(self):
        # Validate fields according to your spec
        if not self.txt_projectName.text().strip():
            return False, "Project Name cannot be empty."

        if len(self.txt_projectName.text()) > 100:
            return False, "Project Name cannot exceed 100 characters."

        if not self.txt_projectLocationPath.text().strip():
            return False, "Project Location cannot be empty."

        if self.txt_targetAppPath.text().strip() and not self.txt_targetAppPath.text().strip().lower().endswith(".exe"):
            return False, "Target application must be a .exe file."

        if not self.txt_reportsPath.text().strip():
            return False, "Reports path cannot be empty."

        return True, ""

    def save_settings(self):
        is_valid, message = self.validate_inputs()
        if not is_valid:
            self.errorMessage.setText(message)
            self.errorMessage.setVisible(True)
            self.errorMessage.setStyleSheet("color: red;")
            return False, message
        
        self.wsmanager.set_workspace_name(self.txt_projectName.text())
        self.wsmanager.set_workspace_path(self.txt_projectLocationPath.text())
        self.wsmanager.set_target_application_path(self.txt_targetAppPath.text())
        self.wsmanager.set_cli_params(self.txt_cmdLineParams.text())
        self.wsmanager.set_reports_path(self.txt_reportsPath.text())
        os.makedirs(self.txt_reportsPath.text(), exist_ok=True)
        assetsPath = os.path.join(self.projectPath, "assets")
        assetsPath = os.path.normpath(assetsPath)  # Normalize the path
        os.makedirs(assetsPath, exist_ok=True)
        tcPath = os.path.join(self.projectPath, "testcases")
        tcPath = os.path.normpath(tcPath)  # Normalize the path
        os.makedirs(tcPath, exist_ok=True)
        self.wsmanager.set_assets_path(assetsPath)
        self.wsmanager.set_setup_script_path(self.txt_setupScriptPath.text())
        self.wsmanager.set_cleanup_script_path(self.txt_cleanupScriptPath.text())
        self.wsmanager.set_auto_connect(self.cb_autoconnect.isChecked())
        self.wsmanager.set_ss_timer(self.txt_screenshotTimer.value())  # 60 minutes session timeout
        self.wsmanager.set_auto_load(self.cb_autoload.isChecked())
        
        result, filepath = self.wsmanager.save_to_file()
        if result:
            self.debug_log.write_recent_file(self.wsmanager.get_workspace_name(),filepath)
            self.workspace_created.emit(self.projectPath)
            self.close()
            return True
        else:
            self.errorMessage.setText("Failed to save settings.")
            self.errorMessage.setVisible(True)
            self.errorMessage.setStyleSheet("color: red;")
            return False
        
    def open_workspace(self,filepath=""):
        # Open the workspace and load settings
        if not filepath:
            file_path, _ = QFileDialog.getOpenFileName(self, "Select Project File", filter="*.atest")
        else:
            file_path = filepath
        if file_path:
            self.wsmanager.load_from_file(file_path)
            self.debug_log.write_recent_file(self.wsmanager.get_workspace_name(),file_path)
            return True
        
        
        
        
    def new_workspace(self):
        # Create a new workspace and load settings
        result = self.show()
        if result:
            return True, self.projectPath
        else:
            return False, None


class NewTestCaseWindow(QDialog, Ui_newTestCaseWindow):
    def __init__(self, testcaseConfig):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.clearWindow()
        self.testcaseConfig = testcaseConfig
        self.populate_details()
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.errorMessage.setVisible(False)
        

    def clearWindow(self):
        # Clear all fields
        self.txt_testCaseId.clear()
        self.txt_description.clear()
        self.txt_targetAppPath.clear()
        self.txt_cmdLineParams.clear()
        self.cb_priority.setCurrentIndex(0)
        self.txt_screenshotTimer.setValue(300)
        self.cb_autoConnect.setChecked(False)

    def populate_details(self):
        # Populate the fields with default values or empty strings
        if self.testcaseConfig.test_case_id:
            self.txt_testCaseId.setText(self.testcaseConfig.test_case_id)
        self.txt_testCaseId.setDisabled(True)
        self.txt_description.setText(self.testcaseConfig.description)
        self.txt_targetAppPath.setText(self.testcaseConfig.target_application_path)
        self.txt_cmdLineParams.setText(self.testcaseConfig.cli_params)
        self.cb_autoConnect.setChecked(self.testcaseConfig.auto_connect)
        self.cb_priority.setCurrentIndex(self.testcaseConfig.priority)
        self.txt_screenshotTimer.setValue(self.testcaseConfig.timer)

    def setup_connections(self):
        self.btn_findPath.clicked.connect(self.browse_file)
        self.cb_autoConnect.toggled.connect(self.toggle_timer_field)
        self.dialogButtons.accepted.connect(self.save_test_case)
        self.dialogButtons.rejected.connect(self.reject)
        self.closeBtn.clicked.connect(self.close)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Target Application", filter="Executable Files (*.exe)")
        if file_path:
            self.txt_targetAppPath.setText(file_path)

    def toggle_timer_field(self):
        is_checked = self.cb_autoConnect.isChecked()
        if(is_checked):
            self.txt_screenshotTimer.setValue(0)
        self.txt_screenshotTimer.setDisabled(is_checked)

    def validate_inputs(self):
        if not self.txt_testCaseId.text().strip():
            return False, "Test Case ID cannot be empty."

        if len(self.txt_testCaseId.text()) > 100:
            return False, "Test Case ID cannot exceed 100 characters."

        if not self.txt_description.text().strip():
            return False, "Test Case Description cannot be empty."

        app_path = self.txt_targetAppPath.text().strip()
        if app_path and not app_path.lower().endswith(".exe"):
            return False, "Target application path must point to a .exe file."

        if self.cb_priority.currentText() not in ["HIGH", "MEDIUM", "LOW"]:
            return False, "Please select a valid Priority."

        return True, ""

    def save_test_case(self):
        is_valid, message = self.validate_inputs()
        if not is_valid:
            self.errorMessage.setText(message)
            self.errorMessage.setVisible(True)
            self.errorMessage.setStyleSheet("color: red;")
            return False

        self.testcaseConfig = TestCaseConfig(
            test_case_id=self.txt_testCaseId.text().strip(),
            description=self.txt_description.text().strip(),
            target_application_path=self.txt_targetAppPath.text().strip(),
            cli_params=self.txt_cmdLineParams.text().strip(),
            timer=self.txt_screenshotTimer.value(),
            auto_connect=self.cb_autoConnect.isChecked(),
            priority=self.cb_priority.currentText(),
            asset_path=self.testcaseConfig.asset_path,
            asset_ids=[]  # You can later extend this dialog to add asset selection
        )

        self.accept()
        return True

    def show_new_test_case(self):
        result = self.exec()
        if result:
            return True, self.testcaseConfig
        else:
            return False, None