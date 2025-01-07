# ui/components/header.py

from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Header(QFrame):
    def __init__(self):
        """
        Initializes Header widget
        """
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFixedHeight(80) 

        self.init_ui()

    def init_ui(self):
        """
        Sets up the user interface components of the header
        """
        # Create a horizontal layout
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.setSpacing(0) 

        # Create the title label
        title_label = QLabel("Prüfungsdateien hochladen")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title_label.setStyleSheet("color: #ffffff;")
        title_label.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet("""
            QFrame {
                background-color: #34495e;
            }
        """)
