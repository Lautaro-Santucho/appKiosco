import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class moduloGrupo:
    def modGrupo(self):
        self.vent= tk.Tk()
        self.vent.geometry("700x500")
        self.vent.title("Modulo de grupo")

        self.__call__()
        self.botonesCRUD()

        self.vent.mainloop()

    def __call__(self):
        # Treeview
        self.treeview = ttk.Treeview(self.vent, columns=("Grupo"))
        self.treeview.grid(column=0, row=0)
        self.treeview.place(width=500, height=200)

        self.treeview.column("#0", width=10)
        self.treeview.column("#1", width=140)


        self.treeview.heading("#0", text="codigo")
        self.treeview.heading("#1", text="Grupo")

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.treeview, orient="vertical", command=self.treeview.yview())
        self.treeview["yscrollcommand"] = self.scrollbar.set

#---------------------Inicio botones CRUD---------------------  

    def botonesCRUD(self):
        self.labelframe1= ttk.Labelframe(self.vent, text="Opciones")
        self.labelframe1.place(x=510, y=0, height=315, width=180)

        #Button
        self.button1 = ttk.Button(self.labelframe1, text="Agregar", width=20).place(x=10, y=0, height=50, width=157)
        self.button2 = ttk.Button(self.labelframe1, text="Modificar", width=20).place(x=10, y=60, height=50, width=157)
        self.button3 = ttk.Button(self.labelframe1, text="Eliminar", width=20).place(x=10, y=120, height=50, width=157)
        self.button4 = ttk.Button(self.labelframe1, text="Cancelar", width=20).place(x=10, y=180, height=50, width=157)
        self.button5 = ttk.Button(self.labelframe1, text="Grabar", width=20).place(x=10, y=240, height=50, width=157)

#---------------------Fin botones CRUD---------------------

    