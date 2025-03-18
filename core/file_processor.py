import os
import shutil
from PyQt6.QtCore import QObject, pyqtSignal, QThread
from datetime import datetime

class Worker(QObject):
    """
    Worker class to process a file in a separate thread.
    """
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    log = pyqtSignal(str)

    def __init__(self, file_path, specializations, exam_parts, file_types, year, period):
        """
        Initializes the worker with the file processing parameters.
        :param file_path: Path of the file to be processed.
        :param specializations: Selected specialization.
        :param exam_parts: Selected exam part.
        :param file_types: Selected file type.
        :param year: Selected year.
        :param period: Selected period.
        """
        super().__init__()
        self.file_path = file_path
        self.specializations = specializations
        self.exam_parts = exam_parts
        self.file_types = file_types
        self.year = year
        self.period = period

    def run(self):
        """
        Executes file processing in steps and emits progress updates.
        """
        try:
            total_steps = 4
            current_step = 0

            self.log.emit(f"Started processing file: {self.file_path}")

            # Step 1: Validate file existence
            self.log.emit("Step 1: Preparation...")
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"File not found: {self.file_path}")
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            # Step 2: Generate a new filename based on the current date and file type
            self.log.emit("Step 2: Generating new filename...")
            original_filename = os.path.basename(self.file_path)
            file_extension = os.path.splitext(original_filename)[1].lower()
            date = datetime.now().strftime("%Y%m%d%H%M%S")
            new_filename = f"{self.file_types}_{date}{file_extension}"
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            # Step 3: Create the destination directory structure
            self.log.emit("Step 3: Creating destination directory...")
            original_directory = os.path.dirname(self.file_path)
            base_destination = os.path.join(original_directory, self.year, self.specializations, self.exam_parts)
            os.makedirs(base_destination, exist_ok=True)
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            # Step 4: Move and rename the file to the new destination
            self.log.emit("Step 4: Moving and renaming the file...")
            destination_path = os.path.join(base_destination, new_filename)
            shutil.move(self.file_path, destination_path)
            self.log.emit(f"File renamed and moved to: {destination_path}")
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))
        except Exception as e:
            self.log.emit(f"Error processing file: {str(e)}")
        finally:
            self.finished.emit()


class FileProcessor(QObject):
    """
    Manages file processing in a separate thread using the Worker.
    """
    log = pyqtSignal(str)
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self):
        """
        Initializes the file processor.
        """
        super().__init__()
        self.thread = None
        self.worker = None

    def process_file(self, file_path, specializations, exam_parts, file_types, year, period):
        """
        Starts processing the specified file in a new thread.
        :param file_path: Path of the file to process.
        :param specializations: Selected specialization.
        :param exam_parts: Selected exam part.
        :param file_types: Selected file type.
        :param year: Selected year.
        :param period: Selected period.
        """
        if self.thread is not None and self.thread.isRunning():
            self.log.emit("Another process is already running.")
            return

        # Initialize the thread and worker
        self.thread = QThread()
        self.worker = Worker(file_path, specializations, exam_parts, file_types, year, period)

        # Connect worker signals to propagate events
        self.worker.progress.connect(self.progress.emit)
        self.worker.log.connect(self.log.emit)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.finished.emit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.cleanup_thread)

        # Move the worker to the thread and start processing
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def cleanup_thread(self):
        """
        Cleans up thread and worker references after processing.
        """
        self.thread = None
        self.worker = None
