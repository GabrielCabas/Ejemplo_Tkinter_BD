# Ejemplo_Tkinter_BD
Ejemplo de Tkinter y CRUD para los alumnos de bases de datos. 

## Requisitos:

 > Python 3
 > Mysql
 > Tkinter

## Librerías de Python 3:

 > mysql
 > matplotlib
 > PIL
 > tkinter

## Instalación de librerías

``` 
pip install mysql-connector-python
pip install matplotlib
pip install PIL
sudo apt-get update
sudo apt install python3-tk
```

## Creación de la base de datos y usuarios:

``` 
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
``` 

## Ejecución: 

``` 
python3 app.py
```

### Actualización: 
En la carpeta ejemplos_graficos hay unos ejemplos de gráficos utilizando matplotlib, numpy y algunos datasets de sklearn. Pueden basarse en esos para crear los suyos dependiendo de cómo sea la información de sus bases de datos. Sean creativos :wink:.

Instalar las siguientes librerías (para los programas en esta carpeta):
```
pip install sklearn
pip install numpy
```
