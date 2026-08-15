@echo off
chcp 65001 >nul

schtasks /Delete /TN "LinkedInRutinaDiaria" /F >nul 2>&1
schtasks /Delete /TN "LinkedInManana" /F >nul 2>&1
schtasks /Delete /TN "LinkedInMediodia" /F >nul 2>&1
schtasks /Delete /TN "LinkedInNoche" /F >nul 2>&1

schtasks /Create /TN "LinkedInManana" /TR "\"C:\Program Files\Python314\python.exe\" \"C:\Users\NOLAN\Desktop\CLAUDE CODE\rutina_diaria.py\" --turno manana" /SC DAILY /ST 08:00 /F
echo MANANA=%errorlevel%
schtasks /Create /TN "LinkedInMediodia" /TR "\"C:\Program Files\Python314\python.exe\" \"C:\Users\NOLAN\Desktop\CLAUDE CODE\rutina_diaria.py\" --turno mediodia" /SC DAILY /ST 13:00 /F
echo MEDIODIA=%errorlevel%
schtasks /Create /TN "LinkedInNoche" /TR "\"C:\Program Files\Python314\python.exe\" \"C:\Users\NOLAN\Desktop\CLAUDE CODE\rutina_diaria.py\" --turno noche" /SC DAILY /ST 20:00 /F
echo NOCHE=%errorlevel%

echo --- VERIFICACION ---
schtasks /Query /TN "LinkedInManana" /FO LIST | findstr /i "TaskName Status Next"
schtasks /Query /TN "LinkedInMediodia" /FO LIST | findstr /i "TaskName Status Next"
schtasks /Query /TN "LinkedInNoche" /FO LIST | findstr /i "TaskName Status Next"
