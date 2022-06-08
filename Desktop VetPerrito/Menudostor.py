from cmath import exp
from tkinter import *

from mysqlx import Column


ventana= Tk()
ventana.geometry("1000x600")
ventana.title("Menu Veterinario de ")
ventana['bg'] = '#a5aae0'



f = ("Times bold", 14)

imagen = PhotoImage(file = "img/imagen3.png")
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
    import Verhorario
    
def nextPage2():
   ventana.destroy()
   import Gestiondostor

    
def nextPage3():
   ventana.destroy()
   import Fichas

def destruir():
    ventana.destroy()


 
#"VER HORARIOS"  "CREAR FICHAS" "GESTIONAR FICHAS" "SALIR"


LoginBtn = Button(ventana, text ="", command = nextPage, relief="groove" , image=imagengestion)
LoginBtn.place(x=60, y=60)

LoginBtn = Button(ventana, text ="", command = nextPage3, relief="groove" , image=imagengestionf)
LoginBtn.place(x=520, y=60)



LoginBtn = Button(ventana, text ="", command = nextPage2, relief="groove" , image=imagengestionf)
LoginBtn.place(x=520, y=250)

LoginBtn = Button(ventana, text ="", command = destruir, relief="groove" , image=salir)
LoginBtn.place(x=800, y=500)





ventana.mainloop()
