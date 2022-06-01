from cmath import exp
from tkinter import *
from Login import yo
from mysqlx import Column


ventana= Tk()
ventana.geometry("400x500")
ventana.title("Menu Veterinario de "+yo)
ventana['bg'] = '#a5aae0'

marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=300,height=400)
marco['bg'] = '#f1d7ff'


f = ("Times bold", 14)

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


Button(
 marco,

 text="VER HORARIOS"
 , 
  
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=TOP,padx=5,pady=5
    )

Button(
 marco,

 text="CREAR FICHAS"
 , 
    command=nextPage3,
    font=f,
   
    ).pack(fill=X, expand=TRUE, side=TOP,padx=5,pady=5
    )

Button(
 marco,

 text="GESTIONAR FICHAS"
 , 
  
    font=f,
    command=nextPage2
   
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
