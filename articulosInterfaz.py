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
        self.buscador()

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

        #Labelframe para valores unitarios
        self.labelframe2=ttk.Labelframe(self.ventProv, text="Valores unitarios")
        self.labelframe2.place(x=373, y=280, width=200, height=215) 
        
        # Labels
        self.label1 = ttk.Label(self.labelframe1, text="Grupo").grid(column=0, row=0, padx=10, pady=10)
        self.label2 = ttk.Label(self.labelframe1, text="CodigoProd").grid(column=0, row=1, padx=10, pady=10)
        self.label3 = ttk.Label(self.labelframe1, text="Descripcion").grid(column=0, row=2, padx=10, pady=10)
        self.label4 = ttk.Label(self.labelframe1, text="Fecha de alta").grid(column=0, row=3, padx=10, pady=10)
        self.label5 = ttk.Label(self.labelframe1, text="Proveedor").grid(column=0, row=4, padx=10, pady=10)
        self.label6 = ttk.Label(self.labelframe1, text="Stock").grid(column=0, row=5, padx=10, pady=10)
        self.label7 = ttk.Label(self.labelframe1, text="Sin IVA").grid(column=0, row=6, padx=10, pady=10)
        self.label9 = ttk.Label(self.labelframe1, text="Cant de bultos").grid(column=0, row=7, padx=10, pady=10)
        self.label10 = ttk.Label(self.labelframe1, text="IVA especial").place(x=342, y=243)
        self.label11 = ttk.Label(self.labelframe1, text="Costo", foreground="red").place(x=230, y=283)
        self.label12 = ttk.Label(self.labelframe1, text="Desc", foreground="green").place(x=385, y=283)

        #Label valores unitarios
        self.label14 = ttk.Label(self.labelframe2, text="Costo").place(x=25, y=5)
        self.label15 = ttk.Label(self.labelframe2, text="Utilidad").place(x=20, y=45)
        self.label16 = ttk.Label(self.labelframe2, text="Neto").place(x=27, y=85)

        # Entry
        self.datoGrupo = tk.StringVar()
        self.entryGrupo = ttk.Entry(self.labelframe1, textvariable=self.datoGrupo).place(x=110, y=10, width=100, height=25)
        
        self.datoCodigoProd = tk.StringVar()
        self.entryCodigoProd = ttk.Entry(self.labelframe1, textvariable=self.datoCodigoProd).place(x=110, y=48, width=100, height=25)
        
        self.datoDescripcion = tk.StringVar()
        self.entryDescripcion = ttk.Entry(self.labelframe1, textvariable=self.datoDescripcion).place(x=110, y=85, width=250, height=25)
        
        self.datoFechaAlta = tk.StringVar()
        self.entryFechaAlta = ttk.Entry(self.labelframe1, textvariable=self.datoFechaAlta).place(x=110, y=125, width=100, height=25)
        
        self.datoProveedor = tk.StringVar()
        self.entryProveedor = ttk.Entry(self.labelframe1, textvariable=self.datoProveedor).place(x=110, y=164, width=100, height=25)
        
        self.datoStock = tk.StringVar()
        self.entryStock = ttk.Entry(self.labelframe1, textvariable=self.datoStock).place(x=110, y=202, width=100, height=25)
        
        self.datoSinIVA = tk.StringVar()
        self.entrySinIVA = ttk.Entry(self.labelframe1, textvariable=self.datoSinIVA)
        self.entrySinIVA.place(x=110, y=240, width=100, height=25)
        self.entrySinIVA.bind("<KeyPress-Tab>", self.calculoIVA)
        
        self.datoCantBultos = tk.StringVar()
        self.entryCantBultos = ttk.Entry(self.labelframe1, textvariable=self.datoCantBultos).place(x=110, y=280, width=100, height=25)
        
        self.datoIVA = tk.StringVar()
        self.entryIVA = ttk.Entry(self.labelframe1, textvariable=self.datoIVA).place(x=420, y=240, width=100, height=25)
        
        self.datoCosto = tk.StringVar()
        self.entryCosto = ttk.Entry(self.labelframe1, textvariable=self.datoCosto)
        self.entryCosto.place(x=275, y=280, width=100, height=25)
        self.entryCosto.bind("<KeyPress-Tab>", self.calculosNeto)
        
        self.datoAgreagarDesc = tk.StringVar()
        self.entryAgreagarDesc = ttk.Entry(self.labelframe1, textvariable=self.datoAgreagarDesc)
        self.entryAgreagarDesc.place(x=420, y=280, width=100, height=25)
        self.entryAgreagarDesc.bind("<KeyPress-Tab>", self.calculoDescuento)

        self.datoDesc = tk.StringVar()
        self.entryDesc = ttk.Entry(self.labelframe1, textvariable=self.datoDesc)
        self.entryDesc.place(x=530, y=280, width=100, height=25)
        self.entryDesc.bind("<KeyPress-Tab>", self.calculoNetoConDescuesto)
      
        #Entry para valores unitarios
        self.datoCostoUnitario=tk.StringVar()
        self.entryCostoUnitario = ttk.Entry(self.labelframe2, textvariable=self.datoCostoUnitario)
        self.entryCostoUnitario.place(x=70, y=4, width=100, height=25)
        
        self.datoUtilidad = tk.StringVar()
        self.entryUtilidad = ttk.Entry(self.labelframe2, textvariable=self.datoUtilidad)
        self.entryUtilidad.place(x=70, y=44, width=100, height=25)
        self.entryUtilidad.bind("<KeyPress-Tab>", self.calculoUtilidad)
        
        self.datoNeto = tk.StringVar()
        self.entryNeto = ttk.Entry(self.labelframe2, textvariable=self.datoNeto)
        self.entryNeto.place(x=70, y=84, width=100, height=25)
        self.entryNeto.bind("<KeyPress-Tab>", self.utilidadExacta)


