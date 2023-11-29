from tkinter import *
from tkinter import ttk
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
        label_subtitle = Label(self.frame, text="Bienvenue !!! Vous pouvez générer un mot de passe et en stocker de manière sécurisé.", font=("Courrier", 25), bg='#800080',
                               fg='white')
        label_subtitle.pack()


    def creer_compte_callback(self):
        nom_utilisateur = self.champ_utilisateur.get()
        mot_de_passe = self.champ_mot_de_passe.get()
        creer_compte(nom_utilisateur, mot_de_passe, base_de_donnees_utilisateurs)
        print("Compte créé avec succès.")


# Display
app = MyApp()
app.window.mainloop()
