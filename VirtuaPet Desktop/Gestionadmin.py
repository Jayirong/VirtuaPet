from ast import Str
from cProfile import label
from tkinter import *
from cgitb import text
from email import message
from operator import mod
import string
from tkinter import messagebox
from Connect import *
from tkinter import *
from tkinter import ttk
from fpdf import *
from fpdf import FPDF


ventana= Tk()
ventana.geometry("700x400")
ventana.title("Generacion De Ficha Veterinaria")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=350,y=20,width=330,height=350)
marco['bg'] = '#f1d7ff'



f = ("Times bold", 14)





db=DataBase()
dia=StringVar()
mes=StringVar()

id=IntVar()
paciente=StringVar()
fecha=StringVar()
numero=StringVar()
motivo=StringVar()
anamnesis=StringVar()
examenf=StringVar()
examenec=StringVar()
indicaciones=StringVar()
observaciones=StringVar()

lbldia=Label(marco, text="PACIENTE").grid(column=1,row=0,padx=5,pady=5)
txtdia=Entry(marco, textvariable=dia)
txtdia.grid(column=2,row=0)



tvagenda=ttk.Treeview(marco, selectmode=NONE)
tvagenda.grid(column=0,row=1,columnspan=4,padx=5,pady=5)
tvagenda["columns"]=("id","Paciente","Fecha","Numero","Motivo_consulta","Anamnesis","Examen_fisico","Examenes_complementarios","Indicaciones","Observacion")
tvagenda.column("#0",width=0,stretch=NO)
tvagenda.column("id",width=10,anchor=CENTER)
tvagenda.column("Paciente",width=150,anchor=CENTER)
tvagenda.column("Fecha",width=150,anchor=CENTER)
tvagenda.column("Numero",width=0,stretch=NO)
tvagenda.column("Motivo_consulta",width=0,stretch=NO)
tvagenda.column("Anamnesis",width=0,stretch=NO)
tvagenda.column("Examen_fisico",width=0,stretch=NO)
tvagenda.column("Examenes_complementarios",width=0,stretch=NO)
tvagenda.column("Indicaciones",width=0,stretch=NO)
tvagenda.column("Observacion",width=0,stretch=NO)




tvagenda.heading("id",text="ID",anchor=CENTER)
tvagenda.heading("Paciente",text="Paciente",anchor=CENTER)
tvagenda.heading("Fecha",text="Fecha",anchor=CENTER)
tvagenda.heading("Numero",text="Numero",anchor=CENTER)
tvagenda.heading("Motivo_consulta",text="Motivo_consulta",anchor=CENTER)
tvagenda.heading("Anamnesis",text="Anamnesis",anchor=CENTER)
tvagenda.heading("Examen_fisico",text="Examen_fisico",anchor=CENTER)
tvagenda.heading("Examenes_complementarios",text="Examenes_complementarios",anchor=CENTER)
tvagenda.heading("Indicaciones",text="Indicaciones",anchor=CENTER)
tvagenda.heading("Observacion",text="Observacion",anchor=CENTER)



tvagenda.config(selectmode=BROWSE)

lblpaciente=Label(ventana, text="DATOS DE LA FICHA").grid(column=1,row=0,padx=5,pady=5)


lblpaciente=Label(ventana, text="PACIENTE").grid(column=0,row=1,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=paciente)
txtpaciente.grid(column=1,row=1)

lblpaciente=Label(ventana, text="FECHA").grid(column=0,row=2,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=fecha)
txtpaciente.grid(column=1,row=2)

lblpaciente=Label(ventana, text="NUMERO").grid(column=0,row=3,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=numero)
txtpaciente.grid(column=1,row=3)


lblpaciente=Label(ventana, text="MOTIVO").grid(column=0,row=4,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=motivo)
txtpaciente.grid(column=1,row=4)


lblpaciente=Label(ventana, text="ANAMNESIS").grid(column=0,row=5,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=anamnesis)
txtpaciente.grid(column=1,row=5)

