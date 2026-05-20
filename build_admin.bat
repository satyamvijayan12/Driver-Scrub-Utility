@echo off
REM ============================================================
REM Driver Scrub Utility - Quick Build Script
REM This script builds the EXE with admin privileges
REM ============================================================

setlocal enabledelayedexpansion

echo.
echo ================================================
echo   Driver Scrub Utility - EXE Builder
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from python.org
    pause
    exit /b 1
)

echo Step 1: Installing PyInstaller...
pip install pyinstaller -q
if errorlevel 1 (
    echo Failed to install PyInstaller
    pause
    exit /b 1
)
echo ✓ PyInstaller installed

echo.
echo Step 2: Cleaning old builds...
if exist build rmdir /s /q build >nul 2>&1
if exist dist rmdir /s /q dist >nul 2>&1
echo ✓ Clean complete

echo.
echo Step 3: Building EXE with admin privileges...
echo This may take 2-5 minutes...
echo.

pyinstaller ^
    --onefile ^
    --windowed ^
    --name "Driver Scrub Utility" ^
    --manifest app.manifest ^
    --add-data "gui;gui" ^
    --add-data "core;core" ^
    --hidden-import=wmi ^
    --hidden-import=PyQt5 ^
    --clean ^
    main.py

if errorlevel 1 (
    echo.
    echo ✗ Build failed!
    pause
    exit /b 1
)

echo.
echo ================================================
echo   ✓ Build Successful!
echo ================================================
echo.
echo EXE Location: dist\Driver Scrub Utility.exe
echo.
echo Features:
echo   ✓ Single executable file
echo   ✓ Administrator privileges enabled
echo   ✓ No console window
echo   ✓ All dependencies included
echo.
echo You can now:
echo   1. Copy dist\Driver Scrub Utility.exe to any location
echo   2. Share it with others
echo   3. Run it - Windows will ask for admin access
echo.
pause
