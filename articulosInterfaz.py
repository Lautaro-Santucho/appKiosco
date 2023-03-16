from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
import baseDatosApp


class articulosInterfaz:
    #poner ventana main
    def ventanaArticulo(self):
        self.ventProv= tk.Toplevel()
        self.ventProv.title("Ventana de productos")
        self.ventProv.geometry("940x680")
        self.DataBase= baseDatosApp.CRUDarticulos

        self.__call__()
        self.agregarProductos()
        self.botonesCRUD()
        self.lista()

        self.ventProv.mainloop()

    
    def __call__(self):
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
        self.labelframe1.place(y=250, width=800, height=500)
        # Labels
        self.label1 = ttk.Label(self.labelframe1, text="Grupo").grid(column=0, row=0, padx=10, pady=10)
        self.label2 = ttk.Label(self.labelframe1, text="CodigoProd").grid(column=0, row=1, padx=10, pady=10)
        self.label3 = ttk.Label(self.labelframe1, text="Descripcion").grid(column=0, row=2, padx=10, pady=10)
        self.label4 = ttk.Label(self.labelframe1, text="Fecha de alta").grid(column=0, row=3, padx=10, pady=10)
        self.label5 = ttk.Label(self.labelframe1, text="Proveedor").grid(column=0, row=4, padx=10, pady=10)
        self.label6 = ttk.Label(self.labelframe1, text="Stock").grid(column=0, row=5, padx=10, pady=10)
        self.label7 = ttk.Label(self.labelframe1, text="Ubicacion fisica").grid(column=0, row=6, padx=10, pady=10)
        self.label9 = ttk.Label(self.labelframe1, text="Cant de bultos").grid(column=0, row=7, padx=10, pady=10)
        self.label10 = ttk.Label(self.labelframe1, text="IVA especial").place(x=342, y=253)
        self.label11 = ttk.Label(self.labelframe1, text="Costo", foreground="red").place(x=230, y=293)
        self.label12 = ttk.Label(self.labelframe1, text="Desc", foreground="green").place(x=385, y=293)

        self.label13 = ttk.Label(self.labelframe1, text="Costo").place(x=385, y=125)
        self.label13 = ttk.Label(self.labelframe1, text="Utilidad").place(x=375, y=168)
        self.label13 = ttk.Label(self.labelframe1, text="Neto").place(x=385, y=208)

        # Entry
        self.datoGrupo = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.datoGrupo).place(x=110, y=13, width=100, height=25)
        self.datoCodigoProd = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.datoCodigoProd).place(x=110, y=53, width=100, height=25)
        self.datoDescripcion = tk.StringVar()
        self.entry3 = ttk.Entry(self.labelframe1, textvariable=self.datoDescripcion).place(x=110, y=93, width=250, height=25)
        self.datoFechaAlta = tk.StringVar()
        self.entry4 = ttk.Entry(self.labelframe1, textvariable=self.datoFechaAlta).place(x=110, y=133, width=100, height=25)
        self.datoProveedor = tk.StringVar()
        self.entry5 = ttk.Entry(self.labelframe1, textvariable=self.datoProveedor).place(x=110, y=173, width=100, height=25)
        self.datoStock = tk.StringVar()
        self.entry6 = ttk.Entry(self.labelframe1, textvariable=self.datoStock).place(x=110, y=213, width=100, height=25)
        self.datoUbiFisica = tk.StringVar()
        self.entry7 = ttk.Entry(self.labelframe1, textvariable=self.datoUbiFisica).place(x=110, y=253, width=100, height=25)
        self.datoCantBultos = tk.StringVar()
        self.entry8 = ttk.Entry(self.labelframe1, textvariable=self.datoCantBultos).place(x=110, y=293, width=100, height=25)
        self.datoIVA = tk.StringVar()
        self.entry9 = ttk.Entry(self.labelframe1, textvariable=self.datoIVA).place(x=420, y=253, width=100, height=25)
        self.datoCosto = tk.StringVar()
        self.entry10 = ttk.Entry(self.labelframe1, textvariable=self.datoCosto).place(x=275, y=293, width=100, height=25)
        self.datoDesc = tk.StringVar()
        self.entry11 = ttk.Entry(self.labelframe1, textvariable=self.datoDesc).place(x=420, y=293, width=100, height=25)
      

        self.datoCosto2 = tk.StringVar()
        self.entry12 = ttk.Entry(self.labelframe1, textvariable=self.datoCosto2).place(x=425, y=125, width=50)
        self.datoUtilidad = tk.StringVar()
        self.entry13 = ttk.Entry(self.labelframe1, textvariable=self.datoUtilidad).place(x=425, y=168, width=50)
        self.datoNeto = tk.StringVar()
        self.entry14 = ttk.Entry(self.labelframe1, textvariable=self.datoNeto).place(x=425, y=208, width=50)



    def botonesCRUD(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Opciones")
        self.labelframe1.place(y=600)

        #Button
        self.button1 = ttk.Button(self.labelframe1, text="Agregar", width=20).grid(column=0, row=0, padx=10, pady=10)
        self.button2 = ttk.Button(self.labelframe1, text="Modificar", width=20).grid(column=1, row=0, padx=10, pady=10)
        self.button3 = ttk.Button(self.labelframe1, text="Eliminar", width=20).grid(column=2, row=0, padx=10, pady=10)
        self.button4 = ttk.Button(self.labelframe1, text="Cancelar", width=20, command=self.cancelar).grid(column=4, row=0, padx=10, pady=10)
        self.button5 = ttk.Button(self.labelframe1, text="Grabar", width=20).grid(column=5, row=0, padx=10, pady=10)

#---------------------fin visualizar datos---------------------        
        
    def lista(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Lista de productos")
        self.labelframe1.place(x=700, y=300, width=220, height=300)
        #Labels
        self.label1 = ttk.Label(self.labelframe1, text="Lista 1").place(x=0, y=30)
        self.label2 = ttk.Label(self.labelframe1, text="Lista 2").place(x=0, y=70)
        self.label3 = ttk.Label(self.labelframe1, text="Lista 3").place(x=0, y=110)
        self.label4 = ttk.Label(self.labelframe1, text="Lista 4").place(x=0, y=150)
        self.label5 = ttk.Label(self.labelframe1, text="Lista 5").place(x=0, y=190)

        self.label6 = ttk.Label(self.labelframe1, text="Lista 5").place(x=50, y=0)
        self.label7 = ttk.Label(self.labelframe1, text="Lista 5").place(x=110, y=0)

        #Entry
        self.datoGrupo = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.datoGrupo, width=20).place(x=50, y=30, width=50)
        self.datoCodigoProd = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.datoCodigoProd, width=20).place(x=50, y=70, width=50)
        self.datoDescripcion = tk.StringVar()
        self.entry3 = ttk.Entry(self.labelframe1, textvariable=self.datoDescripcion, width=20).place(x=50, y=110, width=50)
        self.datoFechaAlta = tk.StringVar()
        self.entry4 = ttk.Entry(self.labelframe1, textvariable=self.datoFechaAlta, width=20).place(x=50, y=150, width=50)
        self.datoProveedor = tk.StringVar()
        self.entry5 = ttk.Entry(self.labelframe1, textvariable=self.datoProveedor, width=20).place(x=50, y=190, width=50)

        self.datoGrupo = tk.StringVar()
        self.entry6 = ttk.Entry(self.labelframe1, textvariable=self.datoGrupo).place(x=110, y=30, width=50)
        self.datoCodigoProd = tk.StringVar()
        self.entry7 = ttk.Entry(self.labelframe1, textvariable=self.datoCodigoProd).place(x=110, y=70, width=50)
        self.datoDescripcion = tk.StringVar()
        self.entry8 = ttk.Entry(self.labelframe1, textvariable=self.datoDescripcion).place(x=110, y=110, width=50)
        self.datoFechaAlta = tk.StringVar()
        self.entry9 = ttk.Entry(self.labelframe1, textvariable=self.datoFechaAlta).place(x=110, y=150, width=50)
        self.datoProveedor = tk.StringVar()
        self.entry10 = ttk.Entry(self.labelframe1, textvariable=self.datoProveedor).place(x=110, y=190, width=50)



    # Pasaje de datos para instrucciones SQL
    def listarProductos(self):
        self.registros = self.treeview.get_children()
        for elementos in self.registros:
            self.treeview.delete(elementos)
        for fila in self.DataBase.listar():
            self.treeview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))

    '''def agregarProductos(self):
        datos = (self.datoGrupo.get(), self.datoCodigoProd.get(), self.datoDescripcion.get(), 
                 self.datoFechaAlta.get(),self.datoStock.get(),self.datoUbiFisica.get(),
                 self.datoCantBultos.get(),self.datoIVA.get(),self.datoCosto.get(),
                 self.datoDesc.get())
        self.DataBase.agregar(datos)
        self.datoGrupo.set("")
        self.datoCodigoProd.set("")
        self.datoDescripcion.set("")
        self.datoFechaAlta.set("")
        self.datoStock.set("")
        self.datoUbiFisica.set("")
        self.datoCantBultos.set("")
        self.datoIVA.set("")
        self.datoCosto.set("")
        self.datoDesc.set("")


        self.listarSelecc()'''

