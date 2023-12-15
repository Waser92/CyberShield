import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string
import subprocess
from Classes import MyWindow_base
from Gestion_mdp import PasswordManager

class MyWindow_Main(MyWindow_base):
    
    def __init__(self):
        # Appeler le constructeur de la classe parente
        super().__init__()

        # Création des composants
        self.create_widgets()
        self.liste_identifiants = []
        self.liste_mots_de_passe = []
        
        self.maj_liste()

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_listbox()
        self.create_buttons()
        
    
    def create_title(self):
        label_title = tk.Label(self.frame_top, text="\n Gestionnaire de Mots de passe ", font=("Courrier", 40), bg='#030720', fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = tk.Label(self.frame_top, text="Connectez vous avec votre nom d'utilisateur \n et votre mot de passe.", font=("Courrier", 25), bg='#030720', fg='white')
        label_subtitle.pack()

    def create_buttons(self):
        # Bouton Déconnecter
        bouton_deconnecter = tk.Button(self.frame_top, text="Déconnecter", command=self.deconnection)
        bouton_deconnecter.pack(pady=10, ipadx=10, ipady=10)

        # Bouton Ajouter
        self.bouton_ajouter = tk.Button(self.frame_bottom, text="Ajouter", command=self.ajouter_mot_de_passe)
        self.bouton_ajouter.pack(pady=10, ipadx=20, ipady=10)

        # Bouton Modifier
        self.bouton_modifier = tk.Button(self.frame_bottom, text="Modifier", command=self.modifier_mot_de_passe)
        self.bouton_modifier.pack(pady=10, ipadx=20, ipady=10)
        self.bouton_modifier.config(state=tk.DISABLED)  # Désactive le bouton au démarrage

        # Bouton Supprimer
        self.bouton_supprimer = tk.Button(self.frame_bottom, text="Supprimer", command=self.supprimer_mot_de_passe)
        self.bouton_supprimer.pack(pady=10, ipadx=20, ipady=10)
        self.bouton_supprimer.config(state=tk.DISABLED)  # Désactive le bouton au démarrage
        
    def create_listbox(self):
        #Listbox pour afficher les mots de passe
        self.listbox = tk.Listbox(self.frame_center, selectmode=tk.SINGLE, font=("Arial", 12, "bold"))
        self.listbox.pack(pady=20)


    def ajouter_mot_de_passe(self):
        # Fenêtre pour saisir les informations du mot de passe
        nouvelle_fenetre = tk.Toplevel(self.frame_center)
        nouvelle_fenetre.title("Ajouter/Modifier un Mot de Passe")

        # Site
        self.entry_site = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        self.entry_site.insert(0, "Site: ")
        self.entry_site.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_site.grid(row=0, column=1, padx=10, pady=5)
        self.entry_site.bind("<FocusIn>", lambda event, widget=self.entry_site: self.clear_entry(event, widget))
        self.entry_site.bind("<FocusOut>", lambda event, widget=self.entry_site: self.restore_default_text(event, widget))

        # Email
        self.entry_email = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)
        self.entry_email.insert(0, "Email: ")
        self.entry_email.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_email.bind("<FocusIn>", lambda event, widget=self.entry_email: self.clear_entry(event, widget))
        self.entry_email.bind("<FocusOut>", lambda event, widget=self.entry_email: self.restore_default_text(event, widget))

        # Identifiant
        self.entry_identifiant = tk.Entry(nouvelle_fenetre, font=("Arial", 12, "bold"))
        self.entry_identifiant.grid(row=2, column=1, padx=10, pady=5)
        self.entry_identifiant.insert(0, "Identifiant")
        self.entry_identifiant.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_identifiant.bind("<FocusIn>", lambda event, widget=self.entry_identifiant: self.clear_entry(event, widget))
        self.entry_identifiant.bind("<FocusOut>", lambda event, widget=self.entry_identifiant: self.restore_default_text(event, widget))

        # Mot de passe
        self.entry_mot_de_passe = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        self.entry_mot_de_passe.grid(row=3, column=1, padx=10, pady=5)
        self.entry_mot_de_passe.insert(0, "Mot de passe")
        self.entry_mot_de_passe.config(fg='grey')  # Couleur gris clair par défaut
        self.entry_mot_de_passe.bind("<FocusIn>", lambda event, widget=self.entry_mot_de_passe: self.clear_entry(event, widget))
        self.entry_mot_de_passe.bind("<FocusOut>", lambda event, widget=self.entry_mot_de_passe: self.restore_default_text(event, widget))

        bouton_valider = tk.Button(nouvelle_fenetre, text="Valider", command=lambda: self.valider_mot_de_passe(
            self.entry_site.get(), self.entry_email.get(), self.entry_identifiant.get(), self.entry_mot_de_passe.get(), nouvelle_fenetre))
        bouton_valider.grid(row=4, column=0, columnspan=2, pady=10)

    def deconnection(self):
        self.open_Entry_window()

    def restore_default_text(self, event, widget):
        initial_text = "Site: " if widget == self.entry_site else "Email: " if widget == self.entry_email else "Identifiant" if widget == self.entry_identifiant else "Mot de passe"

        if not widget.get():
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair

    def valider_mot_de_passe(self, site, email, identifiant, mot_de_passe, fenetre):
        if site and identifiant and mot_de_passe:
            if identifiant in self.liste_identifiants:
                index = self.liste_identifiants.index(identifiant)
                self.liste_mots_de_passe[index] = f"Site: {site}, Email: {email}, Mot de Passe: {mot_de_passe}"
            else:
                self.liste_identifiants.append(identifiant)
                self.liste_mots_de_passe.append(f"Site: {site}, Email: {email}, Mot de Passe: {mot_de_passe}")

            self.password_manager.save_password(identifiant, mot_de_passe)
            self.maj_liste()
            fenetre.destroy()
            
            messagebox.showinfo("Succès", "Mot de passe ajouté/modifié avec succès.")
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs obligatoires.")

    def maj_liste(self):
        # Efface la liste actuelle
        self.listbox.delete(0, tk.END)

        # Ajoute les éléments mis à jour
        for i, identifiant in enumerate(self.liste_identifiants):
            self.listbox.insert(tk.END, f"Site {self.extraire_info('Site', self.liste_mots_de_passe[i])}")
            self.listbox.insert(tk.END, f"     Identifiant: {identifiant}")
            self.listbox.insert(tk.END, f"     Email: {self.extraire_info('Email', self.liste_mots_de_passe[i])}")
            self.listbox.insert(tk.END, f"     Mot de passe: {self.extraire_info('Mot de Passe', self.liste_mots_de_passe[i])}")
            self.listbox.insert(tk.END, "")  # Ajoute une ligne vide pour séparer les entrées

        # Active le bouton "Modifier" et "Supprimer" lorsque la liste n'est pas vide
        if self.liste_identifiants:
            self.bouton_modifier.config(state=tk.NORMAL)
            self.bouton_supprimer.config(state=tk.NORMAL)
        else:
            self.bouton_modifier.config(state=tk.DISABLED)
            self.bouton_supprimer.config(state=tk.DISABLED)

    def modifier_mot_de_passe(self):
        # Récupère l'identifiant sélectionné dans la liste
        index_selection = self.listbox.curselection()
        if index_selection:
            identifiant_selectionne = self.liste_identifiants[index_selection[0]]

            # Récupère les informations associées à l'identifiant
            index_info = self.liste_identifiants.index(identifiant_selectionne)
            infos = self.liste_mots_de_passe[index_info]

            # Affiche la fenêtre d'ajout avec les informations pré-remplies
            self.ajouter_mot_de_passe()
            entry_site, entry_email, entry_identifiant, entry_mot_de_passe = [widget for widget in self.fenetre_principale.winfo_children() if isinstance(widget, tk.Entry)]

            # Pré-remplit les champs avec les informations existantes
            entry_site.insert(0, self.extraire_info("Site", infos))
            entry_email.insert(0, self.extraire_info("Email", infos))
            entry_identifiant.insert(0, identifiant_selectionne)  # Utilise l'identifiant existant
            entry_mot_de_passe.insert(0, self.extraire_info("Mot de Passe", infos))

    def extraire_info(self, champ, infos):
        debut_champ = infos.find(f"{champ}: ") + len(f"{champ}: ")
        fin_champ = infos.find(",", debut_champ) if champ != "Mot de Passe" else len(infos)
        return infos[debut_champ:fin_champ]

    def supprimer_mot_de_passe(self):
        # Récupère l'identifiant sélectionné dans la liste
        index_selection = self.listbox.curselection()
        if index_selection:
            identifiant_selectionne = self.liste_identifiants[index_selection[0]]

            # Supprime l'identifiant et les informations associées de la liste
            index_info = self.liste_identifiants.index(identifiant_selectionne)
            del self.liste_identifiants[index_info]
            del self.liste_mots_de_passe[index_info]

            # Met à jour la liste affichée dans la fenêtre principale
            self.maj_liste()

            messagebox.showinfo("Succès", "Mot de passe supprimé avec succès.")
        # Méthode pour effacer le texte initial lors du clic dans le champ de saisie

    
    def clear_entry(self, event, widget):
        initial_text = "Site: " if widget == self.entry_site else "Email: " if widget == self.entry_email else "Identifiant" if widget == self.entry_identifiant else "Mot de passe"

        if widget.get() == initial_text:
            widget.delete(0, "end")
            widget.config(fg='black')  # Changer la couleur du texte en noir

    def restore_default_text(self, event, widget):
        initial_text = "Site: " if widget == self.entry_site else "Email: " if widget == self.entry_email else "Identifiant" if widget == self.entry_identifiant else "Mot de passe"

        if not widget.get():
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair

        if not widget.get():
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair

# Display
app = MyWindow_Main()
app.window.mainloop()