# 🚀 Instalación en Nuevo Ordenador

Guía completa para transferir el Automatizador GoBarajas a otro ordenador.

## 📋 Requisitos Previos

### 1. Python 3.7 o superior
- Descargar desde: https://www.python.org/downloads/
- **IMPORTANTE**: Marcar "Add Python to PATH" durante la instalación

### 2. Google Chrome
- Descargar desde: https://www.google.com/chrome/
- El automatizador usa ChromeDriver automáticamente

## 📁 Transferencia de Archivos

### Opción 1: Copiar carpeta completa
```
1. Copiar toda la carpeta "automatico" al nuevo ordenador
2. Colocarla en cualquier ubicación (ej: Escritorio, Documentos)
```

### Opción 2: Descargar archivos individuales
Si solo quieres los archivos esenciales:

```
automatico/
├── gobarajas_final_clean.py      # Automatizador principal
├── gobarajas_config.py           # Configuración del sistema
├── gobarajas_config.env          # ⚠️ CONFIGURAR CONTRASEÑA
├── requirements.txt              # Dependencias de Python
├── iniciar_automatico.bat        # Script para iniciar
├── verificar_estado.bat          # Script para verificar
├── monitor_gobarajas.py          # Monitor del sistema
└── README.md                     # Documentación
```

## 🔧 Configuración Paso a Paso

### Paso 1: Verificar Python
```cmd
python --version
```
Debe mostrar: `Python 3.x.x`

### Paso 2: Instalar dependencias
```cmd
cd ruta\a\la\carpeta\automatico
pip install -r requirements.txt
```

### Paso 3: Configurar contraseña
Editar el archivo `gobarajas_config.env`:
```
GOBARAJAS_PASSWORD=tu_contraseña_de_gobarajas
CHECK_INTERVAL_MINUTES=30
HEADLESS_MODE=False
BROWSER_TYPE=chrome
ENABLE_NOTIFICATIONS=True
```

### Paso 4: Crear accesos directos (opcional)
```cmd
# Para crear acceso directo de inicio
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\GoBarajas Automatizador.lnk'); $Shortcut.TargetPath = '%CD%\iniciar_automatico.bat'; $Shortcut.WorkingDirectory = '%CD%'; $Shortcut.Description = 'Iniciar Automatizador GoBarajas'; $Shortcut.Save()"

# Para crear acceso directo de verificación
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\Verificar GoBarajas.lnk'); $Shortcut.TargetPath = '%CD%\verificar_estado.bat'; $Shortcut.WorkingDirectory = '%CD%'; $Shortcut.Description = 'Verificar Estado GoBarajas'; $Shortcut.Save()"
```

## ✅ Verificación de Instalación

### Paso 1: Probar instalación
```cmd
python monitor_gobarajas.py
```

### Paso 2: Probar automatizador
```cmd
iniciar_automatico.bat
```

### Paso 3: Verificar funcionamiento
```cmd
verificar_estado.bat
```

## 🚨 Solución de Problemas Comunes

### Error: "python no se reconoce como comando"
**Solución**: Reinstalar Python marcando "Add to PATH"

### Error: "No module named 'selenium'"
**Solución**: 
```cmd
pip install -r requirements.txt
```

### Error: ChromeDriver no compatible
**Solución**: 
```cmd
pip install --upgrade selenium webdriver-manager
```

### Error: Contraseña incorrecta
**Solución**: Verificar `gobarajas_config.env`

### Error: Puerto ocupado o múltiples procesos
**Solución**: 
```cmd
taskkill /f /im pythonw.exe
```

## 🔄 Configuración Automática (Avanzado)

### Para inicio automático con Windows:
```cmd
schtasks /create /tn "GoBarajas Automatizador" /tr "pythonw.exe %CD%\gobarajas_final_clean.py" /sc onlogon /ru "%USERNAME%" /f
```

### Para eliminar tarea automática:
```cmd
schtasks /delete /tn "GoBarajas Automatizador" /f
```

## 📊 Uso Diario

### Iniciar automatizador:
- Doble clic en "GoBarajas Automatizador" (escritorio)
- O ejecutar: `iniciar_automatico.bat`

### Verificar estado:
- Doble clic en "Verificar GoBarajas" (escritorio)  
- O ejecutar: `verificar_estado.bat`

### Ver logs detallados:
```cmd
python monitor_gobarajas.py
```

### Detener automatizador:
```cmd
taskkill /f /im pythonw.exe
```

## 🎯 Funcionamiento

El automatizador:
- ✅ Se ejecuta cada 30 minutos automáticamente
- ✅ Importa reservas de Parkos y Parkvia
- ✅ Funciona en segundo plano
- ✅ Genera logs detallados
- ✅ Se puede monitorear fácilmente

## 📞 Soporte

### URLs que automatiza:
- Parkos: https://gobarajas.com/app/actualizadorParkos.php
- Parkvia: https://gobarajas.com/app/actualizadorParkvia.php

### Archivos de configuración importantes:
- `gobarajas_config.env` - Contraseña y configuración
- `gobarajas_final_clean.log` - Historial de actividad

---

**¡Listo para funcionar en cualquier ordenador Windows!** 🎉
