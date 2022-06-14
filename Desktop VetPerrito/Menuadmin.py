from cmath import exp
import string
from tkinter import *
import tkinter as mytk
from mysqlx import Column
from tkinter import PhotoImage


ventana= Tk()
ventana.geometry("1000x600")
ventana.resizable(width = False, height = False)
ventana.title("Menu Administrador de ")
ventana['bg'] = '#a5aae0'




f = ("Times bold", 14)
imagen = PhotoImage(file = "img/FONDO ADMIN.png")
background = Label(image = imagen, text = "Imagen de fondo")
imagengestion = PhotoImage(file = "img/Boton_Gestion_Reservas.png")
imagengestionf = PhotoImage(file = "img/Boton_Gestionar_fichas.png")
imagengestionH = PhotoImage(file = "img/Boton_Gestionar_Horarios.png")
imagengestionU = PhotoImage(file = "img/Boton_Gestionar_Usuarios.png")
perrochikito = PhotoImage(file = "img/logochikito.png")
salir = PhotoImage(file = "img/Boton_Salir.png")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)




def nextPage():
   
    ventana.destroy()
    import Mainadmin
    
def nextPage2():
   ventana.destroy()
   import Registro


def nextPage3():
   ventana.destroy()
   import Gestionadmin

def destruir():
    ventana.destroy()

def nextPage4():
   ventana.destroy()
   import Horadmin  


LoginBtn = Button(ventana, text ="", command = nextPage, relief="groove" , image=imagengestion)
LoginBtn.place(x=60, y=60)

LoginBtn = Button(ventana, text ="", command = nextPage3, relief="groove" , image=imagengestionf)
LoginBtn.place(x=520, y=60)

LoginBtn = Button(ventana, text ="", command = nextPage4, relief="groove" , image=imagengestionH)
LoginBtn.place(x=60, y=250)

LoginBtn = Button(ventana, text ="", command = nextPage2, relief="groove" , image=imagengestionU)
LoginBtn.place(x=520, y=250)

LoginBtn = Button(ventana, text ="", command = destruir, relief="groove" , image=salir)
LoginBtn.place(x=800, y=500)

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
        d = MyDialog(ventana)
        self.parent.wait_window(d.top)

app = MyApp(ventana)

ventana.mainloop()