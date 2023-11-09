#!/usr/bin/env python
# coding: utf-8

# In[5]:


import qrcode 
from Conexion1 import *
# para realQrizar conexiones de modulos propios debes de descargar el archivo 
# con terminacion .py


# In[6]:


class CClientes:
    
    def mostrarClientes():
        try:
            cone =CConexion.ConexionBaseDeDatos()
            cursor =cone.cursor()
            # para decir que los parametros son entradas usamos %s
            cursor.execute("SELECT*FROM usuarios;")
            # la variable valores  tiene que ser una tupla
            #como minima expresion es: (valor,) la coma hace que sea una tupla 
            # las tuplas son listas inmutables, esto quiere decir que no se pueden modificar
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
            
            
            
        except mysql.connector.Error as error:
            print("Error de mostrar datos{}".format(error))
            
    
    def ingresarClientes(N_de_cuenta, nombre, celular, sexo):
        
        try:
            cone =CConexion.ConexionBaseDeDatos()
            cursor =cone.cursor()
            # para decir que los parametros son entradas usamos %s
            sql="INSERT INTO usuarios VALUES(null,%s,%s,%s,%s);" 
            # la variable valores  tiene que ser una tupla 
            #como minima expresion es: (valor,) la coma hace que sea una tupla 
            # las tuplas son listas inmutables, esto quiere decir que no se pueden modificar
            
            valores = (N_de_cuenta, nombre, celular, sexo)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
            
            
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos{}".format(error))
            
            
    def modificarClientes(N_de_registro,N_de_cuenta, nombre, celular, sexo):
        
        try:
            cone =CConexion.ConexionBaseDeDatos()
            cursor =cone.cursor()
            # para decir que los parametros son entradas usamos %s
            sql="UPDATE usuarios SET usuarios.N_de_cuenta= %s, usuarios.nombre = %s,usuarios.celular = %s, usuarios.sexo= %s WHERE usuarios.N_de_registro =%s;" 
            # la variable valores  tiene que ser una tupla 
            #como minima expresion es: (valor,) la coma hace que sea una tupla 
            # las tuplas son listas inmutables, esto quiere decir que no se pueden modificar
            # tengo que respetar los la posicion de los nombres de mi consulta
            valores = (N_de_cuenta, nombre, celular, sexo,N_de_registro)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro actualizado")
            cone.close()
            
            
            
        except mysql.connector.Error as error:
            print("Error de actualizacion de datos{}".format(error))
            
    def eliminarClientes(N_de_registro):
        
        try:
            cone =CConexion.ConexionBaseDeDatos()
            cursor =cone.cursor()
            # para decir que los parametros son entradas usamos %s
            
            sql="DELETE FROM usuarios WHERE usuarios.N_de_registro= %s;" 
            
            # la variable valores  tiene que ser una tupla 
            #como minima expresion es: (valor,) la coma hace que sea una tupla 
            # las tuplas son listas inmutables, esto quiere decir que no se pueden modificar
            
            
            valores = (N_de_registro,)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Eliminado")
            cone.close()
            
            
        except mysql.connector.Error as error:
            print("Error de eliminacion{}".format(error))
        #prueba de  crear y guardar qr

    def crearqr(N_de_registro,N_de_cuenta, nombre, celular, sexo):
        
        try:
            cone =CConexion.ConexionBaseDeDatos()
            cursor =cone.cursor()
            
            datos = f"n_de_registro:{N_de_registro},n_de_cuenta:{N_de_cuenta}, Nombre:{nombre}, celular:{celular}, Sexo:{sexo}"
            codigo_qr = qrcode.make(datos)
            
            
            archivo= f"{nombre}codigo_qr.png"
            codigo_qr.save(archivo)
            

            valores = (N_de_registro, N_de_cuenta, nombre, celular, sexo)
            cursor.execute(datos,archivo,valores)
            cone.commit()
            print(cursor.rowcount,"codigo qr generado y guardado")
            cone.close()
                   
        except mysql.connector.Error as error:
            print("Error de crear QR{}".format(error))
            
            

