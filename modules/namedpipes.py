from main import *
import win32pipe
import win32file
import threading
import time

class AutoTestPipeServer:
    def __init__(self, pipe_name=r'\.\pipe\AutoTestPipe'):
        self.pipe_name = pipe_name
        self.pipe = None
        self.connected = False
        self.stop_event = threading.Event()
        self.listener_thread = threading.Thread(target=self._listen_loop, daemon=True)

    def connectPOS(self):
        print("[AutoTestPipeServer] Starting pipe server...")
        self.listener_thread.start()

    def disconnectPOS(self):
        print("[AutoTestPipeServer] Stopping pipe server...")
        self.stop_event.set()
        if self.pipe:
            try:
                win32file.CloseHandle(self.pipe)
            except Exception as e:
                print(f"[AutoTestPipeServer] Error closing pipe: {e}")
        self.listener_thread.join()

    def _listen_loop(self):
        while not self.stop_event.is_set():
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
                self.connected = True
                print("[AutoTestPipeServer] POS connected!")

                while not self.stop_event.is_set():
                    try:
                        result, data = win32file.ReadFile(self.pipe, 64 * 1024)
                        message = data.decode('utf-8').strip()
                        print(f"[AutoTestPipeServer] Received: {message}")

                        if message == 'screenshot_ready':
                            self.on_screenshot_signal()

                    except Exception as e:
                        print(f"[AutoTestPipeServer] Read error or disconnected: {e}")
                        self.connected = False
                        break

            except Exception as e:
                print(f"[AutoTestPipeServer] Pipe error: {e}")
            finally:
                if self.pipe:
                    try:
                        win32file.CloseHandle(self.pipe)
                    except Exception:
                        pass
                self.pipe = None
                self.connected = False

    def on_screenshot_signal(self):
        # Override or connect this to your AUTOTEST trigger
        print("[AutoTestPipeServer] Triggering screenshot capture!")

    def is_connected(self):
        return self.connected