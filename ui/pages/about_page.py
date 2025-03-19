from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from config.config import Config

class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        """
        Shows the about page with application information
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        logo_label = QLabel()
        pixmap = QPixmap("resources/icon.png")
        if not pixmap.isNull():
            logo_label.setPixmap(pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        header_label = QLabel("Über diese Anwendung")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_label.setStyleSheet("font: bold 20pt 'Segoe UI'; color: #222222;")
        layout.addWidget(header_label)

        description_text = (
            "IHK Prüfungsdateien\n"
            "Version " + Config.get_version() + "\n"
            "Verantwortlich: Gruppe 17 / Jonas Pape\n\n"
            "Diese Anwendung dient zum geordneten Ablegen von Prüfungsdokumenten."
        )
        description_label = QLabel(description_text)
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label.setStyleSheet("font: 12pt 'Segoe UI'; color: #555555;")
        layout.addWidget(description_label)

        layout.addStretch()
        self.setLayout(layout)