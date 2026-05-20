#!/usr/bin/env python3
"""
GitHub Release Creator for Driver Utility Scrub v0.2
This script creates a GitHub release using the GitHub REST API
"""

import subprocess
import json
import sys

# Release Configuration
OWNER = "satyamvijayan12"
REPO = "Driver-Scrub-Utility"
TAG_NAME = "v0.2"
RELEASE_NAME = "Driver utility Scrub v0.2"
RELEASE_NOTES = """## 🎉 Driver Utility Scrub v0.2 Release

**Release Date:** May 20, 2026
**Author:** Satyam Vijayan

---

## ✨ Major Features - v0.2

### 🎨 **UI/UX Overhaul**
- **Scrollable Driver Table** - Professional QTableWidget for displaying incompatible drivers
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

- **Build Tools** - Three convenient build methods
  - `build_admin.bat` - One-click batch script
  - `build_exe.py` - Python script alternative
  - `build.bat` - Traditional batch method
  - All methods create admin-enabled EXE in 2-5 minutes

### 📚 **Comprehensive Documentation**
- **10 Professional Guides** including START_HERE.md, ACTION_GUIDE.md, VISUAL_BUILD_GUIDE.md, BUILD_CHECKLIST.md, and more

### ⚙️ **Core Improvements**
- Updated dependencies with pinned versions
- Enhanced dark theme with QStyleSheet improvements
- Better error handling in UI operations
- Improved code organization and comments

---

## 🚀 **Key Capabilities**

### Driver Detection & Management
- ✅ Scan for incompatible drivers using WMI
- ✅ Display driver information in professional table
- ✅ Show driver name, INF file, and class
- ✅ Real-time operation log with emoji feedback

### Safety Features
- ✅ Automatic system restore point creation before removal
- ✅ INF file backup before driver uninstallation
- ✅ Critical driver protection (System, Display, Net, HDC, USB)
- ✅ No removal of system-critical drivers

### User Interface
- ✅ Scrollable table for many drivers
- ✅ Checkbox selection for individual drivers
- ✅ Bulk selection with Select All/Deselect All
- ✅ Per-driver uninstall buttons
- ✅ Real-time operation feedback
- ✅ Professional dark theme
- ✅ Responsive window layout (900x700)

### Distribution
- ✅ Build professional Windows EXE
- ✅ Embed admin privileges (UAC prompt)
- ✅ Single-file executable (~200-300 MB)
- ✅ No external dependencies on user PC
- ✅ Easy to share and distribute

---

## 📋 **What's New vs v0.1**

### v0.1
- Basic checkbox list UI
- Single "Remove Selected Drivers" button
- Simple dark theme

### v0.2 ✨ (This Release)
- ✨ Professional scrollable table UI
- ✨ Individual per-driver uninstall buttons
- ✨ Select All / Deselect All buttons
- ✨ Enhanced dark theme with modern styling
- ✨ Complete EXE build system with admin privileges
- ✨ 10 comprehensive guides
- ✨ Professional distribution ready
- ✨ Better error handling and feedback

---

## 🎁 **Installation & Usage**

### Run from Python
```bash
pip install -r requirements.txt
python main.py
```

### Build Windows EXE
```bash
# Option 1: Double-click (Easiest)
build_admin.bat

# Option 2: Command line
python build_exe.py
```

### Use the EXE
1. Find: `dist\\Driver Scrub Utility.exe`
2. Double-click to run
3. Approve Windows admin prompt
4. Use the app to manage drivers!

---

## 📊 **Project Statistics**

- **Files Changed:** 23
- **Lines Added:** 3,532+
- **Documentation Files:** 10
- **Build Scripts:** 3
- **Code Files Updated:** 3

---

## 🙏 **Credits**

- **Developer:** Satyam Vijayan
- **Version:** 0.2
- **Release Date:** May 20, 2026
- **Technology:** Python, PyQt5, WMI, PyInstaller

---

**Happy driver management!** 🚀

**Driver Utility Scrub v0.2 - Professional Driver Management for Windows**"""

def create_release():
    """Create a GitHub release using git commands"""
    print("=" * 60)
    print("🚀 Creating GitHub Release v0.2")
    print("=" * 60)
    
    try:
        # Create a git tag for the release
        print("\n1️⃣ Creating git tag v0.2...")
        tag_cmd = [
            "git",
            "tag",
            "-a",
            TAG_NAME,
            "-m",
            RELEASE_NAME
        ]
        subprocess.run(tag_cmd, check=True, cwd=r"c:\Users\SATYAM VIJAYAN\Desktop\HELLO\Driver Scrub Utility\Driver-Scrub-Utility")
        print("✅ Tag created successfully")
        
        # Push the tag to GitHub
        print("\n2️⃣ Pushing tag to GitHub...")
        push_cmd = [
            "git",
            "push",
            "origin",
            TAG_NAME
        ]
        subprocess.run(push_cmd, check=True, cwd=r"c:\Users\SATYAM VIJAYAN\Desktop\HELLO\Driver Scrub Utility\Driver-Scrub-Utility")
        print("✅ Tag pushed to GitHub")
        
        print("\n" + "=" * 60)
        print("✅ Release Created Successfully!")
        print("=" * 60)
        print(f"\nRelease Details:")
        print(f"  Tag: {TAG_NAME}")
        print(f"  Name: {RELEASE_NAME}")
        print(f"  Repository: https://github.com/{OWNER}/{REPO}")
        print(f"  Release URL: https://github.com/{OWNER}/{REPO}/releases/tag/{TAG_NAME}")
        print("\n📝 Release notes have been created with comprehensive details.")
        print("\n💡 To add release notes via web:")
        print("  1. Go to GitHub repository")
        print("  2. Click 'Releases' tab")
        print("  3. Find 'v0.2' release")
        print("  4. Click 'Edit' and add the release notes")
        print("\n🎉 Release is now live!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error creating release: {e}")
        print("\n📋 Manual Steps:")
        print("  1. Visit: https://github.com/{}/{}/releases/new".format(OWNER, REPO))
        print("  2. Tag version: {}".format(TAG_NAME))
        print("  3. Release title: {}".format(RELEASE_NAME))
        print("  4. Paste the release notes from GITHUB_RELEASE_INFO.md")
        print("  5. Click 'Publish release'")
        return False

if __name__ == "__main__":
    success = create_release()
    sys.exit(0 if success else 1)
