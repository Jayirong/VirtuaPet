import string
from tokenize import String
import mysql.connector as mysqlconnector
import tkinter as mytk
from tkinter import *
import tkinter.messagebox as mymessagebox
from tkinter import PhotoImage
from tkinter import ttk

ventana= Tk()
ventana.geometry("1000x600")
ventana.resizable(width = False, height = False)
ventana.title("Inicio de Sesion")
ventana['bg'] = ''

font=("Times bold", 15) 
              

imagen = PhotoImage(file = "img/login.png")
imagenbtn = PhotoImage(file = "img/Boton_Inicio_Sesion.png")
imagensalir = PhotoImage(file = "img/Boton_Salir.png")



# Con Label y la opción image, puedes mostrar una imagen en el widget:
background = Label(image = imagen, text = "Imagen de fondo")

# Con place puedes organizar el widget de la imagen posicionandolo
# donde lo necesites (relwidth y relheight son alto y ancho en píxeles):
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Por defecto el fondo es blaco. Accediendo al método config
# de Label podrías, por ejemplo, establecer un color de fondo distinto:
# background.config(bg = "gray")


def Salir():
    ventana.destroy()


def ClicktoLogin(event=None):
    
    mydb = mysqlconnector.connect(host="localhost", user="root", password="", database="virtuapet2")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM personas where User = '"+ UserTxt.get() +"' and Clave = '"+ PassTxt.get() +"';")
    myresult = mycursor.fetchone()
   
    
    global yo

    if myresult==None:
       mymessagebox.showerror("Error", "Usuario o contraseña incorrectos")

       
    elif myresult[5]=='Administrador':
        
        yo = myresult[1]
        ventana.destroy()
        import Menuadmin
       
        
    elif myresult[5]=='Veterinario':
        
        yo = myresult[1]
        ventana.destroy()
        import Menudostor  
        

    elif myresult[5]=='Recepcion':
        
        yo = myresult[1]
        ventana.destroy()
        import Menu   
     

    else:
      mymessagebox.showerror("Error", "Usuario o contraseña incorrectos")   
    
   
     
    mydb.close()
    mycursor.close()


#usuario




UserTxt = Entry(ventana,  width=30, relief="flat", font=font )
UserTxt.place(x=100, y=330,height=30)




UserTxt.focus()

#clave 

PassTxt = Entry(ventana,  width=30 ,relief="flat",font=font)
PassTxt.place(x=100, y=400, height=30)




PassTxt.config(show="*")

LoginBtn = Button(ventana, text ="", command = ClicktoLogin, relief="groove" , image=imagenbtn)
LoginBtn.place(x=80, y=465)

SalirBtn = Button(ventana, text ="", command = Salir, relief="groove" , image=imagensalir)
SalirBtn.place(x=826, y=530)

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
        d = MyDialog(ventana)
        self.parent.wait_window(d.top)

app = MyApp(ventana)

ventana.mainloop()