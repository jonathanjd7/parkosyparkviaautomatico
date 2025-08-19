@echo off
title Configurador GoBarajas - Nuevo Ordenador
echo ========================================
echo    CONFIGURADOR GOBARAJAS
echo    Nuevo Ordenador - Instalacion
echo ========================================
echo.

REM Obtener la ruta actual
set "CURRENT_DIR=%~dp0"
cd /d "%CURRENT_DIR%"

echo Verificando requisitos del sistema...
echo.

REM Verificar Python
echo 1. Verificando Python...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ ERROR: Python no esta instalado
    echo.
    echo SOLUCION:
    echo 1. Descargar Python desde: https://www.python.org/downloads/
    echo 2. Durante la instalacion, marcar "Add Python to PATH"
    echo 3. Reiniciar este script
    echo.
    pause
    exit /b 1
) else (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
    echo ✅ Python instalado: %PYTHON_VERSION%
)

echo.
echo 2. Verificando pip...
pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ ERROR: pip no esta disponible
    echo.
    echo SOLUCION: Reinstalar Python con pip incluido
    pause
    exit /b 1
) else (
    echo ✅ pip disponible
)

echo.
echo 3. Instalando dependencias...
echo.
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo ❌ ERROR: No se pudieron instalar las dependencias
    echo.
    echo SOLUCION:
    echo 1. Verificar conexion a internet
    echo 2. Ejecutar manualmente: pip install -r requirements.txt
    echo.
    pause
    exit /b 1
) else (
    echo ✅ Dependencias instaladas correctamente
)

echo.
echo 4. Verificando archivo de configuracion...
if exist "gobarajas_config.env" (
    echo ✅ Archivo de configuracion encontrado
    echo.
    echo ⚠️  IMPORTANTE: Verificar la contraseña en gobarajas_config.env
    echo.
    echo Contenido actual:
    type gobarajas_config.env
    echo.
    echo ¿La contraseña es correcta? (S/N)
    choice /c SN /m "Selecciona una opcion"
    if errorlevel 2 (
        echo.
        echo Por favor, edita el archivo gobarajas_config.env
        echo y establece la contraseña correcta:
        echo GOBARAJAS_PASSWORD=tu_contraseña_aqui
        echo.
        pause
    )
) else (
    echo ❌ ERROR: No se encontro gobarajas_config.env
    echo.
    echo Creando archivo de configuracion basico...
    echo GOBARAJAS_PASSWORD=CAMBIAR_ESTA_CONTRASEÑA > gobarajas_config.env
    echo CHECK_INTERVAL_MINUTES=30 >> gobarajas_config.env
    echo HEADLESS_MODE=False >> gobarajas_config.env
    echo BROWSER_TYPE=chrome >> gobarajas_config.env
    echo ENABLE_NOTIFICATIONS=True >> gobarajas_config.env
    echo.
    echo ⚠️  ARCHIVO CREADO: Por favor edita gobarajas_config.env
    echo y establece tu contraseña de GoBarajas
    echo.
    pause
)

echo.
echo 5. Probando el sistema...
echo.
echo Ejecutando monitor para verificar configuracion...
python monitor_gobarajas.py
if %ERRORLEVEL% NEQ 0 (
    echo ❌ ERROR: El monitor no funciona correctamente
    pause
    exit /b 1
)

echo.
echo 6. Creando accesos directos en el escritorio...
echo.

REM Crear acceso directo para iniciar automatizador
echo Creando "GoBarajas Automatizador"...
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\GoBarajas Automatizador.lnk'); $Shortcut.TargetPath = '%CURRENT_DIR%iniciar_automatico.bat'; $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; $Shortcut.Description = 'Iniciar Automatizador GoBarajas'; $Shortcut.Save()" >nul 2>&1

REM Crear acceso directo para verificar estado
echo Creando "Verificar GoBarajas"...
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Verificar GoBarajas.lnk'); $Shortcut.TargetPath = '%CURRENT_DIR%verificar_estado.bat'; $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; $Shortcut.Description = 'Verificar Estado GoBarajas'; $Shortcut.Save()" >nul 2>&1

echo ✅ Accesos directos creados en el escritorio

echo.
echo ========================================
echo     CONFIGURACION COMPLETADA
echo ========================================
echo.
echo ✅ Python instalado y funcionando
echo ✅ Dependencias instaladas
echo ✅ Archivos de configuracion listos
echo ✅ Sistema probado y funcionando
echo ✅ Accesos directos creados
echo.
echo PROXIMOS PASOS:
echo.
echo 1. Verificar contraseña en gobarajas_config.env
echo 2. Probar el automatizador:
echo    - Doble clic en "GoBarajas Automatizador" (escritorio)
echo    - O ejecutar: iniciar_automatico.bat
echo.
echo 3. Verificar funcionamiento:
echo    - Doble clic en "Verificar GoBarajas" (escritorio)
echo    - O ejecutar: verificar_estado.bat
echo.
echo COMANDOS UTILES:
echo   Iniciar: .\iniciar_automatico.bat
echo   Verificar: .\verificar_estado.bat
echo   Monitor: python monitor_gobarajas.py
echo   Detener: taskkill /f /im pythonw.exe
echo.
echo ========================================
echo   GOBARAJAS LISTO PARA USAR
echo ========================================
echo.
pause
