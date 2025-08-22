# Automatizador GoBarajas

Automatizador para importar reservas de Parkos y Parkvia en GoBarajas.

## 📁 Estructura del Proyecto

```
parkosyparkviaautomatico/
├── gobarajas_final_clean.py      # Automatizador principal (VERSIÓN MEJORADA)
├── gobarajas_config.py           # Configuración del sistema
├── gobarajas_config.env          # Contraseña y configuración
├── gobarajas_config.env.example  # Archivo de ejemplo para configuración
├── requirements.txt              # Dependencias de Python (ACTUALIZADO)
├── iniciar_automatico.bat        # Script para iniciar automatizador
├── verificar_estado.bat          # Script para verificar estado
├── monitor_gobarajas.py          # Monitor detallado del sistema
├── configurar_nuevo_ordenador.bat # Script de instalación automática
├── gobarajas_final_clean.log     # Logs de actividad
├── INICIO_RAPIDO.txt             # Guía de inicio rápido
├── INSTALACION_NUEVO_ORDENADOR.md # Documentación de instalación
└── README.md                     # Esta documentación
```

## 🚀 Instalación y Configuración

### ⚡ INSTALACIÓN AUTOMÁTICA (RECOMENDADA):
1. Copiar toda la carpeta al nuevo ordenador
2. Ejecutar: `.\configurar_nuevo_ordenador.bat`
3. Seguir las instrucciones en pantalla
4. ¡Listo para usar!

### 🔧 INSTALACIÓN MANUAL:
1. **Instalar Python 3.7+** desde https://www.python.org/downloads/
   - ✅ **IMPORTANTE:** Marcar "Add Python to PATH" durante la instalación
2. **Instalar dependencias:**
   ```bash
   py -m pip install -r requirements.txt
   py -m pip install psutil
   py -m pip install pywin32
   ```
3. **Configurar contraseña:**
   - Copiar `gobarajas_config.env.example` como `gobarajas_config.env`
   - Editar y establecer tu contraseña: `GOBARAJAS_PASSWORD=tu_contraseña_aqui`

## 🎯 Uso

### Iniciar automatizador:
```bash
# Opción 1: Script automático
.\iniciar_automatico.bat

# Opción 2: Manual en segundo plano
Start-Process -FilePath "py" -ArgumentList "gobarajas_final_clean.py" -WindowStyle Hidden

# Opción 3: Directo (para pruebas)
py gobarajas_final_clean.py
```

### Verificar estado:
```bash
# Opción 1: Script automático
.\verificar_estado.bat

# Opción 2: Monitor detallado
py monitor_gobarajas.py

# Opción 3: Verificar procesos
tasklist | findstr python
```

### Ver logs en tiempo real:
```bash
Get-Content gobarajas_final_clean.log -Wait
```

### Detener automatizador:
```bash
taskkill /f /im python.exe
```

## ⚙️ Configuración

### Archivo `gobarajas_config.env`:
```
# Contraseña de acceso a GoBarajas (OBLIGATORIO)
GOBARAJAS_PASSWORD=tu_contraseña_aqui

# Configuración de la automatización
CHECK_INTERVAL_MINUTES=30
HEADLESS_MODE=True
BROWSER_TYPE=chrome

# Configuración de notificaciones
ENABLE_NOTIFICATIONS=True
NOTIFICATION_EMAIL=tu-email@ejemplo.com

# Configuración avanzada (opcional)
# LOGIN_TIMEOUT=15
# IMPORT_TIMEOUT=10
# PAGE_LOAD_TIMEOUT=30
# RETRY_ATTEMPTS=3
```

### Parámetros configurables:
- `CHECK_INTERVAL_MINUTES`: Intervalo de verificación (minutos)
- `HEADLESS_MODE`: Ejecutar sin interfaz gráfica (True/False) - **RECOMENDADO: True**
- `BROWSER_TYPE`: Tipo de navegador (chrome/firefox)
- `ENABLE_NOTIFICATIONS`: Habilitar notificaciones

## 🔄 Funcionamiento

### URLs de actualización:
- **Parkos**: https://gobarajas.com/app/actualizadorParkos.php
- **Parkvia**: https://gobarajas.com/app/actualizadorParkvia.php

