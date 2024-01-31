from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import json
import os
from Gestion_data_user import GestionUserData

class ResearchWindow(GestionUserData):
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.username = self.have_current_username()

        # Appeler le constructeur de la classe parente avec le nom d'utilisateur actuel
        super().__init__(self.username)

        # Nouvelle instance de GestionUserData avec le nom d'utilisateur actuel
        self.user_data_manager = GestionUserData(self.username)

        # Créer la fenêtre de recherche
        self.create_search_window()

    def create_search_window(self):
        # Fenêtre pour rechercher une donnée déjà sauvegardée
        self.search_window = tk.Toplevel()
        self.search_window.title("Rechercher une donnée déjà sauvegardée")

        # Ajout du champ de saisie
        self.site_var = tk.StringVar()
        self.entry_site = Entry(self.search_window, textvariable=self.site_var, font=("Courier", 15))

        # Ajout du texte initial "Nom du Site recherché" en gris clair
        self.entry_site.insert(0, "Nom du Site")
        self.entry_site.config(fg='grey')  # Couleur gris clair par défaut

        # Ajout des gestionnaires d'événements de clic
        self.entry_site.bind("<FocusIn>", self.clear_entry)
        self.entry_site.bind("<FocusOut>", self.restore_default_text)

        self.entry_site.pack(pady=10)

        # Bouton Rechercher
        bouton_rechercher = tk.Button(self.search_window, text="Rechercher", command=self.rechercher_callback)
        bouton_rechercher.pack(pady=10)

        # # Bouton Supprimer
        # bouton_supprimer = tk.Button(self.search_window, text="Supprimer", command=self.supprimer_callback)
        # bouton_supprimer.pack(pady=10)

    # Méthode pour effacer le texte initial lors du clic dans le champ de saisie
    def clear_entry(self, event):
        widget = event.widget
        initial_text = "Nom du Site"

        if widget.get() == initial_text:
            widget.delete(0, "end")
            widget.config(fg='black')  # Changer la couleur du texte en noir

    # Méthode pour restaurer le texte initial si le champ de saisie est vide

    def restore_default_text(self, event):
        widget = event.widget
        initial_text = "Nom du Site"

        if not widget.get():
            widget.insert(0, initial_text)
            widget.config(fg='grey')  # Changer la couleur du texte en gris clair

    def rechercher_callback(self):
        site_recherche = self.entry_site.get()
        data = self.user_data_manager.get_user_data_by_site(site_recherche)

        if data:
            messagebox.showinfo("Résultat de la Recherche", f"Informations trouvées pour le site '{site_recherche}':\n"
                                                             f"Identifiant: {data.get('identifiant', 'N/A')}\n"
                                                             f"Email: {data.get('email', 'N/A')}\n"
                                                             f"Mot de passe: {data.get('mot_de_passe', 'N/A')}")
        else:
            messagebox.showinfo("Résultat de la Recherche", f"Aucune information trouvée pour le site '{site_recherche}'.")

    
    # Méthode pour supprimer les données liées au site
    def supprimer_callback(self):
        site_supprimer = self.entry_site.get()

        if site_supprimer:
            # Appeler la nouvelle méthode pour supprimer les données liées au site
            success = self.user_data_manager.delete_user_data_by_site(site_supprimer)

            if success:
                messagebox.showinfo("Suppression réussie", f"Données pour le site '{site_supprimer}' supprimées avec succès.")
            else:
                messagebox.showinfo("Aucune correspondance", f"Aucune information trouvée pour le site '{site_supprimer}'.")
        else:
            messagebox.showinfo("Entrée vide", "Veuillez entrer un nom de site pour supprimer les données correspondantes.")

    # Méthode pour récupérer le nom d'utilisateur actuel
    def have_current_username(self):
        try:
            with open('current_user.json', 'r') as file:
                user_data = json.load(file)
                current_username = user_data.get("username")
            return current_username
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return None

# Créer une instance de la classe principale
app = ResearchWindow()
app.search_window.mainloop()