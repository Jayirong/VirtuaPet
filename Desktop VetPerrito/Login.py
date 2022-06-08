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


def ClicktoLogin():
    
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


ventana.mainloop()