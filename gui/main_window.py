from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QTextEdit
from PyQt5.QtCore import Qt

from core.scanner import get_incompatible_drivers
from core.remover import safe_remove_driver
from core.restore import create_restore_point
from core.backup import backup_inf

class DriverScrubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Driver Scrub Utility")
        layout = QVBoxLayout()

        title = QLabel("Detected Incompatible Drivers")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.driver_boxes = []
        drivers = get_incompatible_drivers()

        for name, inf, cls in drivers:
            cb = QCheckBox(f"{name} [{inf}]")
            layout.addWidget(cb)
            self.driver_boxes.append((cb, inf, cls))

        self.button = QPushButton("Remove Selected Drivers")
        self.button.clicked.connect(self.remove_drivers)
        layout.addWidget(self.button)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

        # Footer branding
        footer = QLabel("Powered by <b>Text Tool by Zenexis Lab</b>")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #777777; font-size: 12px; padding: 10px; border-top: 1px solid #333333;")
        layout.addWidget(footer)

        self.setLayout(layout)

    def remove_drivers(self):
        try:
            create_restore_point()
            self.log.append("🔄 Created system restore point.\n")
        except Exception as e:
            self.log.append(f"❌ Failed to create restore point: {e}\n")

        for cb, inf, cls in self.driver_boxes:
            if cb.isChecked():
                try:
                    backup_inf(inf)
                    self.log.append(f"📁 Backed up INF: {inf}\n")
                except Exception as e:
                    self.log.append(f"❌ Failed to backup INF {inf}: {e}\n")

                if cls not in ["System", "Display", "Net", "HDC", "USB"]:
                    try:
                        safe_remove_driver(inf)
                        self.log.append(f"🗑 Removed: {inf}\n")
                    except Exception as e:
                        self.log.append(f"❌ Failed to remove {inf}: {e}\n")
                else:
                    self.log.append(f"⚠️ Skipped critical driver: {inf}\n")
