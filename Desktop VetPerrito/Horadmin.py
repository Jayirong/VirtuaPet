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
ventana.geometry("1000x600")
ventana.resizable(width = False, height = False)
ventana.title("Gestion de Horarios de reserva")
ventana['bg'] = '#a5aae0'


imagen = PhotoImage(file = "img/Horas.png")
background = Label(image = imagen, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
imagenatras  = PhotoImage(file = "img/Boton_Atras.png")
imageneliminar  = PhotoImage(file = "img/BotonEliminar_GestionReserva.png")
imagenseleccionar = PhotoImage(file = "img/BotonSeleccionar_GestionReserva.png")
imagenuardar  = PhotoImage(file = "img/BotóneGuardar_Horas.png")
#Dentro del marco
db=DataBase()

hora=StringVar()
amp=StringVar()

#CUADRADO CON LA BDD

tvagenda=ttk.Treeview(ventana, selectmode=NONE,height=15)
tvagenda.place(x=200,y=165)
tvagenda["columns"]=("id","horarios")
tvagenda.column("#0",width=0,stretch=NO)

tvagenda.column("id",width=0,stretch=NO)
tvagenda.column("horarios",width=600,anchor=CENTER)

tvagenda.heading("id",text="ID",anchor=CENTER)
tvagenda.heading("horarios",text="Horarios",anchor=CENTER)




txthora=Entry(ventana, textvariable=hora)
txthora.place(x=500,y=110,width=260,height=28)









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

btnNuevo=Button(ventana,text="GUARDAR", command=lambda:nuevo(),image=imagenuardar)
btnNuevo.place(x=670,y=532)           
btnNuevo=Button(ventana,text="ELIMINAR", command=lambda:eliminar(),image=imageneliminar)
btnNuevo.place(x=495,y=532)     
btnNuevo=Button(ventana,text="VOLVER", command=lambda:nextPage(),image=imagenatras)
btnNuevo.place(x=35,y=532)
llenatabla()
ventana.mainloop()