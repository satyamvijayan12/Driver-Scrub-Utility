# 🚀 Building Driver Scrub Utility EXE with Admin Access

## Quick Build (Choose One Method)

### Method 1: Using Batch File (Recommended for Windows)
1. Open File Explorer
2. Navigate to: `Driver Scrub Utility\Driver-Scrub-Utility`
3. **Double-click:** `build_admin.bat`
4. Wait for build to complete (2-5 minutes)
5. Find your EXE in: `dist\Driver Scrub Utility.exe`

### Method 2: Using Python Script
1. Open Command Prompt (Win + R, type `cmd`)
2. Run: `cd "c:\Users\SATYAM VIJAYAN\Desktop\HELLO\Driver Scrub Utility\Driver-Scrub-Utility"`
3. Run: `python build_exe.py`
4. EXE will be created in: `dist\Driver Scrub Utility.exe`

### Method 3: Manual Command
1. Open Command Prompt as Administrator
2. Navigate to app directory
3. Run these commands:
```cmd
pip install pyinstaller
pyinstaller --onefile --windowed --name "Driver Scrub Utility" --manifest app.manifest --add-data "gui;gui" --add-data "core;core" --hidden-import=wmi --hidden-import=PyQt5 main.py
```

---

## 📋 What You'll Get

| Item | Description |
|------|-------------|
| **File** | `dist\Driver Scrub Utility.exe` |
| **Size** | ~200-300 MB |
| **Admin** | ✅ Automatic (embedded manifest) |
| **Dependencies** | ✅ All included (no Python needed) |
| **GUI** | ✅ Scrollable, selectable, direct uninstall |

---

## ✨ Admin Privileges - How It Works

1. The `app.manifest` file requests admin access
2. When you run the EXE, Windows UAC (User Account Control) shows a prompt
3. Click "Yes" to approve admin access
4. App runs with full privileges to:
   - Detect drivers via WMI
   - Backup INF files
   - Create system restore points
   - Uninstall drivers directly

**Example UAC Prompt:**
```
┌─────────────────────────────────────────┐
│ Do you want to allow this app to make   │
│ changes to your device?                 │
│                                         │
│ Driver Scrub Utility                    │
│                                         │
│        [Yes]            [No]            │
└─────────────────────────────────────────┘
```

---

## 🎯 Using the EXE

### Running Locally
1. Navigate to: `dist\Driver Scrub Utility.exe`
2. Double-click to run
3. Approve admin access
4. Use the UI to:
   - ✓ View all incompatible drivers in a scrollable table
   - ✓ Select drivers with checkboxes
   - ✓ Click "Uninstall" buttons for direct removal
   - ✓ See real-time operation logs

### Sharing the EXE
1. Copy `dist\Driver Scrub Utility.exe` to any location
2. Email it, upload to cloud, put on USB, etc.
3. Recipients can run it directly
4. It will ask for admin access on their system
5. No Python installation required on their computer

---

## 📦 Build Files Included

| File | Purpose |
|------|---------|
| `app.manifest` | XML file that requests admin privileges |
| `build_admin.bat` | Batch script to build EXE (easiest) |
| `build_exe.py` | Python script to build EXE |
| `BUILD_INSTRUCTIONS.md` | Detailed instructions |
| `requirements.txt` | Python dependencies |

---

## ✅ Verification Checklist

After building, verify:
- [ ] `dist\Driver Scrub Utility.exe` exists
- [ ] File size is ~200-300 MB (contains all dependencies)
- [ ] You can double-click and run it
- [ ] Windows shows admin prompt
- [ ] App launches with scrollable table UI
- [ ] "Select All", "Deselect All", "Uninstall" buttons work

---

## 🆘 Troubleshooting

**Build fails with "Python not found"**
- Install Python 3.7+ from https://python.org
- Add Python to PATH during installation
- Restart Command Prompt

**Build fails with "PyInstaller error"**
- Run: `pip install --upgrade pyinstaller`
- Try again

**Build fails with "Missing WMI"**
- Run: `pip install -r requirements.txt`
- Try again

**EXE doesn't ask for admin access**
- This is OK - manifest is embedded
- Right-click EXE → "Run as administrator" if needed
- Or install it in Program Files

**EXE won't run on other computers**
- Ensure they have Windows 7 or later
- EXE should work as-is without Python

---

## 🎓 What's Inside the EXE?

When you run the EXE, it contains:
- Python 3.x runtime
- PyQt5 (GUI framework)
- WMI (driver detection)
- Your app code (main_window.py, scanner.py, etc.)
- All themes and styling

Everything is bundled into one file!

---

## 💡 Tips

1. **Rename the EXE:** You can rename it to anything you want
2. **Create shortcut:** Right-click EXE → "Create shortcut" for desktop
3. **Pin to taskbar:** Right-click EXE → "Pin to taskbar"
4. **Autorun:** Put EXE in `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`

---

## 📞 Need Help?

1. Check that you're in the correct directory
2. Make sure Python is installed: `python --version`
3. Verify dependencies: `pip list | findstr PyQt5`
4. Try running build_admin.bat with admin privileges (right-click → Run as administrator)
