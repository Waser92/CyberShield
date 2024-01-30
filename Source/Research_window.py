from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, messagebox
import subprocess
import os
from Classes import MyWindow_base

class Research_window(MyWindow_base):
    def __init__(self, parent, user_data_manager):
        super().__init__(parent)
        self.user_data_manager = user_data_manager
        self.create_widgets()

    def create_widgets(self):
        self.create_title("Rechercher des Informations")
        self.create_subtitle("Entrez le site que vous souhaitez rechercher.")
        self.create_entry_field()
        self.create_buttons()

    def create_entry_field(self):
        self.entry_site = Entry(self.frame_center, textvariable=self.site_var, font=("Courier", 15))
        self.entry_site.pack(pady=10)

    def create_buttons(self):
        bouton_rechercher = ttk.Button(self.frame_center, text="Rechercher", command=self.rechercher_callback)
        bouton_rechercher.pack(pady=10)

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