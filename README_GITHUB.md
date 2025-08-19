# 🤖 Automatizador GoBarajas

Automatizador para importar reservas de Parkos y Parkvia en GoBarajas (Aeropuerto de Barajas, Madrid).

## 🚀 Instalación Rápida

### 1. Descargar desde GitHub
```bash
git clone https://github.com/tu-usuario/gobarajas-automatizador.git
cd gobarajas-automatizador
```

### 2. Configuración automática (Recomendado)
```bash
# Ejecutar el configurador automático
configurar_nuevo_ordenador.bat
```

### 3. Configuración manual (Alternativa)
```bash
# Instalar dependencias
pip install -r requirements.txt

# Configurar contraseña
copy gobarajas_config.env.example gobarajas_config.env
# Editar gobarajas_config.env y establecer tu contraseña
```

## 📋 Requisitos

- **Windows 10/11**
- **Python 3.7+** ([Descargar](https://www.python.org/downloads/))
- **Google Chrome** ([Descargar](https://www.google.com/chrome/))

## ⚙️ Configuración

### Archivo de configuración
1. Copiar `gobarajas_config.env.example` como `gobarajas_config.env`
2. Editar y establecer tu contraseña:
```env
GOBARAJAS_PASSWORD=tu_contraseña_de_gobarajas
CHECK_INTERVAL_MINUTES=30
HEADLESS_MODE=False
BROWSER_TYPE=chrome
```

## 🎯 Uso

### Iniciar automatizador
```bash
# Opción 1: Script automático
iniciar_automatico.bat

# Opción 2: Manual
pythonw gobarajas_final_clean.py
```

### Verificar estado
```bash
# Verificación rápida
verificar_estado.bat

# Monitor detallado
python monitor_gobarajas.py
```

### Detener automatizador
```bash
taskkill /f /im pythonw.exe
```

## 📊 Funcionamiento

- ✅ **Ejecución automática** cada 30 minutos
- ✅ **Importación de reservas** de Parkos y Parkvia
- ✅ **Funcionamiento en segundo plano**
- ✅ **Logs detallados** para monitoreo
- ✅ **Interfaz simple** con accesos directos

## 🌐 URLs Automatizadas

- **Parkos**: https://gobarajas.com/app/actualizadorParkos.php
- **Parkvia**: https://gobarajas.com/app/actualizadorParkvia.php

## 📁 Estructura del Proyecto

```
gobarajas-automatizador/
├── 🔧 configurar_nuevo_ordenador.bat    # Configuración automática
├── 📄 gobarajas_final_clean.py          # Automatizador principal
├── 📄 gobarajas_config.py               # Configuración del sistema
├── 📄 gobarajas_config.env.example      # Ejemplo de configuración
├── 📄 requirements.txt                  # Dependencias de Python
├── 🚀 iniciar_automatico.bat            # Script para iniciar
├── 🔍 verificar_estado.bat              # Script para verificar
├── 📊 monitor_gobarajas.py              # Monitor detallado
├── 📖 README.md                         # Documentación completa
├── ⚡ INICIO_RAPIDO.txt                 # Guía rápida
└── 📋 INSTALACION_NUEVO_ORDENADOR.md    # Guía detallada
```

## 🛠️ Solución de Problemas

### Error: "python no se reconoce"
```bash
# Reinstalar Python marcando "Add to PATH"
# Descargar desde: https://www.python.org/downloads/
```

### Error: "No module named 'selenium'"
```bash
pip install -r requirements.txt
```

### Error: ChromeDriver no compatible
```bash
pip install --upgrade selenium webdriver-manager
```

### Error: Contraseña incorrecta
```bash
# Verificar gobarajas_config.env
# Asegurarse de que GOBARAJAS_PASSWORD esté configurado
```

### Múltiples procesos ejecutándose
```bash
taskkill /f /im pythonw.exe
```

## 🔒 Seguridad

- ⚠️ **Nunca subir** `gobarajas_config.env` a GitHub
- ✅ Usar `gobarajas_config.env.example` como plantilla
- 🔐 La contraseña se almacena localmente en el archivo `.env`

## 📝 Logs y Monitoreo

### Ver logs en tiempo real
```bash
Get-Content gobarajas_final_clean.log -Wait
```

### Archivos de log importantes
- `gobarajas_final_clean.log` - Historial completo de actividad

## 🤝 Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si tienes problemas:
1. Revisar la sección "Solución de Problemas"
2. Verificar los logs en `gobarajas_final_clean.log`
3. Ejecutar `python monitor_gobarajas.py` para diagnóstico

---

**Desarrollado para GoBarajas - Aeropuerto de Barajas, Madrid** 🛩️
