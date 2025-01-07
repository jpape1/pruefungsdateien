# ui/components/drag_drop.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QProgressBar, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from datetime import datetime


class DragDropSection(QWidget):
    def __init__(self, upload_callback):
        """
        Initializes DragDropSection widget

        Args:
            upload_callback (callable): Function to call when a file is uploaded
        """
        super().__init__()
        self.upload_callback = upload_callback
        self.init_ui()
        self.setAcceptDrops(True) 

    def init_ui(self):
        """
        Sets up user interface components
        """
        drag_drop_layout = QVBoxLayout()
        drag_drop_layout.setContentsMargins(0, 0, 0, 0)
        drag_drop_layout.setSpacing(10)

        # Drag & Drop Frame
        self.drop_frame = QFrame()
        self.drop_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_frame.setObjectName("DropFrame")

        self.drop_label = QLabel("Datei hierher ziehen oder unten auswählen")
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_label.setFont(QFont("Segoe UI", 14))
        self.drop_label.setStyleSheet("color: #2c3e50;")

        drop_layout = QVBoxLayout()
        drop_layout.addStretch()
        drop_layout.addWidget(self.drop_label)
        drop_layout.addStretch()
        self.drop_frame.setLayout(drop_layout)

        # Upload Button
        self.upload_button = QPushButton("📤 Datei wählen")
        self.upload_button.setFixedSize(200, 50)
        self.upload_button.setFont(QFont("Segoe UI", 14))
        self.upload_button.setStyleSheet("""
            QPushButton {
                background-color: #2980b9;
                color: white;
                border: none;
                border-radius: 25px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1abc9c;
            }
            QPushButton:pressed {
                background-color: #16a085;
            }
        """)
        self.upload_button.clicked.connect(self.handle_upload_button)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #2980b9;
                border-radius: 10px;
                text-align: center;
                font-size: 10px;
            }
            QProgressBar::chunk {
                background-color: #1abc9c;
                width: 20px;
            }
        """)

        # Assemble Layout
        drag_drop_layout.addWidget(self.drop_frame, stretch=3)
        drag_drop_layout.addSpacing(30)
        drag_drop_layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        drag_drop_layout.addSpacing(10)
        drag_drop_layout.addWidget(self.progress_bar)

        self.setLayout(drag_drop_layout)
        self.setStyleSheet("""
            #DropFrame {
                border: 2px dashed #2980b9;
                border-radius: 10px;
                background-color: #ecf0f1;
            }
        """)

    def handle_upload_button(self):
        """
        Handles upload button click event by opening file dialog
        """
        self.upload_callback()

    def update_progress(self, value):
        """
        Updates progress bar value

        Args:
            value (int): Progress value from 0 to 100
        """
        self.progress_bar.setValue(value)
        if value >= 100:
            self.progress_bar.setVisible(False)

    def show_progress(self):
        """
        Shows and resets progress bar.
        """
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

    # Drag & Drop Event Handlers
    def dragEnterEvent(self, event):
        """
        Handles drag enter event. Accepts drag if just one file is dragged

        Args:
            event (QDragEnterEvent): The drag enter event
        """
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1:
                event.acceptProposedAction()
                self.drop_frame.setStyleSheet("""
                    #DropFrame {
                        border: 2px dashed #1abc9c;
                        background-color: #d0ece7;
                    }
                """)
            else:
                event.ignore()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        """
        Handles drag leave event. Resets drop frame style

        Args:
            event (QDragLeaveEvent): The drag leave event
        """
        self.drop_frame.setStyleSheet("""
            #DropFrame {
                border: 2px dashed #2980b9;
                background-color: #ecf0f1;
            }
        """)

    def dropEvent(self, event):
        """
        Handles drop event. Processes dropped file if just one file is dropped

        Args:
            event (QDropEvent): The drop event
        """
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) != 1:
                QMessageBox.warning(
                    self,
                    "Warnung",
                    "Bitte ziehen Sie nur eine einzelne Datei in das Fenster.",
                    QMessageBox.Ok
                )
                event.ignore()
                return

            file_path = urls[0].toLocalFile()
            if file_path:
                self.show_progress()
                self.upload_callback(file_path)

            self.drop_frame.setStyleSheet("""
                #DropFrame {
                    border: 2px dashed #2980b9;
                    background-color: #ecf0f1;
                }
            """)