### Proceso automático:
1. Inicia sesión en GoBarajas con la contraseña configurada
2. Ejecuta actualizador de Parkos
3. Ejecuta actualizador de Parkvia
4. Repite cada 30 minutos automáticamente
5. Genera logs detallados de cada operación

## 📊 Monitoreo

### Estado del sistema:
- ✅ **Verificación rápida**: `.\verificar_estado.bat`
- 📊 **Monitor detallado**: `py monitor_gobarajas.py`
- 📝 **Logs en tiempo real**: `Get-Content gobarajas_final_clean.log -Wait`

### Indicadores de funcionamiento:
- Proceso `python.exe` ejecutándose (PID visible)
- Logs actualizándose cada 30 minutos
- Archivo `gobarajas_final_clean.log` creciendo
- Mensajes de éxito: "2/2 actualizadores completados"

## 🛠️ Solución de Problemas

### ❌ Python no reconocido:
```bash
# Verificar instalación
py --version

# Si no funciona, reinstalar Python con PATH
# Descargar desde: https://www.python.org/downloads/
```

### ❌ Error de ChromeDriver:
```bash
# Limpiar caché del webdriver
Remove-Item -Recurse -Force "C:\Users\%USERNAME%\.wdm" -ErrorAction SilentlyContinue

# Reinstalar dependencias
py -m pip install --upgrade selenium webdriver-manager
```

### ❌ Múltiples procesos ejecutándose:
```bash
# Detener todos los procesos
taskkill /f /im python.exe

# Reiniciar automatizador
Start-Process -FilePath "py" -ArgumentList "gobarajas_final_clean.py" -WindowStyle Hidden
```

### ❌ Error de módulos faltantes:
```bash
# Instalar dependencias faltantes
py -m pip install psutil pywin32

# Verificar instalación completa
py -m pip install -r requirements.txt
```

### ❌ Contraseña incorrecta:
1. Verificar archivo `gobarajas_config.env`
2. Asegurar que la contraseña esté correctamente configurada
3. Reiniciar el automatizador

## 🔧 Mejoras Implementadas

### ✅ **Versión 2.0 - Cambios Principales:**
- **ChromeDriver mejorado**: Solución al problema de compatibilidad Win32/Win64
- **Modo headless por defecto**: Ejecución sin interfaz gráfica para mayor estabilidad
- **Dependencias actualizadas**: psutil y pywin32 añadidas
- **Script de instalación automática**: `configurar_nuevo_ordenador.bat`
- **Monitor mejorado**: Detección precisa de procesos y logs
- **Configuración robusta**: Manejo mejorado de errores y timeouts
- **Logs detallados**: Información completa de cada operación

### ✅ **Nuevas Características:**
- **Instalación automática** en nuevo ordenador
- **Detección automática** de problemas de ChromeDriver
- **Configuración simplificada** con archivo de ejemplo
- **Monitoreo en tiempo real** del estado del sistema
- **Gestión mejorada** de procesos en segundo plano

## 📱 Accesos Directos

### Escritorio (creados automáticamente):
- **"GoBarajas Automatizador"** - Iniciar automatizador
- **"Verificar GoBarajas"** - Verificar estado

### Funciones:
- ✅ Inicio automático con verificación de duplicados
- ✅ Auto-cierre de ventanas del navegador
- ✅ Verificación rápida de estado
- ✅ Logs detallados para monitoreo
- ✅ Gestión automática de ChromeDriver
- ✅ Modo headless para mayor estabilidad

## 🚀 Comandos Rápidos

```bash
# Instalación completa
.\configurar_nuevo_ordenador.bat

# Iniciar automatizador
Start-Process -FilePath "py" -ArgumentList "gobarajas_final_clean.py" -WindowStyle Hidden

# Verificar estado
py monitor_gobarajas.py

# Ver logs en tiempo real
Get-Content gobarajas_final_clean.log -Wait

# Detener automatizador
taskkill /f /im python.exe
```

---

**Desarrollado para GoBarajas - AUTOR: Jonathan Doicela**
**Versión 2.0 - Optimizada para instalación en nuevo ordenador**
