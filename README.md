# Ejemplo_Tkinter_BD
Ejemplo de Tkinter y CRUD para los alumnos de bases de datos.

Requisitos:
Python 3

Instalación:
pip install mysql-connector-python
sudo apt-get update
sudo apt install python3-tk

En Mysql: 
create database db_test1;
use db_test1;
CREATE TABLE equipo (
id_equipo int(11) NOT NULL AUTO_INCREMENT,
nom_equipo varchar(150) NOT NULL,
puntos int(11) NOT NULL,
PRIMARY KEY (id_equipo),
UNIQUE KEY EQUIPO_PK (id_equipo));
CREATE TABLE jugador (
id_jugador int(11) NOT NULL AUTO_INCREMENT,
id_equipo int(11) DEFAULT NULL,
nom_jugador varchar(200) NOT NULL,
ape_jugador varchar(200) NOT NULL,
PRIMARY KEY (id_jugador),
UNIQUE KEY JUGADOR_PK (id_jugador),
KEY JUEGA_EN_FK (id_equipo),
CONSTRAINT FK_JUGADOR_JUEGA_EN_EQUIPO FOREIGN KEY
(id_equipo) REFERENCES equipo (id_equipo));
create user 'test'@'localhost' identified by 'test';
grant all privileges on db_test1.* to 'test'@'localhost';
flush privileges;

Ejecución: 
python3 app.py
