import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class moduloGrupo:
    def modGrupo(self):
        self.vent= tk.Tk()
        self.vent.geometry("700x500")
        self.vent.title("Modulo de grupo")

        self.__call__()

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

    