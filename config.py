import os

class Config:
    """Configuración base común a todos los entornos."""
    VERSION = "1.0.0"
    DEBUG = False
    TESTING = False
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Configuración de la base de datos
    DB_USER = os.getenv("DB_USER", "contactos_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "ChangeMe!")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "contactos_db")

class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuración para producción."""
    LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING")

# Selección de configuración según entorno
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

def get_config(env=None):
    """Devuelve la configuración correspondiente al entorno especificado."""
    env = env or os.getenv("FLASK_ENV", "development")
    config_class = config_by_name.get(env, DevelopmentConfig)
    return config_class