#---------------------fin visualizar datos---------------------  

#--------------------- Calculos ---------------------------

    #Calcular costo unitario
    def calculosNeto(self, event): 
        self.costo= float(self.datoCosto.get())
        self.cantBultos= float(self.datoCantBultos.get())
        self.calculoUnit= (self.costo/self.cantBultos)

        self.datoCostoUnitario.set(self.calculoUnit)

    #Calcular neto
    def calculoUtilidad(self, event):
        self.utilidad= float(self.datoUtilidad.get())
        #self.calculoNeto= self.calculoUnit * (self.utilidad + 100)/100
        self.calculaUtilidad= self.utilidad * (self.calculoUnit/100)
        self.calculoNeto= self.calculoUnit + self.calculaUtilidad

        self.datoNeto.set(self.calculoNeto)

    #Calcular IVA
    def calculoIVA(self, event):
        self.sinIVA= float(self.datoSinIVA.get())
        self.IVA= self.sinIVA * 1.21

        self.datoIVA.set(self.IVA)
        self.datoCosto.set(self.IVA)

    #Calcular descuento
    def calculoDescuento(self, event):
        self.desc= float(self.datoAgreagarDesc.get())
        self.sacarPorcentaje= self.costo * (self.desc/100)
        self.calculoDesc= self.costo - self.sacarPorcentaje

        self.datoDesc.set(self.calculoDesc)

    #Calcular el valor neto con el descuento del costo aplicado
    def calculoNetoConDescuesto(self, event):
        self.costoDescuento= float(self.datoDesc.get())
        self.cantBultos= float(self.datoCantBultos.get())
        self.calculoUnitConDescuento= (self.costoDescuento/self.cantBultos)

        self.datoCostoUnitario.set(self.calculoUnitConDescuento)

    #Calcular la utilidad exacta del valor utilidad asignado
    def utilidadExacta(self, event):
        self.neto= float(self.datoNeto.get())
        self.costoUnitario= float(self.datoCostoUnitario.get())
        utilidad= (self.neto / self.costoUnitario)
        self.utilidadReal= utilidad*100-100

        self.datoUtilidad.set(self.utilidadReal.__round__(2))
    
#--------------------- Fin de calculos ---------------------

