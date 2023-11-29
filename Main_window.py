from tkinter import *
from tkinter import ttk
from password_generator import generer_mot_de_passe
from account import creer_compte, authentifier, base_de_donnees_utilisateurs

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberShield")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap("CYBERSHIELD.ico")
        self.window.config(background='#ffd700')

        # Initialization of components
        self.frame = Frame(self.window, bg='#800080')

        # Creation of components
        self.create_widgets()

        # Packaging
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_buttons()

    def create_title(self):
        label_title = Label(self.frame, text="Gestionnaire de Mots de passe", font=("Courrier", 40), bg='#800080',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Bienvenue, veuillez vous identifier ou créer un compte", font=("Courrier", 25), bg='#800080',
                               fg='white')
        label_subtitle.pack()


    def create_buttons(self):
        bouton_creer_compte = ttk.Button(self.frame, text="Créer un compte", command=self.creer_compte_callback)
        bouton_creer_compte.pack(pady=10)

        bouton_authentifier = ttk.Button(self.frame, text="S'authentifier", command=self.authentifier_callback)
        bouton_authentifier.pack(pady=10)


# Display
app = MyApp()
app.window.mainloop()
