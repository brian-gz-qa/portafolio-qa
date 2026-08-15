@echo off
chcp 65001 >nul
title LINKEDIN - Abrir para la rutina diaria
echo.
echo  ==========================================
echo   ABRIENDO EDGE CON LINKEDIN...
echo   (deja esta ventana abierta o cierra la
echo    ventana negra, Edge seguira funcionando)
echo  ==========================================
echo.

REM Abrir Edge con LinkedIn y el puerto de depuracion (9222)
start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="%USERPROFILE%\AppData\Local\Microsoft\Edge\User Data" https://www.linkedin.com/feed/

echo  Esperando a que Edge cargue...
timeout /t 8 /nobreak >nul

REM Verificar que el puerto este activo
powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://127.0.0.1:9222/json/version' -UseBasicParsing -TimeoutSec 5; Write-Host '  [OK] Edge listo en puerto 9222' } catch { Write-Host '  [AVISO] No se pudo verificar el puerto, Edge puede seguir cargando' }"

echo.
echo  Listo! La rutina diaria de LinkedIn podra ejecutarse.
echo  Para probarla:  python rutina_diaria.py --solo-revisar
echo.
pause
