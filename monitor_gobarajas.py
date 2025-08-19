"""
Monitor de GoBarajas
Script para verificar el estado del automatizador en segundo plano
"""

import os
import time
import psutil
import datetime
from pathlib import Path

def verificar_proceso_python():
    """Verificar si hay procesos de Python ejecutándose"""
    procesos_python = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'create_time']):
        try:
            if 'python' in proc.info['name'].lower():
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
                if 'gobarajas' in cmdline.lower():
                    procesos_python.append({
                        'pid': proc.info['pid'],
                        'nombre': proc.info['name'],
                        'comando': cmdline,
                        'inicio': datetime.datetime.fromtimestamp(proc.info['create_time']).strftime('%Y-%m-%d %H:%M:%S')
                    })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return procesos_python

def verificar_logs():
    """Verificar los archivos de log más recientes"""
    logs = []
    
    archivos_log = [
        'gobarajas_final_clean.log',
        'gobarajas_final.log',
        'gobarajas_simple.log',
        'gobarajas_multi_url.log'
    ]
    
    for archivo in archivos_log:
        if os.path.exists(archivo):
            stat = os.stat(archivo)
            ultima_modificacion = datetime.datetime.fromtimestamp(stat.st_mtime)
            tamaño = stat.st_size
            
            # Leer las últimas líneas del log
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                    ultimas_lineas = lineas[-10:] if len(lineas) > 10 else lineas
                    ultimo_mensaje = ultimas_lineas[-1].strip() if ultimas_lineas else "Sin mensajes"
            except:
                ultimo_mensaje = "Error al leer archivo"
            
            logs.append({
                'archivo': archivo,
                'ultima_modificacion': ultima_modificacion.strftime('%Y-%m-%d %H:%M:%S'),
                'tamaño': f"{tamaño:,} bytes",
                'ultimo_mensaje': ultimo_mensaje
            })
    
    return logs

def mostrar_estado():
    """Mostrar el estado completo del sistema"""
    print("=" * 60)
    print("MONITOR DE GOBARAJAS - Estado del Sistema")
    print("=" * 60)
    print(f"Fecha y hora: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Verificar procesos
    print("1. PROCESOS DE PYTHON EJECUTÁNDOSE:")
    print("-" * 40)
    procesos = verificar_proceso_python()
    
    if procesos:
        for proc in procesos:
            print(f"   PID: {proc['pid']}")
            print(f"   Nombre: {proc['nombre']}")
            print(f"   Comando: {proc['comando']}")
            print(f"   Inicio: {proc['inicio']}")
            print()
    else:
        print("   No se encontraron procesos de GoBarajas ejecutándose")
        print()
    
    # Verificar logs
    print("2. ARCHIVOS DE LOG:")
    print("-" * 40)
    logs = verificar_logs()
    
    if logs:
        for log in logs:
            print(f"   Archivo: {log['archivo']}")
            print(f"   Última modificación: {log['ultima_modificacion']}")
            print(f"   Tamaño: {log['tamaño']}")
            print(f"   Último mensaje: {log['ultimo_mensaje']}")
            print()
    else:
        print("   No se encontraron archivos de log")
        print()
    
    # Recomendaciones
    print("3. RECOMENDACIONES:")
    print("-" * 40)
    
    if procesos:
        print("   ✅ El automatizador está ejecutándose en segundo plano")
        print("   📊 Puedes monitorear la actividad en los archivos de log")
        print("   🛑 Para detener: usa el Administrador de tareas o 'taskkill'")
    else:
        print("   ⚠️  No se detectó el automatizador ejecutándose")
        print("   🚀 Para iniciar: pythonw gobarajas_final_clean.py")
        print("   📋 Para verificar manualmente: python gobarajas_final_clean.py")
    
    print()
    print("4. COMANDOS ÚTILES:")
    print("-" * 40)
    print("   Ver este monitor: python monitor_gobarajas.py")
    print("   Iniciar en segundo plano: pythonw gobarajas_final_clean.py")
    print("   Ver logs en tiempo real: Get-Content gobarajas_final_clean.log -Wait")
    print("   Detener proceso: taskkill /f /im pythonw.exe")
    print()

def monitoreo_continuo():
    """Monitoreo continuo cada 30 segundos"""
    print("Iniciando monitoreo continuo... (Ctrl+C para detener)")
    print()
    
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            mostrar_estado()
            print("Actualizando en 30 segundos... (Ctrl+C para detener)")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\nMonitoreo detenido")

def main():
    """Función principal"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--continuo":
        monitoreo_continuo()
    else:
        mostrar_estado()

if __name__ == "__main__":
    main()
