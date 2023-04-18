from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class proveedoresInterfaz:
    def ventanaProveedores(self):
        self.ventProv= tk.Toplevel()
        self.ventProv.title("Ventana de proveedores")
        self.ventProv.geometry("940x680")
        
        self.__call__()
        self.buscador()
        self.agregarClientes()
        self.botonesCRUD()
#        self.agregarJugadores()
#        self.borrarJugadores()
#        self.actualizarJugadores()
#        self.imprimirJugadores()

        self.ventProv.mainloop()

    
    def __call__(self):
        # Treeview
        self.treeview = ttk.Treeview(self.ventProv, columns=("DNI", "nombre", "apellido", "NCamiseta"))
        self.treeview.grid(column=0, row=0)
        self.treeview.place(width=520, height=150)

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

#---------------------Crear buscador---------------------  

    def buscador(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Buscar Datos")
        self.labelframe1.place(x=530, y=0, width=350, height=150)
        self.seleccion= tk.IntVar()
        self.radioButton1= ttk.Radiobutton(self.ventProv, text="Por Codigo", value=1).place(x=545, y=20)
        self.radioButton2= ttk.Radiobutton(self.ventProv, text="Por Nombre", value=2).place(x=545, y=50)
        #Entry
        self.datoBuscador = tk.StringVar()
        self.entry10 = ttk.Entry(self.labelframe1, textvariable=self.datoBuscador).place(x=23, y=70, width=300, height=35)
        #Button
        self.button = ttk.Button(self.labelframe1, text="Buscar", width=20).place(x=115, y=10, width=220, height=35)

#---------------------Fin crear buscador---------------------  

#---------------------Inicio visualizacion de datos---------------------

    def agregarClientes(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="ingresar datos de clientes")
        self.labelframe1.place(y=160, width=880, height=500)
        #Labels
        self.label1 = ttk.Label(self.labelframe1, text="N° cliente").place(x=10, y=10)
        self.label2 = ttk.Label(self.labelframe1, text="Nombre").place(x=10, y=55)
        self.label3 = ttk.Label(self.labelframe1, text="Localidad").place(x=10, y=100)
        
        
        #Entry
        self.NCliente = tk.StringVar()
        self.NCliente = ttk.Entry(self.labelframe1, textvariable=self.NCliente).place(x=70, y=10, width=300, height=25)
        self.Nombre = tk.StringVar()
        self.Nombre = ttk.Entry(self.labelframe1, textvariable=self.Nombre).place(x=65, y=50, width=300, height=25)
        self.NDocumento = tk.StringVar()
        self.NDocumento = ttk.Entry(self.labelframe1, textvariable=self.NDocumento).place(x=73, y=95, width=300, height=25)


#---------------------Fin visualizacion de datos---------------------

#---------------------Inicio botones CRUD---------------------  

    def botonesCRUD(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Opciones")
        self.labelframe1.place(y=350)

        #Button
        self.button1 = ttk.Button(self.labelframe1, text="Agregar", width=20).grid(column=0, row=0, padx=10, pady=10)
        self.button2 = ttk.Button(self.labelframe1, text="Modificar", width=20).grid(column=1, row=0, padx=10, pady=10)
        self.button3 = ttk.Button(self.labelframe1, text="Eliminar", width=20).grid(column=2, row=0, padx=10, pady=10)
        self.button4 = ttk.Button(self.labelframe1, text="Cancelar", width=20).grid(column=4, row=0, padx=10, pady=10)
        self.button5 = ttk.Button(self.labelframe1, text="Grabar", width=20).grid(column=5, row=0, padx=10, pady=10)

#---------------------Fin botones CRUD---------------------

    '''def agregarJugadores(self):
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
        self.button = ttk.Button(self.labelframe1, text="Ingresar")#, command=self.agregarSelecc)
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
        self.button = ttk.Button(self.labelframe1, text="Borrar")#, command=self.borrarSelecc)
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
        self.button = ttk.Button(self.labelframe1, text="Actualizar")#, command=self.actualizarSelecc)
        self.button.grid(column=1, row=5, padx=10, pady=10)
        self.button1 = ttk.Button(self.labelframe1, text="consultar")#, command=self.consultarSelecc)
        self.button1.grid(column=0, row=5, padx=10, pady=10)

    def imprimirJugadores(self):
        self.page4 = ttk.Frame(self.notebook)
        self.notebook.add(self.page4, text="Imprimir jugadores")
        self.labelframe = ttk.Labelframe(self.page4, text="Imprimir")
        self.scrolledtext = st.ScrolledText(self.page4, width=90)
        self.scrolledtext.grid(column=0, row=0, pady=0, padx=0)
        # Button
        self.boton = ttk.Button(self.page4, text="Imprimir")#, command=self.imprimirSelecc)
        self.boton.grid(column=0, row=1, padx=10, pady=10)
        # ScrollBar
        self.ScrollBar = ttk.Scrollbar(self.scrolledtext, orient='vertical', command=self.scrolledtext.yview)
        self.scrolledtext["yscrollcommand"] = self.ScrollBar.set'''

