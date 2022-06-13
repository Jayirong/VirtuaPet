from cgitb import text
from email import message
from operator import mod
from tkinter import messagebox
from xml.dom import NoModificationAllowedErr
from Connect import *
from tkinter import *
from tkinter import ttk

f = ("Times bold", 14)


#VENTANA
ventana= Tk()
ventana.geometry("1000x600")
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'


imagen = PhotoImage(file = "img/GestionUsuarios.png")
background = Label(image = imagen, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

f = ("Times bold", 14)

imageneliminar = PhotoImage(file = "img/Boton_Eliminar.png")
imagenseleccionar = PhotoImage(file = "img/Boton_Seleccionar.png")
imagenguardar = PhotoImage(file = "img/Boton_Guardar.png")
imagenatras = PhotoImage(file = "img/Boton_Atras.png")
#se definen las variables

#Dentro del marco
db=DataBase()
modificar=False


Id=StringVar()
User=StringVar()
Clave=StringVar()
Tipo=StringVar()
Nom=StringVar()
Ape=StringVar()
Num=StringVar()

#Los lables con caja de texto

#lbluser=Label(ventana, text="Usuario").place(x=50, y=305)
txtuser=Entry(ventana, textvariable=User)
txtuser.place(x=40, y=128,width=330)

#lblclave=Label(ventana, text="Contraseña").place(x=50, y=305)
txtclave=Entry(ventana, textvariable=Clave)
txtclave.place(x=40, y=188,width=330)

#lblNom=Label(ventana, text="Nombre").place(x=50, y=305)
txtNom=Entry(ventana, textvariable=Nom)
txtNom.place(x=40, y=307,width=330)

#lblNum=Label(ventana, text="Numero").place(x=50, y=305)
txtNum=Entry(ventana, textvariable=Num)
txtNum.place(x=40, y=432,width=330)




#lbltipo=Label(ventana, text="Perfil De Usuario").place(x=50, y=305)
txttipo=ttk.Combobox(ventana,values=["Administrador","Veterinario","Recepcion"], textvariable=Tipo)
txttipo.place(x=40, y=248,width=330)
txttipo.current(0)


#lblApe=Label(ventana, text="Apellido").place(x=50, y=305)
txtApe=Entry(ventana, textvariable=Ape)
txtApe.place(x=40, y=368,width=330)








#CUADRADO CON LA BDD

tvpersonas=ttk.Treeview(ventana, selectmode=NONE,height=17)

tvpersonas.place(x=400, y=128)
tvpersonas["columns"]=("Id","Nom","Ape","User","Clave","Tipo","Num")
tvpersonas.column("#0",width=0,stretch=NO)
tvpersonas.column("Id",width=10,anchor=CENTER)
tvpersonas.column("Nom",width=90,anchor=CENTER)
tvpersonas.column("Ape",width=100,anchor=CENTER)
tvpersonas.column("User",width=70,anchor=CENTER)
tvpersonas.column("Clave",width=70,anchor=CENTER)
tvpersonas.column("Tipo",width=100,anchor=CENTER)
tvpersonas.column("Num",width=100,anchor=CENTER)



tvpersonas.heading("Id",text="ID",anchor=CENTER)
tvpersonas.heading("Nom",text="Nombre",anchor=CENTER)
tvpersonas.heading("Ape",text="Apellido",anchor=CENTER)
tvpersonas.heading("User",text="Usuario",anchor=CENTER)
tvpersonas.heading("Clave",text="Contraseña",anchor=CENTER)
tvpersonas.heading("Tipo",text="Tipo de cuenta",anchor=CENTER)
tvpersonas.heading("Num",text="Numero",anchor=CENTER)







#Botones 



btnNuevo=Button(ventana,text="GUARDAR", command=lambda:nuevo(),image=imagenguardar)
btnNuevo.place(x=820, y=525)

btnActualizar=Button(ventana,text="SELECCIONAR", command=lambda:actualizar(),image=imagenseleccionar)
btnActualizar.place(x=600, y=525)

btnEliminar=Button(ventana,text="ELIMINAR", command=lambda:eliminar(),image=imageneliminar)
btnEliminar.place(x=440, y=525)






def seleccionar(event):
    Id= tvpersonas.selection()[0]
    if int(Id)>0:
        Nom.set(tvpersonas.item(Id,"values")[1])
        Ape.set(tvpersonas.item(Id,"values")[2])
        User.set(tvpersonas.item(Id,"values")[3])
        Clave.set(tvpersonas.item(Id,"values")[4])
        Tipo.set(tvpersonas.item(Id,"values")[5])
        Num.set(tvpersonas.item(Id,"values")[6])
      
    

tvpersonas.bind("<<TreeviewSelect>>",seleccionar)


def validar():
 
    return len(User.get())>0 and len(Clave.get())>0 and   len(Nom.get())>0 and  len(Ape.get())>0 and len(Num.get())>0 and len(Tipo.get())
        
def modificarF():
 global modificar
 modificar=False
 tvpersonas.config(selectmode=NONE)
 btnNuevo.config(text="GUARDAR")
 btnActualizar.config(text="SELECCIONAR")
 btnEliminar.config(state=DISABLED)

def modificarT():
 global modificar
 modificar=True
 tvpersonas.config(selectmode=BROWSE)
 btnNuevo.config(text="NUEVO")
 btnActualizar.config(text="ACTUALIZAR")
 btnEliminar.config(state=NORMAL)

def limpiar():
    User.set("")
    Clave.set("")
    Ape.set("")
    Nom.set("")
    Num.set("")
#eliminar fila por fila
def vaciatabla():
    filas= tvpersonas.get_children()
    for fila in filas:
        tvpersonas.delete(fila)
 

#llenar tabla fila por fila
def llenatabla():
    vaciatabla()
    sql="select * from personas"
    db.cursor.execute(sql)
    filas= db.cursor.fetchall()
    for fila in filas:
        id= fila[0]
        tvpersonas.insert("",END,id,text="id", values=fila)
def eliminar():
    id= tvpersonas.selection()[0]
    respuesta = messagebox.askquestion(message="¿Esta Segur@ De Eliminar la Cuenta?", title="Aviso")
    if int(id)>0 and respuesta=='yes': 
        sql="delete from personas where Id="+id
        db.cursor.execute(sql)
        db.connection.commit()
        tvpersonas.delete(id)
       
        messagebox.showinfo("Aviso","Se Elimino El Usuario Correctamente")
        limpiar()
    else:
        messagebox.showinfo("Aviso","no se a seleccionado un Usuario para eliminar")
def nuevo():
    if modificar==False:
    
     if validar():
       val=(Nom.get(),Ape.get(),User.get(),Clave.get(),Tipo.get(),Num.get())
       sql="insert into personas (Nom,Ape,User,Clave,Tipo,Num) values (%s,%s,%s,%s,%s,%s)"
       db.cursor.execute(sql, val)
       db.connection.commit() 
       messagebox.showinfo("Aviso","Se Guardo El Usuario Correctamente")
       llenatabla()
       limpiar()
     else:
       messagebox.showerror("ERROR","LOS CAMPOS NO DEBEN ESTAR VACIOS")
    else:
       limpiar()
       modificarF()


def actualizar():

    if modificar==True:
    
     if validar():
       id=tvpersonas.selection()[0]
       val=(Nom.get(),Ape.get(),User.get(),Clave.get(),Tipo.get(),Num.get())
       sql="update personas set Nom=%s,Ape=%s,User=%s,Clave=%s,Tipo=%s,Num=%s where id="+id
       db.cursor.execute(sql, val)
       db.connection.commit() 
       messagebox.showinfo("Aviso","Se Actualizo El Usuario Correctamente")
       llenatabla()
       limpiar()
     else:
      messagebox.showerror("ERROR","ERROR, LOS CAMPOS NO DEBEN ESTAR VACIOS",fg="red")
    else:
       modificarT()


def nextPage():
    ventana.destroy()
    import Menuadmin

Button(
 ventana,

 text="ATRAS"
 , 
  
    font=f,
    command=nextPage
    ,image=imagenatras,
    ).place(x=42, y=528)
        


llenatabla()




ventana.mainloop()