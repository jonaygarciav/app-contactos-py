import os

class Config:
    """Configuración base común a todos los entornos."""
    # Versión de la aplicación
    VERSION = "1.0.0"

def get_config(env=None):
    return Config

