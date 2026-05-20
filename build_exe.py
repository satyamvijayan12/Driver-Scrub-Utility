#!/usr/bin/env python3
"""
Build script to create Driver Scrub Utility EXE with admin privileges
"""
import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description=""):
    """Run a command and report status"""
    if description:
        print(f"\n{'='*60}")
        print(f"📦 {description}")
        print(f"{'='*60}")
    try:
        result = subprocess.run(cmd, check=True, shell=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False

def main():
    app_dir = Path(__file__).parent
    os.chdir(app_dir)
    
    print("\n🚀 Driver Scrub Utility - EXE Builder with Admin Privileges\n")
    
    # Step 1: Install PyInstaller
    if not run_command(
        "pip install pyinstaller -q",
        "Installing PyInstaller..."
    ):
        print("Failed to install PyInstaller")
        return False
    
    # Step 2: Clean old builds
    run_command("rmdir /s /q build dist", "Cleaning old builds...")
    
    # Step 3: Build EXE with admin manifest
    build_cmd = (
        "pyinstaller "
        "--onefile "
        "--windowed "
        "--name \"Driver Scrub Utility\" "
        "--manifest app.manifest "
        "--add-data \"gui;gui\" "
        "--add-data \"core;core\" "
        "--hidden-import=wmi "
        "--hidden-import=PyQt5 "
        "--icon=assets/icon.ico " if Path("assets/icon.ico").exists() else ""
        "--clean "
        "main.py"
    )
    
    if run_command(build_cmd, "Building EXE with admin privileges..."):
        exe_path = app_dir / "dist" / "Driver Scrub Utility.exe"
        if exe_path.exists():
            print(f"\n✅ Success! EXE created at:")
            print(f"   {exe_path}")
            print(f"\n✨ Features:")
            print(f"   ✓ Single executable file")
            print(f"   ✓ Administrator privileges enabled")
            print(f"   ✓ No console window")
            print(f"   ✓ All dependencies embedded")
            return True
    
    print("\n❌ Build failed!")
    return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
