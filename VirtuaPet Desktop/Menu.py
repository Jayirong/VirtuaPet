from cmath import exp
from tkinter import *

from mysqlx import Column


ventana= Tk()
ventana.geometry("400x500")
ventana.title("Menu Recepcion")
ventana['bg'] = '#a5aae0'

marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=300,height=400)
marco['bg'] = '#f1d7ff'


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

 text="INFORME C"
 , 
    command=nextPage3,
    font=f,
   
    ).pack(fill=X, expand=TRUE, side=TOP,padx=5,pady=5
    )

Button(
 marco,

 text="CREAR ARCHIVO FICHAS"
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

