CREATE DATABASE IF NOT EXISTS contactos_db;
USE contactos_db;

CREATE TABLE IF NOT EXISTS contacto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido1 VARCHAR(50) NOT NULL,
    apellido2 VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15) NOT NULL
);

INSERT INTO contacto (nombre, apellido1, apellido2, email, telefono) VALUES
('Juan', 'Perez', 'Gomez', 'juan.perez@example.com', '+34612345678'),
('Ana', 'Martinez', 'Lopez', 'ana.martinez@example.com', '+34687654321'),
('Carlos', 'Rodriguez', 'Fernandez', 'carlos.rodriguez@example.com', '+34711122334'),
('Elena', 'Gonzalez', 'Hernandez', 'elena.gonzalez@example.com', '+34755667788'),
('Pedro', 'Sanchez', 'Diaz', 'pedro.sanchez@example.com', '+34766778899'),
('Laura', 'Ramirez', 'Castro', 'laura.ramirez@example.com', '+34998877665'),
('Diego', 'Torres', 'Vega', 'diego.torres@example.com', '+34112233445'),
('Marta', 'Flores', 'Ortiz', 'marta.flores@example.com', '+34223344556'),
('Luis', 'Moreno', 'Ruiz', 'luis.moreno@example.com', '+34334455667'),
('Sara', 'Jimenez', 'Navarro', 'sara.jimenez@example.com', '+34445566778');
