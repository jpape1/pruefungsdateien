from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget
)
from PyQt6.QtGui import QIcon

# Import UI components and pages
from ui.components.sidebar import Sidebar
from ui.components.settings_section import SettingsSection
from ui.components.status_bar import CustomStatusBar

from ui.pages.upload_page import UploadPage
from ui.pages.settings_page import SettingsPage
from ui.pages.about_page import AboutPage

class MainWindow(QMainWindow):
    """
    The main window of the application with sidebar, stacked pages, and status bar.
    """
    def __init__(self) -> None:
        super().__init__()
        # Set up basic window properties (title, icon, geometry)
        self._setup_window_properties()
        # Initialize UI components such as sidebar, pages, and status bar
        self._init_ui_components()
        # Apply the custom stylesheet for visual styling
        self._apply_stylesheet()

    def _setup_window_properties(self) -> None:
        """
        Configure the window's title, icon, and size/position.
        """
        self.setWindowTitle("IHK Prüfungsdateien")
        self.setWindowIcon(QIcon("resources/icon.png"))
        self.setGeometry(150, 150, 1400, 900)

    def _init_ui_components(self) -> None:
        """
        Initialize UI components and set up the layout of the main window.
        """
        # Create the sidebar component with the current window as parent
        self.sidebar = Sidebar(self)
        # Initialize the stacked pages used for different sections
        self._init_stacked_pages()

        # Create and set a custom status bar at the bottom of the window
        self.status_bar = CustomStatusBar()
        self.setStatusBar(self.status_bar)

        # Create the main widget and layout: sidebar on the left, content on the right
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.sidebar, stretch=1)

        # Create a vertical layout for the content (stacked pages) with padding
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.addWidget(self.stacked_widget)
        main_layout.addLayout(content_layout, stretch=4)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Connect sidebar buttons to switch between pages in the stacked widget
        self.sidebar.btn_upload.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.sidebar.btn_settings.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.sidebar.btn_about.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

    def _init_stacked_pages(self) -> None:
        """
        Initialize and add the different pages to the stacked widget.
        """
        self.settings_section = SettingsSection()
        self.upload_page = UploadPage(self.settings_section)
        self.settings_page = SettingsPage(self.settings_section)
        self.about_page = AboutPage()

        # Create a QStackedWidget to manage multiple pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.upload_page)   # Index 0
        self.stacked_widget.addWidget(self.settings_page)   # Index 1
        self.stacked_widget.addWidget(self.about_page)      # Index 2

    def _apply_stylesheet(self) -> None:
        """
        Apply a custom stylesheet to the main window to adjust visual appearance.
        """
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QPushButton {
                transition: all 0.2s ease-in-out;
            }
        """)