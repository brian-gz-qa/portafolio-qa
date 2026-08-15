@echo off
REM ============================================================
REM  INSTALADOR DEL CRONOGRAMA DIARIO DE LINKEDIN
REM  Crea un acceso directo para abrir Edge con LinkedIn (puerto 9222)
REM  y programa la rutina diaria en el Programador de tareas.
REM ============================================================
chcp 65001 >nul
echo.
echo  === INSTALADOR DEL CRONOGRAMA DIARIO DE LINKEDIN ===
echo.

REM --- 1. Crear el lanzador de Edge con LinkedIn ---
set "EDGE_PATH=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not exist "%EDGE_PATH%" set "EDGE_PATH=C:\Program Files\Microsoft\Edge\Application\msedge.exe"
if not exist "%EDGE_PATH%" (
    echo [ERROR] No se encontro Microsoft Edge. Abre Edge manualmente.
    pause
    exit /b 1
)

set "LAUNCHER=%USERPROFILE%\Desktop\LINKEDIN_ABRIR.bat"
(
echo @echo off
echo chcp 65001 ^>nul
echo REM Abre Edge con LinkedIn y el puerto de depuracion para la rutina diaria
echo start "" "%EDGE_PATH%" --remote-debugging-port=9222 --user-data-dir="%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data" https://www.linkedin.com/feed/
echo timeout /t 5 /nobreak ^>nul
echo echo  Edge abierto. La rutina diaria ya puede ejecutarse.
) > "%LAUNCHER%"
echo [OK] Lanzador creado: %LAUNCHER%

REM --- 2. Programar la rutina diaria ---
set "PYTHON=C:\Program Files\Python314\python.exe"
if not exist "%PYTHON%" set "PYTHON=python"
set "SCRIPT=%CD%\rutina_diaria.py"

REM Eliminar tarea anterior si existe
schtasks /Delete /TN "LinkedInRutinaDiaria" /F >nul 2>&1

REM Crear la tarea diaria a las 10:00 (ejecuta rutina_diaria.py)
schtasks /Create /TN "LinkedInRutinaDiaria" /TR "\"%PYTHON%\" \"%SCRIPT%\"" /SC DAILY /ST 10:00 /F
if %errorlevel%==0 (
    echo [OK] Tarea diaria programada: LinkedInRutinaDiaria a las 10:00
) else (
    echo [ERROR] No se pudo programar la tarea (puede requerir permisos de administrador).
    echo        Ejecuta este archivo "como administrador" o crea la tarea manualmente.
)

echo.
echo  === RESUMEN ===
echo  1. Abre tu LinkedIn con:  doble clic en "%LAUNCHER%"
echo     (Edge se abrira con tu sesion iniciada)
echo  2. La rutina diaria correra a las 10:00 y hara:
echo     - 1 comentario con valor en el feed
echo     - 1 publicacion con imagen generada (tema del dia)
echo     - revisar la bandeja de mensajes
echo  3. Para probar ahora:  python rutina_diaria.py
echo.
echo  IMPORTANTE: Edge debe estar abierto (con el lanzador) para que funcione.
echo             Si no abres el lanzador, la rutina no podra conectarse.
echo.
pause
