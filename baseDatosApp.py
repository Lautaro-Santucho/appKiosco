import sqlite3
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


#-------------------Base de datos de CRUD de articulos-------------------

class CRUDarticulos:
    def __init__(self):
        self.conexion= sqlite3.connect("base_datos.db")

    def abrir(self):
        cursor= self.conexion.cursor()

        try:
            cursor.execute("""CREATE TABLE "Articulos" (
	"GRUPO"	TEXT,
	"CODIGO_PRODUCTO"	INTEGER NOT NULL UNIQUE,
	"DESCRIPCION"	TEXT NOT NULL,
	"FECHA_ALTA"	TEXT,
	"PROVEEDOR"	TEXT,
	"STOCK"	TEXT,
	"CANT_BULTOS"	INTEGER NOT NULL,
	"COSTO"	INTEGER NOT NULL,
	"DESCUENTO"	INTEGER,
	"TOTAL_DESCUENTO"	INTEGER,
	"SIN_IVA"	INTEGER,
	"CON_IVA"	INTEGER,
	"COSTO_UNITARIO"	INTEGER NOT NULL,
	"UTILIDAD"	INTEGER,
	"NETO"	INTEGER NOT NULL,
	"LISTA1_UTIL"	INTEGER,
	"LISTA1_NETO"	INTEGER,
	"LISTA2_UTIL"	INTEGER,
	"LISTA2_NETO"	INTEGER,
	"LISTA3_UTIL"	INTEGER,
	"LISTA3_NETO"	INTEGER,
	"LISTA4_UTIL"	INTEGER,
	"LISTA4_NETO"	INTEGER,
	"LISTA5_UTIL"	INTEGER,
	"LISTA5_NETO"	INTEGER,
	PRIMARY KEY("CODIGO_PRODUCTO" AUTOINCREMENT))""")
            messagebox.showinfo("Base de datos", "La base de datos se ha creado con exito")
            
        except:
            messagebox.showwarning("!Advertencia¡", "La base de datos ya existe")

    def agregar_datos(self, arts):
        #conexion= sqlite3.connect("base_datos.db")
        cursor=self.conexion.cursor()
        instruction= """INSERT INTO "Articulos" ("GRUPO", "CODIGO_PRODUCTO", "DESCRIPCION", "FECHA_ALTA", "PROVEEDOR", "STOCK", "CANT_BULTOS", "COSTO", "DESCUENTO", "TOTAL_DESCUENTO", "SIN_IVA", "CON_IVA", "COSTO_UNITARIO", "UTILIDAD", "NETO", "LISTA1_UTIL", "LISTA1_NETO", "LISTA2_UTIL", "LISTA2_NETO", "LISTA3_UTIL", "LISTA3_NETO", "LISTA4_UTIL", "LISTA4_NETO", "LISTA5_UTIL", "LISTA5_NETO") 
                        VALUES (?, NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(instruction, arts)
        self.conexion.commit()
        self.conexion.close()

    '''def listar(self):
            cursor= self.conexion.cursor()
            instrction= "SELECT * FROM Articulos ORDER BY CODIGO"
            cursor.execute(instrction)
            self.conexion.close()
            return cursor.fetchall()'''
    
'''    def borrar(self, datos):
        cursor= conexion.cursor()
        instrction= "DELETE FROM Articulos WHERE CODIGO= %s"
        cursor.execute(instrction, datos)
        conexion.commit()
        conexion.close()

    

    def consultar(self, datos):
        cursor= conexion.cursor()
        instruction= "SELECT CODIGO, DNI, NOMBRE, APELLIDO, N_CAMISETA FROM JUGADORES WHERE CODIGO= %s ORDER BY CODIGO ASC"
        cursor.execute(instruction, datos)
        conexion.close()
        return cursor.fetchall()

    def actualizar(self, datos):
        cursor= conexion.cursor()
        instruccion= "UPDATE Articulos SET DNI= %s, NOMBRE= %s, APELLIDO= %s, N_CAMISETA= %s WHERE CODIGO= %s"
        cursor.execute(instruccion, datos)
        conexion.commit()
        conexion.close()

    def imprimir(self):
        cursor=conexion.cursor()
        instruction= "SELECT * FROM Articulos ORDER BY CODIGO ASC"
        cursor.execute(instruction)
        conexion.close
        return cursor.fetchall()'''


#-------------------Base de datos de CRUD de proveedores-------------------
