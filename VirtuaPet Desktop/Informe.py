from cgitb import text
from email import message
from operator import mod
from tkinter import messagebox

from mysqlx import Row
from Connect import *
from tkinter import *
from tkinter import ttk
from fpdf import FPDF

ventana= Tk()
ventana.geometry("800x400")
ventana.title("Informe de concurrencia")
ventana['bg'] = '#a5aae0'

marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=700,height=300)
marco['bg'] = '#f1d7ff'


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




tvagenda=ttk.Treeview(marco, selectmode=NONE)
tvagenda.grid(column=0,row=5,columnspan=4,padx=5)
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



lbldia=Label(marco, text="MES").grid(column=0,row=4,padx=5,pady=5)
txtdia=ttk.Combobox(marco,values=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"], textvariable=mes)
txtdia.grid(column=1,row=4)
txtdia.current(0)

btnEliminar=Button(marco,text="FILTRAR POR MES", command=lambda:filtrar())
btnEliminar.grid(column=3,row=6,padx=5,pady=5)

btnEliminar=Button(marco,text="MOSTRAR TODO", command=lambda:llenatabla())
btnEliminar.grid(column=2,row=6,padx=5,pady=5)

btnEliminar=Button(marco,text="GENERAR PDF POR MES", command=lambda:pidief())
btnEliminar.grid(column=1,row=6,padx=5,pady=5)

btnEliminar=Button(marco,text="ATRAS", command=lambda:atras())
btnEliminar.grid(column=0,row=6,padx=5,pady=5)


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
ventana.mainloop()