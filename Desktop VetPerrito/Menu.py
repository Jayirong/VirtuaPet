from cmath import exp
from tkinter import *

from mysqlx import Column


ventana= Tk()
ventana.geometry("1000x600")
ventana.title("Menu Recepcion De ")
ventana['bg'] = '#a5aae0'




f = ("Times bold", 14)



def nextPage():
   
    ventana.destroy()
    import Main
    
    
def nextPage2():
   ventana.destroy()
   import Excel

def nextPage3():
    ventana.destroy()
    import Informe

def destruir():
    ventana.destroy()

#"GESTION DE RESERVAS" "INFORME C" "CREAR ARCHIVO FICHAS" "SALIR"

imagen = PhotoImage(file = "img/imagen1.png")
background = Label(image = imagen, text = "Imagen de fondo")
imagengestion = PhotoImage(file = "img/Boton_Gestion_Reservas.png")
imagengestionf = PhotoImage(file = "img/Boton_Generar_Archivo.png")
imagengestionH = PhotoImage(file = "img/Boton_Gestionar_fichas.png")
imagengestionU = PhotoImage(file = "img/Boton_Gestionar_Usuarios.png")
perrochikito = PhotoImage(file = "img/logochikito.png")
salir = PhotoImage(file = "img/Boton_Salir.png")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)



LoginBtn = Button(ventana, text ="", command = nextPage, relief="groove" , image=imagengestion)
LoginBtn.place(x=60, y=60)

LoginBtn = Button(ventana, text ="", command = nextPage3, relief="groove" , image=imagengestionf)
LoginBtn.place(x=520, y=60)



LoginBtn = Button(ventana, text ="", command = nextPage2, relief="groove" , image=imagengestionH)
LoginBtn.place(x=520, y=250)

LoginBtn = Button(ventana, text ="", command = destruir, relief="groove" , image=salir)
LoginBtn.place(x=800, y=500)



ventana.mainloop()

