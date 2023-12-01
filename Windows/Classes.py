from tkinter import *
from tkinter import ttk

class MyWindow_base:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberShield")
        self.window.geometry("800x480")
        self.window.minsize(800, 360)
        self.window.iconbitmap("")
        self.window.config(background='#030720')
        self.nom_utilisateur_var = StringVar()
        self.mot_de_passe_var = StringVar()

        # Initialisation of components
        self.frame_top = Frame(self.window, bg='#030720')
        self.frame_center = Frame(self.window, bg='#030720')
        self.frame_bottom = Frame(self.window, bg='#030720')

        # Packaging
        self.frame_top.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_center.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)