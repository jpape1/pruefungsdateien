# ui/components/filters.py

from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from config.config import Config
from datetime import datetime


class FiltersSection(QGroupBox):
    def __init__(self):
        """
        Initializes FiltersSection widget with filter settings
        """
        super().__init__("Filtereinstellungen")
        self.init_ui()

    def init_ui(self):
        """
        Sets up user interface components of the filters section
        """
        filters_layout = QHBoxLayout()
        filters_layout.setContentsMargins(10, 10, 10, 10) 
        filters_layout.setSpacing(20) 

        labels = ["Fachrichtung:", "Prüfungsteil:", "Dateityp:", "Jahr:", "Zeitraum:"]
        combos = [
            self.create_combobox(Config.get_specializations(), "Fachrichtung auswählen", "fachrichtung_combo"),
            self.create_combobox(Config.get_exam_parts(), "Prüfungsteil auswählen", "pruefungsteil_combo"),
            self.create_combobox(Config.get_file_types(), "Dateityp auswählen", "dateityp_combo"),
            self.create_year_combobox("jahr_combo"),
            self.create_combobox(Config.get_periods(), "Zeitraum auswählen", "zeitraum_combo")
        ]

        for label_text, combo in zip(labels, combos):
            vbox = QVBoxLayout()
            label = QLabel(label_text)
            label.setFont(QFont("Segoe UI", 11))
            label.setStyleSheet("color: #2c3e50;")
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            vbox.addWidget(label)
            vbox.addWidget(combo)
            vbox.setAlignment(Qt.AlignTop)
            filters_layout.addLayout(vbox)

        filters_layout.addStretch()
        self.setLayout(filters_layout)
        self.setStyleSheet("""
            QGroupBox {
                border: 1px solid #2980b9;
                border-radius: 8px;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #2980b9;
                font-weight: bold;
            }
        """)

    def create_combobox(self, items, tooltip, object_name):
        """
        Creates a styled QComboBox with the given items, tooltip, and object name

        Args:
            items (list[str]): List of items to populate the combo box
            tooltip (str): Tooltip text for the combo box
            object_name (str): Object name for the combo box

        Returns:
            QComboBox: Configured combo box widget
        """
        combo = QComboBox()
        combo.addItems(items)
        combo.setToolTip(tooltip)
        combo.setObjectName(object_name)
        combo.setFont(QFont("Segoe UI", 12))
        combo.setIconSize(QSize(10, 10))
        combo.setStyleSheet("""
            QComboBox {
                padding: 5px 30px 5px 10px;
                border: 1px solid #2980b9;
                border-radius: 5px;
                background-color: #ffffff;
                font-size: 12px;
                color: #2c3e50;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: none;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                background-color: transparent;
            }
            QComboBox QAbstractItemView {
                background-color: #ffffff;
                selection-background-color: #1abc9c;
                selection-color: #ffffff;
                font-size: 12px;
                border: 1px solid #2980b9;
                border-radius: 5px;
            }
            QComboBox QAbstractItemView::item {
                padding: 5px 10px;
                color: #2c3e50;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #16a085;
                color: #ffffff;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #1abc9c;
                color: #ffffff;
            }
        """)
        return combo

    def create_year_combobox(self, object_name):
        """
        Creates a QComboBox for selecting year, populated with a range of years

        Args:
            object_name (str): Object name for the year combo box

        Returns:
            QComboBox: Configured year combo box widget
        """
        combo = QComboBox()
        current_year = datetime.now().year
        years_list = [str(year) for year in range(current_year - 5, current_year + 6)]
        combo.addItems(years_list)
        combo.setCurrentText(str(current_year))
        combo.setToolTip("Wählen Sie das Prüfungsjahr")
        combo.setObjectName(object_name)
        combo.setFont(QFont("Segoe UI", 12))
        combo.setIconSize(QSize(10, 10))
        combo.setStyleSheet("""
            QComboBox {
                padding: 5px 30px 5px 10px;
                border: 1px solid #2980b9;
                border-radius: 5px;
                background-color: #ffffff;
                font-size: 12px;
                color: #2c3e50;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: none;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                background-color: transparent;
            }
            QComboBox QAbstractItemView {
                background-color: #ffffff;
                selection-background-color: #1abc9c;
                selection-color: #ffffff;
                font-size: 12px;
                border: 1px solid #2980b9;
                border-radius: 5px;
            }
            QComboBox QAbstractItemView::item {
                padding: 5px 10px;
                color: #2c3e50;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #16a085;
                color: #ffffff;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #1abc9c;
                color: #ffffff;
            }
        """)
        return combo
