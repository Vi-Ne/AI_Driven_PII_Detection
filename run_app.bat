@echo off
echo Starting PII Detection System...

:: Check if models exist
if not exist "models\model_v2\model.bin" (
    echo [ERROR] Model files matching 'models\model_v2\model.bin' not found.
    echo Please ensure you have placed the trained model in the correct directory.
    pause
    exit /b
)

:: Set PYTHONPATH to current directory
set PYTHONPATH=%CD%

:: Run the server
python -m src.main
pause
