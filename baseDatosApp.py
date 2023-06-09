import sqlite3
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


#-------------------Base de datos de CRUD de articulos-------------------

class CRUDarticulos:
    def abrir(self):
        conexion= sqlite3.connect("Base de datos")
        cursor= conexion.cursor()

        try:
            cursor.execute("""CREATE TABLE ARTICULOS(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                GRUPO INTEGER,
                                CODIGO INTEGER,
                                DESCRIPCION VARCHAR (100),
                                FECHA_ALTA VARCHAR (11),
                                STOCK INTEGER,
                                UBICACION_FISICA INTEGER,
                                CANT_BULTOS INTEGER,
                                COSTO INTEGER);""")
            
            messagebox.showinfo("Base de datos", "La base de datos se ha creado con exito")
            
        except:
            messagebox.showwarning("!Advertencia¡", "La base de datos ya existe")

    def agregar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instruction= "INSERT INTO jugadores VALUES (NULL, ?, ?, ?, ?)"
        cursor.execute(instruction, datos)
        conexion.commit()
        conexion.close()

    def listar(self):
            conexion= self.abrir()
            cursor= conexion.cursor()
            instrction= "SELECT * FROM jugadores ORDER BY CODIGO"
            cursor.execute(instrction)
            conexion.close()
            return cursor.fetchall()
    
'''    def borrar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instrction= "DELETE FROM jugadores WHERE CODIGO= %s"
        cursor.execute(instrction, datos)
        conexion.commit()
        conexion.close()

    

    def consultar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instruction= "SELECT CODIGO, DNI, NOMBRE, APELLIDO, N_CAMISETA FROM JUGADORES WHERE CODIGO= %s ORDER BY CODIGO ASC"
        cursor.execute(instruction, datos)
        conexion.close()
        return cursor.fetchall()

    def actualizar(self, datos):
        conexion= self.abrir()
        cursor= conexion.cursor()
        instruccion= "UPDATE jugadores SET DNI= %s, NOMBRE= %s, APELLIDO= %s, N_CAMISETA= %s WHERE CODIGO= %s"
        cursor.execute(instruccion, datos)
        conexion.commit()
        conexion.close()

    def imprimir(self):
        conexion=self.abrir()
        cursor=conexion.cursor()
        instruction= "SELECT * FROM JUGADORES ORDER BY CODIGO ASC"
        cursor.execute(instruction)
        conexion.close
        return cursor.fetchall()'''


#-------------------Base de datos de CRUD de proveedores-------------------
