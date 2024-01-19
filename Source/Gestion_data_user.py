import json
import os

class GestionUserData:
    def __init__(self, username):
        self.username = username
        self.user_data_filename = f"{self.username}.json"

    def have_current_username(self):
        try:
            with open('current_user.json', 'r') as file:
                user_data = json.load(file)
                current_username = user_data[0].strip()
            return current_username
        except (FileNotFoundError, json.JSONDecodeError, IndexError):
            return None

    def save_user_data(self, data):
        # Charger les données existantes (si le fichier existe)
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = {}

        # Mettre à jour les données existantes avec les nouvelles données
        existing_data.update(data)

        # Écrire les données dans le fichier
        with open(self.user_data_filename, 'w') as file:
            json.dump(existing_data, file, indent=4)

    def load_user_data(self):
        # Charger les données existantes (si le fichier existe)
        if os.path.exists(self.user_data_filename):
            with open(self.user_data_filename, 'r') as file:
                user_data = json.load(file)
        else:
            user_data = {}

        return user_data