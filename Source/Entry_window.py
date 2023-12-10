from tkinter import *
from tkinter import ttk
import subprocess
from Classes import MyWindow_base
#030720

class MyWindow_Entry(MyWindow_base):

    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()

        # Creation of components
        self.create_widgets()

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_buttons()

    def create_title(self):
        label_title = Label(self.frame_top, text="\nGestionnaire de Mots de passe\n", font=("Courrier", 40), bg='#030720',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame_top, text="Bienvenue, veuillez vous identifier ou créer un compte", font=("Courrier", 25), bg='#030720',
                               fg='white')
        label_subtitle.pack()

    def create_buttons(self):
        # Ajustez le style des boutons pour augmenter la taille
        style = ttk.Style()
        style.configure("TButton", padding=(20, 10))

        bouton_creer_compte = ttk.Button(self.frame_center, text="S'inscrire", command=self.open_create_account)
        bouton_creer_compte.pack(pady=10)

        bouton_authentifier = ttk.Button(self.frame_bottom, text="Se connecter", command=self.open_connection_window)
        bouton_authentifier.pack(pady=10)

    def open_create_account(self):
        subprocess.Popen(["python", "C:/Users/thoma/Documents/Programme/Projets/Password_Manager/Source/Create_account_window.py"])
        self.window.destroy()

    def open_connection_window(self):
        subprocess.Popen(["python", "C:/Users/thoma/Documents/Programme/Projets/Password_Manager/Source/Connection_window.py"])
        self.window.destroy()



# Display
app = MyWindow_Entry()
app.window.mainloop()

