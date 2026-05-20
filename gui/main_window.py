from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                             QCheckBox, QTextEdit, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QScrollArea, QFrame)
from PyQt5.QtCore import Qt

from core.scanner import get_incompatible_drivers
from core.remover import safe_remove_driver
from core.restore import create_restore_point
from core.backup import backup_inf

class DriverScrubWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Driver Scrub Utility")
        self.setGeometry(100, 100, 900, 700)
        
        main_layout = QVBoxLayout()

        # Title
        title = QLabel("Detected Incompatible Drivers")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        main_layout.addWidget(title)

        # Control buttons layout
        control_layout = QHBoxLayout()
        select_all_btn = QPushButton("Select All")
        select_all_btn.clicked.connect(self.select_all_drivers)
        select_all_btn.setMaximumWidth(150)
        
        deselect_all_btn = QPushButton("Deselect All")
        deselect_all_btn.clicked.connect(self.deselect_all_drivers)
        deselect_all_btn.setMaximumWidth(150)
        
        remove_selected_btn = QPushButton("Remove Selected")
        remove_selected_btn.clicked.connect(self.remove_selected_drivers)
        remove_selected_btn.setMaximumWidth(150)
        
        control_layout.addWidget(select_all_btn)
        control_layout.addWidget(deselect_all_btn)
        control_layout.addWidget(remove_selected_btn)
        control_layout.addStretch()
        main_layout.addLayout(control_layout)

        # Driver table in scroll area
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Select", "Driver Name", "INF File", "Action"])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(3, 100)
        
        self.drivers = get_incompatible_drivers()
        self.table.setRowCount(len(self.drivers))
        
        for row, (name, inf, cls) in enumerate(self.drivers):
            # Checkbox column
            checkbox = QCheckBox()
            self.table.setCellWidget(row, 0, checkbox)
            
            # Driver name
            name_item = QTableWidgetItem(name)
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            self.table.setItem(row, 1, name_item)
            
            # INF file
            inf_item = QTableWidgetItem(inf)
            inf_item.setFlags(inf_item.flags() & ~Qt.ItemIsEditable)
            self.table.setItem(row, 2, inf_item)
            
            # Uninstall button
            uninstall_btn = QPushButton("Uninstall")
            uninstall_btn.setMaximumWidth(90)
            uninstall_btn.clicked.connect(lambda checked, r=row, i=inf, c=cls: self.uninstall_driver(r, i, c))
            self.table.setCellWidget(row, 3, uninstall_btn)
            
            self.table.resizeRowToContents(row)

        main_layout.addWidget(self.table)

        # Log output
        log_label = QLabel("Operation Log")
        log_label.setStyleSheet("font-weight: bold; padding: 5px 0px 0px 0px;")
        main_layout.addWidget(log_label)
        
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setMaximumHeight(150)
        main_layout.addWidget(self.log)

        # Footer branding
        footer = QLabel("Powered by <b>Text Tool by Zenexis Lab</b>")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #777777; font-size: 12px; padding: 10px; border-top: 1px solid #333333;")
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

    def select_all_drivers(self):
        for row in range(self.table.rowCount()):
            checkbox = self.table.cellWidget(row, 0)
            checkbox.setChecked(True)

    def deselect_all_drivers(self):
        for row in range(self.table.rowCount()):
            checkbox = self.table.cellWidget(row, 0)
            checkbox.setChecked(False)

    def remove_selected_drivers(self):
        try:
            create_restore_point()
            self.log.append("🔄 Created system restore point.\n")
        except Exception as e:
            self.log.append(f"❌ Failed to create restore point: {e}\n")

        for row in range(self.table.rowCount()):
            checkbox = self.table.cellWidget(row, 0)
            if checkbox.isChecked():
                inf = self.table.item(row, 2).text()
                cls = self.drivers[row][2]
                self._perform_driver_removal(inf, cls)

    def uninstall_driver(self, row, inf, cls):
        try:
            create_restore_point()
            self.log.append(f"🔄 Created system restore point for: {inf}\n")
        except Exception as e:
            self.log.append(f"❌ Failed to create restore point: {e}\n")

        self._perform_driver_removal(inf, cls)

    def _perform_driver_removal(self, inf, cls):
        try:
            backup_inf(inf)
            self.log.append(f"📁 Backed up INF: {inf}\n")
        except Exception as e:
            self.log.append(f"❌ Failed to backup INF {inf}: {e}\n")

        if cls not in ["System", "Display", "Net", "HDC", "USB"]:
            try:
                safe_remove_driver(inf)
                self.log.append(f"✅ Successfully removed: {inf}\n")
            except Exception as e:
                self.log.append(f"❌ Failed to remove {inf}: {e}\n")
        else:
            self.log.append(f"⚠️ Skipped critical driver: {inf} (Class: {cls})\n")
