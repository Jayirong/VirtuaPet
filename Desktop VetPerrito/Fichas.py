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
ventana.geometry("830x520")
ventana.title("Ficha Medica")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=730,height=420)
marco['bg'] = '#f1d7ff'

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

lblMensaje=Label(marco,text="  TEXTO DE EJEMPLO ",width=50,height=3)
lblMensaje.grid(column=0,row=0,columnspan=4,padx=5,pady=5)



lblpaciente=Label(marco, text="Paciente").grid(column=0,row=1,padx=5,pady=5),
txtpaciente=Entry(marco, textvariable=paciente)
txtpaciente.grid(column=1,row=1,ipadx=200)

lblfecha=Label(marco, text="Fecha").grid(column=0,row=2,padx=5,pady=5),
txtfecha=Entry(marco, textvariable=fecha)
txtfecha.grid(column=1,row=2,ipadx=200)

lblnumero=Label(marco, text="Numero").grid(column=0,row=3,padx=5,pady=5),
txtnumero=Entry(marco, textvariable=numero)
txtnumero.grid(column=1,row=3,ipadx=200)

lblmotiv=Label(marco, text="Motivo de la visita").grid(column=0,row=4,padx=5,pady=5),
txtmotiv=Entry(marco,textvariable=motivo )

txtmotiv.grid(column=1,row=4,padx=5,pady=5, ipadx=200)

lblanam=Label(marco, text="Anamnesis").grid(column=0,row=5,padx=5,pady=5),
txtanam=Entry(marco, textvariable=anamnesis)

txtanam.grid(column=1,row=5,padx=5,pady=5,ipadx=200)

lblfisc=Label(marco, text="Examen Fisico").grid(column=0,row=6,padx=5,pady=5),
txtfisc=Entry(marco, textvariable=examenf)

txtfisc.grid(column=1,row=6,padx=5,pady=5,ipadx=200)

lblexc=Label(marco, text="Examenes Complementario").grid(column=0,row=7,padx=5,pady=5),
txtexc=Entry(marco, textvariable=examenec)

txtexc.grid(column=1,row=7,padx=5,pady=5,ipadx=200)

lblind=Label(marco, text="Indicaciones").grid(column=0,row=8,padx=5,pady=5),
txtind=Entry(marco, textvariable=indicaciones)

txtind.grid(column=1,row=8,padx=5,pady=5,ipadx=200)

lbluser=Label(marco, text="Observaciones").grid(column=0,row=9,padx=5,pady=5),
txtuser=Entry(marco, textvariable=observaciones)

txtuser.grid(column=1,row=9,padx=5,pady=5,ipadx=200)


## BOTONES


btnNuevo=Button(marco,text="ATRAS", command=lambda:volver())
btnNuevo.grid(column=0,row=10,padx=5,pady=10)

btnNuevo=Button(marco,text="GUARDAR", command=lambda:nuevo())
btnNuevo.grid(column=1,row=10,padx=5,pady=10)

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