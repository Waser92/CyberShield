from tkinter import *
from tkinter import ttk
import webbrowser
import random
import string
from password_generator import generer_mot_de_passe
from account import creer_compte, authentifier, base_de_donnees_utilisateurs
#3d5cde


def creer_compte_callback():
    nom_utilisateur = champ_utilisateur.get()
    mot_de_passe = champ_mot_de_passe.get()
    creer_compte(nom_utilisateur, mot_de_passe, base_de_donnees_utilisateurs)
    print("Compte créé avec succès.")

def authentifier_callback():
    nom_utilisateur = champ_utilisateur.get()
    mot_de_passe = champ_mot_de_passe.get()
    if authentifier(nom_utilisateur, mot_de_passe, base_de_donnees_utilisateurs):
        print("Authentification réussie.")
        # Ajoutez ici le code pour permettre à l'utilisateur d'accéder aux fonctionnalités après l'authentification
    else:
        print("Nom d'utilisateur ou mot de passe incorrect.")

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberShield")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap("")
        self.window.config(background='#3d5cde')

        # initialization des composants
        self.frame = Frame(self.window, bg='#3d5cde')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()

    def create_title(self):
        label_title = Label(self.frame, text="Gestionnaire de Mots de passe", font=("Courrier", 40), bg='#3d5cde',
                            fg='white')
        label_title.pack()

    def subtitle(self):
        label_subtitle = Label(self.frame, text="Bienvenue, veuillez vous identifiez ou créer un compte", font=("Courrier", 25), bg='#3d5cde',
                               fg='white')
        label_subtitle.pack()

    def create_entry_fields(self):
        self.champ_utilisateur = ttk.Entry(self.frame, width=30)
        self.champ_utilisateur.insert(0, "Nom d'utilisateur")
        self.champ_utilisateur.pack(pady=10)

        self.champ_mot_de_passe = ttk.Entry(self.frame, show="*", width=30)
        self.champ_mot_de_passe.insert(0, "Mot de passe")
        self.champ_mot_de_passe.pack(pady=10)

    def create_buttons(self):
        bouton_creer_compte = ttk.Button(self.frame, text="Créer un compte", command=self.creer_compte_callback)
        bouton_creer_compte.pack(pady=10)

        bouton_authentifier = ttk.Button(self.frame, text="S'authentifier", command=self.authentifier_callback)
        bouton_authentifier.pack(pady=10)

    def creer_compte_callback(self):
        nom_utilisateur = self.champ_utilisateur.get()
        mot_de_passe = self.champ_mot_de_passe.get()
        creer_compte(nom_utilisateur, mot_de_passe, base_de_donnees_utilisateurs)
        print("Compte créé avec succès.")

    def authentifier_callback(self):
        nom_utilisateur = self.champ_utilisateur.get()
        mot_de_passe = self.champ_mot_de_passe.get()
        if authentifier(nom_utilisateur, mot_de_passe, base_de_donnees_utilisateurs):
            print("Authentification réussie.")
            # Ajoutez ici le code pour permettre à l'utilisateur d'accéder aux fonctionnalités après l'authentification
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")

# afficher
app = MyApp()
app.window.mainloop()