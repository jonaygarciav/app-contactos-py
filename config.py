import os

class Config:
    """Configuración base común a todos los entornos."""
    VERSION = "1.0.0"

    # Configuración de la base de datos
    DB_USER = os.getenv("DB_USER", "contactos_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "ChangeMe!")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "contactos_db")

def get_config(env=None):
    return Config
