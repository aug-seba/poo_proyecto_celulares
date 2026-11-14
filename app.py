import tkinter as tk
from view.form_frame import FormFrame
from controller.controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana principal")
        
        
        self.frame = FormFrame(self)
        



if __name__=="__main__":
    Controller().create_table()
    Controller().create_table_ventas()
    app = App()
    app.mainloop()
    
    
