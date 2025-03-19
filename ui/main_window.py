from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget
)
from PyQt6.QtGui import QIcon

# Import UI components and pages
from ui.components.sidebar import Sidebar
from ui.components.settings_section import SettingsSection

from ui.pages.upload_page import UploadPage
from ui.pages.settings_page import SettingsPage
from ui.pages.about_page import AboutPage

class MainWindow(QMainWindow):
    """
    The main window of the application with sidebar, stacked pages
    """
    def __init__(self) -> None:
        super().__init__()
        self._setup_window_properties()
        self._init_ui_components()

    def _setup_window_properties(self) -> None:
        """
        Configure the windows title, icon, and size/position
        """
        self.setWindowTitle("IHK Prüfungsdateien")
        self.setWindowIcon(QIcon("resources/icon.png"))
        self.setGeometry(150, 150, 1400, 900)

    def _init_ui_components(self) -> None:
        """
        Initialize UI components and set up the layout of the main window
        """
        self.sidebar = Sidebar(self)
        self._init_stacked_pages()


        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.sidebar, stretch=1)

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.addWidget(self.stacked_widget)
        main_layout.addLayout(content_layout, stretch=4)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.sidebar.btn_upload.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.sidebar.btn_settings.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.sidebar.btn_about.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

    def _init_stacked_pages(self) -> None:
        """
        Initialize and add the different pages to the stacked widget
        """
        self.settings_section = SettingsSection()
        self.upload_page = UploadPage(self.settings_section)
        self.settings_page = SettingsPage(self.settings_section)
        self.about_page = AboutPage()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.upload_page)
        self.stacked_widget.addWidget(self.settings_page)
        self.stacked_widget.addWidget(self.about_page)