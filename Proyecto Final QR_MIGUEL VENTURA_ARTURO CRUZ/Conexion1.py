#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector 


# In[2]:


class CConexion:
    
    def ConexionBaseDeDatos():
        try:
            conexion =mysql.connector.connect(user='root', password='root', host='127.0.0.1',
                                             database='registro',port='3306')
            print("conexion correcta")
            
            return conexion
        
        
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos{}".format(error))
            return conexion
            
    ConexionBaseDeDatos()


# In[ ]:




