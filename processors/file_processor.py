import os
import shutil
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from datetime import datetime


class Worker(QObject):
    # Signals to communicate with the main thread
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    log = pyqtSignal(str)

    def __init__(self, file_path, specializations, exam_parts, file_types, year, period):
        """
        Worker class to handle file processing in a separate thread

        Args:
            file_path (str): Path to the file to be processed
            specializations (str): Selected specialization
            exam_parts (str): Selected exam part
            file_types (str): Selected file type
            year (str): Selected year
            period (str): Selected period
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
        Execute file processing logic step-by-step and emit progress updates
        """
        try:
            total_steps = 4
            current_step = 0

            self.log.emit(f"Verarbeitung von Datei begonnen: {self.file_path}")

            # Step 1: Validate and prepare
            self.log.emit("Schritt 1: Vorbereitung...")
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"Datei nicht gefunden: {self.file_path}")
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            # Step 2: Generate new file name and path
            self.log.emit("Schritt 2: Dateiname generieren...")
            original_filename = os.path.basename(self.file_path)
            file_extension = os.path.splitext(original_filename)[1].lower()

            date = datetime.now().strftime("%Y%m%d%H%M%S")
            new_filename = f"{self.file_types}_{date}{file_extension}"
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            # Step 3: Create destination directory
            self.log.emit("Schritt 3: Zielverzeichnis erstellen...")
            original_directory = os.path.dirname(self.file_path)
            base_destination = os.path.join(original_directory, self.year, self.specializations, self.exam_parts)
            os.makedirs(base_destination, exist_ok=True)
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))

            # Step 4: Move and rename file
            self.log.emit("Schritt 4: Datei verschieben und umbenennen...")
            destination_path = os.path.join(base_destination, new_filename)
            shutil.move(self.file_path, destination_path)
            self.log.emit(f"Datei umbenannt und verschoben nach: {destination_path}")
            current_step += 1
            self.progress.emit(int((current_step / total_steps) * 100))
        except Exception as e:
            # Log any error that occurs
            self.log.emit(f"Fehler bei der Verarbeitung der Datei: {str(e)}")
        finally:
            # Signal that the process has finished
            self.finished.emit()


class FileProcessor(QObject):
    # Signals to communicate with the UI
    log = pyqtSignal(str)
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self):
        """
        FileProcessor class manages Worker thread and handles file processing requests
        """
        super().__init__()
        self.thread = None
        self.worker = None

    def process_file(self, file_path, specializations, exam_parts, file_types, year, period):
        """
        Start the file processing in a separate thread

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

        # Initialize thread and worker
        self.thread = QThread()
        self.worker = Worker(file_path, specializations, exam_parts, file_types, year, period)

        # Connect signals
        self.worker.progress.connect(self.progress.emit)
        self.worker.log.connect(self.log.emit)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.finished.emit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.cleanup_thread)

        # Move worker to thread and start
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

    def cleanup_thread(self):
        """
        Clean up thread and worker references
        """
        self.thread = None
        self.worker = None