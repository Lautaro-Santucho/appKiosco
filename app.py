import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as st
import baseDatosApp


class Interfaz:
    def __init__(self):
        self.vent = tk.Tk()
        self.vent.title("Base de datos de Seleccion Argentina")
        self.vent.geometry("600x400")
        self.Database = baseDatosApp.Selecc()
        self.notebook = ttk.Notebook(self.vent)
        self.notebook.grid(column=0, row=0, padx=10, pady=10)

        """#Treeview
        self.treeview = ttk.Treeview(self.vent, columns=("codigo", "DNI", "nombre", "apellido", "NCamiseta"))
        self.treeview.grid(column=1, row=0)

        self.treeview.column("#0", width=80)
        self.treeview.column("#1", width=80)
        self.treeview.column("#2", width=80)
        self.treeview.column("#3", width=80)
        self.treeview.column("#4", width=80)

        self.treeview.heading("#0", text="codigo")
        self.treeview.heading("#1", text="DNI")
        self.treeview.heading("#2", text="nombre")
        self.treeview.heading("#3", text="apellido")
        self.treeview.heading("#4", text="NCamiseta")"""

        self.agregarJugadores()
        self.borrarJugadores()
        self.actualizarJugadores()
        self.imprimirJugadores()
        self.treeview()
        self.listarSelecc()

        self.vent.mainloop()

    def treeview(self):
        # Treeview
        self.treeview = ttk.Treeview(self.vent, columns=("DNI", "nombre", "apellido", "NCamiseta"))
        self.treeview.grid(column=1, row=0)

        self.treeview.column("#0", width=80)
        self.treeview.column("#1", width=80)
        self.treeview.column("#2", width=80)
        self.treeview.column("#3", width=80)
        self.treeview.column("#4", width=80)

        self.treeview.heading("#0", text="codigo")
        self.treeview.heading("#1", text="DNI")
        self.treeview.heading("#2", text="nombre")
        self.treeview.heading("#3", text="apellido")
        self.treeview.heading("#4", text="NCamiseta")
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.treeview, orient="vertical", command=self.treeview.yview())
        self.treeview["yscrollcommand"] = self.scrollbar.set

    def agregarJugadores(self):
        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="Ingresar jugador")
        self.labelframe1 = ttk.Labelframe(self.page1, text="Ingrese los datos del jugador")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        # Labels
        self.label1 = ttk.Label(self.labelframe1, text="Codigo")
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        self.label2 = ttk.Label(self.labelframe1, text="DNI")
        self.label2.grid(column=0, row=1, padx=10, pady=10)
        self.label3 = ttk.Label(self.labelframe1, text="Nombre")
        self.label3.grid(column=0, row=2, padx=10, pady=10)
        self.label4 = ttk.Label(self.labelframe1, text="Apellido")
        self.label4.grid(column=0, row=3, padx=10, pady=10)
        self.label5 = ttk.Label(self.labelframe1, text="N de Camiseta")
        self.label5.grid(column=0, row=4, padx=10, pady=10)
        # Entry
        self.datoCodigo = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.datoCodigo)
        self.entry1.grid(column=1, row=0, padx=10, pady=10)
        self.datoDNI = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.datoDNI)
        self.entry2.grid(column=1, row=1, padx=10, pady=10)
        self.datoNombre = tk.StringVar()
        self.entry3 = ttk.Entry(self.labelframe1, textvariable=self.datoNombre)
        self.entry3.grid(column=1, row=2, padx=10, pady=10)
        self.datoApellido = tk.StringVar()
        self.entry4 = ttk.Entry(self.labelframe1, textvariable=self.datoApellido)
        self.entry4.grid(column=1, row=3, padx=10, pady=10)
        self.datoNCamiseta = tk.StringVar()
        self.entry5 = ttk.Entry(self.labelframe1, textvariable=self.datoNCamiseta)
        self.entry5.grid(column=1, row=4, padx=10, pady=10)
        # Button
        self.button = ttk.Button(self.labelframe1, text="Ingresar", command=self.agregarSelecc)
        self.button.grid(column=1, row=5, padx=10, pady=10)

    def borrarJugadores(self):
        self.page2 = ttk.Frame(self.notebook)
        self.notebook.add(self.page2, text="Borrar jugador")
        self.labelframe1 = ttk.Labelframe(self.page2, text="Borrar jugadores")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        # Label
        self.label = ttk.Label(self.labelframe1, text="Selecciones un jugador para borrar")
        self.label.grid(column=0, row=0, padx=10, pady=10)
        # Button
        self.button = ttk.Button(self.labelframe1, text="Borrar", command=self.borrarSelecc)
        self.button.grid(column=0, row=1, padx=10, pady=10)

    def actualizarJugadores(self):
        self.page3 = ttk.Frame(self.notebook)
        self.notebook.add(self.page3, text="Actualizar/Consultar")
        self.labelframe1 = ttk.Labelframe(self.page3, text="Actualizar/Mostrar jugadores")
        self.labelframe1.grid(column=0, row=0, pady=10, padx=10)
        # Labels
        self.label1 = ttk.Label(self.labelframe1, text="Codigo")
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        self.label2 = ttk.Label(self.labelframe1, text="DNI")
        self.label2.grid(column=0, row=1, padx=10, pady=10)
        self.label3 = ttk.Label(self.labelframe1, text="Nombre")
        self.label3.grid(column=0, row=2, padx=10, pady=10)
        self.label4 = ttk.Label(self.labelframe1, text="Apellido")
        self.label4.grid(column=0, row=3, padx=10, pady=10)
        self.label5 = ttk.Label(self.labelframe1, text="N de Camiseta")
        self.label5.grid(column=0, row=4, padx=10, pady=10)
        # Entry
        self.datoCodigo2 = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.datoCodigo2, state="readonly")
        self.entry1.grid(column=1, row=0, padx=10, pady=10)
        self.datoDNI2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.datoDNI2)
        self.entry2.grid(column=1, row=1, padx=10, pady=10)
        self.datoNombre2 = tk.StringVar()
        self.entry3 = ttk.Entry(self.labelframe1, textvariable=self.datoNombre2)
        self.entry3.grid(column=1, row=2, padx=10, pady=10)
        self.datoApellido2 = tk.StringVar()
        self.entry4 = ttk.Entry(self.labelframe1, textvariable=self.datoApellido2)
        self.entry4.grid(column=1, row=3, padx=10, pady=10)
        self.datoNCamiseta2 = tk.StringVar()
        self.entry5 = ttk.Entry(self.labelframe1, textvariable=self.datoNCamiseta2)
        self.entry5.grid(column=1, row=4, padx=10, pady=10)
        # Button
        self.button = ttk.Button(self.labelframe1, text="Actualizar", command=self.actualizarSelecc)
        self.button.grid(column=1, row=5, padx=10, pady=10)
        self.button1 = ttk.Button(self.labelframe1, text="consultar", command=self.consultarSelecc)
        self.button1.grid(column=0, row=5, padx=10, pady=10)

    def imprimirJugadores(self):
        self.page4 = ttk.Frame(self.notebook)
        self.notebook.add(self.page4, text="Imprimir jugadores")
        self.labelframe = ttk.Labelframe(self.page4, text="Imprimir")
        self.scrolledtext = st.ScrolledText(self.page4, width=90)
        self.scrolledtext.grid(column=0, row=0, pady=0, padx=0)
        # Button
        self.boton = ttk.Button(self.page4, text="Imprimir", command=self.imprimirSelecc)
        self.boton.grid(column=0, row=1, padx=10, pady=10)
        # ScrollBar
        self.ScrollBar = ttk.Scrollbar(self.scrolledtext, orient='vertical', command=self.scrolledtext.yview)
        self.scrolledtext["yscrollcommand"] = self.ScrollBar.set

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

    def borrarSelecc(self):
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


inter = Interfaz()
