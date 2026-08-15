@echo off
chcp 65001 >nul
schtasks /Delete /TN "LinkedInRutinaDiaria" /F >nul 2>&1
schtasks /Create /TN "LinkedInRutinaDiaria" /TR "\"C:\Program Files\Python314\python.exe\" \"C:\Users\NOLAN\Desktop\CLAUDE CODE\rutina_diaria.py\"" /SC DAILY /ST 10:00 /F
echo RESULTADO_CREATE=%errorlevel%
schtasks /Query /TN "LinkedInRutinaDiaria" /FO LIST | findstr /i "TaskName Status Next"
