import sqlite3

try:
    # Mantén la conexión abierta
    db = sqlite3.connect('C:\\Users\\Meunier\\Documents\\ProyectosPersonales\\BasesLocales\\Hospital.db') #Aca iria la ruta de la base de datos suya
    cursor = db.cursor()
except sqlite3.Error as e:
    print(f"Error de base de datos: {e}")  



# Correr el siguiente codigo de tablas en su base de datos
'''
CREATE TABLE medicos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    telefono VARCHAR(15)
);

CREATE TABLE pacientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    direccion VARCHAR(100),
    enfermedad VARCHAR(50)
);

CREATE TABLE citas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    paciente_id INT NOT NULL,
    medico_id INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (medico_id) REFERENCES medicos(id)
);

CREATE TABLE historial_clinico (
    id INT PRIMARY KEY AUTO_INCREMENT,
    paciente_id INT NOT NULL,
    fecha DATE NOT NULL,
    diagnostico TEXT NOT NULL,
    tratamiento TEXT,
    medico_id INT NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
    FOREIGN KEY (medico_id) REFERENCES medicos(id)
);

CREATE TABLE habitaciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero INT NOT NULL UNIQUE,
    tipo VARCHAR(50) NOT NULL,
    capacidad INT NOT NULL,
    estado VARCHAR(20) NOT NULL
); 
'''