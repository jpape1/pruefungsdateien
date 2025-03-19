from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Sidebar(QWidget):
    """
    Sidebar widget for navigation
    Displays a header and navigation buttons for different sections
    """

    def __init__(self, parent=None) -> None:
        """
        Initializes the sidebar widget

        :param parent: The parent widget
        """
        super().__init__(parent)
        self.setObjectName("Sidebar")
        self.init_ui()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)

    def init_ui(self) -> None:
        """
        Sets up the sidebar UI including the header and navigation buttons
        """
        self.setFixedWidth(260)
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(20)

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

        self.btn_upload = QPushButton("Datei hochladen")
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

        self.active_button = None
        self.set_active_button(self.btn_upload)

        self.btn_upload.clicked.connect(lambda: self.set_active_button(self.btn_upload))
        self.btn_settings.clicked.connect(lambda: self.set_active_button(self.btn_settings))
        self.btn_about.clicked.connect(lambda: self.set_active_button(self.btn_about))

    def set_active_button(self, button) -> None:
        """
        Sets the active navigation button and updates its style

        :param button: The button to set as active
        """
        if self.active_button:
            self.active_button.setProperty("class", "")
            self.active_button.style().unpolish(self.active_button)
            self.active_button.style().polish(self.active_button)

        button.setProperty("class", "active")
        button.style().unpolish(button)
        button.style().polish(button)

        self.active_button = button