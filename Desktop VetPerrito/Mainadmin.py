from cgitb import text
from email import message
from operator import mod
from tkinter import messagebox
from Connect import *
from tkinter import *
from tkinter import ttk
import tkinter as mytk

f = ("Times bold", 14)


#VENTANA
ventana= Tk()
ventana.geometry("1000x600")
ventana.resizable(width = False, height = False)
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'

imagen = PhotoImage(file = "img/GestionReserva.png")
background = Label(image = imagen, text = "Imagen de fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
imagenatras  = PhotoImage(file = "img/BotonVolver_GestionReserva.png")
imageneliminar  = PhotoImage(file = "img/BotonEliminar_GestionReserva.png")
imagenseleccionar = PhotoImage(file = "img/BotonSeleccionar_GestionReserva.png")
imagenuardar  = PhotoImage(file = "img/BotonGuardar_GestionReserva.png")

#Dentro del marco
db=DataBase()
modificar=False

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

#Los lables con caja de texto

sql="select horarios from Horarios"
db.cursor.execute(sql)
horas= db.cursor.fetchall()
lista =list(horas)
    


#lblnombre=Label(ventana1, text="NOMBRE").place(x=520, y=60),
txtnombre=Entry(ventana, textvariable=nombre, width=55)
txtnombre.place(x=40, y=128)

#lblapellido=Label(ventana1, text="APELLIDO").place(x=520, y=60)
txtapellido=Entry(ventana, textvariable=apellido, width=55)
txtapellido.place(x=40, y=188)

#lblnombrem=Label(ventana1, text="NOMBRE MASCOTA").place(x=520, y=60)
txtnombrem=Entry(ventana, textvariable=nombrem, width=55)
txtnombrem.place(x=40, y=368)

#lblsexo=Label(ventana1, text="SEXO MASCOTA").place(x=520, y=60)
txtsexo=ttk.Combobox(ventana,values=["Macho","Hembra"], textvariable=sexo)
txtsexo.place(x=40, y=425)
txtsexo.current(0)

#lblnumero=Label(ventana1, text="NUMERO").place(x=520, y=60)
txtnumero=Entry(ventana, textvariable=numero, width=55)
txtnumero.place(x=40, y=248)

#lblraza=Label(ventana1, text="ESPECIE").place(x=520, y=60)
txtraza=ttk.Combobox(ventana,values=["Perro","Gato","Hamster","Tortuga","Conejo","Otros"], textvariable=raza)
txtraza.place(x=218, y=425)
txtraza.current(0)

#lbldia=Label(ventana1, text="DIA").place(x=520, y=60)
txtdia=ttk.Combobox(ventana,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"], textvariable=dia)
txtdia.place(x=40, y=308,width=100)
txtdia.current(0)

#lbldia=Label(ventana1, text="MES").place(x=520, y=60)
txtdia=ttk.Combobox(ventana,values=["ENERO","FEBRERO","MARZO","ABRIL","MAYO","JUNIO","JULIO","AGOSTO","SEPTIEMBRE","OCTUBRE","NOVIEMBRE","DICIEMBRE"], textvariable=mes)
txtdia.place(x=155, y=308,width=100)
txtdia.current(0)

#lblhora=Label(ventana1, text="HORA").place(x=520, y=60)
txthora=ttk.Combobox(ventana,values=lista, textvariable=hora)
txthora.place(x=270, y=308,width=100)
txthora.current(0)


#lblMensaje=Label(ventana1,text="Texto en verde ᵃ",fg="green")
#lblMensaje.place(x=320, y=60)

#CUADRADO CON LA BDD

tvagenda=ttk.Treeview(ventana, selectmode=NONE)
tvagenda.place(x=410, y=130,height=360)
tvagenda["columns"]=("id","Mes","Dia","Hora","Nombre","Apellido","Numero","Nombre_Mascota","Sexo_Mascota","Raza_Mascota")
tvagenda.column("#0",width=0,stretch=NO)
tvagenda.column("id",width=10,anchor=CENTER)
tvagenda.column("Mes",width=60,anchor=CENTER)
tvagenda.column("Dia",width=25,anchor=CENTER)
tvagenda.column("Hora",width=40,anchor=CENTER)
tvagenda.column("Nombre",width=70,anchor=CENTER)
tvagenda.column("Apellido",width=70,anchor=CENTER)
tvagenda.column("Numero",width=70,anchor=CENTER)
tvagenda.column("Nombre_Mascota",width=60,anchor=CENTER)
tvagenda.column("Sexo_Mascota",width=60,anchor=CENTER)
tvagenda.column("Raza_Mascota",width=70,anchor=CENTER)


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





#Botones 


btnNuevo=Button(ventana,text="GUARDAR", command=lambda:nuevo(),image=imagenuardar)
btnNuevo.place(x=820, y=525) 

btnActualizar=Button(ventana,text="SELECCIONAR", command=lambda:actualizar(),image=imagenseleccionar)
btnActualizar.place(x=600, y=525) 

btnEliminar=Button(ventana,text="ELIMINAR", command=lambda:eliminar(),image=imageneliminar)
btnEliminar.place(x=440, y=525)  



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

def validar():
    return len(nombre.get())>0 and len(apellido.get())>0 and  len(numero.get())>0 and  len(nombrem.get())>0
        
def modificarF():
 global modificar
 modificar=False
 tvagenda.config(selectmode=NONE)
 btnNuevo.config(text="GUARDAR")
 btnActualizar.config(text="SELECCIONAR")
 btnEliminar.config(state=DISABLED)

def modificarT():
 global modificar
 modificar=True
 tvagenda.config(selectmode=BROWSE)
 btnNuevo.config(text="NUEVO")
 btnActualizar.config(text="ACTUALIZAR")
 btnEliminar.config(state=NORMAL)

def limpiar():
    nombre.set("")
    apellido.set("")
    numero.set("")
    nombrem.set("")
#eliminar fila por fila
def vaciatabla():
    filas= tvagenda.get_children()
    for fila in filas:
        tvagenda.delete(fila)
 
#llenar tabla fila por fila
def llenatabla():
    vaciatabla()
    sql="select * from agenda order by id desc"
    db.cursor.execute(sql)
    filas= db.cursor.fetchall()
    for fila in filas:
        id= fila[0]
        tvagenda.insert("",END,id,text="id", values=fila)
def eliminar():
    id= tvagenda.selection()[0]
    respuesta = messagebox.askquestion(message="¿Esta Segur@ De Eliminar la Reserva?", title="Aviso")
    if int(id)>0 and respuesta=='yes': 
        sql="delete from agenda where ID="+id
        db.cursor.execute(sql)
        db.connection.commit()
        tvagenda.delete(id)
     
        messagebox.showinfo("Aviso","Se Elimino El Registro Correctamente")
        limpiar()
    else:
        messagebox.showinfo("Aviso","no se a seleccionado un registro para eliminar")
def nuevo():
    if modificar==False:
    
     if validar():
       val=(mes.get(),dia.get(),hora.get(),nombre.get(),apellido.get(),numero.get(),nombrem.get(),sexo.get(),raza.get())
       sql="insert into agenda (Mes,Dia,Hora,Nombre,Apellido,Numero,Nombre_Mascota,Sexo_Mascota,Raza_Mascota) values (%s,%s,%s,%s,%s,%s,%s,%s)"
       db.cursor.execute(sql, val)
       db.connection.commit() 
       messagebox.showinfo("Aviso","Se Guardo El Registro Correctamente")
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
       id=tvagenda.selection()[0]
       val=(mes.get(),dia.get(),hora.get(),nombre.get(),apellido.get(),numero.get(),nombrem.get(),sexo.get(),raza.get())
       sql="update agenda set Mes=%s, Dia=%s,Hora=%s,Nombre=%s,Apellido=%s,Numero=%s,Nombre_Mascota=%s,Sexo_Mascota=%s,Raza_Mascota=%s where id="+id
       db.cursor.execute(sql, val)
       db.connection.commit() 
       messagebox.showinfo("Aviso","Se Actualizo El Registro Correctamente")
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
 , image=imagenatras,
  
    font=f,
    command=nextPage
    ).place(x=35, y=525)     

llenatabla()

#se define la ventana que pregunta si se quiere cerrar

class MyDialog:
    def __init__(self, parent):
        self.top = mytk.Toplevel(parent)

        # bloque usado para centrar la ventana toplevel
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