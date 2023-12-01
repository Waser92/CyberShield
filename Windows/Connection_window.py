from tkinter import *
from tkinter import ttk
#030720

class MyApp:

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


        # Creation of components
        self.create_widgets()

        # Packaging
        self.frame_top.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_center.pack(side=TOP, fill=BOTH, expand=YES)
        self.frame_bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)


    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.entry_fields()
        self.create_buttons()

    def create_title(self):
        label_title = Label(self.frame_top, text="\n Gestionnaire de Mots de passe\n ", font=("Courrier", 40), bg='#030720',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame_top, text="Connectez vous avec votre nom d'utilisateur \n et votre mot de passe.", font=("Courrier", 25), bg='#030720',
                               fg='white')
        label_subtitle.pack()


    def entry_fields(self):
        # Ajout des champs de saisie (Entry) pour le nom d'utilisateur et le mot de passe
        self.entry_nom_utilisateur = Entry(self.frame_center, textvariable=self.nom_utilisateur_var, font=("Courrier", 15))
        self.entry_mot_de_passe = Entry(self.frame_center, textvariable=self.mot_de_passe_var, font=("Courrier", 15))

        # Ajout du texte initial "Nom d'utilisateur" en gris clair
        self.entry_nom_utilisateur.insert(0, "Nom d'utilisateur")
        self.entry_nom_utilisateur.config(fg='grey')  # Couleur gris clair par défaut

        # Ajout du texte initial "Créer un compte" en gris clair
        self.entry_mot_de_passe.insert(0, "Mot de passe")
        self.entry_mot_de_passe.config(fg='grey')  # Couleur gris clair par défaut

        # Ajout des gestionnaires d'événements de clic
        self.entry_nom_utilisateur.bind("<FocusIn>", self.clear_entry)
        self.entry_nom_utilisateur.bind("<FocusOut>", self.restore_default_text)

        self.entry_mot_de_passe.bind("<FocusIn>", self.clear_entry)
        self.entry_mot_de_passe.bind("<FocusOut>", self.restore_default_text)
        
        # Ajout des champs de saisie à la fenêtre
        self.entry_nom_utilisateur.pack(pady=10)
        self.entry_mot_de_passe.pack(pady=10)
        

    def create_buttons(self):
        
        # Ajustez le style des boutons pour augmenter la taille
        style = ttk.Style()
        style.configure("TButton", padding=(20, 10))

        bouton_valider = ttk.Button(self.frame_center, text="Valider", command=self.authentifier_callback)
        bouton_valider.pack(pady=10)


    def authentifier_callback(self):
        nom_utilisateur = self.entry_nom_utilisateur.get()
        mot_de_passe = self.entry_mot_de_passe.get()
        # Méthode pour effacer le texte initial lors du clic dans le champ de saisie
    
    # Méthode pour effacer le texte initial lors du clic dans le champ de saisie
    def clear_entry(self, event):
        widget = event.widget
        initial_text = "Nom d'utilisateur" if widget == self.entry_nom_utilisateur else "Mot de passe"

        if widget.get() == initial_text:
            widget.delete(0, "end")
            widget.config(fg='black')  # Changer la couleur du texte en noir

    # Méthode pour restaurer le texte initial si le champ de saisie est vide
    def restore_default_text(self, event):
        widget = event.widget
        initial_text = "Nom d'utilisateur" if widget == self.entry_nom_utilisateur else "Mot de passe"

        if not widget.get():
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair
# Display
app = MyApp()
app.window.mainloop()
