# ACA SE IMPORTAN TODAS LAS LIBRERIAS QUE UTILIZARE EN ESTA PAGINA

from cgitb import text
from sqlite3 import Date
from tkinter import *
from Connect import *
from tkinter import messagebox

## SE DEFINE EL FORMATO DEL TEXTO Y EL TAMAÑO
f = ("Times bold", 14)


#VENTANA
ventana= Tk()
ventana.geometry("1000x600")
ventana.title("Ficha Medica")
ventana['bg'] = '#a5aae0'

imagen = PhotoImage(file = "img/fichaMedica.png")
background = Label(image = imagen, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

imagen1 = PhotoImage(file = "img/Boton_Guardar.png")
imagen2 = PhotoImage(file = "img/BotónVolver_FichaMedica.png")


#SE DEFINEN LAS VARIABLES
db=DataBase()
modificar=False


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

## CAJAS DE TEXTO Y ENTRADAS





#"Paciente"
txtpaciente=Entry(ventana, textvariable=paciente,width=39)
txtpaciente.place(x=50, y=133)

#"Fecha"
txtfecha=Entry(ventana, textvariable=fecha,width=29)
txtfecha.place(x=320, y=133)

#lblnumero=Label(ventana, text="Numero").grid(column=0,row=3,padx=5,pady=5),
txtnumero=Entry(ventana, textvariable=numero,width=30)
txtnumero.place(x=525, y=133)

#lblmotiv=Label(ventana, text="Motivo de la visita").grid(column=0,row=4,padx=5,pady=5),
txtmotiv=Entry(ventana,textvariable=motivo,width=70)

txtmotiv.place(x=50, y=205,height=35)

#lblanam=Label(ventana, text="Anamnesis").grid(column=0,row=5,padx=5,pady=5),
txtanam=Entry(ventana, textvariable=anamnesis,width=70)

txtanam.place(x=510, y=305,height=35)

#lblfisc=Label(ventana, text="Examen Fisico").grid(column=0,row=6,padx=5,pady=5),
txtfisc=Entry(ventana, textvariable=examenf,width=70)

txtfisc.place(x=510, y=205,height=35)

#lblexc=Label(ventana, text="Examenes Complementario").grid(column=0,row=7,padx=5,pady=5),
txtexc=Entry(ventana, textvariable=examenec,width=70)

txtexc.place(x=50, y=305,height=35)

#lblind=Label(ventana, text="Indicaciones").grid(column=0,row=8,padx=5,pady=5),
txtind=Entry(ventana, textvariable=indicaciones,width=70)

txtind.place(x=510, y=400,height=35)

#lbluser=Label(ventana, text="Observaciones").grid(column=0,row=9,padx=5,pady=5),
txtuser=Entry(ventana, textvariable=observaciones,width=70)
txtuser.place(x=50, y=400,height=35)


## BOTONES


btnNuevo=Button(ventana,text="ATRAS", command=lambda:volver(),image=imagen2)
btnNuevo.place(x=35, y=530)

btnNuevo=Button(ventana,text="GUARDAR", command=lambda:nuevo(),image=imagen1)
btnNuevo.place(x=630, y=530)

##Funcion para volver al menu

def volver():
    ventana.destroy()
    import Menudostor
    
#revisa que las cajas no esten vacias   
def validar():
    return len(paciente.get())>0 and len(fecha.get())>0 and  len(numero.get())>0 and  len(motivo.get())>0 and  len(anamnesis.get())>0 and  len(examenf.get())>0 and  len(examenec.get())>0 and  len(indicaciones.get())>0 and  len(observaciones.get())>0
    

#crea una ficha usando los valores insertados en la caja de texto
def nuevo():
   
    
    if validar():
      val=(paciente.get(),fecha.get(),numero.get(),motivo.get(),anamnesis.get(),examenf.get(),examenec.get(),indicaciones.get(),observaciones.get())
      sql="insert into ficha (Paciente,Fecha,Numero,Motivo_consulta,Anamnesis,Examen_fisico,Examenes_complementarios,Indicaciones,Observacion	) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      db.cursor.execute(sql, val)
      db.connection.commit() 
      messagebox.showinfo("Aviso","Se Guardo La Ficha Correctamente")
       
    else:
       messagebox.showerror("ERROR","LOS CAMPOS NO DEBEN ESTAR VACIOS")
    
       

ventana.mainloop()