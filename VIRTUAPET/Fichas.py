from sqlite3 import Date
from tkinter import *
from Connect import *

f = ("Times bold", 14)


#VENTANA
ventana= Tk()
ventana.geometry("760x520")
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=660,height=420)
marco['bg'] = '#f1d7ff'

#Dentro del marco
db=DataBase()
modificar=False

id=IntVar()
paciente=StringVar()
fecha=StringVar()
numero=IntVar()
motivo=StringVar()
anamnesis=StringVar()
examenf=StringVar()
examenec=StringVar()
indicaciones=StringVar()
observaciones=StringVar()





ventana.mainloop()