# 🚀 Instalación en Nuevo Ordenador - GoBarajas Automatizador

## 📋 Requisitos Previos

### Sistema Operativo:
- ✅ Windows 10/11 (64-bit)
- ✅ Google Chrome instalado
- ✅ Conexión a internet

### Software Requerido:
- ✅ Python 3.7+ (https://www.python.org/downloads/)
- ✅ **IMPORTANTE:** Marcar "Add Python to PATH" durante la instalación

## 🔧 Instalación Automática (RECOMENDADA)

### Paso 1: Preparar archivos
1. Copiar toda la carpeta `parkosyparkviaautomatico` al nuevo ordenador
2. Abrir la carpeta en el explorador de Windows

### Paso 2: Ejecutar instalación automática
1. Hacer doble clic en `configurar_nuevo_ordenador.bat`
2. Seguir las instrucciones en pantalla
3. El script verificará automáticamente:
   - ✅ Instalación de Python
   - ✅ Instalación de dependencias
   - ✅ Configuración de archivos
   - ✅ Creación de accesos directos

### Paso 3: Configurar contraseña
1. Editar el archivo `gobarajas_config.env`
2. Cambiar la línea: `GOBARAJAS_PASSWORD=tu_contraseña_aqui`
3. Establecer tu contraseña real de GoBarajas

### Paso 4: Probar el sistema
1. Ejecutar: `py monitor_gobarajas.py`
2. Verificar que no hay errores
3. ¡Listo para usar!

## 🔧 Instalación Manual (ALTERNATIVA)

### Paso 1: Instalar Python
1. Descargar Python desde: https://www.python.org/downloads/
2. **CRÍTICO:** Marcar "Add Python to PATH" durante la instalación
3. Verificar instalación: `py --version`

### Paso 2: Instalar dependencias
```bash
# Abrir PowerShell en la carpeta del proyecto
py -m pip install -r requirements.txt
py -m pip install psutil
py -m pip install pywin32
```

### Paso 3: Configurar archivos
1. Copiar `gobarajas_config.env.example` como `gobarajas_config.env`
2. Editar `gobarajas_config.env` y establecer tu contraseña
3. Verificar que el archivo existe y tiene el formato correcto

### Paso 4: Probar instalación
```bash
# Probar monitor
py monitor_gobarajas.py

# Probar automatizador (modo prueba)
py gobarajas_final_clean.py
```

## 🎯 Uso Diario

### Iniciar automatizador:
```bash
# Opción 1: Script automático
.\iniciar_automatico.bat

# Opción 2: Manual en segundo plano
Start-Process -FilePath "py" -ArgumentList "gobarajas_final_clean.py" -WindowStyle Hidden

# Opción 3: Acceso directo del escritorio
# "GoBarajas Automatizador"
```

### Verificar estado:
```bash
# Opción 1: Script automático
.\verificar_estado.bat

# Opción 2: Monitor detallado
py monitor_gobarajas.py

# Opción 3: Acceso directo del escritorio
# "Verificar GoBarajas"
```

### Ver logs en tiempo real:
```bash
Get-Content gobarajas_final_clean.log -Wait
```

### Detener automatizador:
```bash
taskkill /f /im python.exe
```

## 🛠️ Solución de Problemas

### ❌ Error: "Python no reconocido"
```bash
# Verificar instalación
py --version

# Si no funciona:
# 1. Reinstalar Python desde https://www.python.org/downloads/
# 2. Marcar "Add Python to PATH" durante la instalación
# 3. Reiniciar PowerShell
```

### ❌ Error: "No module named selenium"
```bash
# Instalar dependencias
py -m pip install -r requirements.txt
py -m pip install psutil pywin32
```

### ❌ Error: "ChromeDriver no válido"
```bash
# Limpiar caché
Remove-Item -Recurse -Force "C:\Users\%USERNAME%\.wdm" -ErrorAction SilentlyContinue

# Reinstalar webdriver-manager
py -m pip install --upgrade webdriver-manager
```

### ❌ Error: "Contraseña incorrecta"
1. Verificar archivo `gobarajas_config.env`
2. Asegurar que la contraseña esté correctamente configurada
3. Reiniciar el automatizador

### ❌ Múltiples procesos ejecutándose
```bash
# Detener todos los procesos
taskkill /f /im python.exe

# Reiniciar automatizador
Start-Process -FilePath "py" -ArgumentList "gobarajas_final_clean.py" -WindowStyle Hidden
```

## 📊 Verificación de Funcionamiento

### Indicadores de éxito:
- ✅ Proceso `python.exe` ejecutándose (visible en `tasklist`)
- ✅ Archivo `gobarajas_final_clean.log` creciendo
- ✅ Logs muestran: "2/2 actualizadores completados"
- ✅ Monitor muestra estado "funcionando"

### Comandos de verificación:
```bash
# Verificar procesos
tasklist | findstr python

# Verificar logs
Get-Content gobarajas_final_clean.log -Tail 10

# Verificar estado completo
py monitor_gobarajas.py
```

## 🔄 Configuración Avanzada

### Modificar intervalo de ejecución:
Editar `gobarajas_config.env`:
```
CHECK_INTERVAL_MINUTES=15  # Cambiar a 15 minutos
```

### Cambiar modo de ejecución:
```
HEADLESS_MODE=False  # Para ver el navegador
HEADLESS_MODE=True   # Modo invisible (recomendado)
```

### Configurar notificaciones:
```
ENABLE_NOTIFICATIONS=True
NOTIFICATION_EMAIL=tu-email@ejemplo.com
```

## 📱 Accesos Directos Creados

El script de instalación crea automáticamente:
- **"GoBarajas Automatizador"** - Iniciar automatizador
- **"Verificar GoBarajas"** - Verificar estado

## 🎉 ¡Listo!

Una vez completada la instalación:
1. ✅ El automatizador se ejecutará cada 30 minutos
2. ✅ Importará automáticamente reservas de Parkos y Parkvia
3. ✅ Funcionará en segundo plano sin interrumpir tu trabajo
4. ✅ Generará logs detallados para monitoreo

### Comandos rápidos para uso diario:
```bash
# Iniciar
Start-Process -FilePath "py" -ArgumentList "gobarajas_final_clean.py" -WindowStyle Hidden

# Verificar
py monitor_gobarajas.py

# Detener
taskkill /f /im python.exe
```

---

**Desarrollado para GoBarajas - AUTOR: Jonathan Doicela**
**Versión 2.0 - Instalación optimizada para nuevo ordenador**
