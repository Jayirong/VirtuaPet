from cgitb import text
from email import message
from operator import mod
import string
from tkinter import messagebox
from Connect import *
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
import tkinter as mytk

f = ("Times bold", 14)



#VENTANA
ventana= Tk()
ventana.geometry("1000x600")
ventana.resizable(width = False, height = False)
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'


imagen = PhotoImage(file = "img/VerReservas.png")
background = Label(image = imagen, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

f = ("Times bold", 14)

imagenbuscar = PhotoImage(file = "img/Boton_Buscar.png")
imagengenerar = PhotoImage(file = "img/BotónGenerarArchivo_GenerarFicha.png")
imagenatras = PhotoImage(file = "img/Boton_Atras.png")

#se definen las variables

db=DataBase()
dia=IntVar()
mes=StringVar()


txtdia=ttk.Combobox(ventana,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"], textvariable=dia,width=25)
txtdia.place(x=285, y=110,height=30)
txtdia.current(0)


txtmes=ttk.Combobox(ventana,values=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"], textvariable=mes,width=25)
txtmes.place(x=740, y=110,height=30)
txtmes.current(0)




tvagenda=ttk.Treeview(ventana, selectmode=NONE,height=14)
tvagenda.place(x=115, y=180)
tvagenda["columns"]=("id","Mes","Dia","Hora","Nombre","Apellido","Numero","Nombre_Mascota","Sexo_Mascota","Raza_Mascota")
tvagenda.column("#0",width=0,stretch=NO)
tvagenda.column("id",width=20,anchor=CENTER)
tvagenda.column("Mes",width=80,anchor=CENTER)
tvagenda.column("Dia",width=40,anchor=CENTER)
tvagenda.column("Hora",width=60,anchor=CENTER)
tvagenda.column("Nombre",width=90,anchor=CENTER)
tvagenda.column("Apellido",width=90,anchor=CENTER)
tvagenda.column("Numero",width=100,anchor=CENTER)
tvagenda.column("Nombre_Mascota",width=110,anchor=CENTER)
tvagenda.column("Sexo_Mascota",width=90,anchor=CENTER)
tvagenda.column("Raza_Mascota",width=100,anchor=CENTER)


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








btnNuevo=Button(ventana,text="BUSCAR", command=lambda:llenatabla(),image=imagenbuscar)
btnNuevo.place(x=680, y=526)


btnNuevo=Button(ventana,text="ATRAS", command=lambda:volver() ,image=imagenatras)
btnNuevo.place(x=35, y=526)




def volver():
    ventana.destroy()
    import Menudostor
    

def vaciatabla():
    filas= tvagenda.get_children()
    for fila in filas:
        tvagenda.delete(fila)
     
def llenatabla():
    vaciatabla()
    val=(mes.get(),dia.get())
  
    sql="""select * from agenda where Mes=%s AND Dia=%s order by Hora AND ID DESC"""
    db.cursor.execute(sql,val)
    filas= db.cursor.fetchall()
    for fila in filas:
        id= fila[0]
        tvagenda.insert("",END,id,text="id", values=fila)

#se define la ventana que pregunta si se quiere cerrar

class MyDialog:
    def __init__(self, parent):
        self.top = mytk.Toplevel(parent)

        # bloque usado para centrar la ventana toplevel
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