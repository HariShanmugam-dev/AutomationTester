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
        self.recent_files_file = os.path.join(self.log_folder, "recent_files.txt")

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
            if datetime.now() - file_creation_time > timedelta(days=30): #can change it to 30 days
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

    def delete_recent_file(self, file_path):
        """Remove a recent file entry by file path."""
        recent_files = self.read_recent_files()

        # Find and remove the entry
        updated_files = [rf for rf in recent_files if rf["file_path"] != file_path]

        if len(updated_files) == len(recent_files):
            self.write_log(f"No recent file found for removal: {file_path}")
        else:
            self.write_log(f"Removed recent file: {file_path}")

        # Write back updated list
        with open(self.recent_files_file, "w", encoding="utf-8") as f:
            for entry in updated_files:
                line = f'{entry["project_name"]}|{entry["file_path"]}|{entry["opened_date"]}\n'
                f.write(line)
                
    def write_recent_file(self, project_name, file_path):
        """Add or update a recent file entry with project name, path, and opened date."""
        recent_files = self.read_recent_files()

        # Check if file already exists
        existing_entry = next((rf for rf in recent_files if rf["file_path"].upper() == file_path.upper()), None)

        if existing_entry:
            # Remove old entry
            recent_files.remove(existing_entry)
            self.write_log(f"Updated recent file: {file_path}")

        # Add new/updated entry at top
        new_entry = {
            "project_name": project_name,
            "file_path": file_path,
            "opened_date": datetime.now().strftime("%Y-%m-%d")
        }
        recent_files.insert(0, new_entry)

        # Keep only latest 10
        recent_files = recent_files[:10]

        # Write back to file
        with open(self.recent_files_file, "w", encoding="utf-8") as f:
            for entry in recent_files:
                line = f'{entry["project_name"]}|{entry["file_path"]}|{entry["opened_date"]}\n'
                f.write(line)

    def read_recent_files(self):
        """Read and return recent files as a list of dicts."""
        if not os.path.exists(self.recent_files_file):
            return []

        recent_files = []
        with open(self.recent_files_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    recent_files.append({
                        "project_name": parts[0],
                        "file_path": parts[1],
                        "opened_date": parts[2]
                    })
        return recent_files