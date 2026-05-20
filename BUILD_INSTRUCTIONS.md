# Driver Scrub Utility - EXE Build Guide

## 🚀 Quick Start (3 Steps)

### Step 1: Open Command Prompt or PowerShell
- Press `Win + R`
- Type `cmd` and press Enter
- Or search for "Command Prompt" in Start menu

### Step 2: Navigate to the App Directory
```cmd
cd "c:\Users\SATYAM VIJAYAN\Desktop\HELLO\Driver Scrub Utility\Driver-Scrub-Utility"
```

### Step 3: Run the Build Script
```cmd
python build_exe.py
```

The script will:
- ✅ Install PyInstaller automatically
- ✅ Build the EXE with admin privileges
- ✅ Create a standalone executable file
- ✅ Output to: `dist\Driver Scrub Utility.exe`

---

## 📋 What's Included

### Files Created for Building:

1. **app.manifest** - XML manifest file that requests admin privileges
   - Tells Windows to always run with administrator access
   - Enables WMI and driver operations

2. **build_exe.py** - Python build script
   - Installs PyInstaller
   - Compiles Python → EXE
   - Embeds all dependencies
   - Applies admin manifest

3. **build.bat** - Alternative batch script (run this if build_exe.py doesn't work)
   ```cmd
   build.bat
   ```

---

## 🎯 Result

After building, you'll have:
- **Location:** `dist\Driver Scrub Utility.exe`
- **Size:** ~200-300 MB (includes Python runtime + all dependencies)
- **Admin Privileges:** ✅ Automatic (no UAC prompt needed - it will silently escalate)
- **No Python Required:** Users don't need Python installed to run it

---

## ✨ Features of the Generated EXE

| Feature | Status |
|---------|--------|
| Single file executable | ✅ |
| Administrator privileges | ✅ |
| No console window | ✅ |
| All dependencies embedded | ✅ |
| PyQt5 GUI included | ✅ |
| WMI driver detection included | ✅ |

---

## 🔧 Manual Build (If Script Fails)

If the Python script doesn't work, run this in Command Prompt:

```cmd
pip install pyinstaller

pyinstaller --onefile --windowed --name "Driver Scrub Utility" --manifest app.manifest --add-data "gui;gui" --add-data "core;core" --hidden-import=wmi --hidden-import=PyQt5 main.py
```

---

## 📦 Distributing the EXE

1. Find the EXE at: `dist\Driver Scrub Utility.exe`
2. Share this single file with others
3. Users can run it directly - no installation needed
4. Admin prompt will appear on first run (Windows UAC) - this is normal
5. After approval, it runs with full driver access

---

## 🛠️ Troubleshooting

**Q: Build fails with "PyInstaller not found"**
- Run: `pip install pyinstaller`
- Then run the build script again

**Q: Build fails with "WMI module not found"**
- Run: `pip install -r requirements.txt`
- Then run the build script again

**Q: EXE is very large (200+ MB)**
- This is normal - includes Python runtime + PyQt5 + all dependencies
- Can be reduced with UPX compression (optional)

**Q: "Access Denied" error during build**
- Close any antivirus or Windows Defender real-time scanning
- Try running Command Prompt as Administrator
- Then run the build script

**Q: EXE doesn't request admin privileges**
- The manifest is already embedded
- Windows will prompt for admin on first run
- Or right-click EXE → "Run as administrator"

---

## ✅ Testing the EXE

After build completes:

1. Open File Explorer
2. Navigate to: `dist\Driver Scrub Utility.exe`
3. Double-click to run
4. Click "Yes" when Windows asks for admin access
5. App should launch with the new scrollable UI

---

## 📞 Support

If you encounter issues:
1. Ensure Python 3.7+ is installed
2. Ensure all requirements are installed: `pip install -r requirements.txt`
3. Try running from Command Prompt (not IDE)
4. Check that you're in the correct directory
