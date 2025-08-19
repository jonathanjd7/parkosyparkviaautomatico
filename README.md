# Automatizador GoBarajas

Automatizador para importar reservas de Parkos y Parkvia en GoBarajas.

## 📁 Estructura del Proyecto

```
automatico/
├── gobarajas_final_clean.py      # Automatizador principal
├── gobarajas_config.py           # Configuración del sistema
├── gobarajas_config.env          # Contraseña y configuración
├── requirements.txt              # Dependencias de Python
├── iniciar_automatico.bat        # Script para iniciar automatizador
├── verificar_estado.bat          # Script para verificar estado
├── monitor_gobarajas.py          # Monitor detallado del sistema
├── gobarajas_final_clean.log     # Logs de actividad
└── README.md                     # Esta documentación
```

## 🚀 Instalación y Configuración

### 1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 2. Configurar contraseña:
Editar `gobarajas_config.env` y establecer tu contraseña:
```
GOBARAJAS_PASSWORD=tu_contraseña_aqui
```

## 🎯 Uso

### Iniciar automatizador:
```bash
.\iniciar_automatico.bat
```
**O hacer doble clic en "GoBarajas Automatizador" del escritorio**

### Verificar estado:
```bash
.\verificar_estado.bat
```
**O hacer doble clic en "Verificar GoBarajas" del escritorio**

### Monitor detallado:
```bash
python monitor_gobarajas.py
```

### Ver logs en tiempo real:
```bash
Get-Content gobarajas_final_clean.log -Wait
```

### Detener automatizador:
```bash
taskkill /f /im pythonw.exe
```

## ⚙️ Configuración

### Archivo `gobarajas_config.env`:
```
GOBARAJAS_PASSWORD=tu_contraseña
CHECK_INTERVAL_MINUTES=30
HEADLESS_MODE=False
BROWSER_TYPE=chrome
ENABLE_NOTIFICATIONS=True
```

### Parámetros configurables:
- `CHECK_INTERVAL_MINUTES`: Intervalo de verificación (minutos)
- `HEADLESS_MODE`: Ejecutar sin interfaz gráfica (True/False)
- `BROWSER_TYPE`: Tipo de navegador (chrome/firefox)
- `ENABLE_NOTIFICATIONS`: Habilitar notificaciones

## 🔄 Funcionamiento

### URLs de actualización:
- **Parkos**: https://gobarajas.com/app/actualizadorParkos.php
- **Parkvia**: https://gobarajas.com/app/actualizadorParkvia.php

### Proceso automático:
1. Inicia sesión en GoBarajas
2. Ejecuta actualizador de Parkos
3. Ejecuta actualizador de Parkvia
4. Repite cada 30 minutos
5. Genera logs detallados

## 📊 Monitoreo

### Estado del sistema:
- ✅ **Verificación rápida**: `.\verificar_estado.bat`
- 📊 **Monitor detallado**: `python monitor_gobarajas.py`
- 📝 **Logs en tiempo real**: `Get-Content gobarajas_final_clean.log -Wait`

### Indicadores de funcionamiento:
- Proceso `pythonw.exe` ejecutándose
- Logs actualizándose cada 30 minutos
- Archivo `gobarajas_final_clean.log` creciendo

## 🛠️ Solución de Problemas

### El automatizador no inicia:
1. Verificar que Python esté instalado
2. Ejecutar: `pip install -r requirements.txt`
3. Verificar contraseña en `gobarajas_config.env`

### Múltiples procesos ejecutándose:
1. Detener todos: `taskkill /f /im pythonw.exe`
2. Reiniciar: `.\iniciar_automatico.bat`

### Error de ChromeDriver:
1. Actualizar Selenium: `pip install --upgrade selenium`
2. Limpiar cache: `Remove-Item -Recurse -Force "C:\Users\%USERNAME%\.wdm"`

## 📱 Accesos Directos

### Escritorio:
- **"GoBarajas Automatizador"** - Iniciar automatizador
- **"Verificar GoBarajas"** - Verificar estado

### Funciones:
- ✅ Inicio automático con verificación de duplicados
- ✅ Auto-cierre de ventanas
- ✅ Verificación rápida de estado
- ✅ Logs detallados para monitoreo

---

**Desarrollado para GoBarajas - Aeropuerto de Barajas, Madrid**
