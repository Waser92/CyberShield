import json
import bcrypt

class PasswordManager:
    def __init__(self, file_path='data.json'):
        self.file_path = file_path

    def hash_password(self, password):
        # Génère un sel aléatoire
        salt = bcrypt.gensalt()

        # Hache le mot de passe avec le sel
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        return hashed_password

    def save_password(self, username, password):
        # Hache le mot de passe
        hashed_password = self.hash_password(password)

        # Enregistre le nom d'utilisateur et le mot de passe haché dans un fichier
        with open(self.file_path, 'a') as file:
            data = {'username': username, 'hashed_password': hashed_password.decode('utf-8')}
            json.dump(data, file)
            file.write('\n')  # Ajoute une nouvelle ligne pour chaque enregistrement

    def check_password(self, username, password):
        # Charge les données depuis le fichier
        with open(self.file_path, 'r') as file:
            for line in file:
                data = json.loads(line.strip())

                # Vérifie si le nom d'utilisateur correspond
                if data['username'] == username:
                    # Vérifie si le mot de passe correspond
                    if bcrypt.checkpw(password.encode('utf-8'), data['hashed_password'].encode('utf-8')):
                        return True

        return False

    def get_saved_passwords(self):
        # Charge tous les mots de passe enregistrés depuis le fichier
        passwords = []
        with open(self.file_path, 'r') as file:
            for line in file:
                data = json.loads(line.strip())
                passwords.append(data)
        return passwords
