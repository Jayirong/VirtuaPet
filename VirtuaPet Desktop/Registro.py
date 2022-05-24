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
ventana.geometry("800x520")
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=700,height=420)
marco['bg'] = '#f1d7ff'

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

lbluser=Label(marco, text="Usuario").grid(column=0,row=0,padx=5,pady=5),
txtuser=Entry(marco, textvariable=User)
txtuser.grid(column=1,row=0)

lblclave=Label(marco, text="Contraseña").grid(column=0,row=1,padx=5,pady=5)
txtclave=Entry(marco, textvariable=Clave)
txtclave.grid(column=1,row=1)

lblNom=Label(marco, text="Nombre").grid(column=2,row=0,padx=5,pady=5)
txtNom=Entry(marco, textvariable=Nom)
txtNom.grid(column=3,row=0)

lblNum=Label(marco, text="Numero").grid(column=2,row=2,padx=5,pady=5)
txtNum=ttk.Entry(marco, textvariable=Num)
txtNum.grid(column=3,row=2)




lbltipo=Label(marco, text="Perfil De Usuario").grid(column=0,row=2,padx=5,pady=5)
txttipo=ttk.Combobox(marco,values=["Administrador","Veterinario","Recepcion"], textvariable=Tipo)
txttipo.grid(column=1,row=2)
txttipo.current(0)


lblApe=Label(marco, text="Apellido").grid(column=2,row=1,padx=5,pady=5)
txtApe=ttk.Entry(marco, textvariable=Ape)
txtApe.grid(column=3,row=1)






lblMensaje=Label(marco,text="Texto en verde ᵃ",fg="green")
lblMensaje.grid(column=0,row=3,columnspan=4,padx=2,pady=2)

#CUADRADO CON LA BDD

tvpersonas=ttk.Treeview(marco, selectmode=NONE)
tvpersonas.grid(column=0,row=5,columnspan=4,padx=5,pady=5)
tvpersonas["columns"]=("Id","Nom","Ape","User","Clave","Tipo","Num")
tvpersonas.column("#0",width=0,stretch=NO)
tvpersonas.column("Id",width=10,anchor=CENTER)
tvpersonas.column("Nom",width=100,anchor=CENTER)
tvpersonas.column("Ape",width=100,anchor=CENTER)
tvpersonas.column("User",width=150,anchor=CENTER)
tvpersonas.column("Clave",width=70,anchor=CENTER)
tvpersonas.column("Tipo",width=130,anchor=CENTER)
tvpersonas.column("Num",width=100,anchor=CENTER)



tvpersonas.heading("Id",text="ID",anchor=CENTER)
tvpersonas.heading("Nom",text="Nombre",anchor=CENTER)
tvpersonas.heading("Ape",text="Apellido",anchor=CENTER)
tvpersonas.heading("User",text="Usuario",anchor=CENTER)
tvpersonas.heading("Clave",text="Contraseña",anchor=CENTER)
tvpersonas.heading("Tipo",text="Tipo de cuenta",anchor=CENTER)
tvpersonas.heading("Num",text="Numero",anchor=CENTER)







#Botones 



btnNuevo=Button(marco,text="GUARDAR", command=lambda:nuevo())
btnNuevo.grid(column=0,row=6)

btnActualizar=Button(marco,text="SELECCIONAR", command=lambda:actualizar())
btnActualizar.grid(column=1,row=6)

btnEliminar=Button(marco,text="ELIMINAR", command=lambda:eliminar())
btnEliminar.grid(column=3,row=6)






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
        lblMensaje.config(text="se elimino el Usuario")
        messagebox.showinfo("Aviso","Se Elimino El Usuario Correctamente")
        limpiar()
    else:
        lblMensaje.config(text="no se a seleccionado un Usuario para eliminar")
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
    ).pack(side=BOTTOM,padx=5,pady=5
    )       


llenatabla()




ventana.mainloop()