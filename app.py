import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import baseDatosApp
import articulosInterfaz
import proveedoresInterfaz
import clientesInterfaz


class Interfaz:
    def __init__(self):
        self.vent = tk.Tk()
        self.vent.title("Base de datos de Seleccion Argentina")
        self.vent.geometry("1024x720")
        self.Database = baseDatosApp.CRUDarticulos()
        self.Provee= proveedoresInterfaz.proveedoresInterfaz()
        self.Artic= articulosInterfaz.articulosInterfaz()
        self.Clientes= clientesInterfaz.clientesInterfaz()

        self.barraSuperior()

        self.vent.mainloop()



#-------------------Interfaz grafica del CRUD de articulos-------------------
    def barraSuperior(self):
        barraMenu= tk.Menu(self.vent)
        self.vent.config(menu=barraMenu)
        conexionMenu= tk.Menu(barraMenu, tearoff=0)
        conexionMenu.add_command(label="Conexion", command=self.Database.abrir)

        articuloMenu= tk.Menu(barraMenu, tearoff=0)
        articuloMenu.add_command(label="Articulos", command=self.Artic.ventanaArticulo)

        proveedorMenu= tk.Menu(barraMenu, tearoff=0)
        proveedorMenu.add_command(label="Proveedor", command=self.Provee.ventanaProveedores)

        clientesMenu= tk.Menu(barraMenu, tearoff=0)
        clientesMenu.add_command(label="Clientes", command= self.Clientes.ventanaClientes)

        barraMenu.add_cascade(label="Conectar", menu=conexionMenu)
        barraMenu.add_cascade(label="Articulo", menu=articuloMenu)
        barraMenu.add_cascade(label="Proveedores", menu=proveedorMenu)
        barraMenu.add_cascade(label="Clientes", menu=clientesMenu)



    # Pasaje de datos para instrucciones SQL
    def listarSelecc(self):
        self.registros = self.treeview.get_children()
        for elementos in self.registros:
            self.treeview.delete(elementos)
        for fila in self.Database.listar():
            self.treeview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

    def agregarSelecc(self):
        datos = (self.datoCodigo.get(), self.datoDNI.get(), self.datoNombre.get(), self.datoApellido.get(),
                 self.datoNCamiseta.get())
        self.Database.agregar(datos)
        self.datoCodigo.set("")
        self.datoDNI.set("")
        self.datoNombre.set("")
        self.datoApellido.set("")
        self.datoNCamiseta.set("")
        self.listarSelecc()

'''    def borrarSelecc(self):
        datos = (self.treeview.item(self.treeview.selection())["text"],)
        self.Database.borrar(datos)
        self.listarSelecc()

    def consultarSelecc(self):
        datos = (self.treeview.item(self.treeview.selection())["text"],)
        self.Database.consultar(datos)
        self.datoCodigo2.set(self.treeview.item(self.treeview.selection())["text"])
        self.datoDNI2.set(self.treeview.item(self.treeview.selection())["values"][0])
        self.datoNombre2.set(self.treeview.item(self.treeview.selection())["values"][1])
        self.datoApellido2.set(self.treeview.item(self.treeview.selection())["values"][2])
        self.datoNCamiseta2.set(self.treeview.item(self.treeview.selection())["values"][3])

    def actualizarSelecc(self):
        datos = (self.datoDNI2.get(), self.datoNombre2.get(), self.datoApellido2.get(), self.datoNCamiseta2.get(),
                 self.datoCodigo2.get())
        self.Database.actualizar(datos)
        self.datoCodigo2.set("")
        self.datoDNI2.set("")
        self.datoNombre2.set("")
        self.datoApellido2.set("")
        self.datoNCamiseta2.set("")
        self.listarSelecc()

    def imprimirSelecc(self):
        lista = self.Database.imprimir()
        self.scrolledtext.delete("1.0", tk.END)
        for jugadores in lista:
            self.scrolledtext.insert(tk.END, "Codigo: " + str(jugadores[0]) + ",DNI: " + str(jugadores[1]) +
                                     ",Nombre: " + str(jugadores[2]) + ",Apellido: " + str(jugadores[3]) +
                                     ",Numero de camiseta: " + str(jugadores[4]) +
                                     "\n--------------------------------------------------------------------------\n")
'''

inter = Interfaz()
