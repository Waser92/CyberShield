import bcrypt
import json
import base64

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Convertir les bytes en une représentation JSON compatible
    salt_str = base64.b64encode(salt).decode('utf-8')
    hashed_password_str = hashed_password.decode('utf-8')

    return {'salt': salt_str, 'hashed_password': hashed_password_str}

def save_password(username, password):
    try:
        with open('accounts.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # Vérifiez si le nom d'utilisateur est déjà pris
    for account in data:
        if account['username'] == username:
            return True  # Nom d'utilisateur déjà pris

    # Ajoutez le nouvel utilisateur à la liste des comptes avec le mot de passe hashé
    hashed_password = hash_password(password)
    data.append({'username': username, 'password': hashed_password})

    # Enregistrez la liste mise à jour dans le fichier avec un encodeur personnalisé
    with open('accounts.json', 'w') as file:
        json.dump(data, file, default=lambda x: x.__dict__)

    return False  # Pas d'erreur, le compte est ajouté avec succès

def check_credentials(username, password):
    try:
        with open('accounts.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                stored_username = entry['username']
                stored_password = entry['password']
                if username == stored_username and verify_password(password, stored_password):
                    return True
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    return False


def verify_password(input_password, stored_password):
    stored_salt = base64.b64decode(stored_password['salt'])
    stored_hashed_password = stored_password['hashed_password']

    # Hasher le mot de passe d'entrée avec le sel stocké
    hashed_input_password = bcrypt.hashpw(input_password.encode('utf-8'), stored_salt)

    # Comparer le mot de passe hashé avec le mot de passe hashé stocké
    return hashed_input_password == stored_hashed_password