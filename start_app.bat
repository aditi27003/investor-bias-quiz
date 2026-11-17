@echo off
cd /d "%~dp0"
set PY=python
if exist "%USERPROFILE%\anaconda3\python.exe" set PY="%USERPROFILE%\anaconda3\python.exe"
echo Using %PY% > setup_log.txt
echo Installing tools (only slow the first time)...
%PY% -m pip install -r requirements.txt >> setup_log.txt 2>&1
echo Starting Investor Bias Quiz at http://localhost:8502 ...
echo Keep this window open while you use the app. Close it to stop the app.
%PY% -m streamlit run app.py --server.port 8502 >> setup_log.txt 2>&1
echo The app stopped. See setup_log.txt for details.
pause
