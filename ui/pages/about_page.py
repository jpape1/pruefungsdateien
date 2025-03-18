from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        Shows the about page with application information.
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        # Display logo at the top
        logo_label = QLabel()
        pixmap = QPixmap("resources/icon.png")
        if not pixmap.isNull():
            logo_label.setPixmap(pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        # Header label
        header_label = QLabel("Über diese Anwendung")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_label.setStyleSheet("font: bold 20pt 'Segoe UI'; color: #222222;")
        layout.addWidget(header_label)

        # Detailed description text
        description_text = (
            "IHK Prüfungsdateien\n"
            "Version 2.0\n"
            "Entwickelt von Jonas Pape\n\n"
            "Diese Anwendung legt Prüfungsdateien strukturiert und geordnet ab."
        )
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label.setStyleSheet("font: 12pt 'Segoe UI'; color: #555555;")
        layout.addWidget(description_label)

        layout.addStretch()
        self.setLayout(layout)