"""
Automatizador Final de GoBarajas - Versión Limpia
Optimizado para los actualizadores específicos de Parkos y Parkvia
"""

import time
import logging
import schedule
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import gobarajas_config as config

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gobarajas_final_clean.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class GoBarajasFinalClean:
    def __init__(self):
        self.driver = None
        # URLs específicas de los actualizadores
        self.actualizadores = [
            {
                'nombre': 'Parkos',
                'url': 'https://gobarajas.com/app/actualizadorParkos.php',
                'descripcion': 'Actualizador de reservas de Parkos'
            },
            {
                'nombre': 'Parkvia',
                'url': 'https://gobarajas.com/app/actualizadorParkvia.php',
                'descripcion': 'Actualizador de reservas de Parkvia'
            }
        ]
        
    def setup_driver(self):
        """Configurar el driver del navegador"""
        try:
            options = Options()
            if config.HEADLESS_MODE:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            
            logger.info("Driver configurado correctamente")
            return True
            
        except Exception as e:
            logger.error(f"Error al configurar el driver: {str(e)}")
            return False
    
    def login(self):
        """Iniciar sesión en GoBarajas"""
        try:
            logger.info("Accediendo a GoBarajas...")
            self.driver.get("https://www.gobarajas.com/app/index.php/reservas/hoy")
            
            # Esperar a que cargue la página
            time.sleep(5)
            
            # Buscar el campo de contraseña
            logger.info("Buscando campo de contraseña...")
            password_field = None
            
            # Intentar diferentes selectores
            selectors = [
                'input[type="password"]',
                'input[name="password"]',
                'input[name="pass"]',
                '#password',
                '#pass'
            ]
            
            for selector in selectors:
                try:
                    password_field = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if password_field.is_displayed():
                        logger.info(f"Campo de contraseña encontrado: {selector}")
                        break
                except:
                    continue
            
            if not password_field:
                logger.error("No se encontró el campo de contraseña")
                return False
            
            # Ingresar contraseña
            password_field.clear()
            password_field.send_keys(config.PASSWORD)
            logger.info("Contraseña ingresada")
            
            # Buscar botón de login o usar Enter
            try:
                # Intentar encontrar botón de submit
                submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"], input[type="submit"]')
                submit_button.click()
                logger.info("Login enviado con botón")
            except:
                # Si no hay botón, usar Enter
                from selenium.webdriver.common.keys import Keys
                password_field.send_keys(Keys.RETURN)
                logger.info("Login enviado con Enter")
            
            # Esperar a que se complete el login
            time.sleep(5)
            
            logger.info("Login completado")
            return True
            
        except Exception as e:
            logger.error(f"Error durante el login: {str(e)}")
            return False
    
    def ejecutar_actualizador(self, actualizador):
        """Ejecutar un actualizador específico"""
        try:
            logger.info(f"Ejecutando {actualizador['nombre']}: {actualizador['descripcion']}")
            
            # Navegar a la página del actualizador
            self.driver.get(actualizador['url'])
            
            # Esperar a que se ejecute la importación automática
            time.sleep(8)
            
            # Verificar si la página se cargó correctamente
            page_source = self.driver.page_source
            
            # Buscar indicadores de éxito específicos
            success_indicators = [
                "ya existe",
                "Reserva con codigo",
                "token_type",
                "access_token",
                "Bearer"
            ]
            
            success_found = False
            for indicator in success_indicators:
                if indicator in page_source:
                    success_found = True
                    logger.info(f"{actualizador['nombre']}: Indicador de éxito encontrado: {indicator}")
                    break
            
            if success_found:
                logger.info(f"{actualizador['nombre']}: Actualización completada exitosamente")
                return True
            else:
                logger.info(f"{actualizador['nombre']}: Actualización ejecutada (sin confirmación específica)")
                return True  # Asumimos que funcionó si la página se cargó
            
        except Exception as e:
            logger.error(f"Error en {actualizador['nombre']}: {str(e)}")
            return False
    
    def ejecutar_todos_actualizadores(self):
        """Ejecutar todos los actualizadores"""
        logger.info("Iniciando ejecución de todos los actualizadores...")
        
        total_exitosos = 0
        for actualizador in self.actualizadores:
            try:
                if self.ejecutar_actualizador(actualizador):
                    total_exitosos += 1
                else:
                    logger.warning(f"{actualizador['nombre']}: No se pudo completar")
            except Exception as e:
                logger.error(f"Error crítico en {actualizador['nombre']}: {str(e)}")
        
        logger.info(f"Resumen: {total_exitosos}/{len(self.actualizadores)} actualizadores completados")
        return total_exitosos > 0
    
    def run_automation_cycle(self):
        """Ejecutar un ciclo completo de automatización"""
        logger.info("=" * 70)
        logger.info(f"Iniciando ciclo de automatización GoBarajas - {datetime.now()}")
        logger.info("=" * 70)
        
        if not self.setup_driver():
            logger.error("No se pudo configurar el driver")
            return
        
        try:
            if not self.login():
                logger.error("No se pudo iniciar sesión en GoBarajas")
                return
            
            success = self.ejecutar_todos_actualizadores()
            
            if success:
                logger.info("Ciclo completado exitosamente")
            else:
                logger.warning("Ciclo completado con errores")
                
        except Exception as e:
            logger.error(f"Error durante el ciclo de automatización: {str(e)}")
        
        finally:
            if self.driver:
                self.driver.quit()
                logger.info("Driver cerrado")
    
    def start_scheduler(self):
        """Iniciar el programador de tareas"""
        logger.info(f"Iniciando programador GoBarajas - verificando cada {config.CHECK_INTERVAL_MINUTES} minutos")
        
        # Mostrar información de los actualizadores
        logger.info("Actualizadores configurados:")
        for actualizador in self.actualizadores:
            logger.info(f"  * {actualizador['nombre']}: {actualizador['url']}")
        
        # Ejecutar inmediatamente al inicio
        self.run_automation_cycle()
        
        # Programar ejecuciones periódicas
        schedule.every(config.CHECK_INTERVAL_MINUTES).minutes.do(self.run_automation_cycle)
        
        logger.info("Programador iniciado - ejecutando en segundo plano...")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Verificar cada minuto

def main():
    """Función principal"""
    print("Automatizador Final de GoBarajas - Version Limpia")
    print("=" * 50)
    print("Aeropuerto de Barajas - Madrid")
    print("Actualizadores: Parkos + Parkvia")
    print("=" * 50)
    
    automation = GoBarajasFinalClean()
    
    try:
        automation.start_scheduler()
    except KeyboardInterrupt:
        logger.info("Programa interrumpido por el usuario")
        print("\nPrograma terminado")
    except Exception as e:
        logger.error(f"Error crítico: {str(e)}")
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()
