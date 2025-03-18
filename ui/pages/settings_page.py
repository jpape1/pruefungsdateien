from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class SettingsPage(QWidget):
    """
    Widget for displaying application settings.
    This page integrates a settings section that allows users to adjust various settings.
    """

    def __init__(self, settings_section):
        """
        Initialize the SettingsPage widget.

        :param settings_section: A widget containing options/settings.
        """
        super().__init__()
        self.settings_section = settings_section
        self.init_ui()

    def init_ui(self):
        """
        Set up the user interface for the settings page.
        Includes a header and the provided settings section.
        """
        # Create the main vertical layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Create the header label
        header = QLabel("Einstellungen")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font: 18pt 'Segoe UI'; color: #333333;")
        layout.addWidget(header)

        # Add the settings section widget to the layout
        layout.addWidget(self.settings_section)

        # Add stretch to push the content upward if needed
        layout.addStretch()
        self.setLayout(layout)
