@echo off
echo === CI Build Started ===
echo Checking source files...
dir
echo === Running Application ===
python app.py
if errorlevel 1 (
    echo APPLICATION FAILED
    exit /b 1
)
echo === Running Application Tests ===
python -m unittest discover -s tests -t .
if errorlevel 1 (
    echo TESTS FAILED
    exit /b 1
)
echo === CI Build Completed Successfully ===
exit /b 0
