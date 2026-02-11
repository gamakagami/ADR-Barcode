
import qtawesome as qta
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QFrame, QLabel, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont

class Sidebar(QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(250)
        self.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                color: white;
                border: none;
            }
            QPushButton {
                text-align: left;
                padding: 12px 20px;
                border: none;
                background-color: transparent;
                color: #ecf0f1;
                font-size: 14px;
                border-radius: 5px;
                margin: 2px 10px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:checked {
                background-color: #3498db;
                font-weight: bold;
            }
            QLabel#Logo {
                padding: 20px;
                font-size: 18px;
                font-weight: bold;
                color: white;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # Logo
        logo = QLabel("ADR Barcode")
        logo.setObjectName("Logo")
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        # Navigation Buttons
        self.dashboard_btn = self.create_nav_button("Dashboard", "fa5s.home")
        layout.addWidget(self.dashboard_btn)

        self.settings_btn = self.create_nav_button("Settings", "fa5s.cog")
        layout.addWidget(self.settings_btn)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Version info
        version_label = QLabel("v1.0.0")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("color: #7f8c8d; font-size: 10px; padding-bottom: 10px;")
        layout.addWidget(version_label)

    def create_nav_button(self, text, icon_name):
        btn = QPushButton(text)
        icon = qta.icon(icon_name, color='white')
        btn.setIcon(icon)
        btn.setIconSize(QSize(20, 20))
        btn.setCheckable(True)
        btn.setAutoExclusive(True)
        if text == "Dashboard":
            btn.setChecked(True)
        return btn