#---------------------Inicio botones CRUD---------------------  

    def botonesCRUD(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Opciones")
        self.labelframe1.place(y=600)

        #Button
        self.button1 = ttk.Button(self.labelframe1, text="Agregar", width=20).grid(column=0, row=0, padx=10, pady=10)
        self.button2 = ttk.Button(self.labelframe1, text="Modificar", width=20).grid(column=1, row=0, padx=10, pady=10)
        self.button3 = ttk.Button(self.labelframe1, text="Eliminar", width=20).grid(column=2, row=0, padx=10, pady=10)
        self.button4 = ttk.Button(self.labelframe1, text="Cancelar", width=20).grid(column=4, row=0, padx=10, pady=10)
        self.button5 = ttk.Button(self.labelframe1, text="Grabar", width=20).grid(column=5, row=0, padx=10, pady=10)

#---------------------Fin botones CRUD---------------------

#---------------------Inicio lista---------------------
        
    def lista(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Lista de productos")
        self.labelframe1.place(x=700, y=300, width=220, height=300)
        #Labels
        self.label1 = ttk.Label(self.labelframe1, text="Lista 1").place(x=25, y=30)
        self.label2 = ttk.Label(self.labelframe1, text="Lista 2").place(x=25, y=70)
        self.label3 = ttk.Label(self.labelframe1, text="Lista 3").place(x=25, y=110)
        self.label4 = ttk.Label(self.labelframe1, text="Lista 4").place(x=25, y=150)
        self.label5 = ttk.Label(self.labelframe1, text="Lista 5").place(x=25, y=190)

        self.label6 = ttk.Label(self.labelframe1, text="Utilidad").place(x=70, y=0)
        self.label7 = ttk.Label(self.labelframe1, text="Precio").place(x=130, y=0)

        #Entry - utilidad
        self.datoUtilidadLista1 = tk.StringVar()
        self.entryUtilidadLista1 = ttk.Entry(self.labelframe1, textvariable=self.datoUtilidadLista1, width=20)
        self.entryUtilidadLista1.place(x=70, y=30, width=50)
        self.entryUtilidadLista1.bind("<KeyPress-Tab>", self.calculosLista1)
        #self.entryUtilidadLista1.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista1, add= "+")

        self.datoUtilidadLista2 = tk.StringVar()
        self.entryUtilidadLista2 = ttk.Entry(self.labelframe1, textvariable=self.datoUtilidadLista2, width=20)
        self.entryUtilidadLista2.place(x=70, y=70, width=50)
        self.entryUtilidadLista2.bind("<KeyPress-Tab>", self.calculosLista2)
        #self.entryUtilidadLista2.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista2, add= "+")

        self.datoUtilidadLista3 = tk.StringVar()
        self.entryUtilidadLista3 = ttk.Entry(self.labelframe1, textvariable=self.datoUtilidadLista3, width=20)
        self.entryUtilidadLista3.place(x=70, y=110, width=50)
        self.entryUtilidadLista3.bind("<KeyPress-Tab>", self.calculosLista3)
        #self.entryUtilidadLista1.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista3, add= "+")

        self.datoUtilidadLista4 = tk.StringVar()
        self.entryUtilidadLista4 = ttk.Entry(self.labelframe1, textvariable=self.datoUtilidadLista4, width=20)
        self.entryUtilidadLista4.place(x=70, y=150, width=50)
        self.entryUtilidadLista4.bind("<KeyPress-Tab>", self.calculosLista4)
        #self.entryUtilidadLista1.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista4, add= "+")

        self.datoUtilidadLista5 = tk.StringVar()
        self.entryUtilidadLista5 = ttk.Entry(self.labelframe1, textvariable=self.datoUtilidadLista5, width=20)
        self.entryUtilidadLista5.place(x=70, y=190, width=50)
        self.entryUtilidadLista5.bind("<KeyPress-Tab>", self.calculosLista5)
        #self.entryUtilidadLista1.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista5, add= "+")

        #Entry - neto
        self.datoNetoLista1 = tk.StringVar()
        self.entryNetoLista1 = ttk.Entry(self.labelframe1, textvariable=self.datoNetoLista1)
        self.entryNetoLista1.place(x=130, y=30, width=50)
        self.entryNetoLista1.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista1)

        self.datoNetoLista2 = tk.StringVar()
        self.entryNetoLista2 = ttk.Entry(self.labelframe1, textvariable=self.datoNetoLista2)
        self.entryNetoLista2.place(x=130, y=70, width=50)
        self.entryNetoLista2.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista2)

        self.datoNetoLista3 = tk.StringVar()
        self.entryNetoLista3 = ttk.Entry(self.labelframe1, textvariable=self.datoNetoLista3)
        self.entryNetoLista3.place(x=130, y=110, width=50)
        self.entryNetoLista3.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista3)

        self.datoNetoLista4 = tk.StringVar()
        self.entryNetoLista4 = ttk.Entry(self.labelframe1, textvariable=self.datoNetoLista4)
        self.entryNetoLista4.place(x=130, y=150, width=50)
        self.entryNetoLista4.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista4)

        self.datoNetoLista5 = tk.StringVar()
        self.entryNetoLista5 = ttk.Entry(self.labelframe1, textvariable=self.datoNetoLista5)
        self.entryNetoLista5.place(x=130, y=190, width=50)
        self.entryNetoLista5.bind("<KeyPress-Tab>", self.calculoUtilidadRealLista5)

