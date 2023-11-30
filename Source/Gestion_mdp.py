import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from account import authentifier

class GestionMotsDePasse:
    def __init__(self, fenetre_principale, nom_utilisateur):
        self.fenetre_gestion = tk.Toplevel(fenetre_principale)
        self.fenetre_gestion.title("Gestion des Mots de Passe")

        self.nom_utilisateur = nom_utilisateur
        self.mots_de_passe = {}

        self.etiquette_nom_utilisateur = ttk.Label(self.fenetre_gestion, text=f"Bonjour, {self.nom_utilisateur}!")
        self.etiquette_nom_utilisateur.grid(row=0, column=0, columnspan=2, pady=10)

        self.etiquette_site = ttk.Label(self.fenetre_gestion, text="Site Web:")
        self.etiquette_site.grid(row=1, column=0, padx=10, pady=10)

        self.champ_site = ttk.Entry(self.fenetre_gestion)
        self.champ_site.grid(row=1, column=1, padx=10, pady=10)

        self.etiquette_mot_de_passe = ttk.Label(self.fenetre_gestion, text="Mot de passe:")
        self.etiquette_mot_de_passe.grid(row=2, column=0, padx=10, pady=10)

        self.champ_mot_de_passe = ttk.Entry(self.fenetre_gestion, show="*")
        self.champ_mot_de_passe.grid(row=2, column=1, padx=10, pady=10)

        self.bouton_ajouter = ttk.Button(self.fenetre_gestion, text="Ajouter Mot de Passe", command=self.ajouter_mot_de_passe)
        self.bouton_ajouter.grid(row=3, column=0, columnspan=2, pady=10)

    def ajouter_mot_de_passe(self):
        site = self.champ_site.get()
        mot_de_passe = self.champ_mot_de_passe.get()

        if site and mot_de_passe:
            self.mots_de_passe[site] = mot_de_passe
            messagebox.showinfo("Succès", "Mot de passe ajouté avec succès!")
        else:
            messagebox.showwarning("Erreur", "Veuillez saisir le site et le mot de passe.")

