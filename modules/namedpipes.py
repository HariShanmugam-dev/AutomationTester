from main import *
import win32pipe
import win32file
import threading
import time

import ctypes

class AutoTestPipeServer:
    _instance = None  # Singleton instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AutoTestPipeServer, cls).__new__(cls)
            cls._instance.__init_pipes()  # Initialize only once
        return cls._instance
    
    def __init_pipes(self, pipe_name=r'\\.\pipe\AutoTestPipe'):
        self.pipe_name = pipe_name
        self.pipe = None
        self.connected = False
        self.stop_event = threading.Event()
        
    def connectPOS(self):
        # Connect POS when initializing
        connected = self._connect_pipe()
        if not connected:
            print("[AutoTestPipeServer] Could not connect to POS after retries.")

    def _connect_pipe(self):
        connection_result = threading.Event()

        def connect_thread():
            try:
                print("[AutoTestPipeServer] Creating named pipe...")
                self.pipe = win32pipe.CreateNamedPipe(
                    self.pipe_name,
                    win32pipe.PIPE_ACCESS_DUPLEX,
                    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
                    1, 65536, 65536, 0, None
                )

                print("[AutoTestPipeServer] Waiting for POS to connect...")
                win32pipe.ConnectNamedPipe(self.pipe, None)
                if not self.stop_event.is_set():
                    self.connected = True
                    print("[AutoTestPipeServer] POS connected successfully!")
                connection_result.set()

            except Exception as e:
                print(f"[AutoTestPipeServer] Connection attempt failed: {e}")
                self._close_pipe()
                connection_result.set()

        thread = threading.Thread(target=connect_thread)
        thread.start()

        connection_result.wait(timeout=5)

        if not self.connected:
            print("[AutoTestPipeServer] POS did not connect within 9 seconds — disconnecting.")
            self.stop_event.set()

            try:
                # Open a dummy client connection to unblock ConnectNamedPipe
                dummy_pipe = win32file.CreateFile(
                    self.pipe_name,
                    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                    0, None,
                    win32file.OPEN_EXISTING,
                    0, None
                )
                win32file.CloseHandle(dummy_pipe)
            except Exception as e:
                print(f"[AutoTestPipeServer] Dummy connect error (expected if no listener): {e}")

            self._close_pipe()
            return False

        return True

    def listen_for_screenshot_signal(self):
        if not self.connected:
            print("[AutoTestPipeServer] Cannot listen — POS not connected.")
            return False

        print("[AutoTestPipeServer] Listening for screenshot signals...")

        start_time = time.time()

        while not self.stop_event.is_set():
            elapsed = time.time() - start_time
            if elapsed > 30:
                print("[AutoTestPipeServer] No signal received in 30 seconds — disconnecting.")
                self.disconnectPOS()
                return False

            try:
                # Check if there's data available
                _, available, _ = win32pipe.PeekNamedPipe(self.pipe, 0)
                if available > 0:
                    result, data = win32file.ReadFile(self.pipe, 64 * 1024)
                    message = data.decode('utf-8').strip()
                    print(f"[AutoTestPipeServer] Received: {message}")

                    if message == 'screenshot_ready':
                        self.on_screenshot_signal()
                        return True  # Signal received

            except Exception as e:
                print(f"[AutoTestPipeServer] Read error or disconnected: {e}")
                self.connected = False
                break

            time.sleep(0.1)  # Small sleep to avoid tight CPU loop

        print("[AutoTestPipeServer] Stopped listening for signals.")
        return False

    def disconnectPOS(self):
        print("[AutoTestPipeServer] Stopping pipe server...")
        self.stop_event.set()
        self._close_pipe()

    def _close_pipe(self):
        if self.pipe:
            try:
                win32file.CloseHandle(self.pipe)
            except Exception as e:
                print(f"[AutoTestPipeServer] Error closing pipe: {e}")
        self.pipe = None

    def on_screenshot_signal(self):
        # Override this or connect to your AUTOTEST trigger
        print("[AutoTestPipeServer] Screenshot trigger received!")

    def is_connected(self):
        return self.connected
    