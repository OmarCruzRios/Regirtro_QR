create database registro;
-- drop database registro ; --
-- drop table usuarios --
use registro;
 
usuarioscreate table usuarios(
N_de_registro int auto_increment primary key not null, N_de_cuenta VARCHAR(8), nombre VARCHAR(100), 
celular VARCHAR(12), sexo VARCHAR(20)
);
 
 
INSERT INTO usuarios VALUES(null,'1926648','miguel','5514371287',
'Masculino');
 
UPDATE usuarios SET usuarios.N_de_cuenta= 1926649, usuarios.nombre = 'alfred',usuarios.celular ='5514371287', usuarios.sexo= 'Masculino'WHERE usuarios.N_de_registro =2;
 
DELETE FROM usuarios WHERE usuarios.N_de_registro=12;
SELECT * FROM usuarios