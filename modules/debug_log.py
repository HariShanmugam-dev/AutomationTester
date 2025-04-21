import os
from os import walk
import tempfile
import logging
from datetime import datetime, timedelta
import traceback
import shutil

# Define a persistent folder
my_temp_folder = os.path.join(tempfile.gettempdir(), "AutoTest")

class DebugLogger:
    """Logging class for writing logs to the AutoTEST output log file."""
    _instance = None  # Singleton instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DebugLogger, cls).__new__(cls)
            cls._instance.__init_logger()  # Initialize only once
        return cls._instance
    
    def __init_logger(self):
        """Initialize the logger, set up log file, and check for old logs."""
        self.log_folder = my_temp_folder  # Get temp directory
        self.log_file = os.path.join(self.log_folder, "outputlog.txt")

        # Ensure the Autotest directory exists
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

        # Check if log file exists and delete if it's older than 1 month
        self._check_old_logs()
        self._check_old_testcases()

        # Set up logging configuration
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="[%(asctime)s] %(message)s",
            datefmt="%Y/%m/%d %H:%M:%S",
        )

    def _check_old_testcases(self):
        for dirpath, dirnames, filenames in walk(my_temp_folder):
                for dirname in dirnames:  # Loop through each subdirectory
                    if dirname.startswith("TestCase"):
                        path = os.path.join(my_temp_folder, dirname)
                        shutil.rmtree(path)

    def _check_old_logs(self):
        """Check if log file is older than 1 month; delete if necessary."""
        if os.path.exists(self.log_file):
            file_creation_time = datetime.fromtimestamp(os.path.getctime(self.log_file))
            if datetime.now() - file_creation_time > timedelta(days=1): #can change it to 30 days
                os.remove(self.log_file)  # Delete the old log file
                open(self.log_file, "w").close()  # Create a fresh log file

    def write_log(self, message):
        """Write a log message to the output log file."""
        logging.info(message)

    def log_exception(self, error_message="Exception occurred"):
        """Capture and log application exceptions with traceback."""
        exception_details = traceback.format_exc()
        full_message = f"{error_message}\n{exception_details}"
        logging.error(full_message)
