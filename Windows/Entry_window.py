from tkinter import *
from tkinter import ttk
import subprocess
#030720

class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberShield")
        self.window.geometry("800x480")
        self.window.minsize(800, 360)
        self.window.iconbitmap("")
        self.window.config(background='#030720')

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

        bouton_creer_compte = ttk.Button(self.frame_center, text="Créer un compte", command=self.ouvrir_create_account)
        bouton_creer_compte.pack(pady=10)

        bouton_authentifier = ttk.Button(self.frame_bottom, text="S'authentifier", command=self.ouvrir_connection_window)
        bouton_authentifier.pack(pady=10)

    def ouvrir_create_account(self):
    # Appeler le script Create_account.py
        subprocess.run(["python", "C:/Users/thoma/Documents/Programme/Projets/Password_Manager/Windows/Create_account_window.py"])

    def ouvrir_connection_window(self):
    # Appeler le script Connection_window.py
        subprocess.run(["python", "C:/Users/thoma/Documents/Programme/Projets/Password_Manager/Windows/Connection_window.py"])
# Display
app = MyApp()
app.window.mainloop()