#---------------------Fin lista---------------------

#---------------------Calculos de la lista---------------------

    def calculosLista1(self, event):
        utilidadLista1= float(self.datoUtilidadLista1.get())
        calculoUtilidad= utilidadLista1 * (self.calculoUnit/100)
        calculoNeto= calculoUtilidad + self.calculoUnit

        self.datoNetoLista1.set(calculoNeto)

    def calculosLista2(self, event):
        utilidadLista2= float(self.datoUtilidadLista2.get())
        calculoUtilidad= utilidadLista2 * (self.calculoUnit/100)
        calculoNeto= calculoUtilidad + self.calculoUnit

        self.datoNetoLista2.set(calculoNeto)

    def calculosLista3(self, event):
        utilidadLista3= float(self.datoUtilidadLista3.get())
        calculoUtilidad= utilidadLista3 * (self.calculoUnit/100)
        calculoNeto= calculoUtilidad + self.calculoUnit

        self.datoNetoLista3.set(calculoNeto)

    def calculosLista4(self, event):
        utilidadLista4= float(self.datoUtilidadLista4.get())
        calculoUtilidad= utilidadLista4 * (self.calculoUnit/100)
        calculoNeto= calculoUtilidad + self.calculoUnit

        self.datoNetoLista4.set(calculoNeto)

    def calculosLista5(self, event):
        utilidadLista5= float(self.datoUtilidadLista5.get())
        calculoUtilidad= utilidadLista5 * (self.calculoUnit/100)
        calculoNeto= calculoUtilidad + self.calculoUnit

        self.datoNetoLista5.set(calculoNeto)

    #Calculo de utilidad real
    def calculoUtilidadRealLista1(self, event):
        costoUnitario= float(self.datoCostoUnitario.get())
        netoLista1= float(self.datoNetoLista1.get())
        utilidad= (netoLista1 / costoUnitario)
        self.utilidadReal= utilidad*100-100

        self.datoUtilidadLista1.set(self.utilidadReal.__round__(2))

    def calculoUtilidadRealLista2(self, event):
        costoUnitario= float(self.datoCostoUnitario.get())
        netoLista2= float(self.datoNetoLista2.get())
        utilidad= (netoLista2 / costoUnitario)
        utilidadReal= utilidad*100-100

        self.datoUtilidadLista2.set(utilidadReal.__round__(2))

    def calculoUtilidadRealLista3(self, event):
        costoUnitario= float(self.datoCostoUnitario.get())
        netoLista3= float(self.datoNetoLista3.get())
        utilidad= (netoLista3 / costoUnitario)
        self.utilidadReal= utilidad*100-100

        self.datoUtilidadLista3.set(self.utilidadReal.__round__(2))

    def calculoUtilidadRealLista4(self, event):
        costoUnitario= float(self.datoCostoUnitario.get())
        netoLista4= float(self.datoNetoLista4.get())
        utilidad= (netoLista4 / costoUnitario)
        self.utilidadReal= utilidad*100-100

        self.datoUtilidadLista4.set(self.utilidadReal.__round__(2))

    def calculoUtilidadRealLista5(self, event):
        costoUnitario= float(self.datoCostoUnitario.get())
        netoLista5= float(self.datoNetoLista5.get())
        utilidad= (netoLista5 / costoUnitario)
        self.utilidadReal= utilidad*100-100

        self.datoUtilidadLista5.set(self.utilidadReal.__round__(2))

        

#---------------------Fin de calculos de lista---------------------

#---------------------Crear buscador---------------------  

    def buscador(self):
        self.labelframe1= ttk.Labelframe(self.ventProv, text="Buscar Datos")
        self.labelframe1.place(x=630, y=0, width=300, height=200)
        self.seleccion= tk.IntVar()
        self.radioButton1= ttk.Radiobutton(self.ventProv, text="Por Codigo", value=1).place(x=645, y=20)
        self.radioButton2= ttk.Radiobutton(self.ventProv, text="Por Nombre", value=2).place(x=645, y=50)
        #Entry
        self.datoBuscador = tk.StringVar()
        self.entry10 = ttk.Entry(self.labelframe1, textvariable=self.datoBuscador).place(x=23, y=85, width=200, height=35)
        #Button
        self.button = ttk.Button(self.labelframe1, text="Buscar", width=20).place(x=115, y=10, width=150, height=40)

#---------------------Fin crear buscador---------------------  




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

