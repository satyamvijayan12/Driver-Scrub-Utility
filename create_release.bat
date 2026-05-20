@echo off
REM Create GitHub Release v0.2
REM This script creates a release tag and pushes it to GitHub

echo.
echo ================================================
echo   Driver Utility Scrub v0.2 - GitHub Release
echo ================================================
echo.

cd /d "c:\Users\SATYAM VIJAYAN\Desktop\HELLO\Driver Scrub Utility\Driver-Scrub-Utility"

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Error: Git is not installed or not in PATH
    pause
    exit /b 1
)

echo Creating release tag v0.2...
git tag -a v0.2 -m "Driver utility Scrub v0.2"
if errorlevel 1 (
    echo Error: Failed to create tag
    pause
    exit /b 1
)

echo Pushing tag to GitHub...
git push origin v0.2
if errorlevel 1 (
    echo Error: Failed to push tag
    pause
    exit /b 1
)

echo.
echo ================================================
echo   ✓ Release Created Successfully!
echo ================================================
echo.
echo Release Details:
echo   Tag: v0.2
echo   Name: Driver utility Scrub v0.2
echo   URL: https://github.com/satyamvijayan12/Driver-Scrub-Utility/releases/tag/v0.2
echo.
echo Next Steps:
echo   1. Visit the release URL above
echo   2. Click Edit button
echo   3. Add release notes from GITHUB_RELEASE_INFO.md
echo   4. Save changes
echo.
pause
