import bcrypt
import json

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def save_password(username, password):
    try:
        with open('accounts.json', 'r') as file:
            # Vérifiez si le fichier est vide
            data = file.read()
            if not data:
                data = []
            else:
                # Revenez au début du fichier car nous avons déjà lu son contenu
                file.seek(0)
                data = json.load(file)
    except FileNotFoundError:
        data = []

    # Vérifiez si le nom d'utilisateur est déjà pris
    for account in data:
        if account['username'] == username:
            return True  # Nom d'utilisateur déjà pris

    # Ajoutez le nouvel utilisateur à la liste des comptes
    data.append({'username': username, 'password': password})

    # Enregistrez la liste mise à jour dans le fichier
    with open('accounts.json', 'w') as file:
        json.dump(data, file)

    return False  # Pas d'erreur, le compte est ajouté avec succès

def check_credentials(username, password):
    Identification = False
    try:
        with open('Password.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                stored_username = entry['username']
                hashed_password = entry['password']
                if username == stored_username and verify_password(password, hashed_password):
                    Identification = True
                    break  # Arrête la boucle dès qu'une correspondance est trouvée
    except FileNotFoundError:
        Identification = False

    return Identification

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))