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
        if isinstance(cmd, list):
            result = subprocess.run(cmd, check=True, shell=False)
        else:
            result = subprocess.run(cmd, check=True, shell=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return False


def ensure_icon(app_dir: Path) -> Path | None:
    """Ensure a Windows ICO file exists for the app icon."""
    ico_path = app_dir / "assets" / "icon.ico"
    png_path = app_dir / "assets" / "icon.png"

    if ico_path.exists():
        return ico_path

    if not png_path.exists():
        return None

    try:
        from PIL import Image
    except ImportError:
        if not run_command("pip install pillow -q", "Installing Pillow for icon generation..."):
            return None
        from PIL import Image

    try:
        with Image.open(png_path) as img:
            img = img.convert("RGBA")
            sizes = [256, 128, 64, 48, 32, 16]
            img.save(ico_path, format="ICO", sizes=[(s, s) for s in sizes])
        return ico_path
    except Exception as e:
        print(f"❌ Failed to convert icon.png to icon.ico: {e}")
        return None

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

    icon_path = ensure_icon(app_dir)
    if icon_path is None:
        print("⚠️  No icon found. Continuing without a custom app icon.")

    # Step 3: Build EXE with admin manifest
    build_parts = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name",
        "Driver Scrub Utility",
        "--manifest",
        "app.manifest",
        "--add-data",
        "gui;gui",
        "--add-data",
        "core;core",
        "--hidden-import",
        "wmi",
        "--hidden-import",
        "PyQt5",
        "--clean",
        "main.py",
    ]

    if icon_path is not None:
        icon_index = len(build_parts) - 2
        build_parts[icon_index:icon_index] = ["--icon", str(icon_path)]

    build_cmd = build_parts

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
