from cmath import exp
import string
from tkinter import *
from Login import yo
from mysqlx import Column



ventana= Tk()
ventana.geometry("400x500")
ventana.title("Menu Administrador de "+yo)
ventana['bg'] = '#a5aae0'

marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=300,height=400)
marco['bg'] = '#f1d7ff'


f = ("Times bold", 14)

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


Button(
 marco,

 text="GESTION DE RESERVAS"
 , 
  
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=TOP,padx=5,pady=5
    )

Button(
 marco,

 text="GESTIONAR FICHAS"
 , 
    command=nextPage3,
    font=f,
   
    ).pack(fill=X, expand=TRUE, side=TOP,padx=5,pady=5
    )

Button(
 marco,

 text="GESTIONAR USUARIOS"
 , 
  
    font=f,
    command=nextPage2
   
    ).pack(fill=X, expand=TRUE, side=TOP,padx=5,pady=5
    )    

Button(
 marco,

 text="GESTIONAR HORARIOS"
 , 
  
    font=f,
    command=nextPage4
   
    ).pack(fill=X, expand=TRUE, side=TOP,padx=5,pady=5
    )     

Button(
 marco,

 text="SALIR"
 , 
  
    font=f,
    command=destruir
    ).pack(fill=X, expand=TRUE, side=BOTTOM,padx=5,pady=5)
 





ventana.mainloop()

