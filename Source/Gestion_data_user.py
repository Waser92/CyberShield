import json
import os

class GestionUserData:
    def __init__(self, username):
        self.username = username
        self.user_data_filename = f"{self.username}.json"

    def save_user_data(self, data):
        # Charger les données existantes (si le fichier existe)
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Utiliser le site comme clé principale
        site_key = data.get('site', 'default_site_key')  # Utilisez une clé par défaut si 'site' n'est pas présent
        existing_data[site_key] = data

        # Écrire les données dans le fichier
        with open(self.user_data_filename, 'w') as file:
            json.dump(existing_data, file, indent=4)

    def get_all_user_data(self):
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                user_data = json.load(file)
            return list(user_data.values())
        else:
            return []
        
    def load_user_data(self):
        # Charger les données existantes (si le fichier existe)
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                user_data = json.load(file)

            # Triez les données par le site
            sorted_data = sorted(user_data.values(), key=lambda x: x.get('site', 'default_site_key'))

            return sorted_data
        else:
            return []