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
        site_key = data.get('entry_site')

        # Vérifier si 'site' est présent dans les données
        if site_key is not None:
            # Ajouter ou mettre à jour les données pour le site spécifié
            existing_data[site_key] = {
                "site": data.get("entry_site"),
                "email": data.get("entry_email"),
                "identifiant": data.get("entry_identifiant"),
                "mot_de_passe": data.get("entry_password")
            }
        else:
            pass

        # Écrire les données dans le fichier
        with open(self.user_data_filename, 'w') as file:
           json.dump(existing_data, file, indent=4)

    def load_user_data(self):
        # Charger les données existantes (si le fichier existe)
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                user_data = json.load(file)

            # Triez les données par le site
            sorted_data = sorted(user_data.items(), key=lambda x: x[0])

            return [data[1] for data in sorted_data]
        else:
            return []
        
    def get_user_data_by_site(self, site):
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                user_data = json.load(file)
            return user_data.get(site, {})
        else:
            return {}