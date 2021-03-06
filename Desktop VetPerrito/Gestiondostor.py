from ast import Str
from cProfile import label
from tkinter import *
from cgitb import text
from email import message
from operator import mod
import tkinter as mytk
import string
from tkinter import messagebox
from Connect import *
from tkinter import *
from tkinter import ttk
from fpdf import *
from fpdf import FPDF

#VENTANA y sus parametros
ventana= Tk()
ventana.geometry("1000x600")
ventana.resizable(width = False, height = False)
ventana.title("Generacion De Ficha Veterinaria")
ventana['bg'] = '#a5aae0'

imagen = PhotoImage(file = "img/GenerarFicha.png")
background = Label(image = imagen, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

f = ("Times bold", 14)

imagenbuscar = PhotoImage(file = "img/BotónBuscar_GenerarFicha.png")
imagengenerar = PhotoImage(file = "img/BotónGenerarArchivo_GenerarFicha.png")
imagenatras = PhotoImage(file = "img/Boton_Atras.png")
#se definen las variables


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

#caja de texto paciente y entrada de texto


txtdia=Entry(ventana,width=37, textvariable=dia)
txtdia.place(x=710,y=130,height=25)


#cuadro con la info de la bdd
tvagenda=ttk.Treeview(ventana, selectmode=NONE,height=14)
tvagenda.place(x=595, y=185)
tvagenda["columns"]=("id","Paciente","Fecha","Numero","Motivo_consulta","Anamnesis","Examen_fisico","Examenes_complementarios","Indicaciones","Observacion")
tvagenda.column("#0",width=0,stretch=NO)
tvagenda.column("id",width=10,anchor=CENTER)
tvagenda.column("Paciente",width=170,anchor=CENTER)
tvagenda.column("Fecha",width=170,anchor=CENTER)
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

#cajas de texto





txtpaciente=Entry(ventana,width=37, textvariable=paciente)
txtpaciente.place(x=35, y=165)


txtpaciente=Entry(ventana,width=17, textvariable=fecha)
txtpaciente.place(x=290, y=165)


txtpaciente=Entry(ventana, textvariable=numero)
txtpaciente.place(x=420, y=165)



txtpaciente=Entry(ventana,width=37, textvariable=motivo)

txtpaciente.place(x=35, y=220,height=60)



txtpaciente=Entry(ventana, textvariable=anamnesis,width=40)
txtpaciente.place(x=295, y=330,height=50)

txtpaciente=Entry(ventana,width=40, textvariable=examenf)
txtpaciente.place(x=295, y=220,height=60)


txtpaciente=Entry(ventana,width=37, textvariable=examenec)
txtpaciente.place(x=35, y=330,height=50)



txtpaciente=Entry(ventana,width=37, textvariable=indicaciones)
txtpaciente.place(x=35, y=435,height=55)


txtpaciente=Entry(ventana,width=40, textvariable=observaciones)
txtpaciente.place(x=295, y=435,height=55)





#botones



btnNuevo=Button(ventana,text="BUSCAR", command=lambda:llenatabla(),image=imagenbuscar)
btnNuevo.place(x=563, y=534)



btnNuevo=Button(ventana,text="ATRAS", command=lambda:volver(),image=imagenatras)
btnNuevo.place(x=40, y=534)
btnNuevo=Button(ventana,text="GENERAR ARCHIVO", command=lambda:pidief(),image=imagengenerar)
btnNuevo.place(x=220, y=534)
#funcion de generar pdf

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
    pdf.cell(200,10,txt="Nombre del paciente: "+pac+",  Atendido El "+fech+"." ,ln=5,align="L")
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
    
#llenar cajas de texo
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
    import Menudostor
    

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
        
        respuesta = messagebox.askyesno("Aviso","¿Desea Salir de la App?")
        
        if respuesta == TRUE:

            ventana.destroy()
       


        
        #d = MyDialog(ventana)
        #self.parent.wait_window(d.top)


app = MyApp(ventana)

ventana.mainloop()