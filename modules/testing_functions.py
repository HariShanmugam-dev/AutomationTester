from PySide6 import QtWidgets as qtw, QtCore as qtc
from . report_functions import *
from main import *
from skimage.metrics import structural_similarity
from .test_report_ui import Ui_TestReport
from . settings import *
import pyautogui
import concurrent.futures
import pygetwindow as gw
from pynput import keyboard, mouse
from pynput.mouse import Controller

class StartTestingDialog(qtw.QDialog):

    def __init__(self):
        super().__init__()

        # Dialog Title & Size
        self.setWindowTitle("Confirm Testing")
        self.setFixedSize(400, 250)

        # Main Text Message
        self.message = qtw.QLabel(
            "Testing will start in 10 seconds.\n"
            "Once testing is started, please refrain from using the mouse or keyboard.\n"
            "In the middle of testing process, if you wish to stop testing, press ESC to stop immediately.",
            self
        )
        self.message.setWordWrap(True)
        self.message.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)

        # Timer Label
        self.timer_label = qtw.QLabel("Starting in: 10s", self)
        self.timer_label.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setStyleSheet("font-weight: bold; color: red; font-size: 14px;")

        # Buttons (Proceed & Abort)
        self.proceed_button = qtw.QPushButton("Proceed")
        self.abort_button = qtw.QPushButton("Abort")

        # Button Layout
        button_layout = qtw.QHBoxLayout()
        button_layout.addWidget(self.proceed_button)
        button_layout.addWidget(self.abort_button)

        # Main Layout
        layout = qtw.QVBoxLayout(self)
        layout.addWidget(self.message)
        layout.addWidget(self.timer_label)
        layout.addLayout(button_layout)

        # Connect Buttons
        self.proceed_button.clicked.connect(self.proceed)
        self.abort_button.clicked.connect(self.abort)

        # Timer for countdown
        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.remaining_time = 10  # 10 seconds countdown
        self.timer.start(1000)  # Tick every 1 second

    def update_progress(self):
        """ Updates the progress bar and timer label every second """
        self.remaining_time -= 1
        self.timer_label.setText(f"Starting in: {self.remaining_time}s")

        if self.remaining_time <= 0:
            self.timer.stop()
            self.accept()  # Auto-close the dialog after countdown ends

    def proceed(self):
        """ User clicked Proceed, stop timer and return True """
        self.timer.stop()
        self.accept()

    def abort(self):
        """ User clicked Abort, stop timer and return False """
        self.timer.stop()
        self.reject()

