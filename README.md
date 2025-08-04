🧼 Driver Scrub Utility
Remove outdated or incompatible drivers from your Windows system—safely, efficiently, and stylishly.

Powered by Text Tool by Zenexis Lab Designed by Satyam Vijayan

## 📦 Features
🔍 Incompatible Driver Scanner Detects unused or legacy drivers no longer associated with active devices.

✅ Checkbox Selection UI Easy-to-use interface for manual selection of drivers to remove.

🧼 Safe Removal Engine Backs up .INF files and skips critical drivers to protect your system.

🔄 System Restore Integration Automatically creates a restore point before changes.

🌙 Dark Mode UI Sleek, modern PyQt5 interface with electric teal highlights.

📜 Log Viewer Displays real-time status of each action: backup, skipped, or removed.

## 🗂 Folder Structure
DriverScrub/
├── main.py
├── gui/
│   ├── main_window.py
│   ├── dark_theme.py
├── core/
│   ├── scanner.py
│   ├── remover.py
│   ├── restore.py
│   ├── backup.py
├── backups/
│   └── *.inf
├── assets/
│   └── icon.png
├── logs/
│   └── removal_log.txt
├── README.md
└── requirements.txt

## 🚀 Getting Started
1. Clone the repo
bash
git clone https://github.com/satyamvijayan12/Driver-Scrub-Utility
cd DriverScrub
2. Install dependencies
pip install -r requirements.txt
3. Run the tool
python main.py

## ⚙ Dependencies
PyQt5

wmi

## Install with:
(bash)
pip install PyQt5 wmi

## 🛡 Safety Notes
INF files are backed up before removal.

Critical drivers (System, Network, Display, etc.) are skipped by default.

A system restore point is created automatically using PowerShell.
