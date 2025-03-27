from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from config import get_config

# Cargar variables desde .env si no están definidas en el entorno
load_dotenv()

# Crear app Flask
app = Flask(__name__)

# Obtener configuración base
config = get_config()

# Intentar obtener las variables de conexión desde:
# 1. Variables de entorno
# 2. .env (cargado previamente por load_dotenv)
# 3. config.py (si las anteriores fallan)
# 4. Lanzar error si no se encuentra alguna

required_vars = ['DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_NAME']
missing_vars = []

db_user = os.getenv("DB_USER") or getattr(config, 'DB_USER', None)
db_password = os.getenv("DB_PASSWORD") or getattr(config, 'DB_PASSWORD', None)
db_host = os.getenv("DB_HOST") or getattr(config, 'DB_HOST', None)
db_name = os.getenv("DB_NAME") or getattr(config, 'DB_NAME', None)

# Validar que están todas
vars_dict = {
    'DB_USER': db_user,
    'DB_PASSWORD': db_password,
    'DB_HOST': db_host,
    'DB_NAME': db_name
}

for var, value in vars_dict.items():
    if not value:
        missing_vars.append(var)

if missing_vars:
    raise EnvironmentError(
        f"⚠️ Error: Faltan las siguientes variables de conexión a la base de datos: {', '.join(missing_vars)}"
    )

# Configuración de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido1 = db.Column(db.String(50), nullable=False)
    apellido2 = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)    
    telefono = db.Column(db.String(15), nullable=False)

@app.route('/')
def index():
    contactos = Contacto.query.all()
    return render_template('index.html', contactos=contactos, version=config.VERSION)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

