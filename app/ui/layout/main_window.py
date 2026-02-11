
import sys
import qtawesome as qta
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from app.ui.layout.sidebar import Sidebar
from app.ui.pages.dashboard import DashboardPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADR Barcode Generator")
        self.resize(1000, 600)
        
        # Main layout container
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Sidebar
        self.sidebar = Sidebar()
        self.main_layout.addWidget(self.sidebar)

        # Content Area
        self.content_area = QFrame()
        self.content_area.setStyleSheet("background-color: #f5f6fa;")
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.addWidget(self.content_area)

        # Initialize pages
        self.dashboard_page = DashboardPage()
        self.content_layout.addWidget(self.dashboard_page)

        # Connect signals
        self.sidebar.dashboard_btn.clicked.connect(lambda: self.switch_page(self.dashboard_page))

    def switch_page(self, page_widget):
        # Clear current layout (simplified for this example, usually a QStackedWidget is better)
        pass # Only one page for now

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set app style
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())