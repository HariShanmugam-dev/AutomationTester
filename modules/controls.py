from main import *
from . debug_log import *
from . test_case import TestCaseManager, TestCase
from . recorder import *
from PySide6 import QtWidgets as qtw
from textwrap import dedent
import webbrowser
from . testing_functions import *
from . report_functions import *

from threading import Thread
import time
import threading
from PIL.ImageQt import ImageQt
from PIL import Image

class Control(QObject):

    generate_report = Signal()
    def __init__(self, MainWindow):
        super().__init__()
        self.debug_log = DebugLogger()
        self.workspacePath = ""
        self.test_manager = TestCaseManager()
        self.Main = MainWindow
        self.recorder = None

        self.control_definitions()
        self.validation_failed_img = {}

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
             return True
        
        return False
         
    def open_workspace(self):
        try:
            self.debug_log.write_log("clicked Open_workspace()")
            Path = qtw.QFileDialog.getExistingDirectory(self.Main, "Open Workspace")
            if self.set_workspace(Path):
                self.Main.ui.labelWorkspacePath.setText(self.get_workspace().upper())
                self.Main.ui.labelHome.setVisible(True)
                self.Main.ui.labelWorkspacePath.setVisible(True)
                self.Main.ui.button_closeWorkspace.setVisible(True)
                self.Main.ui.button_newTestCase.setVisible(False)
                self.Main.ui.button_openWorkspace.setVisible(False)

                #update UI initially
                test_case_files = []  # List to store found text files
                # Walk through the workspace directory
                for dirpath, dirnames, filenames in walk(self.get_workspace()):
                    for dirname in dirnames:  # Loop through each subdirectory
                        if not dirname.startswith("TestCase"): #only look for test case file
                            continue
                        subdir_path = os.path.join(dirpath, dirname)
                        # Check for .txt files inside the subdirectory
                        for file in os.listdir(subdir_path):
                            if file.endswith(".json"):
                                file_path = os.path.join(subdir_path, file)
                                test_case_files.append(file_path)
                
                for file in test_case_files:
                    if file.endswith(".json"):
                        pathname = os.path.join(self.get_workspace(),file)
                        testcaseFileHandler = TestCase("", "", [])
                        testcaseFileHandler.load_test_case(pathname)
                        test_case_id = self.test_manager.add_test_case(testcaseFileHandler)
                        folderpath = os.path.dirname(pathname)
                        self.test_manager.update_test_case_path(test_case_id,folderpath)
                        if test_case_id:
                            self.update_explorer(test_case_id) 
                self.debug_log.write_log(f"Workpace set: {self.get_workspace()}")
                self.Main.ui.btn_explorer.click()
                self.fetch_reports()
            else:
                self.debug_log.write_log("Workpace Not set/ Not found")
        except Exception as e:
                self.debug_log.write_log(str(e))
                m = dedent("Unkown error occured while Opening workspace. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))

    def reloadWorkspace(self):
        workspace = self.get_workspace()
        if workspace:
            self.Main.ui.filesList.clear()
            test_case_files = []
            for dirpath, dirnames, filenames in walk(self.get_workspace()):
                    for dirname in dirnames:  # Loop through each subdirectory
                        if not dirname.startswith("TestCase"): #only look for test case file
                            continue
                        subdir_path = os.path.join(dirpath, dirname)
                        # Check for .txt files inside the subdirectory
                        for file in os.listdir(subdir_path):
                            if file.endswith(".json"):
                                file_path = os.path.join(subdir_path, file)
                                test_case_files.append(file_path)
            
            for file in test_case_files:
                    if file.endswith(".json"):
                        pathname = os.path.join(self.get_workspace(),file)
                        testcaseFileHandler = TestCase("", "", [])
                        testcaseFileHandler.load_test_case(pathname)
                        test_case_id = self.test_manager.add_test_case(testcaseFileHandler)
                        folderpath = os.path.dirname(pathname)
                        self.test_manager.update_test_case_path(test_case_id,folderpath)
                        if test_case_id:
                            self.update_explorer(test_case_id)
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
            self.Main.ui.labelWorkspacePath.setText("")
            self.Main.ui.labelHome.setVisible(False)
            self.Main.ui.labelWorkspacePath.setVisible(False)
            self.Main.ui.button_closeWorkspace.setVisible(False)
            self.Main.ui.button_newTestCase.setVisible(True)
            self.Main.ui.button_openWorkspace.setVisible(True)
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
                file_path = qtw.QFileDialog.getExistingDirectory(self.Main, "Select Test Case Folder")
                if file_path != "":
                    shutil.copytree(file_path, workspacepath, dirs_exist_ok=True)
                    for file in os.listdir(file_path):
                        if file.endswith(".json"):
                            pathname = os.path.join(workspacepath,file)
                            testcaseFileHandler = TestCase("", "", [])
                            testcaseFileHandler.load_test_case(pathname)
                            test_case_id = self.test_manager.add_test_case(testcaseFileHandler)
                            folderpath = os.path.dirname(pathname)
                            self.test_manager.update_test_case_path(test_case_id,folderpath)
                            if test_case_id:
                                self.update_explorer(test_case_id) 
            except:
                m = dedent("Unkown error occured while loading script. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))
    
    def load_alltestCase(self):
        if self.Main.ui.filesList.count() > 0:
            for i in range(self.Main.ui.filesList.count()):
                item = self.Main.ui.filesList.item(i)
                test_case_id = item.data(Qt.UserRole)
                test_case = self.test_manager.get_test_case(test_case_id)
                self.populate_test_suite_table(test_case,test_case_id)
        else:
            QMessageBox.critical(self.Main, "Error", "Please open a workspace to load the test cases")

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

        delete_button = qtw.QPushButton("Delete")
        #delete_button.setIcon(QIcon("Icon\\delete.png"))
        delete_button.setToolTip("Delete Test Case")
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
    def startTesting(self):
        self.testsuite_Screen_state = True
        dialog = StartTestingDialog()
        result = dialog.exec()

        if result == qtw.QDialog.Accepted:
            self.debug_log.write_log("User clicked Proceed. Start Testing!")
        else:
            self.debug_log.write_log("Testing Aborted")
            return

        self.debug_log.write_log("Testing Started")
        self.Main.ui.label_message.setText("Testing Started")
        #update the test cases
        for test_case in self.test_manager.get_loaded_test_cases():
            self.test_manager.update_test_case_status(test_case.test_case_id, "Pending")
            row = self.find_row_by_test_case_id(test_case.test_case_id)
            item = self.Main.ui.testSuiteTable.item(row, 4)
            item.setBackground(QBrush(QColor(255,255,255)))
            item.setForeground(QBrush(QColor(191, 227, 254)))
            if row != -1:
                self.Main.ui.testSuiteTable.setItem(row, 2, qtw.QTableWidgetItem("Pending")) #clear pre check
                self.Main.ui.testSuiteTable.setItem(row, 4, qtw.QTableWidgetItem("Pending")) #clear status
        self.Main.ui.startTesting.setEnabled(False)
        self.Main.ui.stopTesting.setEnabled(True)

        test_cases = []
        for row in range(self.Main.ui.testSuiteTable.rowCount()):
            if row > 0:
                item = self.Main.ui.testSuiteTable.item(row, 0)
                if item:
                    test_cases.append(item.text())

        #create report thread - in parallel
        self.report_worker = ReportingManager(self.get_workspace())
        self.report_thread = qtc.QThread()
        self.report_worker.moveToThread(self.report_thread)
        self.report_worker.finished.connect(self.update_test_report)
        self.generate_report.connect(self.report_worker.finalize_report)
        self.report_worker.finished.connect(self.report_thread.quit)
        self.report_worker.finished.connect(self.report_worker.deleteLater)
        self.report_thread.finished.connect(self.report_thread.deleteLater)
        

        # Create a testing thread in parallel
        self.testingthread = qtc.QThread()
        self.testingworker = TestingManager(self.test_manager, self.report_worker, test_cases)
        self.testingworker.moveToThread(self.testingthread)
        # Connect signals and slots
        self.mutex.lock()
        self.testingthread.started.connect(self.testingworker.run)
        self.testingworker.finished.connect(self.testingthread.quit)
        self.testingworker.finished.connect(self.testingworker.deleteLater)
        self.testingthread.finished.connect(self.testingthread.deleteLater)
        self.mutex.unlock()

        #start the keyboard listener for kill switch
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

    def start_listener(self):
        def on_press(key):
            try:
                if key == keyboard.Key.esc:
                    self.log.display_log_message("ESC Key detected - STOP Requested")
                    self.button_stop_testing(self.rerunTest, self.genreport, self.start, self.stop)
                    return False
            except AttributeError:
                pass

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
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
        filepath = os.path.join(self.get_workspace(), "TestCase -" +test_case_id, "screenshot-"+test_case_id, f"screenshot_{index:04d}.png")
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
            
        reply = qtw.QMessageBox.question(self, "Testing Stopped", "Do you want to prepare a report for the completed test cases?",
                                            qtw.QMessageBox.Yes | qtw.QMessageBox.No, qtw.QMessageBox.No)
            
        if reply == qtw.QMessageBox.No :
            self.report_worker.stop()
            self.reports_window.show()
            #self.widget_2.setVisible(True)
            #self.genreport.setVisible(False)
            #self.genTestReportinfo.setText("Report Not available. Please run the tests again to generate report")
            self.Main.ui.rerunTesting.setEnabled(True)
        else:
            #self.log.display_log_message("Preparing report. Please wait.......")
            print("Preparing report. Please wait.......")
            self.update_test_reports()
        self.listener.stop()
    def update_test_reports(self):
        if self.listener and self.listener.running:
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
            #self.widget_2.setVisible(True)
            #self.genreport.setVisible(False)
            #self.genTestReportinfo.setText("Report Not available. Please run the tests again to generate report")
            self.Main.ui.rerunTesting.setEnabled(True)
            return
            
        #summary = self.test_report["execution_summary"]

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
        if self.listener and self.listener.running:
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
        self.recorder = Recorder(self.Main,self)
        self.recorder.show()
        self.recorder.raise_()
        self.recorder.activateWindow()

    def cancel_recording(self):
        self.Main.ui.initialFrame.setEnabled(True)
        self.Main.ui.initialFrame.setVisible(True)
        self.Main.ui.finalFrame.setEnabled(False)
        self.Main.ui.finalFrame.setVisible(False)
        self.recorder = None

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
                self.recorder.record_ctrl.testcase.update_test_case(self.recorder.record_ctrl.temp_file,description)
                self.populate_test_suite_table(self.recorder.record_ctrl.testcase)
                test_case_id = self.recorder.record_ctrl.testcase.test_case_id
                test_case = self.test_manager.get_test_case(test_case_id)
                if not test_case.strSourcePath.startswith(self.get_workspace()):
                    destination_full_path = os.path.join(self.get_workspace(), "TestCase -" +test_case_id)
                    shutil.copytree(get_test_case_path(test_case_id), destination_full_path, dirs_exist_ok=True)
                    shutil.rmtree(get_test_case_path(test_case_id))  # Delete the source directory
                    self.test_manager.update_test_case_path(test_case_id, destination_full_path)
                    self.update_explorer(test_case_id)
                else:
                    self.debug_log.write_log("Already saved into workspace")
                    print("Already saved into workspace")
            except:
                m = dedent("Unkown error occured while loading script. Please try again.")
                QMessageBox.critical(self.Main, "Error", str(m))


    def fetch_reports(self):
        if self.get_workspace():
            try:
                file_path = self.get_workspace()
                for file in os.listdir(file_path):
                    if file.endswith(".pdf"):
                        # Get file details
                        pathname = os.path.join(self.get_workspace(), file)
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
            header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Second column auto-fits content
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
            view_btn.setFixedSize(80, 30) 
            view_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed) 
            view_btn.clicked.connect(lambda _, path=filepath: self.view_pdf(path))
            btn_layout.addWidget(view_btn)

            # Delete button
            del_btn = QPushButton("Delete")
            del_btn.setFixedSize(80, 30) 
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

    def store_failed_screenshots(self,test_case_id,imagepath,actual_image):
        #self.validation_failed_img[test_case_id] = [expected_image,actual_image]
        """Store screenshots in order for the same test case ID."""
        if test_case_id not in self.validation_failed_img:
            self.validation_failed_img[test_case_id] = []
        
        # Append the new screenshot pair in order
        self.validation_failed_img[test_case_id].append((imagepath, actual_image))

    def get_failed_screenshots(self, test_case_id):
        return self.validation_failed_img.get(test_case_id, [])
    
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