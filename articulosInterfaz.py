from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class articulosInterfaz:
    def ventanaArticulo(self):
        self.ventProv= tk.Toplevel()
        self.ventProv.title("Ventana de proveedores")
        self.ventProv.geometry("940x680")

        
        self.treeview()
        self.agregarProductos()
        self.botonesCRUD()
#        self.imprimirProductos()

        self.ventProv.mainloop()

    
    def treeview(self):
        # Treeview
        self.treeview = ttk.Treeview(self.ventProv, columns=("Descripcion", "Costo", "Precio", "Stock"))
        self.treeview.grid(column=0, row=0)
        self.treeview.place(width=620)

        self.treeview.column("#0", width=50)
        self.treeview.column("#1", width=350)
        self.treeview.column("#2", width=5)
        self.treeview.column("#3", width=5)
        self.treeview.column("#4", width=5)

        self.treeview.heading("#0", text="Codigo")
        self.treeview.heading("#1", text="Descripcion")
        self.treeview.heading("#2", text="Costo")
        self.treeview.heading("#3", text="Precio")
        self.treeview.heading("#4", text="Stock")
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.treeview, orient="vertical", command=self.treeview.yview())
        self.treeview["yscrollcommand"] = self.scrollbar.set

#---------------------visualizar datos---------------------

    def agregarProductos(self):

        self.labelframe1 = ttk.Labelframe(self.ventProv)
        self.labelframe1.place(y=250)
        # Labels
        self.label1 = ttk.Label(self.labelframe1, text="Grupo").grid(column=0, row=0, padx=10, pady=10)
        self.label2 = ttk.Label(self.labelframe1, text="CodigoProd").grid(column=0, row=1, padx=10, pady=10)
        self.label3 = ttk.Label(self.labelframe1, text="Descripcion").grid(column=0, row=2, padx=10, pady=10)
        self.label4 = ttk.Label(self.labelframe1, text="Fecha de alta").grid(column=0, row=3, padx=10, pady=10)
        self.label5 = ttk.Label(self.labelframe1, text="Proveedor").grid(column=0, row=4, padx=10, pady=10)
        self.label6 = ttk.Label(self.labelframe1, text="Stock").grid(column=0, row=5, padx=10, pady=10)
        self.label7 = ttk.Label(self.labelframe1, text="Ubicacion fisica").grid(column=0, row=6, padx=10, pady=10)
        self.label9 = ttk.Label(self.labelframe1, text="Cant de bultos").grid(column=0, row=7, padx=10, pady=10)
        self.label10 = ttk.Label(self.labelframe1, text="IVA especial").grid(column=2, row=6, padx=10, pady=10)
        self.label11 = ttk.Label(self.labelframe1, text="Costo", foreground="red").grid(column=2, row=7, padx=10, pady=10)
        self.label12 = ttk.Label(self.labelframe1, text="Desc", foreground="green").grid(column=4, row=7, padx=10, pady=10)

        self.label13 = ttk.Label(self.labelframe1, text="Costo").grid(column=4, row=3, padx=10, pady=10)
        self.label13 = ttk.Label(self.labelframe1, text="Utilidad").grid(column=4, row=4, padx=10, pady=10)
        self.label13 = ttk.Label(self.labelframe1, text="Neto").grid(column=4, row=5, padx=10, pady=10)

        # Entry
        self.datoGrupo = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.datoGrupo).grid(column=1, row=0, padx=10, pady=10)
        self.datoCodigoProd = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.datoCodigoProd).grid(column=1, row=1, padx=10, pady=10)
        self.datoDescripcion = tk.StringVar()
        self.entry3 = ttk.Entry(self.labelframe1, textvariable=self.datoDescripcion).grid(column=1, row=2, padx=10, pady=10)
        self.datoFechaAlta = tk.StringVar()
        self.entry4 = ttk.Entry(self.labelframe1, textvariable=self.datoFechaAlta).grid(column=1, row=3, padx=10, pady=10)
        self.datoProveedor = tk.StringVar()
        self.entry5 = ttk.Entry(self.labelframe1, textvariable=self.datoProveedor).grid(column=1, row=4, padx=10, pady=10)
        self.datoStock = tk.StringVar()
        self.entry6 = ttk.Entry(self.labelframe1, textvariable=self.datoStock).grid(column=1, row=5, padx=10, pady=10)
        self.datoUbiFisica = tk.StringVar()
        self.entry7 = ttk.Entry(self.labelframe1, textvariable=self.datoUbiFisica).grid(column=1, row=6, padx=10, pady=10)
        self.datoCantBultos = tk.StringVar()
        self.entry8 = ttk.Entry(self.labelframe1, textvariable=self.datoCantBultos).grid(column=1, row=7, padx=10, pady=10)
        self.datoIVA = tk.StringVar()
        self.entry9 = ttk.Entry(self.labelframe1, textvariable=self.datoIVA).grid(column=3, row=6, padx=10, pady=10)
        self.datoCosto = tk.StringVar()
        self.entry10 = ttk.Entry(self.labelframe1, textvariable=self.datoCosto).grid(column=3, row=7, padx=10, pady=10)
        self.datoDesc = tk.StringVar()
        self.entry11 = ttk.Entry(self.labelframe1, textvariable=self.datoDesc).grid(column=5, row=7, padx=10, pady=10)
        

        self.datoCosto2 = tk.StringVar()
        self.entry12 = ttk.Entry(self.labelframe1, textvariable=self.datoCosto2).grid(column=5, row=3, padx=10, pady=10)
        self.datoUtilidad = tk.StringVar()
        self.entry13 = ttk.Entry(self.labelframe1, textvariable=self.datoUtilidad).grid(column=5, row=4, padx=10, pady=10)
        self.datoNeto = tk.StringVar()
        self.entry14 = ttk.Entry(self.labelframe1, textvariable=self.datoNeto).grid(column=5, row=5, padx=10, pady=10)

#---------------------visualizar datos---------------------

    def botonesCRUD(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Opciones")
        self.labelframe1.place(y=600)

        #Button
        self.button1 = ttk.Button(self.labelframe1, text="Agregar", width=20).grid(column=0, row=0, padx=10, pady=10)
        self.button2 = ttk.Button(self.labelframe1, text="Modificar", width=20).grid(column=1, row=0, padx=10, pady=10)
        self.button3 = ttk.Button(self.labelframe1, text="Eliminar", width=20).grid(column=2, row=0, padx=10, pady=10)
        self.button4 = ttk.Button(self.labelframe1, text="Cancelar", width=20).grid(column=4, row=0, padx=10, pady=10)
        self.button5 = ttk.Button(self.labelframe1, text="Grabar", width=20).grid(column=5, row=0, padx=10, pady=10)
        
        