# ui/main_window.py

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog,
    QSpacerItem, QSizePolicy, QAction, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

from config.config import Config
from processors.file_processor import FileProcessor

from .components.header import Header
from .components.filters import FiltersSection
from .components.drag_drop import DragDropSection
from .components.log_section import LogSection
from .components.status_bar import CustomStatusBar


class MainWindow(QMainWindow):
    """
    Main window
    """

    def __init__(self):
        """
        Initializes the main window, sets up UI components and layout
        """
        super().__init__()

        # Set window properties
        self.setWindowTitle("Prüfungsdateien hochladen")
        self.setWindowIcon(QtGui.QIcon('resources/icon.ico'))
        self.setGeometry(150, 150, 1000, 800)

        # Initialize UI components
        self.create_menu()
        self.header = Header()
        self.filters_section = FiltersSection()
        self.drag_drop_section = DragDropSection(self.open_file_dialog)
        self.log_section = LogSection()
        self.status_bar = CustomStatusBar()
        self.setStatusBar(self.status_bar)
        self.create_file_processor()
        self.apply_stylesheet()

        # Set the central widget layout
        self.init_layout()

    def init_layout(self):
        """
        Sets up main layout of the central widget
        """
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)

        # Add Header
        main_layout.addWidget(self.header)

        # Add Spacer
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Add Filters
        filters_container = QWidget()
        filters_container_layout = QHBoxLayout()
        filters_container_layout.addStretch()
        filters_container_layout.addWidget(self.filters_section)
        filters_container_layout.addStretch()
        filters_container.setLayout(filters_container_layout)

        main_layout.addWidget(filters_container)
        main_layout.addSpacerItem(QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Add Drag & Drop Section
        main_layout.addWidget(self.drag_drop_section, stretch=4)
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Add Log Section
        main_layout.addWidget(self.log_section, stretch=1)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def create_menu(self):
        """
        Creates the menu bar with File and Help menus
        """
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("Datei")

        # Open file action
        open_action = QAction("Datei öffnen...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file_dialog)
        file_menu.addAction(open_action)

        # Exit action
        exit_action = QAction("Beenden", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help menu
        help_menu = menu_bar.addMenu("Hilfe")

        # About action
        about_action = QAction("Über", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)

    def create_file_processor(self):
        """
        Initializes FileProcessor instance and connects its signals
        """
        self.file_processor = FileProcessor()
        self.file_processor.progress.connect(self.drag_drop_section.update_progress)
        self.file_processor.log.connect(self.log_section.append_log)
        self.file_processor.finished.connect(self.on_processing_finished)

    def apply_stylesheet(self):
        """
        Applies stylesheet to the main window
        """
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ecf0f1;
            }
        """)

    def open_file_dialog(self, file_path=None):
        """
        Opens a file dialog to allow the user to select a single file or handles a dropped file

        Args:
            file_path (str, optional): Path to the file to be processed
        """
        if not file_path:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getOpenFileName(
                self,
                "Datei auswählen",
                "",
                "Alle Dateien (*);;PDF-Dateien (*.pdf);;Word-Dokumente (*.docx)",
                options=options
            )
        
        if file_path:
            # Show progress bar
            self.drag_drop_section.show_progress()

            # Retrieve current filter values
            specializations = self.filters_section.findChild(QComboBox, "fachrichtung_combo").currentText()
            exam_parts = self.filters_section.findChild(QComboBox, "pruefungsteil_combo").currentText()
            file_types = self.filters_section.findChild(QComboBox, "dateityp_combo").currentText()
            year = self.filters_section.findChild(QComboBox, "jahr_combo").currentText()
            period = self.filters_section.findChild(QComboBox, "zeitraum_combo").currentText()

            # Pass filter values to the FileProcessor
            self.file_processor.process_file(file_path, specializations, exam_parts, file_types, year, period)


    def show_about_dialog(self):
        """
        Displays About dialog with application information
        """
        about_text = (
            "<h2>Prüfungsdateien automatisiert umbenennen und sortieren</h2>"
            "<p>Diese Anwendung ermöglicht das automatische Umbenennen und Sortieren von Prüfungsdateien.</p>"
            "<p>Version 1.0</p>"
            "<p>Entwickelt von Jonas Pape</p>"
        )
        QMessageBox.about(self, "Über", about_text)

    def on_processing_finished(self):
        """
        Slot that is called when file processing is completed
        """
        self.status_bar.update_status("Verarbeitung abgeschlossen.", 5000)