lblpaciente=Label(ventana, text="EXAMEN FISICO").grid(column=0,row=6,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=examenf)
txtpaciente.grid(column=1,row=6)


lblpaciente=Label(ventana, text="EXAMENES COMPLEMENTARIOS").grid(column=0,row=7,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=examenec)
txtpaciente.grid(column=1,row=7)


lblpaciente=Label(ventana, text="INDICACIONES").grid(column=0,row=8,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=indicaciones)
txtpaciente.grid(column=1,row=8)

lblpaciente=Label(ventana, text="OBSERVACION").grid(column=0,row=9,padx=5,pady=5)
txtpaciente=Entry(ventana, textvariable=observaciones)
txtpaciente.grid(column=1,row=9)









btnNuevo=Button(marco,text="BUSCAR", command=lambda:llenatabla())
btnNuevo.grid(column=1,row=6,padx=5,pady=5)



btnNuevo=Button(ventana,text="ATRAS", command=lambda:volver())
btnNuevo.grid(column=0,row=10,padx=5,pady=5)
btnNuevo=Button(ventana,text="GENERAR ARCHIVO", command=lambda:pidief())
btnNuevo.grid(column=1,row=10,padx=5,pady=5)



def pidief():
    pdf=FPDF()
    pac=paciente.get()
    fech=fecha.get()
    nume=numero.get()
    mot=motivo.get()
    ana=anamnesis.get()
    exaf=examenf.get()
    exac=examenec.get()
    obs=observaciones.get()
    indc=indicaciones.get()

    pdf.add_page()
    pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt="Ficha Veterinaria VetPerrito",ln=1,align="C")
    pdf.cell(200,10,txt="Nombre del paciente: "+pac+",         Atendido El "+fech+"." ,ln=5,align="L")
    pdf.cell(200,10,txt="Numero De contacto del Tutor: "+nume+"." ,ln=7,align="L")

    pdf.cell(200,10,txt="Motivo De La Visita: "+mot, ln=9,align="L")
    pdf.cell(200,10,txt="Anamnesis: "+ana, ln=11,align="L")
    pdf.cell(200,10,txt="Examen Fisico: "+exaf, ln=13,align="L")
    pdf.cell(200,10,txt="Examenes Complementarios: "+exac, ln=15,align="L")
    pdf.cell(200,10,txt="Observaciones: "+obs, ln=17,align="L")
    pdf.cell(200,10,txt="Indicaciones: "+indc, ln=19,align="L")
    pdf.cell(200,10,txt=" VetPerrito.   ", ln=21,align="R")
    pdf.image('img/logo.png',x=10,y=10,w=10,h=10,type="",link='')
    

    pdf.output("Ficha Veterinaria "+pac+".pdf")
    messagebox.showinfo(message="Archivo Generado Correctamente", title="Archivo generado exitosamente")


def seleccionar(event):
    id= tvagenda.selection()[0]
    if int(id)>0:
        paciente.set(tvagenda.item(id,"values")[1])
        fecha.set(tvagenda.item(id,"values")[2])
        numero.set(tvagenda.item(id,"values")[3])
        motivo.set(tvagenda.item(id,"values")[4])
        anamnesis.set(tvagenda.item(id,"values")[5])
        examenf.set(tvagenda.item(id,"values")[6])
        examenec.set(tvagenda.item(id,"values")[7])
        indicaciones.set(tvagenda.item(id,"values")[8])
        observaciones.set(tvagenda.item(id,"values")[9])


tvagenda.bind("<<TreeviewSelect>>",seleccionar)

def volver():
    ventana.destroy()
    import Menuadmin
    

def vaciatabla():
    filas= tvagenda.get_children()
    for fila in filas:
        tvagenda.delete(fila)
     
def llenatabla():
    vaciatabla()
    val=(dia.get())
  
    sql="""select * from ficha where Paciente=%s """
    db.cursor.execute(sql,(val,))
    filas= db.cursor.fetchall()
    for fila in filas:
        id= fila[0]
        tvagenda.insert("",END,id,text="id", values=fila)

       



ventana.mainloop()