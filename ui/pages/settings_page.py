from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class SettingsPage(QWidget):
    """
    Widget for displaying application settings
    """

    def __init__(self, settings_section) -> None:
        """
        Initialize the SettingsPage widget

        :param settings_section: A widget containing options/settings
        """
        super().__init__()
        self.settings_section = settings_section
        self.init_ui()

    def init_ui(self) -> None:
        """
        Set up the user interface for the settings page
        Includes a header and the provided settings section
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        header = QLabel("Einstellungen")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font: 18pt 'Segoe UI'; color: #333333;")
        layout.addWidget(header)

        layout.addWidget(self.settings_section)

        layout.addStretch()
        self.setLayout(layout)