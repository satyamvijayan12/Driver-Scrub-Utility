🧼 Driver Scrub Utility
Remove outdated or incompatible drivers from your Windows system—safely, efficiently, and efficiently.

Handcrafted Windows Utility Tool By Zenexis Studios Designed by Satyam Vijayan

## ✨ Major Features - v0.2 Update

### 🎨 **UI/UX Overhaul**
- **Scrollable Driver Table** - Professional QTableWidget
  - Auto-scrolling for large driver lists
  - Clean 4-column layout (Select, Driver Name, INF File, Action)
  - Responsive design with proper sizing

- **Selectable Drivers** - Enhanced selection interface
  - Individual checkboxes for each driver
  - "Select All" button to check all drivers at once
  - "Deselect All" button to clear all selections
  - "Remove Selected" button for batch driver removal

- **Direct Uninstall Capability** - Per-driver control
  - Individual "Uninstall" button for each driver
  - Direct one-click driver removal without selection
  - Bulk removal via "Remove Selected" option
  - Safety features: Automatic restore point creation and INF backup

### 🎯 **Enhanced Dark Theme**
- Modern cyan accent color (#00FFD0) throughout
- Improved button styling with hover effects
- Enhanced checkbox styling with visual feedback
- Professional table styling with proper contrast
- Smooth scrollbar integration
- Better overall visual hierarchy

### 🔒 **Professional Distribution**
- **EXE Build System** - Complete Windows executable generation
  - Single-file executable with embedded Python runtime
  - Administrator privileges via Windows manifest
  - No Python installation required for end users
  - Works on Windows 7, 8, 10, and 11



### ⚙️ SYSTEM FILES

## 📋 Directory Structure After Update

```
Driver-Scrub-Utility/
├── 🔶 Update_admin.bat              ← DOUBLE-CLICK THIS!
├── build_exe.py
├── Driver scrub utility.bat
├── app.manifest
│
├── 📖 README.md              ← START HERE
├── 📖 QUICK_START_BUILD.md
├── 📖 VISUAL_BUILD_GUIDE.md
├── 📖 README_EXE_BUILD.md
│
├── main.py
├── requirements.txt
├── gui/
│   ├── main_window.py              ← NEW: Table UI
│   ├── dark_theme.py               ← NEW: Enhanced theme
│   └── ...
├── core/
│   ├── scanner.py
│   ├── remover.py
│   └── ...
│
├── dist/                           ← BUILD OUTPUT
│   └── Driver Scrub Utility.exe    ← YOUR EXE ✨
│
└── build/                          ← Temporary build files
```



| File | Purpose |
|------|---------|
| **app.manifest** | Requests admin privileges from Windows |
| **requirements.txt** | Python dependencies (PyQt5, WMI) |


## 🚀 Getting Started

### 🎯 Step-by-step Start up Guide
- Open your file location
- Run Update Admin (Cmd will open and install pkg dependencies)
- Run Driver Scrub utility v0.2 (To update dependencies if update available!!!)
- Open Driver Scrub utility.exe (Application)
- Happy cleaning!!!


| Tool | How to Use | Difficulty |
|------|-----------|-----------|
| **Update_admin.bat** | Double-click it | ⭐ Easiest |
| **build_exe.py** | `python build_exe.py` | ⭐⭐ Easy |
| **Driver Scrub Utility v0.2.bat** | `build.bat` | ⭐⭐ Easy |

**Recommendation:** Use `Update_admin.bat` - just double-click!
```
User Double-Clicks: Driver Scrub Utility.exe
                           ↓
        Windows Detects Admin Requirement
        (from embedded app.manifest)
                           ↓
        ┌────────────────────────────────────┐
        │  User Account Control (UAC)        │
        │  ┌──────────────────────────────┐  │
        │  │ Do you want to allow this    │  │
        │  │ app to make changes to your  │  │
        │  │ device?                      │  │
        │  │ Driver Scrub Utility         │  │
        │  │                              │  │
        │  │ [Yes]      [No]              │  │
        │  └──────────────────────────────┘  │
        └────────────────────────────────────┘
                           ↓
                      User Clicks YES
                           ↓
                   App Runs with Admin
                   Can now access drivers!
```


**Note:** Your app will request admin privileges because:

1. **Driver detection** requires WMI access (admin)
2. **System restore points** need registry access (admin)
3. **INF backup** requires reading system directories (admin)
4. **Driver uninstall** needs system-level access (admin)


## ✨ Features Of Driver Scrub Utility v0.23

```
✅ Single File              Your whole app in ONE file
✅ Admin Privileges         Automatic UAC prompt on launch
✅ No Python Required       Works on any Windows PC
✅ All Dependencies         PyQt5, WMI, everything bundled
✅ Scrollable UI            New table-based driver list
✅ Selectable              Checkboxes for driver selection
✅ Direct Uninstall        Per-driver uninstall buttons
✅ Professional Look        Dark theme, modern design
✅ Portable                 Copy & share anywhere
✅ Small Dependencies       Not dependencies, everything inside!
```



## ⚙ Dependencies (Just for knowledge)
- PyQt5
- wmi

## Install with: (if using previous versions)
(bash)
pip install PyQt5 wmi

## 🛡 Safety Notes
INF files are backed up before removal.

### Sharing with Others:
```
1. Copy: dist\Driver Scrub Utility.exe
2. Send via email, cloud, USB, etc.
3. They double-click it
4. Windows asks for admin → They click Yes
5. It works! ✨

No Python installation needed on their PC!
```

## QnA Section
## 🆘 Common Issues & Quick Fixes

| Issue | Fix |
|-------|-----|
| "Build doesn't start" | Run as Administrator (right-click batch → Run as admin) |
| "Python not found" | Install Python from python.org (add to PATH) |
| "PyInstaller error" | Run: `pip install --upgrade pyinstaller` |
| "Module not found" | Run: `pip install -r requirements.txt` |
| "Access denied" | Disable antivirus temporarily during build |
| "Build is slow" | Wait! 2-5 minutes is normal ☕ |



Critical drivers (System, Network, Display, etc.) are skipped by default.

A system restore point is created automatically using PowerShell.

### Feel free to fork and patch bugs, for inquiries mailto:genesislabsinc@gmail.com



