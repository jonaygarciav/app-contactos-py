from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from config import get_config

app = Flask(__name__)

# Obtener configuración según el entorno
config = get_config()

# Cargar configuración desde variables de entorno o desde config.py
db_user = os.getenv("DB_USER", config.DB_USER)
db_password = os.getenv("DB_PASSWORD", config.DB_PASSWORD)
db_host = os.getenv("DB_HOST", config.DB_HOST)
db_name = os.getenv("DB_NAME", config.DB_NAME)

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
