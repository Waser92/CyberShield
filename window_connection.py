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
        label_subtitle = Label(self.frame, text="Connectez vous avec votre nom d'utilisateur et votre mot de passe.", font=("Courrier", 25), bg='#800080',
                               fg='white')
        label_subtitle.pack()

    def entry_field(self):
        # Ajout des champs de saisie (Entry) pour le nom d'utilisateur et le mot de passe
        entry_nom_utilisateur = Entry(self.frame, textvariable=self.nom_utilisateur_var, font=("Courrier", 15))
        entry_mot_de_passe = Entry(self.frame, textvariable=self.mot_de_passe_var, font=("Courrier", 15), show='*')

        # Ajout des champs de saisie à la fenêtre
        entry_nom_utilisateur.pack(pady=10)
        entry_mot_de_passe.pack(pady=10)

        # ...

        # Ajout du bouton "Valider" avec la fonction associée
        bouton_valider = ttk.Button(self.frame, text="Valider", command=self.valider_callback)
        bouton_valider.pack(pady=10)



    def create_buttons(self):
        bouton_creer_compte = ttk.Button(self.frame, text="Valider", command=self.valider_callback)
        bouton_creer_compte.pack(pady=10)


    def authentifier_callback(self):
        nom_utilisateur = self.champ_utilisateur.get()
        mot_de_passe = self.champ_mot_de_passe.get()
        if authentifier(nom_utilisateur, mot_de_passe, base_de_donnees_utilisateurs):
            print("Authentification réussie.")
        # Add code here to allow the user to access features after authentication
        else:
            print("Nom d'utilisateur ou mot de passe incorrect.")
    
    def valider_callback(self):
        # Récupération des valeurs des champs de saisie
        nom_utilisateur = self.nom_utilisateur_var.get()
        mot_de_passe = self.mot_de_passe_var.get()


# Display
app = MyApp()
app.window.mainloop()
