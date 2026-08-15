@echo off
REM ============================================================
REM  SUBE EL PORTAFOLIO A GITHUB (GitHub Pages)
REM  ============================================================
REM  INSTRUCCIONES (solo 3 pasos, ~10 minutos):
REM
REM  PASO 1: Crea tu cuenta en https://github.com/signup
REM          (usa tu correo gz.sotto@gmail.com)
REM
REM  PASO 2: Crea un repositorio NUEVO:
REM          - Nombre: portafolio-qa
REM          - Debe ser PUBLICO (para GitHub Pages gratis)
REM          - NO marques "Add a README" (ya tenemos todo listo)
REM
REM  PASO 3: Vuelve a esta ventana y escribe tu usuario:
REM          Ejemplo: set USUARIO=tu-nombre-de-usuario
REM
REM  Despues ejecuta este archivo de nuevo. Eso es todo.
REM  ============================================================

set USUARIO=TU_USUARIO_DE_GITHUB_AQUI

if "%USUARIO%"=="TU_USUARIO_DE_GITHUB_AQUI" (
    echo.
    echo  [!] Primero edita este archivo y pon tu usuario de GitHub:
    echo      Abrelo con el Bloc de notas y cambia la linea:
    echo      set USUARIO=TU_USUARIO_DE_GITHUB_AQUI
    echo.
    pause
    exit /b
)

echo.
echo  [1/3] Agregando repositorio remoto...
git remote remove origin 2>nul
git remote add origin https://github.com/%USUARIO%/portafolio-qa.git

echo  [2/3] Subiendo a GitHub...
git branch -M main
git push -u origin main

echo  [3/3] Activando GitHub Pages...
echo   - Ve a https://github.com/%USUARIO%/portafolio-qa/settings/pages
echo   - En "Branch" selecciona: main  y carpeta: / (root)
echo   - Clic en "Save"
echo   - Espera 1-2 minutos y tu portafolio estara en:
echo.
echo   https://%USUARIO%.github.io/portafolio-qa
echo.
echo  [!] Si pide usuario y contrasena al subir:
echo      - Usuario: tu usuario de GitHub
echo      - Contrasena: crea un "Personal Access Token" en
echo        https://github.com/settings/tokens (marca repo) y pegalo
echo.
pause
