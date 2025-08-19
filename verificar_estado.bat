@echo off
title Verificar Estado GoBarajas
echo ========================================
echo   VERIFICAR ESTADO GOBARAJAS
echo ========================================
echo.

cd /d "%~dp0"

echo Verificando procesos de Python...
echo.

tasklist | findstr pythonw.exe >nul
if %ERRORLEVEL% EQU 0 (
    echo ✅ AUTOMATIZADOR FUNCIONANDO
    echo.
    echo Procesos encontrados:
    tasklist | findstr pythonw.exe
    echo.
    echo El automatizador esta ejecutandose en segundo plano
    echo Se ejecuta automaticamente cada 30 minutos
    echo.
) else (
    echo ❌ AUTOMATIZADOR NO EJECUTANDOSE
    echo.
    echo Para iniciar el automatizador:
    echo - Doble clic en "GoBarajas Automatizador" del escritorio
    echo - O ejecutar: iniciar_automatico.bat
    echo.
)

echo Para ver monitor detallado: python monitor_gobarajas.py
echo Para ver logs recientes: Get-Content gobarajas_final_clean.log -Tail 10
echo.

if exist "gobarajas_final_clean.log" (
    echo ========================================
    echo   ULTIMOS LOGS
    echo ========================================
    echo.
    powershell -Command "Get-Content gobarajas_final_clean.log -Tail 5"
    echo.
)

echo.
echo Presiona cualquier tecla para cerrar...
pause >nul
