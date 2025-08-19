import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv('gobarajas_config.env')

# Configuración específica para GoBarajas
WEBSITE_URL = "https://www.gobarajas.com/app/index.php/reservas/hoy"
PASSWORD = os.getenv('GOBARAJAS_PASSWORD', '')

# Configuración de la automatización
CHECK_INTERVAL_MINUTES = int(os.getenv('CHECK_INTERVAL_MINUTES', '30'))
HEADLESS_MODE = os.getenv('HEADLESS_MODE', 'False').lower() == 'true'
BROWSER_TYPE = os.getenv('BROWSER_TYPE', 'chrome')

# Configuración de notificaciones
ENABLE_NOTIFICATIONS = os.getenv('ENABLE_NOTIFICATIONS', 'True').lower() == 'true'
NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL', '')

# Configuración específica de GoBarajas
GOBARAJAS_CONFIG = {
    'login_timeout': 15,
    'import_timeout': 10,
    'page_load_timeout': 30,
    'retry_attempts': 3
}
