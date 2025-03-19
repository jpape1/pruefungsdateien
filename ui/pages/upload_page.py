from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFileDialog
from PyQt6.QtCore import Qt
from ui.components.drag_drop_section import DragDropSection
from core.file_processor import FileProcessor


class UploadPage(QWidget):
    """
    Widget for uploading files
    """

    def __init__(self, settings_section) -> None:
        """
        Initialize the UploadPage widget

        :param settings_section: Instance of the settings section to retrieve settings
        """
        super().__init__()
        self.init_ui()
        self.settings_section = settings_section

        self.file_processor = FileProcessor()
    def init_ui(self) -> None:
        """
        Set up the user interface for the upload page, including header text and the drag-and-drop section
        """
        self.drag_drop_section = DragDropSection(self.open_file_dialog)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        header = QLabel("Dateien hochladen")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font: 18pt 'Segoe UI'; color: #333333;")
        layout.addWidget(header)

        layout.addWidget(self.drag_drop_section, stretch=3)
        layout.addStretch()
        self.setLayout(layout)

    def open_file_dialog(self, file_path: str = None) -> None:
        """
        Open a file dialog and start the file processing, including retrieving settings values from the settings section.

        :param file_path: Optional file path - If provided, the file dialog is bypassed
        """
        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Datei auswählen",
                "",
                "Alle Dateien (*);;PDF-Dateien (*.pdf);;Word-Dokumente (*.docx)"
            )
        if file_path:
            specialization = self.settings_section.get_setting("specialization")
            exam_part = self.settings_section.get_setting("exam_part")
            file_type = self.settings_section.get_setting("file_type")
            year = self.settings_section.get_setting("year")
            period = self.settings_section.get_setting("period")

            self.file_processor.process_file(file_path, specialization, exam_part, file_type, year, period)

    def on_processing_finished(self) -> None:
        """
        Handle actions to perform when the file processing is finished.
        """
        # Display a notification – currently just a simple console output
        print("Verarbeitung abgeschlossen")
