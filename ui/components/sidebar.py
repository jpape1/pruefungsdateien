from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Sidebar(QWidget):
    """
    Sidebar widget for navigation.
    Displays a header and navigation buttons for different sections.
    """

    def __init__(self, parent=None):
        """
        Initializes the sidebar widget.

        :param parent: The parent widget
        """
        super().__init__(parent)
        # Set an object name to target the entire sidebar in the stylesheet
        self.setObjectName("Sidebar")
        self.init_ui()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)

    def init_ui(self):
        """
        Sets up the sidebar UI including the header and navigation buttons.
        """
        # Set a fixed width for the sidebar
        self.setFixedWidth(260)
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)

        # Header title
        title = QLabel("Prüfungsdateien")
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font: 20pt "Segoe UI";
            font-weight: bold;
            color: #333333;
            border-bottom: 3px solid #4a90e2;
            padding-bottom: 5px;
        """)
        layout.addWidget(title)

        # Navigation buttons
        self.btn_upload = QPushButton("Hochladen")
        self.btn_upload.setObjectName("navBtn")
        layout.addWidget(self.btn_upload)

        self.btn_settings = QPushButton("Einstellungen")
        self.btn_settings.setObjectName("navBtn")
        layout.addWidget(self.btn_settings)

        self.btn_about = QPushButton("Über")
        self.btn_about.setObjectName("navBtn")
        layout.addWidget(self.btn_about)

        layout.addStretch()
        self.setLayout(layout)

        # Set the first button as active by default
        self.active_button = None
        self.set_active_button(self.btn_upload)

        # Connect button clicks to update the active state
        self.btn_upload.clicked.connect(lambda: self.set_active_button(self.btn_upload))
        self.btn_settings.clicked.connect(lambda: self.set_active_button(self.btn_settings))
        self.btn_about.clicked.connect(lambda: self.set_active_button(self.btn_about))

        # Apply stylesheet
        self.setStyleSheet("""
            /* Apply background to the entire sidebar via its object name */
            #Sidebar {
                background-color: #e0e0e0;
            }
            QPushButton#navBtn {
                background-color: transparent;
                border: none;
                font: 12pt "Segoe UI";
                text-align: left;
                padding: 10px;
                border-radius: 8px;
                color: black;
            }
            QPushButton#navBtn:hover {
                background-color: #d0e2ff;
            }
            QPushButton#navBtn[class="active"] {
                background-color: #a4c8ff;
                font-weight: bold;
            }
        """)

    def set_active_button(self, button):
        """
        Sets the active navigation button and updates its style.

        :param button: The button to set as active.
        """
        if self.active_button:
            self.active_button.setProperty("class", "")
            self.active_button.style().unpolish(self.active_button)
            self.active_button.style().polish(self.active_button)

        button.setProperty("class", "active")
        button.style().unpolish(button)
        button.style().polish(button)

        self.active_button = button
