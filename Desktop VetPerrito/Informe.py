from cgitb import text
from email import message
from operator import mod
from tkinter import messagebox
import tkinter as mytk
from mysqlx import Row
from Connect import *
from tkinter import *
from tkinter import ttk
from fpdf import FPDF
#parametros de la ventana
ventana= Tk()
ventana.geometry("1000x600")
ventana.resizable(width = False, height = False)
ventana.title("Informe de concurrencia")
ventana['bg'] = '#a5aae0'


imagen = PhotoImage(file = "img/informeConcurrencia.png")
background = Label(image = imagen, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
imagenatras  = PhotoImage(file = "img/Boton_Atras.png")
imagenpdfm = PhotoImage(file = "img/BotónGenerarPdfPorMes_Informe.png")
imagenfiltrar = PhotoImage(file = "img/BotónFiltrarPorMes_Informe.png")
imagenmostrartodo  = PhotoImage(file = "img/BotónMostrarTodo_Informe.png")

#f1d7ff'

#se definene variables
db=DataBase()


id=StringVar()
mes=StringVar()
nombre=StringVar()
apellido=StringVar()
sexo=StringVar()
nombrem=StringVar()
numero=StringVar()
raza=StringVar()
hora=StringVar()
dia=StringVar()


#cuadro con la info de la bdd

tvagenda=ttk.Treeview(ventana, selectmode=NONE,height=15)
tvagenda.place(x=50,y=166,width=900)
tvagenda["columns"]=("id","Mes","Dia","Hora","Nombre","Apellido","Numero","Nombre_Mascota","Sexo_Mascota","Raza_Mascota")
tvagenda.column("#0",width=0,stretch=NO)
tvagenda.column("id",width=10,anchor=CENTER)
tvagenda.column("Mes",width=70,anchor=CENTER)
tvagenda.column("Dia",width=30,anchor=CENTER)
tvagenda.column("Hora",width=50,anchor=CENTER)
tvagenda.column("Nombre",width=80,anchor=CENTER)
tvagenda.column("Apellido",width=80,anchor=CENTER)
tvagenda.column("Numero",width=90,anchor=CENTER)
tvagenda.column("Nombre_Mascota",width=70,anchor=CENTER)
tvagenda.column("Sexo_Mascota",width=70,anchor=CENTER)
tvagenda.column("Raza_Mascota",width=90,anchor=CENTER)


tvagenda.heading("id",text="ID",anchor=CENTER)
tvagenda.heading("Mes",text="Mes",anchor=CENTER)
tvagenda.heading("Dia",text="Dia",anchor=CENTER)
tvagenda.heading("Hora",text="Hora",anchor=CENTER)
tvagenda.heading("Nombre",text="Nombre",anchor=CENTER)
tvagenda.heading("Apellido",text="Apellido",anchor=CENTER)
tvagenda.heading("Numero",text="Numero",anchor=CENTER)
tvagenda.heading("Nombre_Mascota",text="Nombre_M",anchor=CENTER)
tvagenda.heading("Sexo_Mascota",text="Sexo_M",anchor=CENTER)
tvagenda.heading("Raza_Mascota",text="Especie",anchor=CENTER)

#botones

#lbldia=Label(ventana, text="MES").grid(column=0,row=4,padx=5,pady=5)
txtdia=ttk.Combobox(ventana,values=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"], textvariable=mes)
txtdia.place(x=280,y=112,width=240,height=27)
txtdia.current(0)

btnEliminar=Button(ventana,text="FILTRAR POR MES", command=lambda:filtrar(),image=imagenfiltrar)
btnEliminar.place(x=725,y=530)

btnEliminar=Button(ventana,text="MOSTRAR TODO", command=lambda:llenatabla(),image=imagenmostrartodo)
btnEliminar.place(x=497,y=530)

btnEliminar=Button(ventana,text="GENERAR PDF POR MES", command=lambda:pidief(),image=imagenpdfm)
btnEliminar.place(x=190,y=530)

btnEliminar=Button(ventana,text="ATRAS", command=lambda:atras(),image=imagenatras)
btnEliminar.place(x=40,y=530)


#funciones
def seleccionar(event):
    id= tvagenda.selection()[0]
    if int(id)>0:
        mes.set(tvagenda.item(id,"values")[1])
        dia.set(tvagenda.item(id,"values")[2])
        hora.set(tvagenda.item(id,"values")[3])
        nombre.set(tvagenda.item(id,"values")[4])
        apellido.set(tvagenda.item(id,"values")[5])
        numero.set(tvagenda.item(id,"values")[6])
        nombrem.set(tvagenda.item(id,"values")[7])
        sexo.set(tvagenda.item(id,"values")[8])
        raza.set(tvagenda.item(id,"values")[9])
    

tvagenda.bind("<<TreeviewSelect>>",seleccionar)


def filtrar():
    val=mes.get()
    vaciatabla()
    sql="select * from agenda where Mes=%s"
    db.cursor.execute(sql,(val,))
    filas= db.cursor.fetchall()
    for fila in filas:
        id= fila[0]
        tvagenda.insert("",END,id,text="id", values=fila)


def atras():
    ventana.destroy()
    import Menu


def llenatabla():
    vaciatabla()
    sql="select * from agenda"
    db.cursor.execute(sql)
    filas= db.cursor.fetchall()
    for fila in filas:
        id= fila[0]
        tvagenda.insert("",END,id,text="id", values=fila)

def vaciatabla():
    filas= tvagenda.get_children()
    for fila in filas:
        tvagenda.delete(fila)

#se genera el pdf
def pidief():
    mess=mes.get()
    plus=1
    val=(mes.get())
    sql="select * from agenda where mes=%s"
    db.cursor.execute(sql,(val,))
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    filas= db.cursor.fetchall()
    pdf.cell(200,10,txt="Informe De Reservas Mensual De "+mess,ln=1,align="C")
    das=tvagenda.get_children()
    plus2=0
    pdf.cell(200,10,txt="formato (ID | MES | DIA | NOMBRE | APELLIDO | NUMERO | MASCOTA | SEXO | ESPECIE) ",ln=1,align="L")

    for fila in filas:
        
        aaa = ' | '.join(map(str, filas[plus2]))
        plus2=plus2+1
        plus=plus+1
        pdf.cell(200,10,txt=""+aaa ,ln=plus,align="L")
       
    pdf.cell(200,10,txt=" VetPerrito.  ", ln=21,align="R")
    pdf.image('img/logo.png',x=10,y=10,w=10,h=10,type="",link='')
    
    pdf.output("Informe VetPerrito "+mess+".pdf ")
    messagebox.showinfo(message="Archivo Generado Correctamente", title="Archivo generado exitosamente")

         

llenatabla()

#se define la ventana que pregunta si se quiere cerrar

class MyDialog:
    def __init__(self, parent):
        self.top = mytk.Toplevel(parent)

        ancho_ventana = 240
        alto_ventana = 60
        x_ventana = self.top.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.top.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.top.geometry(posicion)
        self.top.title("¿Cerrar?")


        self.top.overrideredirect(True)
        self.parent = parent
        self.top.title("Salir")

        mytk.Label(self.top, text="¿Está seguro?").grid(row=0, column=0, columnspan=2)

        self.button1 = mytk.Button(self.top, text="Si, salir de la app.", command=self.salir)
        self.button2 = mytk.Button(self.top, text="No, solo minimizar.", command=self.minimizar)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=1, padx=5, pady=5)

    def salir(self):
        self.top.destroy()
        self.parent.destroy()

    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()

class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        d = MyDialog(ventana)
        self.parent.wait_window(d.top)

app = MyApp(ventana)

ventana.mainloop()