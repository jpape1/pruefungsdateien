# processors/file_processor.py

import os
import shutil
import time
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from datetime import datetime


class FileProcessor(QObject):
    """
    FileProcessor for handling file operations
    Executes file processing in a separate thread to prevent blocking the UI
    Emits progress and log messages to the main window
    """

    # Signals emitted to the main window
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    log = pyqtSignal(str)

    def __init__(self):
        """
        Initializes FileProcessor
        """
        super().__init__()
        self.thread = None

    def process_file(self, file_path, specializations, exam_parts, file_types, year, period):
        """
        Starts the file processing in a separate thread

        Args:
            file_path (str): Path to the file to be processed
            specializations (str): Selected specialization
            exam_parts (str): Selected exam part
            file_types (str): Selected file type
            year (str): Selected year
            period (str): Selected period
        """
        if self.thread is not None and self.thread.isRunning():
            self.log.emit("Es läuft bereits ein anderer Prozess.")
            return

        # Initialize new thread
        self.thread = QThread()

        # Move this object to the new thread
        self.moveToThread(self.thread)

        # Connect the threads started signal to the run method with parameters
        self.thread.started.connect(lambda: self.run(file_path, specializations, exam_parts, file_types, year, period))

        # Connect the finished signal to quit and delete the thread
        self.finished.connect(self.thread.quit)
        self.finished.connect(self.thread.deleteLater)

        # Start the thread
        self.thread.start()

    def run(self, file_path, specializations, exam_parts, file_types, year, period):
        """
        Performs the actual file processing: renaming and moving the file based on the provided settings

        Args:
            file_path (str): Path to the file to be processed
            specializations (str): Selected specialization
            exam_parts (str): Selected exam part
            file_types (str): Selected file type
            year (str): Selected year
            period (str): Selected period
        """
        try:
            self.log.emit(f"Verarbeitung von Datei begonnen: {file_path}")

            # Determine new filename
            original_filename = os.path.basename(file_path)
            file_extension = os.path.splitext(original_filename)[1].lower()

            if not file_extension:
                file_extension = f".{file_types.lower()}"

            # Create new filename
            date = datetime.now().strftime("%Y%m%d%H%M%S")
            new_filename = f"{file_types}_{date}{file_extension}"

            # Determine original directory
            original_directory = os.path.dirname(file_path)

            # Determine destination directory within original directory
            base_destination = os.path.join(original_directory, year, specializations, exam_parts)

            # Create destination directory if it does not exist
            os.makedirs(base_destination, exist_ok=True)

            # Full destination path
            destination_path = os.path.join(base_destination, new_filename)

            # Move and rename file
            shutil.move(file_path, destination_path)
            self.log.emit(f"Datei umbenannt und verschoben nach: {destination_path}")

            # Simulate progress  (no real progress indication, just a delay)
            for i in range(101):
                time.sleep(0.01) 
                self.progress.emit(i)

        except Exception as e:
            # Log error message in case of an exception
            self.log.emit(f"Fehler bei der Verarbeitung der Datei: {str(e)}")
        finally:
            self.finished.emit()