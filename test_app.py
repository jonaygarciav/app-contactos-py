import unittest
import os
from app import app, db, Contacto
from config import get_config

class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Configura el entorno de prueba."""
        app.config['TESTING'] = True
        
        # Obtener configuración según el entorno
        config = get_config()
        db_user = os.getenv("DB_USER", config.DB_USER)
        db_password = os.getenv("DB_PASSWORD", config.DB_PASSWORD)
        db_host = os.getenv("DB_HOST", config.DB_HOST)
        db_name = os.getenv("DB_NAME", config.DB_NAME)
        
        app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.client = app.test_client()
    
    def test_primer_usuario(self):
        """Verifica que el primer usuario sea Juan Perez."""
        with app.app_context():
            primer_contacto = Contacto.query.first()
            self.assertEqual(primer_contacto.nombre, 'Juan')
            self.assertEqual(primer_contacto.apellido1, 'Perez')
            self.assertEqual(primer_contacto.apellido2, 'Gomez')
            self.assertEqual(primer_contacto.email, 'juan.perez@example.com')
            self.assertEqual(primer_contacto.telefono, '+34612345678')
    
    def test_ultimo_usuario(self):
        """Verifica que el último usuario sea Sara Jimenez."""
        with app.app_context():
            ultimo_contacto = Contacto.query.order_by(Contacto.id.desc()).first()
            self.assertEqual(ultimo_contacto.nombre, 'Sara')
            self.assertEqual(ultimo_contacto.apellido1, 'Jimenez')
            self.assertEqual(ultimo_contacto.apellido2, 'Navarro')
            self.assertEqual(ultimo_contacto.email, 'sara.jimenez@example.com')
            self.assertEqual(ultimo_contacto.telefono, '+34445566778')
    
    def test_total_usuarios(self):
        """Verifica que haya exactamente 10 usuarios en la base de datos."""
        with app.app_context():
            total_contactos = Contacto.query.count()
            self.assertEqual(total_contactos, 10)

if __name__ == '__main__':
    unittest.main()
