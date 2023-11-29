from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
sys.path.append(r'C:\Password_Manager\Source')
class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberShield")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
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
        label_title = Label(self.frame_top, text="\n CyberShield\n ", font=("Courrier", 40), bg='#030720',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame_top, text="Voici vos mots de passe enregistrés", font=("Courrier", 25), bg='#030720',
                               fg='white')
        label_subtitle.pack()

    def create_buttons():
        generer_button = tk.Button(self.frame_center, text="Générer Mot de Passe", command=generer_et_afficher_mot_de_passe)
        copier_button = tk.Button(self.frame_center, text="Copier dans le Presse-Papier", command=copier_dans_presse_papier)

    def entry_mot_de_passe_généré():
        mot_de_passe_entry = tk.Entry(root, width=20, show='*')
    
    def generer_et_afficher_mot_de_passe():
        mot_de_passe_genere = generer_mot_de_passe()
        mot_de_passe_entry.delete(0, tk.END)
        mot_de_passe_entry.insert(0, mot_de_passe_genere)

    def copier_dans_presse_papier():
        mot_de_passe = mot_de_passe_entry.get()
        root.clipboard_clear()
        root.clipboard_append(mot_de_passe)
        root.update()
        messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papier.")



# Placement des widgets dans la fenêtre
generer_button.pack(pady=10)
mot_de_passe_entry.pack(pady=10)
copier_button.pack(pady=10)




# Display
app = MyApp()
app.window.mainloop()

def generer_et_afficher_mot_de_passe():
    mot_de_passe_genere = generer_mot_de_passe()
    mot_de_passe_entry.delete(0, tk.END)
    mot_de_passe_entry.insert(0, mot_de_passe_genere)

def copier_dans_presse_papier():
    mot_de_passe = mot_de_passe_entry.get()
    root.clipboard_clear()
    root.clipboard_append(mot_de_passe)
    root.update()
    messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papier.")


# Création des widgets
generer_button = tk.Button(root, text="Générer Mot de Passe", command=generer_et_afficher_mot_de_passe)
copier_button = tk.Button(root, text="Copier dans le Presse-Papier", command=copier_dans_presse_papier)
mot_de_passe_entry = tk.Entry(root, width=20, show='*')

# Placement des widgets dans la fenêtre
generer_button.pack(pady=10)
mot_de_passe_entry.pack(pady=10)
copier_button.pack(pady=10)
