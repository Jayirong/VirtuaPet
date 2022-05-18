from cgitb import text
from email import message
from operator import mod
import string
from tkinter import messagebox
from Connect import *
from tkinter import *
from tkinter import ttk

f = ("Times bold", 14)



#VENTANA
ventana= Tk()
ventana.geometry("780x420")
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=680,height=320)
marco['bg'] = '#f1d7ff'

db=DataBase()
dia=IntVar()
mes=StringVar()

lbldia=Label(marco, text="SELECCIONAR DIA").grid(column=1,row=0,padx=5,pady=5)
txtdia=ttk.Combobox(marco,values=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"], textvariable=dia)
txtdia.grid(column=2,row=0)
txtdia.current(0)

lbldia=Label(marco, text="MES").grid(column=3,row=0,padx=5,pady=5)
txtdia=ttk.Combobox(marco,values=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"], textvariable=mes)
txtdia.grid(column=4,row=0)
txtdia.current(0)


tvagenda=ttk.Treeview(marco, selectmode=NONE)
tvagenda.grid(column=1,row=5,columnspan=4,padx=5,pady=5)
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








btnNuevo=Button(marco,text="BUSCAR", command=lambda:llenatabla())
btnNuevo.grid(column=2,row=6,padx=5,pady=5)


btnNuevo=Button(marco,text="ATRAS", command=lambda:volver())
btnNuevo.grid(column=1,row=6,padx=5,pady=5)

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



ventana.mainloop()