class TestingManager(QObject):
    finished = Signal()
    progress = Signal(str, str)
    log      = Signal(str, str)
    error    = Signal(str, str)
    precheck = Signal(str, str)
    time_elapsed = Signal(str, str)
    report_testStarted = Signal(str, str)
    report_compareImages = Signal(object,object,object)
    report_writeReport = Signal(str, str, str)
    failedscreens = Signal(str,int,object)
    stopped = Signal()

    def __init__(self, test_manager_hndle, report_worker, test_cases):
        super().__init__()
        self.test_manager = test_manager_hndle
        self._is_running = True
        self.windowTitle = ""
        self._screenshots = []
        self.ssindex = 0
        self.report_worker = report_worker
        self.loaded_test_cases = test_cases
        self.image_iterator = None
        self.error_msg = "Unkown Error - Please check the logs."
        self.curr_test_start_time = None
        self.screenvalidationFailed = False

    def run(self):

        #create parallel running report thread
        self.report_thread = self.report_worker.thread()
        #connect to signals
        self.report_testStarted.connect(self.report_worker.test_started)
        self.report_compareImages.connect(self.report_worker.compare_screens)
        self.report_writeReport.connect(self.report_worker.write_report)
        #self.report_stop.connect(self.report_worker.finalize_report)
        self.report_thread.start()

        for test_case_id in self.loaded_test_cases:

            self.screenvalidationFailed = False
            if not self._is_running:
                break

            self.ssindex = 1

            test_case = self.test_manager.get_test_case(test_case_id)

            #report that test case started
            self.report_testStarted.emit(test_case.test_case_id, test_case.description)

            #clear the list
            self._screenshots = []

            self.precheck.emit(test_case.test_case_id, "⚠️In Progress")
            if not self.execute_pre_check(test_case):
                self.report_writeReport.emit(test_case.test_case_id,"Blocked","Pre_check Failed - Missing ref images")
                continue

            self.progress.emit(test_case.test_case_id, "⚠️In progress")
            print(f"Running test case {test_case.description}")
            self.curr_test_start_time = time.time()
            # Execute test case steps
            try:
                success = self.execute_test_case(test_case)
                
                execution_time = f"{int(time.time() - self.curr_test_start_time)}s"  # Calculate time taken per test
                self.time_elapsed.emit(test_case.test_case_id,execution_time)
                # Update test case status in UI and report manager
                if success == True and not self.screenvalidationFailed:
                    #self.test_manager.update_test_case_status(test_case.test_case_id, "✅Passed")
                    self.progress.emit(test_case.test_case_id, "Passed")
                    self.report_writeReport.emit(test_case.test_case_id,"Passed", "")
                elif self.screenvalidationFailed or success == False:
                    self.report_writeReport.emit(test_case.test_case_id,"Failed",self.error_msg)
                    #self.test_manager.update_test_case_status(test_case.test_case_id, "❌Failed")
                    self.progress.emit(test_case.test_case_id, "Failed")
                else:
                    self.report_writeReport.emit(test_case.test_case_id,"Stopped",self.error_msg)
                    self.progress.emit(test_case.test_case_id, "Stopped")
                    self.stopped.emit()
                    return

                
                    
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                self.report_writeReport.emit(test_case.test_case_id,"Failed","Unkown Error")
                self.progress.emit(test_case.test_case_id, "Failed")
                self.stop()
        self.finished.emit()
        #self.stop()

    def execute_pre_check(self, test_case):
        try:
            get_config(test_case.strSourcePath)
            TotalScreenshot = CONFIG.getint('DEFAULT','screen shot index')
            dirname = os.path.join(test_case.strSourcePath,f"screenshot-{test_case.test_case_id}")
            for filename in os.listdir(dirname):
                if filename.lower().endswith((".png")):
                    filepath = os.path.join(dirname, filename)
                    refImage = cv2.imread(filepath)
                    self._screenshots.append(refImage)
            
            if TotalScreenshot != len(self._screenshots):
                self.precheck.emit(test_case.test_case_id, f'Only {len(self._screenshots)}/{TotalScreenshot} are loaded ')
                self.precheck.emit(test_case.test_case_id, "❌Failed")
                self.progress.emit(test_case.test_case_id, "❌Failed")
                return False
            else:
                self.image_iterator = iter(self._screenshots)
                self.precheck.emit(test_case.test_case_id, "✅Passed")
                return True
        except Exception as e:
            self.error.emit(test_case.test_case_id,f"Error in getting screenshots: {e}")
            self.precheck.emit(test_case.test_case_id, "Failed")
            self.progress.emit(test_case.test_case_id, "Failed")
            return False
        
    def execute_test_case(self, test_case):
        """Executes all steps in a test case."""
        if not len(test_case.steps):
            return False
        for index, step in enumerate(test_case.steps):

            if not self._is_running:
                break  # Stop execution if requested

            if "#SCREENSHOT" in step:
                current_screen = pyautogui.screenshot(region=(self.activeWindow_left,self.activeWindow_top, self.activeWindow_width, self.activeWindow_height))
                self.validate_screenshot(test_case.test_case_id, current_screen)
                #if self.validate_screenshot(test_case.test_case_id, current_screen):
                #    continue
                #else:
                    #report worker emit to compare and write report
                #    return False

            elif "#SKIP" in step:
                print(f"⏭️ Skipping step {index + 1}")
                continue

            elif "#ACTIVEWINDOW=" in step:
                name = step.split("=",1)[1].strip()[1:-1]
                print(f"name = {name}")
                if(name != self.windowTitle):
                    retry = 0
                    while (retry < 5 and name != self.windowTitle):
                        activesessions = gw.getWindowsWithTitle(name)
                        print(f"activesessions = {activesessions}")
                        if not activesessions:
                            print(f"❌ Cannot activate the window - Failing Test case")
                        else:
                            self.activeWindow = activesessions[0]
                            print(f"self.activeWindow = {self.activeWindow}")
                            try:
                                self.activeWindow.activate()
                            except:
                                self.activeWindow.minimize()
                                self.activeWindow.activate()
                            print("after activate")
                            self.windowTitle = gw.getActiveWindowTitle()
                            if self.activeWindow.isMaximized:
                                self.activeWindow_left, self.activeWindow_top,self.activeWindow_width, self.activeWindow_height = 0, 0, self.activeWindow.width-20,self.activeWindow.height-20
                            else:
                                self.activeWindow_left, self.activeWindow_top,self.activeWindow_width, self.activeWindow_height = self.activeWindow.left+10, self.activeWindow.top+5, self.activeWindow.width-20,self.activeWindow.height-20
                        retry+=1

                    print("comparison")
                    if(name != self.windowTitle):
                        self.error_msg = "Test Case Failed due to no active window"
                        self.error.emit(test_case.test_case_id,self.error_msg)
                        return False
                    

            else:
                try:
                    exec(step)  # Execute pyautogui steps
                    print(f"{step}")
                    #time.sleep(0.2)
                except Exception as e:
                    print(f"❌ Error executing step {index + 1}: {e}")
                    return False  # Stop test case if an error occurs
                
        print(f"In execute test case - length - index{len(test_case.steps)} - {index}")
        if len(test_case.steps)-1 == index:
            return True
        else:
            return -1 
    
    #Function to validate and give the score for images
    def validate_screenshot(self,test_case_id, current_screen):
        """Compares a screenshot to determine pass/fail."""
        message = f"📸 Validating screenshot - {self.ssindex}"
        print(message)
        self.log.emit(test_case_id,message)
        current_image = np.array(current_screen)
        expected_image = next(self.image_iterator) #loads the next image

        current_image_gray = cv2.cvtColor(current_image,cv2.COLOR_RGB2GRAY)
        expected_image_gray = cv2.cvtColor(expected_image,cv2.COLOR_BGR2GRAY)
        
        (score, diff) = structural_similarity(expected_image_gray,current_image_gray, full=True)
        message = "Image Similarity: {:.4f}%".format(score * 100)
        self.log.emit(test_case_id,message)
        print(message)
        if score < 0.9999:
            self.screenvalidationFailed = True
            self.error_msg = "The screens does not match"
            self.error.emit(test_case_id,self.error_msg)
            self.report_compareImages.emit(diff,expected_image,current_image)
            self.failedscreens.emit(test_case_id,self.ssindex,current_image)
        
        self.ssindex+=1
            #return False
        #else:
        #    return True
        

    def stop(self):
        """Stops execution of all test cases."""
        #responding to STOP Testing from the application
        if self._is_running:
            self._is_running = False
        #if not self.report_worker == None:
            #self.report_writeReport(test_case.test_case_id,"Failed","Unkown Error")
            #self.report_stop.emit()
            #self.report_thread.wait()

class TestingCompleteDialog(qtw.QDialog, Ui_TestReport):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.default_report()
        # MINIMIZE
        #self.minimize.clicked.connect(lambda: self.showMinimized()) 
        # CLOSE window
        #self.close.clicked.connect(self.close)
        #self.accept.clicked.connect(self.close)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint  | Qt.FramelessWindowHint)
    def default_report(self):
        self.widget_2.setVisible(False)
        self.lbl_reports.setText("Report Not available. Please run the tests again to generate report")

    def load_report(self,test_report):
        self.widget_2.setVisible(True)
        summary = test_report["execution_summary"]
        formatted_time = summary["total_execution_time"]
        self.txt_elapsedTime.setText(formatted_time)
        self.txt_Passed.setText(f'{summary["passed"]}/{summary["total"]}') 
        self.txt_Failed.setText(f'{summary["failed"]}/{summary["total"]}')
        self.txt_Blocked.setText(f'{summary["blocked"]}/{summary["total"]}')
        self.lbl_reports.setText("Report generated!. Reports can be accessed in Reports Tab.")
        