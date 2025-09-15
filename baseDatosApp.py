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

    def agregar_datos(self, datos):
        try:
            conexion = sqlite3.connect("base_datos.db")
            cursor = conexion.cursor()
            instruction = """INSERT INTO "Articulos" ("GRUPO", "DESCRIPCION", "FECHA_ALTA", "PROVEEDOR", "STOCK", "CANT_BULTOS", "COSTO", "DESCUENTO", "TOTAL_DESCUENTO", "SIN_IVA", "CON_IVA", "COSTO_UNITARIO", "UTILIDAD", "NETO", "LISTA1_UTIL", "LISTA1_NETO", "LISTA2_UTIL", "LISTA2_NETO", "LISTA3_UTIL", "LISTA3_NETO", "LISTA4_UTIL", "LISTA4_NETO", "LISTA5_UTIL", "LISTA5_NETO")
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            cursor.execute(instruction, datos)
            conexion.commit()
            conexion.close()
        except Exception as e:
             messagebox.showerror("Error", f"Error al agregar datos: {str(e)}")

    def listar(self):
        conexion = sqlite3.connect("base_datos.db")
        cursor = conexion.cursor()
        instruction = "SELECT CODIGO_PRODUCTO, DESCRIPCION, COSTO_UNITARIO, NETO FROM Articulos ORDER BY DESCRIPCION ASC"
        cursor.execute(instruction)
        datos = cursor.fetchall()
        conexion.close()
        return datos
    
    def borrar(self, datos):
        conexion = sqlite3.connect("base_datos.db")
        cursor= conexion.cursor()
        instruction= "DELETE FROM Articulos WHERE CODIGO_PRODUCTO= ?"
        cursor.execute(instruction, datos)
        conexion.commit()
        conexion.close()

    def consultar(self, datos):
        conexion= sqlite3.connect("base_datos.db")
        cursor= conexion.cursor()
        instruction= "SELECT GRUPO, DESCRIPCION, FECHA_ALTA, PROVEEDOR, STOCK, CANT_BULTOS, COSTO, DESCUENTO, TOTAL_DESCUENTO, SIN_IVA, CON_IVA, COSTO_UNITARIO, UTILIDAD, NETO, LISTA1_UTIL, LISTA1_NETO, LISTA2_UTIL, LISTA2_NETO, LISTA3_UTIL, LISTA3_NETO, LISTA4_UTIL, LISTA4_NETO, LISTA5_UTIL, LISTA5_NETO FROM Articulos WHERE CODIGO_PRODUCTO= ? ORDER BY DESCRIPCION ASC"
        cursor.execute(instruction, datos)
        data = cursor.fetchall()
        conexion.close()
        return data


    def actualizar(self, datos):
        conexion= sqlite3.connect("base_datos.db")
        cursor= conexion.cursor()
        instruccion= "UPDATE Articulos SET GRUPO= ?, DESCRIPCION= ?, FECHA_ALTA= ?, PROVEEDOR= ?, STOCK= ?, CANT_BULTOS= ?, COSTO= ?, DESCUENTO= ?, TOTAL_DESCUENTO= ?, SIN_IVA= ?, CON_IVA= ?, COSTO_UNITARIO= ?, UTILIDAD= ?, NETO= ?, LISTA1_UTIL= ?, LISTA1_NETO= ?, LISTA2_UTIL= ?, LISTA2_NETO= ?, LISTA3_UTIL= ?, LISTA3_NETO= ?, LISTA4_UTIL= ?, LISTA4_NETO= ?, LISTA5_UTIL= ?, LISTA5_NETO= ? WHERE CODIGO_PRODUCTO= ?"
        cursor.execute(instruccion, datos)
        conexion.commit()
        conexion.close()

    '''def imprimir(self):
        cursor=conexion.cursor()
        instruction= "SELECT * FROM Articulos ORDER BY CODIGO ASC"
        cursor.execute(instruction)
        conexion.close
        return cursor.fetchall()'''


#-------------------Base de datos de CRUD de proveedores-------------------
