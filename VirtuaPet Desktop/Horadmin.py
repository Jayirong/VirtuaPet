from cgitb import text
from email import message
from operator import mod
from tkinter import messagebox
from Connect import *
from tkinter import *
from tkinter import ttk

f = ("Times bold", 14)


#VENTANA Y SUS PARAMETROS
ventana= Tk()
ventana.geometry("760x520")
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=660,height=420)
marco['bg'] = '#f1d7ff'

#Dentro del marco
db=DataBase()

hora=StringVar()
amp=StringVar()

#CUADRADO CON LA BDD

tvagenda=ttk.Treeview(marco, selectmode=NONE)
tvagenda.grid(column=0,row=5,columnspan=4,padx=5)
tvagenda["columns"]=("id","horarios")
tvagenda.column("#0",width=0,stretch=NO)

tvagenda.column("id",width=0,stretch=NO)
tvagenda.column("horarios",width=200,anchor=CENTER)

tvagenda.heading("id",text="ID",anchor=CENTER)
tvagenda.heading("horarios",text="Horarios",anchor=CENTER)



lblhora=Label(marco, text="HORA('00:00' AM/PM)").grid(column=1,row=1,padx=5,pady=5)
txthora=Entry(marco, textvariable=hora)
txthora.grid(column=2,row=1)









#funciones
def seleccionar(event):
    id= tvagenda.selection()[0]
    if int(id)>0:
     hora.set(tvagenda.item(id,"values")[1])

def validar():
    return len(hora.get())>0   

tvagenda.bind("<<TreeviewSelect>>",seleccionar)

tvagenda.config(selectmode=BROWSE)

def limpiar():
    hora.set("")
 
#eliminar fila por fila
def vaciatabla():
    filas= tvagenda.get_children()
    for fila in filas:
        tvagenda.delete(fila)


def llenatabla():
    vaciatabla()
    sql="select * from Horarios order by 1"
    db.cursor.execute(sql)
    filas= db.cursor.fetchall()
    for fila in filas:
        id= fila[0]
        tvagenda.insert("",END,id,text="Horarios", values=fila)       

def nuevo():
  
    
    if validar():
       
       val=(hora.get())
       sql="insert into Horarios (horarios) values (%s)"
       db.cursor.execute(sql, (val,))
       db.connection.commit() 
       messagebox.showinfo("Aviso","Se Guardo El Registro Correctamente")
       llenatabla()
       limpiar()
    else:
       messagebox.showerror("ERROR","LOS CAMPOS NO DEBEN ESTAR VACIOS")
   
def eliminar():
    id= tvagenda.selection()[0]
    respuesta = messagebox.askquestion(message="¿Esta Segur@ De Eliminar la Hora?", title="Aviso")
    if  int(id)>0 and respuesta=='yes': 
        sql="delete from Horarios where id="+id
        db.cursor.execute(sql)
        db.connection.commit()
        tvagenda.delete(id)
        
        messagebox.showinfo("Aviso","Se Elimino El Registro Correctamente")
        limpiar()
    else:
        messagebox.showerror("Error","No se a seleccionado un valor")       
def nextPage():
    ventana.destroy()
    import Menuadmin         

btnNuevo=Button(marco,text="GUARDAR", command=lambda:nuevo())
btnNuevo.grid(column=1,row=6,padx=5,pady=5)         
btnNuevo=Button(marco,text="ELIMINAR", command=lambda:eliminar())
btnNuevo.grid(column=2,row=6,padx=5,pady=5)      
btnNuevo=Button(marco,text="VOLVER", command=lambda:nextPage())
btnNuevo.grid(column=3,row=6,padx=5,pady=5)  
llenatabla()
ventana.mainloop()