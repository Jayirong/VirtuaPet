from tkinter import *

ventana= Tk()
ventana.geometry("820x520")
ventana.title("Gestion de Reserva")
ventana['bg'] = '#a5aae0'


marco = LabelFrame(ventana)
marco.place(x=50,y=50,width=720,height=420)
marco['bg'] = '#f1d7ff'

f = ("Times bold", 14)


def nextPage():
    ventana.destroy()
    import Menu

Button(
 ventana,

 text="ATRAS"
 , 
  
    font=f,
    command=nextPage
    ).pack(side=BOTTOM,padx=5,pady=5
    )       

ventana.mainloop()