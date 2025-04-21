from main import *
from textwrap import dedent
from . recorder_ui import Ui_RecorderWindow
from . test_case import TestCase, TestCaseManager
from . settings import *
import time
import os
from datetime import datetime
from threading import Thread
from ctypes import windll
import pyautogui
import concurrent.futures
import pygetwindow as gw
from pynput import keyboard, mouse
from pynput.mouse import Controller
from . debug_log import *
import math
from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
# Define the path to the temporary file
def get_test_case_id():
    return datetime.today().strftime('%Y%m%d%H%M')

def get_temp_folder_path(test_case_id):
    return os.path.join(my_temp_folder, f"TestCase -{test_case_id}")

def get_test_case_path(test_case_id):
    return os.path.join(my_temp_folder, f"TestCase -{test_case_id}")

def get_temp_file_path(test_case_id):
    return os.path.join(get_temp_folder_path(test_case_id), f"TestCase -{test_case_id}.json")

def get_screenshot_path(test_case_id):
    return os.path.join(get_temp_folder_path(test_case_id), f"screenshot-{test_case_id}")

def get_header(test_case_id):
    return f"#TestCase ID - {test_case_id}\n"


class Recorder(QWidget, Ui_RecorderWindow):


    def __init__(self, main_window, control):
        super().__init__()
        self.debug_log = DebugLogger()
        self.setupUi(self)
        self.main_window = main_window  # Store reference to MainWindow
        self.control = control
        self.record_ctrl = RecordCtrl(self)

        self.btn_play.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_reset.setEnabled(False)
        # MINIMIZE
        self.minimizeAppBtn.clicked.connect(lambda: self.showMinimized()) 
        # CLOSE APPLICATION
        self.closeAppBtn.clicked.connect(lambda: self.close_recorder())

        self.play_ctrl = PlayCtrl()
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint| Qt.FramelessWindowHint)
        self.btn_start.clicked.connect(self.toggle_recording)
        self.btn_play.clicked.connect(self.start_playback)
        self.btn_save.clicked.connect(self.save_file)
        self.btn_reset.clicked.connect(self.reset_recorder)
        self.old_pos = None

        self.timer = QTimer(self)                 # Timer to update the label
        self.time_elapsed = QTime(0, 0)           # Store elapsed time
        self.timer.timeout.connect(self.update_timer_label)

        # In your menu creation:
        self.toggleBarcode = QAction("Enabled Barcode Scanning", self.settings)  # Store the QAction as an instance variable

        # Create a menu
        menu = QMenu(self.settings)
        menu.setStyleSheet("background-color: #05151f;")
        # Add actions to the menu
        menu.addAction(self.toggleBarcode)
        self.toggleBarcode.triggered.connect(self.toggle_barcode_mode)

        # Connect the tool button to show the menu
        self.settings.setMenu(menu)
        

    def toggle_barcode_mode(self):
        #Toggle barcode scanning mode
        self.record_ctrl.barcode_mode = not self.record_ctrl.barcode_mode
        enabled = self.record_ctrl.barcode_mode  # Get the current state

        if enabled:
            self.toggleBarcode.setText("Disable Barcode Scanning")  # Update menu text
        else:
            self.toggleBarcode.setText("Enable Barcode Scanning")  # Update menu text

        print(f"Barcode mode {'enabled' if enabled else 'disabled'}")
        self.debug_log.write_log(f"Barcode mode {'enabled' if enabled else 'disabled'}")

    def toggle_recording(self):
        if self.record_ctrl.recording:
            icon5 = QIcon()
            icon5.addFile(u":/Icons/record_start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.btn_start.setIcon(icon5)
            self.record_ctrl.stop_recording()

            self.btn_start.setEnabled(False)
            self.btn_play.setEnabled(True)
            self.btn_save.setEnabled(True)
            self.btn_reset.setEnabled(True)
            self.timer.stop()  
            self.lbl_message.setText("Would you like to play and verify?")
        else:
            icon5 = QIcon()
            icon5.addFile(u":/Icons/record_stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.btn_start.setIcon(icon5)
            self.record_ctrl.start_recording()
             # Reset and start the timer
            self.time_elapsed = QTime(0, 0)       # Reset time to 00:00
            self.lbl_timer.setText("00:00")       # Reset the label
            self.timer.start(1000)                # Update every 1 second
            self.lbl_message.setText("Recording Started")
            self.btn_play.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.btn_reset.setEnabled(False)

    def update_timer_label(self):
        #Update the QLabel with the elapsed time.
        self.time_elapsed = self.time_elapsed.addSecs(1)  # Increment by 1 second
        self.lbl_timer.setText(self.time_elapsed.toString("mm:ss"))

    def start_playback(self):
        self.lbl_message.setText("Playing..")
        self.play_ctrl.start_playback(self.record_ctrl.current_TestCaseId)
        self.lbl_message.setText("Would you like to play and verify?")
    
    def save_file(self):
        try:
            self.main_window.show()
            self.main_window.raise_()
            self.main_window.activateWindow()
            self.main_window.ui.initialFrame.setEnabled(False)
            self.main_window.ui.initialFrame.setVisible(False)
            self.main_window.ui.finalFrame.setEnabled(True)
            self.main_window.ui.finalFrame.setVisible(True)
            description = "Test Case - " + self.record_ctrl.current_TestCaseId
            self.main_window.ui.description.setText(description)
            self.load_screenshot()
            #send description and everything back to main window
            self.main_window.recorder_screen_state = True #preserve state
            self.close()
        except:
            print("Error saving file.")
            self.debug_log.write_log("Error saving file.")
            self.lbl_message.setText("Error saving file.")
            self.main_window.ui.label_message.setText("Error saving file.")
            return
        

    def load_screenshot(self):
        directory = self.record_ctrl.temp_screenshotpath
        # --- Clear previous content ---
        if self.main_window.ui.gridLayout_15 is not None:
            # Remove all widgets from the layout
            for i in reversed(range(self.main_window.ui.gridLayout_15.count())):
                widget = self.main_window.ui.gridLayout_15.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
        
        # --- Create a new layout for the screenshots ---
        self.main_window.ui.gridLayout_15 = QGridLayout(self.main_window.ui.scrollAreaScreenshots)
        self.main_window.ui.gridLayout_15.setSpacing(10)
        self.main_window.ui.gridLayout_15.setContentsMargins(10, 10, 10, 10)
        self.main_window.ui.scrollAreaScreenshots.setWidgetResizable(True)
        self.main_window.ui.scrollAreaScreenshots.setStyleSheet("background-color: #05151f;")
        self.main_window.ui.scrollAreaScreenshots.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_window.ui.scrollAreaScreenshots.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Load images
        screenshots = [f for f in os.listdir(directory) if f.endswith((".png", ".jpg", ".jpeg"))]
        screenshots.sort()

        if not screenshots:
            print("No screenshots found.")
            self.debug_log.write_log("No screenshots found.")
            return

        # --- Configure the scroll area ---
        container_widget = QWidget()
        container_layout = QGridLayout(container_widget)
        container_layout.setSpacing(10)
        container_layout.setContentsMargins(10, 10, 10, 10)

        # --- Dynamically calculate image size ---
        max_cols = 2
        max_rows = 2

        # Get the available scroll area size dynamically
        available_width = self.main_window.ui.scrollAreaScreenshots.width() - 40
        available_height = self.main_window.ui.scrollAreaScreenshots.height() - 40

        img_width = available_width // max_cols
        img_height = available_height // max_rows

        # --- Display images in a scrollable grid ---
        row, col = 0, 0

        for idx, filename in enumerate(screenshots):
            filepath = os.path.join(directory, filename)

            # Create image label
            label = QLabel()
            pixmap = QPixmap(filepath)
            label.setPixmap(pixmap.scaled(img_width, img_height, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            label.setAlignment(Qt.AlignCenter)
            label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Add label to grid
            container_layout.addWidget(label, row, col)

            col += 1
            if col >= max_cols:
                col = 0
                row += 1

        # Set the scrollable widget and add the grid layout
        container_widget.setLayout(container_layout)
        self.main_window.ui.scrollAreaScreenshots.setWidget(container_widget)

    def reset_recorder(self):
        self.lbl_message.setText("Reset completed.Start Recording!")
        self.record_ctrl._capture = [get_header(self.record_ctrl.current_TestCaseId)]
        self.record_ctrl._screenshots = []
        self.record_ctrl.screenshot_index = 1
        self.windowTitle = ""
        shutil.rmtree(self.record_ctrl.temp_screenshotpath)
        self.btn_start.setEnabled(True)
        self.btn_play.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_reset.setEnabled(False)
        self.lbl_timer.setText("00:00")
    def close_recorder(self):
        if self.record_ctrl.recording:
            self.record_ctrl.stop_recording()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            self.move(event.globalPosition().toPoint() - self.old_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None
            event.accept()

class RecordCtrl(QObject):
    NUMKEYPAD_KEY = {
        96: 'num0',
        97: 'num1',
        98: 'num2',
        99: 'num3',
        100: 'num4',
        101: 'num5',
        102: 'num6',
        103: 'num7',
        104: 'num8',
        105: 'num9',
        
    }
    LOOKUP_SPECIAL_KEY = {
        keyboard.Key.alt: 'alt',
        keyboard.Key.alt_l: 'altleft',
        keyboard.Key.alt_r: 'altright',
        keyboard.Key.backspace: 'backspace',
        keyboard.Key.caps_lock: 'capslock',
        keyboard.Key.ctrl: 'ctrlleft',
        keyboard.Key.ctrl_r: 'ctrlright',
        keyboard.Key.delete: 'delete',
        keyboard.Key.down: 'down',
        keyboard.Key.end: 'end',
        keyboard.Key.enter: 'enter',
        keyboard.Key.esc: 'esc',
        keyboard.Key.f1: 'f1',
        keyboard.Key.f2: 'f2',
        keyboard.Key.f3: 'f3',
        keyboard.Key.f4: 'f4',
        keyboard.Key.f5: 'f5',
        keyboard.Key.f6: 'f6',
        keyboard.Key.f7: 'f7',
        keyboard.Key.f8: 'f8',
        keyboard.Key.f9: 'f9',
        keyboard.Key.f10: 'f10',
        keyboard.Key.f11: 'f11',
        keyboard.Key.f12: 'f12',
        keyboard.Key.home: 'home',
        keyboard.Key.left: 'left',
        keyboard.Key.page_down: 'pagedown',
        keyboard.Key.page_up: 'pageup',
        keyboard.Key.right: 'right',
        keyboard.Key.shift: 'shift',
        keyboard.Key.shift_r: 'shiftright',
        keyboard.Key.space: 'space',
        keyboard.Key.tab: 'tab',
        keyboard.Key.up: 'up',
    }
    def __init__(self, recorder_window):
        super().__init__()
        self._screenshots = []
        self._lastx, self._lasty = pyautogui.position()
        self.recording = False
        self.last_time = time.perf_counter()
        self._error = "### This key is not supported yet"
        self.windowTitle = ""
        self.current_TestCaseId = get_test_case_id()
        self._capture = [get_header(self.current_TestCaseId)]
        self.testcase = None
        self.temp_folder = get_temp_folder_path(self.current_TestCaseId)
        self.temp_file = get_temp_file_path(self.current_TestCaseId)
        self.temp_screenshotpath = get_screenshot_path(self.current_TestCaseId)
        self.screenshot_index = 1
        self.executor = None
        self.debug_log = DebugLogger()
        # Barcode handling variables
        self.barcode_mode = False           # Toggle for barcode scanning
        self.barcode_buffer = []            # Buffer for barcode data
        self.barcode_last_time = time.perf_counter()  # For detecting gaps
        self.barcode_timeout = 0.05         # Timeout between key presses
        self.mouse_down = False
        self.mouse_drag = False
        self.mouse_drag_duration = 0.0
        self.recorder_window = recorder_window

    def start_recording(self):
        self.recording = True
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
        self.listener_mouse = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.listener_keyboard = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener_mouse.start()
        self.listener_keyboard.start()
        self.last_time = time.perf_counter()

    def stop_recording(self):
        self.recording = False
        if self.executor:
            self.executor.shutdown(wait=True)  # Wait for all tasks to finish
            self.executor = None
        try:
            self.save_screenshot()
            description = f"Test Case - {self.current_TestCaseId}"
            # Remove the recording trigger event
            self._capture.pop()
            self._capture.pop()
            self.testcase = TestCase(self.current_TestCaseId,description,self._capture)

            with open(self.temp_file, 'w') as f:
                json.dump(self.testcase.to_dict(), f, indent=4)  # Save as JSON
            get_config(self.temp_folder)
            CONFIG["DEFAULT"]["screen shot index"] = str(self.screenshot_index-1)
            save_config()
        except Exception as e:
            self.debug_log.write_log(f"Error during stop recording: {e}")
            print(f"Error during stop recording: {e}")

    def capture_screenshot(self):
        if not self.recording:
            return False
        try:
            time.sleep(0.3)
            b = time.perf_counter()
            timeout = float(b - self.last_time)
            if timeout > 0.0:
                self._capture.append(f"time.sleep({timeout})")
            self.last_time = b

            self.activeWindow = gw.getWindowsWithTitle(self.windowTitle)[0]
            # Get exact window bounds
            if self.activeWindow:
                left, top, width, height = (
                        self.activeWindow.left, self.activeWindow.top, 
                        self.activeWindow.width, self.activeWindow.height
                    )
                #modify the bounds by cutting the edges
                if self.activeWindow.isMaximized:
                    left, top,width, height = 0, 0, width-20,height-20
                else:
                    left, top,width, height = left+10, top+5, width-20,height-20
                self._capture.append(f"#SCREENSHOT")
                self.recorder_window.showMinimized()
                captureScreen = pyautogui.screenshot(region=(left,top, width, height))
                self.recorder_window.showNormal()
                self._screenshots.append(captureScreen)
                self.debug_log.write_log("Screenshot captured")
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
            self.debug_log.write_log(f"Error capturing screenshot: {e}")

    def save_screenshot(self):
        screenshotlist = []
        if not os.path.exists(self.temp_screenshotpath):
            os.makedirs(self.temp_screenshotpath)
        for i, screenshot in enumerate(self._screenshots):
            ssname = f"screenshot_{self.screenshot_index:04d}.png"
            filename = os.path.join(self.temp_screenshotpath, ssname)
            screenshotlist.append(ssname)
            try:
                screenshot.save(filename)
                self.screenshot_index += 1
            except Exception as e:
                print(f"Failed to save screenshot {ssname}: {e}")
                self.debug_log.write_log(f"Failed to save screenshot {filename}: {e}")
        return screenshotlist
    

    def on_move(self, x, y):
        if not self.recording:
            return False
        if self.mouse_down:
            self.mouse_drag = True
            b = time.perf_counter()
            timeout = float(b - self.last_time)
            if timeout > 0.0:
                self.mouse_drag_duration += timeout
            self.last_time = b
        else:
            b = time.perf_counter()
            timeout = float(b - self.last_time)
            if timeout > 0.0:
                self._capture.append(f"time.sleep({timeout})")
            self.last_time = b
            self._capture.append(f"pyautogui.moveTo({x}, {y}, _pause=False)")

    def get_active_window(self):
        self.windowTitle = gw.getActiveWindowTitle()
        if not "Recorder" in self.windowTitle:
            last_line = self._capture.pop()
            if "mouseDown" in last_line:
                self._capture.append(f'#ACTIVEWINDOW="{self.windowTitle}"')
                self._capture.append(last_line)
            else:
                self._capture.append(last_line)
                self._capture.append(f'#ACTIVEWINDOW="{self.windowTitle}"')
            return True
        return False
    
    def on_click(self, x, y, button, pressed):
        #Triggered by a mouse click.
        if not self.recording:
            return False
        
        if pressed:
            self.mouse_down = True
            if button == mouse.Button.left:
                self.write_mouse_action(
                    move="mouseDown", parameters=f"{x}, {y}, 'left'")
            elif button == mouse.Button.right:
                self.write_mouse_action(
                    move="mouseDown", parameters=f"{x}, {y}, 'right'")
            elif button == mouse.Button.middle:
                self.write_mouse_action(
                    move="mouseDown", parameters=f"{x}, {y}, 'middle'")
            else:
                print("Mouse Button not recognized")
                self.debug_log.write_log("Mouse Button not recognized")
        else:
            if self.mouse_drag:
                self._capture.append(f"pyautogui.dragTo({x}, {y}, duration={self.mouse_drag_duration},_pause=False)")
                self.mouse_drag = False
                self.mouse_drag_duration = 0.0
            self.mouse_down = False
            bActiveWindow = self.get_active_window()
            if button == mouse.Button.left:
                self.write_mouse_action(
                    move="mouseUp", parameters=f"{x}, {y}, 'left'")
            elif button == mouse.Button.right:
                self.write_mouse_action(
                    move="mouseUp", parameters=f"{x}, {y}, 'right'")
            elif button == mouse.Button.middle:
                self.write_mouse_action(
                    move="mouseUp", parameters=f"{x}, {y}, 'middle'")
            else:
                print("Mouse Button not recognized")
                self.debug_log.write_log("Mouse Button not recognized")
            if bActiveWindow:
                self.executor.submit(self.capture_screenshot)

    def on_scroll(self, x, y, dx, dy):
        
        if not self.recording:
            return False

        b = time.perf_counter()
        timeout = float(b - self.last_time)

        if timeout > 0.0:
            self._capture.append(f"time.sleep({timeout})")
        self.last_time = b
        self._capture.append(f"mouse.Controller().scroll({dx}, {dy})")

    def on_press(self, key):
        if not self.recording:
            return False

        b = time.perf_counter()
        timeout = float(b - self.last_time)

        if timeout > 0.0:
            self._capture.append(f"time.sleep({timeout})")
        self.last_time = b

        try:
            # Barcode mode logic
            if self.barcode_mode:
                # Record barcode keys together
                if time.perf_counter() - self.barcode_last_time > self.barcode_timeout:
                    if self.barcode_buffer:
                        # Save the entire barcode as a single entry
                        barcode = ''.join(self.barcode_buffer)
                        self.write_keyboard_action(move="typewrite", key=barcode)
                        self.write_keyboard_action(move="keyDown", key="enter")
                        self.barcode_buffer = []

                self.barcode_last_time = time.perf_counter()

            # Regular key recording
            if hasattr(key, 'char') and key.char:
                if self.barcode_mode:
                    self.barcode_buffer.append(key.char)  # Append key to buffer
                else:
                    self.write_keyboard_action(move='keyDown', key=key.char)
            
            elif hasattr(key, 'vk') and key.vk is not None:
                key_name = self.NUMKEYPAD_KEY.get(key.vk, self._error)
                if self.barcode_mode:
                    self.barcode_buffer.append(key_name)  # Append numpad key to buffer
                else:
                    self.write_keyboard_action(move="keyDown", key=key_name)
                    
            else:
                key_name = self.LOOKUP_SPECIAL_KEY.get(key, self._error)
                if self.barcode_mode and self.barcode_buffer.count:
                    barcode = ''.join(self.barcode_buffer)
                    self.write_keyboard_action(move="typewrite", key=barcode)
                    self.write_keyboard_action(move="keyDown", key=key_name)
                    self.barcode_buffer = []
                else:
                    self.write_keyboard_action(move="keyDown", key=key_name)

        except AttributeError:
            key_name = self.LOOKUP_SPECIAL_KEY.get(key, self._error)
            if self.barcode_mode:
                self.barcode_buffer.append(key_name)
            else:
                self.write_keyboard_action(move="keyDown", key=key_name)

    def on_release(self, key):
        #Triggered by a key released.
        if not self.recording:
            return False

        if self.barcode_mode:
            key_name = self.LOOKUP_SPECIAL_KEY.get(key, self._error)
            if key_name:
                self.write_keyboard_action(move="keyUp", key=key_name)
            return

        if hasattr(key, 'char') and key.char:
            self.write_keyboard_action(move='keyUp', key=key.char)
        elif hasattr(key, 'vk') and key.vk is not None:
            key_name = self.NUMKEYPAD_KEY.get(key.vk, self._error)
            self.write_keyboard_action(move="keyUp", key=key_name)
        else:
            key_name = self.LOOKUP_SPECIAL_KEY.get(key, self._error)
            self.write_keyboard_action(move="keyUp", key=key_name)
        if key == keyboard.Key.enter:
            self.executor.submit(self.capture_screenshot)

    def write_mouse_action(self, engine="pyautogui", move="", parameters=""):
        def isinteger(s):
            try:
                int(s)
                return True
            except:
                return False
        if move == "moveTo":
            coordinates = [int(s)
                           for s in parameters.split(", ") if isinteger(s)]
            #if abs(coordinates[0] - self._lastx) < self.mouse_sensibility \
            #   and abs(coordinates[1] - self._lasty) < self.mouse_sensibility:
            #    return
            #else:
            self._lastx, self._lasty = coordinates
        self._capture.append(engine + "." + move + '(' + parameters + ',_pause=False)')

    def write_keyboard_action(self, engine="pyautogui", move="", key=""):
        #Write the keyboard action to the capture log.
        if self.barcode_mode and move == "keyDown":
            # Skip individual keyDown events in barcode mode
            return

        suffix = f"({repr(key)})"
        
        # Handle multiple key presses efficiently
        if move == "keyDown" and len(self._capture) > 0 and move + suffix in self._capture[-1]:
            move = 'press'
            self._capture[-1] = engine + "." + move + suffix
        else:
            self._capture.append(engine + "." + move + suffix)

class PlayCtrl:
    def __init__(self):
        self.play_thread = None
        self.debug_log = DebugLogger()

    def play(self, test_case_id):
        if os.path.exists(get_temp_file_path(test_case_id)):
            with open(get_temp_file_path(test_case_id), 'r') as f:
                test_case = json.load(f)
            steps = test_case.get("TestCaseSteps",[])
            if not steps:
                print(f"No steps found in test case {test_case_id}.") #TODO error logging
                self.debug_log.write_log(f"No steps found in test case {test_case_id}.")
                return
            for step in steps:
                try:
                    if not step.startswith("#"):
                        exec(step)  # Executes Python commands (only if safe)
                    
                except Exception as e:
                    print(f"Error executing step '{step}': {e}")
                    self.debug_log.write_log(f"TC - {test_case_id}: Error executing step '{step}': {e}")

    def start_playback(self, test_case_id):
        self.play_thread = Thread(target=self.play(test_case_id))
        self.play_thread.start()


