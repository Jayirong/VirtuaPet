import tkinter as tk    
from tkinter import *

class MyDialog:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.parent = parent
        self.top.title("Salir")

        tk.Label(self.top, text="¿Está seguro?").grid(row=0, column=0, columnspan=2)

        self.button1 = tk.Button(self.top, text="Si, salir de la app.", command=self.salir)
        self.button2 = tk.Button(self.top, text="No, solo minimizar.", command=self.minimizar)
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
        d = MyDialog(root)
        self.parent.wait_window(d.top)

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()