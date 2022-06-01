import string
from tokenize import String
import mysql.connector as mysqlconnector
import tkinter as mytk
from tkinter import *
import tkinter.messagebox as mymessagebox


ventana= Tk()
ventana.geometry("450x300")
ventana.title("Inicio de Sesion")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=350,height=200)
marco['bg'] = '#f1d7ff'








def ClicktoLogin():
    
    mydb = mysqlconnector.connect(host="localhost", user="root", password="", database="virtuapet2")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM personas where User = '"+ UserTxt.get() +"' and Clave = '"+ PassTxt.get() +"';")
    myresult = mycursor.fetchone()
   
    global yo
    yo = myresult[1]

    if myresult==None:
       mymessagebox.showerror("Error", "Usuario o contraseña incorrectos")

       
    elif myresult[5]=='Administrador':
        
        ventana.destroy()
        import Menuadmin
       
        
    elif myresult[5]=='Veterinario':
        ventana.destroy()
        import Menudostor  
        

    elif myresult[5]=='Recepcion':
        ventana.destroy()
        import Menu   
     

    else:
      mymessagebox.showerror("Error", "Usuario o contraseña incorrectos")   
    
     
    mydb.close()
    mycursor.close()




Bannerlabel = Label(marco, text = "INICIO DE SESION", width=40)
Bannerlabel.place(x=20, y=20)

UserLabel = Label(marco, text = "Usuario:", width=10)
UserLabel.place(x=20, y=60)

UserTxt = Entry(marco,  width=27, relief="flat")
UserTxt.place(x=120, y=60)




UserTxt.focus()

PassLabel = Label(marco, text = "Contraseña:", width=10)
PassLabel.place(x=20, y=90)

PassTxt = Entry(marco,  width=27, relief="flat")
PassTxt.place(x=120, y=90)




PassTxt.config(show="*")

LoginBtn = Button(marco, text ="Iniciar Sesion", command = ClicktoLogin, relief="groove")
LoginBtn.place(x=150, y=140)




ventana.mainloop()