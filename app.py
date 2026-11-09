import tkinter as tk
from view.form_frame import FormFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana principal")
        
        
        self.frame = FormFrame(self)
        



if __name__=="__main__":
    app = App()
    app.mainloop()
    
