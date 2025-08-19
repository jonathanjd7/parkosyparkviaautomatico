@echo off
title GoBarajas Automatizador
echo ========================================
echo    AUTOMATIZADOR GOBARAJAS
echo ========================================
echo.
echo Iniciando automatizador...
echo.
cd /d "%~dp0"

echo Verificando si ya esta ejecutandose...
tasklist | findstr pythonw.exe >nul
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ATENCION: Ya hay un automatizador ejecutandose
    echo.
    echo Opciones:
    echo 1. Cerrar este programa (recomendado)
    echo 2. Detener todos y ejecutar uno nuevo
    echo.
    choice /c 12 /m "Selecciona una opcion"
    if errorlevel 2 goto detener_y_continuar
    if errorlevel 1 exit
)

:detener_y_continuar
echo.
echo Deteniendo automatizadores anteriores...
taskkill /f /im pythonw.exe >nul 2>&1
timeout /t 2 /nobreak >nul

:continuar
echo.
echo Iniciando automatizador en segundo plano...
echo.
start /b pythonw gobarajas_final_clean.py

echo.
echo ========================================
echo   AUTOMATIZADOR INICIADO EXITOSAMENTE
echo ========================================
echo.
echo El automatizador esta funcionando en segundo plano
echo Se ejecutara automaticamente cada 30 minutos
echo.
echo Para verificar el estado:
echo   python monitor_gobarajas.py
echo.
echo Para detener el automatizador:
echo   taskkill /f /im pythonw.exe
echo.
echo Esta ventana se cerrara en 10 segundos...
timeout /t 10 /nobreak >nul
exit
