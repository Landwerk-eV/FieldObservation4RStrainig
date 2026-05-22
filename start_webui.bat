@echo off
setlocal

cd /d "%~dp0"

set "PYTHON_EXE=%~dp0.venv\Scripts\python.exe"
set "APP_URL=http://127.0.0.1:8000"

if not exist "%PYTHON_EXE%" (
  echo [ERROR] Python virtual environment not found at:
  echo         %PYTHON_EXE%
  echo.
  echo Create it first, then install dependencies:
  echo   python -m venv .venv
  echo   .venv\Scripts\python.exe -m pip install -r requirements-webui.txt
  pause
  exit /b 1
)

echo [INFO] Checking Web UI dependencies...
"%PYTHON_EXE%" -c "import fastapi,uvicorn,jinja2,geopandas,fiona,shapely,pyproj" >nul 2>&1
if errorlevel 1 (
  echo [INFO] Missing dependencies detected. Installing from requirements-webui.txt ...
  "%PYTHON_EXE%" -m pip install --disable-pip-version-check -r requirements-webui.txt
  if errorlevel 1 (
    echo [ERROR] Dependency installation failed.
    pause
    exit /b 1
  )
) else (
  echo [INFO] Dependencies already installed.
)

echo [INFO] Starting Web UI server...
echo [INFO] URL: %APP_URL%
echo [INFO] This window stays open while the server is running.
echo [INFO] Press CTRL+C to stop the server.
start "" "%APP_URL%"
"%PYTHON_EXE%" -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

echo.
echo [INFO] Web UI server stopped.
pause
