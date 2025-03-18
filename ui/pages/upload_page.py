from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFileDialog
from PyQt6.QtCore import Qt
from ui.components.drag_drop_section import DragDropSection
from core.file_processor import FileProcessor


class UploadPage(QWidget):
    """
    Widget for uploading files. This page allows users to upload files through a drag-and-drop interface,
    retrieve filter settings from a filters section, and process the file using a FileProcessor.
    """

    def __init__(self, filters_section):
        """
        Initialize the UploadPage widget.

        :param filters_section: Instance of the filters section to retrieve filter settings.
        """
        super().__init__()
        self.init_ui()
        self.filters_section = filters_section

        # Instantiate the FileProcessor and connect its signals to the corresponding handlers
        self.file_processor = FileProcessor()
        self.file_processor.progress.connect(self.drag_drop_section.update_progress)
        self.file_processor.finished.connect(self.on_processing_finished)

    def init_ui(self):
        """
        Set up the user interface for the upload page, including header text and the drag-and-drop section.
        """
        # Create the drag-and-drop section and pass the open_file_dialog callback
        self.drag_drop_section = DragDropSection(self.open_file_dialog)

        # Create the main layout for the widget
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        # Create the header label
        header = QLabel("Dateien hochladen")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font: 18pt 'Segoe UI'; color: #333333;")
        layout.addWidget(header)

        # Add the drag-and-drop section to the layout with extra space allocation
        layout.addWidget(self.drag_drop_section, stretch=3)
        layout.addStretch()
        self.setLayout(layout)

    def open_file_dialog(self, file_path: str = None) -> None:
        """
        Open a file dialog (if no file path is provided) and start the file processing,
        including retrieving filter values from the filters section.

        :param file_path: Optional file path. If provided, the file dialog is bypassed.
        """
        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Datei auswählen",
                "",
                "Alle Dateien (*);;PDF-Dateien (*.pdf);;Word-Dokumente (*.docx)"
            )
        if file_path:
            self.drag_drop_section.show_progress()

            # Retrieve filter values using the filters section
            specialization = self.filters_section.get_setting("specialization")
            exam_part = self.filters_section.get_setting("exam_part")
            file_type = self.filters_section.get_setting("file_type")
            year = self.filters_section.get_setting("year")
            period = self.filters_section.get_setting("period")

            # Process the file with the provided filter settings
            self.file_processor.process_file(file_path, specialization, exam_part, file_type, year, period)

    def on_processing_finished(self) -> None:
        """
        Handle actions to perform when the file processing is finished.
        """
        # Display a notification – currently just a simple console output
        print("Verarbeitung abgeschlossen")
