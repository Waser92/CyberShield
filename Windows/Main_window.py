import tkinter as tk
from tkinter import simpledialog, messagebox

class GestionnaireMotsDePasse:
    def __init__(self, fenetre_principale):
        self.fenetre_principale = fenetre_principale
        self.fenetre_principale.title("Gestionnaire de Mots de Passe")

        self.liste_identifiants = []
        self.liste_mots_de_passe = []

        self.listbox = tk.Listbox(self.fenetre_principale, selectmode=tk.SINGLE, font=("Arial", 12, "bold"))
        self.listbox.pack(pady=10)

        self.bouton_ajouter = tk.Button(self.fenetre_principale, text="Ajouter", command=self.ajouter_mot_de_passe)
        self.bouton_ajouter.pack(pady=5)

        self.bouton_modifier = tk.Button(self.fenetre_principale, text="Modifier", command=self.modifier_mot_de_passe)
        self.bouton_modifier.pack(pady=5)
        self.bouton_modifier.config(state=tk.DISABLED)  # Désactive le bouton au démarrage

        self.bouton_supprimer = tk.Button(self.fenetre_principale, text="Supprimer", command=self.supprimer_mot_de_passe)
        self.bouton_supprimer.pack(pady=5)
        self.bouton_supprimer.config(state=tk.DISABLED)  # Désactive le bouton au démarrage

        self.maj_liste()

    def ajouter_mot_de_passe(self):
        # Fenêtre pour saisir les informations du mot de passe
        nouvelle_fenetre = tk.Toplevel(self.fenetre_principale)
        nouvelle_fenetre.title("Ajouter/Modifier un Mot de Passe")

        label_site = tk.Label(nouvelle_fenetre, text="Site:", font=("Arial", 12))
        label_site.grid(row=0, column=0, padx=10, pady=5)
        entry_site = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        entry_site.grid(row=0, column=1, padx=10, pady=5)

        label_email = tk.Label(nouvelle_fenetre, text="Email:", font=("Arial", 12))
        label_email.grid(row=1, column=0, padx=10, pady=5)
        entry_email = tk.Entry(nouvelle_fenetre, font=("Arial", 12))
        entry_email.grid(row=1, column=1, padx=10, pady=5)

        label_identifiant = tk.Label(nouvelle_fenetre, text="Identifiant:", font=("Arial", 12))
        label_identifiant.grid(row=2, column=0, padx=10, pady=5)
        entry_identifiant = tk.Entry(nouvelle_fenetre, font=("Arial", 12, "bold"))
        entry_identifiant.grid(row=2, column=1, padx=10, pady=5)

        label_mot_de_passe = tk.Label(nouvelle_fenetre, text="Mot de Passe:", font=("Arial", 12))
        label_mot_de_passe.grid(row=3, column=0, padx=10, pady=5)
        entry_mot_de_passe = tk.Entry(nouvelle_fenetre, show="*", font=("Arial", 12))
        entry_mot_de_passe.grid(row=3, column=1, padx=10, pady=5)

        bouton_valider = tk.Button(nouvelle_fenetre, text="Valider", command=lambda: self.valider_mot_de_passe(
            entry_site.get(), entry_email.get(), entry_identifiant.get(), entry_mot_de_passe.get(), nouvelle_fenetre))
        bouton_valider.grid(row=4, column=0, columnspan=2, pady=10)

    def valider_mot_de_passe(self, site, email, identifiant, mot_de_passe, fenetre):
        if site and identifiant and mot_de_passe:
            # Ajoutez ou modifiez les informations du mot de passe à la liste
            if identifiant in self.liste_identifiants:
                index = self.liste_identifiants.index(identifiant)
                self.liste_mots_de_passe[index] = f"Site: {site}, Email: {email}, Mot de Passe: {mot_de_passe}"
            else:
                self.liste_identifiants.append(identifiant)
                self.liste_mots_de_passe.append(f"Site: {site}, Email: {email}, Mot de Passe: {mot_de_passe}")

            # Met à jour la liste affichée dans la fenêtre principale
            self.maj_liste()

            # Ferme la fenêtre de saisie
            fenetre.destroy()

            messagebox.showinfo("Succès", "Mot de passe ajouté/modifié avec succès.")
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs obligatoires.")

    def maj_liste(self):
        # Efface la liste actuelle
        self.listbox.delete(0, tk.END)

        # Ajoute les éléments mis à jour
        for i, identifiant in enumerate(self.liste_identifiants):
            self.listbox.insert(tk.END, f"Identifiant: {identifiant}")
            self.listbox.insert(tk.END, f"  {self.extraire_info('Site', self.liste_mots_de_passe[i])}")
            self.listbox.insert(tk.END, f"  {self.extraire_info('Email', self.liste_mots_de_passe[i])}")
            self.listbox.insert(tk.END, f"  {self.extraire_info('Mot de Passe', self.liste_mots_de_passe[i])}")
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

if __name__ == "__main__":
    fenetre = tk.Tk()
    gestionnaire = GestionnaireMotsDePasse(fenetre)
    fenetre.mainloop()
