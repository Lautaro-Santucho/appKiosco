import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class moduloGrupo:
    def modGrupo(self):
        self.ventProv= tk.Tk()
        self.ventProv.geometry("800x600")
        self.ventProv.title("Modulo de grupo")

        self.__call__()
        self.botonesCRUD()
        self.mostrarDatos()

        self.ventProv.mainloop()

    def __call__(self):
        # Treeview
        self.treeview = ttk.Treeview(self.ventProv, columns=("Grupo"))
        self.treeview.grid(column=0, row=0)
        self.treeview.place(width=585, height=325)

        self.treeview.column("#0", width=10)
        self.treeview.column("#1", width=140)


        self.treeview.heading("#0", text="codigo")
        self.treeview.heading("#1", text="Grupo")

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.treeview, orient="vertical", command=self.treeview.yview())
        self.treeview["yscrollcommand"] = self.scrollbar.set

#---------------------Inicio botones CRUD---------------------  

    def botonesCRUD(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Opciones")
        self.labelframe1.place(x=595, y=0, height=325, width=180)

        #Button
        self.button1 = ttk.Button(self.labelframe1, text="Agregar", width=20).place(x=10, y=0, height=50, width=157)
        self.button2 = ttk.Button(self.labelframe1, text="Modificar", width=20).place(x=10, y=60, height=50, width=157)
        self.button3 = ttk.Button(self.labelframe1, text="Eliminar", width=20).place(x=10, y=120, height=50, width=157)
        self.button4 = ttk.Button(self.labelframe1, text="Cancelar", width=20).place(x=10, y=180, height=50, width=157)
        self.button5 = ttk.Button(self.labelframe1, text="Grabar", width=20).place(x=10, y=240, height=50, width=157)

#---------------------Fin botones CRUD---------------------

#---------------------Visualizacion de datos---------------------

    def mostrarDatos(self):
        #Datos
        self.labelframe=ttk.Labelframe(self.ventProv, text="Datos")
        self.labelframe.place(x=0, y=330, height=115, width=775)

        #Label
        self.label1 = ttk.Label(self.labelframe, text="Codigo").place(x=0, y=14)
        self.label1 = ttk.Label(self.labelframe, text="Grupo").place(x=0, y=49)
        
        #Entry
        self.datoCodigo=tk.StringVar()
        self.entry=ttk.Entry(self.labelframe, textvariable=self.datoCodigo, width=20).place(x=50, y=12, width=350, height=27)
        self.datoCodigo=tk.StringVar()
        self.entry=ttk.Entry(self.labelframe, textvariable=self.datoCodigo, width=20).place(x=50, y=46, width=350, height=27)

        #Busqueda
        self.labelframe2=ttk.Labelframe(self.ventProv, text="Busqueda")
        self.labelframe2.place(x=0, y=450, height=140, width=775)

        self.seleccion= tk.IntVar()
        self.radioButton1= ttk.Radiobutton(self.labelframe2, text="Por Codigo", value=1).place(x=5, y=0)
        self.radioButton2= ttk.Radiobutton(self.labelframe2, text="Por Nombre", value=2).place(x=5, y=25)      
        
        #Entry
        self.datoBuscador = tk.StringVar()
        self.entry10 = ttk.Entry(self.labelframe2, textvariable=self.datoBuscador).place(x=160, y=52, width=250, height=35)        
        
        #Button
        self.button = ttk.Button(self.labelframe2, text="Buscar", width=20).place(x=5, y=50, width=140, height=40)
    