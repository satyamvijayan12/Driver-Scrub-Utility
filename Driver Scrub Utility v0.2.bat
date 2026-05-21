@echo off
REM Build script to create Driver Scrub Utility EXE with admin privileges
REM Install PyInstaller if not already installed
pip install pyinstaller --quiet

REM Create the executable with:
REM - Single file (--onefile)
REM - Admin manifest (--manifest)
REM - Icon (if available)
REM - Hidden console window
REM - Optimized runtime

echo Building Driver Scrub Utility EXE...

pyinstaller ^
    --onefile ^
    --windowed ^
    --name "Driver Scrub Utility" ^
    --manifest app.manifest ^
    --add-data "gui:gui" ^
    --add-data "core:core" ^
    --hidden-import=wmi ^
    --hidden-import=PyQt5 ^
    --clean ^
    main.py

echo.
echo Build complete! EXE location: dist\Driver Scrub Utility.exe
echo.
pause
