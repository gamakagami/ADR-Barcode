
import os
import qtawesome as qta
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QComboBox, QFrame, QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from app.barcode import generate_barcode

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignTop)

        # Header
        header = QLabel("Generate Barcode")
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(header)

        # Form Container
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #dcdde1;
            }
            QLabel {
                font-weight: bold;
                color: #2c3e50;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                color: #2c3e50;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #3498db;
            }
        """)
        form_layout = QVBoxLayout(form_frame)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setSpacing(15)

        # Data Input
        self.data_input = QLineEdit()
        self.data_input.setPlaceholderText("Enter data to encode...")
        form_layout.addWidget(QLabel("Data:"))
        form_layout.addWidget(self.data_input)

        # Barcode Type Selection
        self.type_combo = QComboBox()
        self.type_combo.addItems([
            "code128", "ean13", "ean8", "gs1", "gtin", 
            "isbn", "isbn10", "isbn13", "issn", "jan", 
            "pzn", "upc", "upca"
        ])
        form_layout.addWidget(QLabel("Barcode Type:"))
        form_layout.addWidget(self.type_combo)

        # Generate Button
        self.generate_btn = QPushButton("Generate Barcode")
        self.generate_btn.setIcon(qta.icon('fa5s.barcode', color='white'))
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #2574a9;
            }
        """)
        self.generate_btn.clicked.connect(self.handle_generate)
        form_layout.addWidget(self.generate_btn)

        layout.addWidget(form_frame)

        # Result Area
        self.result_frame = QFrame()
        self.result_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #dcdde1;
                min-height: 200px;
            }
        """)
        self.result_layout = QVBoxLayout(self.result_frame)
        self.result_layout.setAlignment(Qt.AlignCenter)
        
        self.image_label = QLabel("Barcode preview will appear here")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.result_layout.addWidget(self.image_label)

        # Save Button (hidden initially)
        self.save_btn = QPushButton("Save Image")
        self.save_btn.setIcon(qta.icon('fa5s.save', color='#2c3e50'))
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #ecf0f1;
                color: #2c3e50;
                padding: 8px 15px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #bdc3c7;
            }
        """)
        self.save_btn.clicked.connect(self.save_image)
        self.save_btn.setVisible(False)
        self.result_layout.addWidget(self.save_btn)

        layout.addWidget(self.result_frame)
        
        # Current temp file path
        self.current_barcode_path = None

    def handle_generate(self):
        data = self.data_input.text().strip()
        if not data:
            QMessageBox.warning(self, "Input Error", "Please enter data to encode.")
            return

        barcode_type = self.type_combo.currentText()
        
        try:
            # Generate to a temporary location
            import tempfile
            # We don't need NamedTemporaryFile context for just getting a path, 
            # and we want to control the base name.
            
            from app.barcode import generate_barcode
            
            temp_dir = tempfile.gettempdir()
            # Use random component to avoid conflicts if needed, but pid is okay for single user app session
            base_name = os.path.join(temp_dir, f"adr_barcode_{os.getpid()}")
            
            # Note: generate_barcode appends extension. 
            # We need to capture the returned full path.
            final_path = generate_barcode(data, base_name, barcode_type)
            self.current_barcode_path = final_path
            
            # Display image
            pixmap = QPixmap(final_path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(
                    self.image_label.size(), 
                    Qt.KeepAspectRatio, 
                    Qt.SmoothTransformation
                ))
                self.image_label.setText("")
                self.save_btn.setVisible(True)
            else:
                 self.image_label.setText("Error loading barcode image.")

        except Exception as e:
            QMessageBox.critical(self, "Generation Error", str(e))

    def save_image(self):
        if not self.current_barcode_path or not os.path.exists(self.current_barcode_path):
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Barcode Image", "barcode.png", "Images (*.png *.svg *.jpeg)"
        )
        
        if file_path:
            try:
                # Copy file
                import shutil
                shutil.copy2(self.current_barcode_path, file_path)
                QMessageBox.information(self, "Success", f"Barcode saved to {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Save Error", str(e))