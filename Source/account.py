import bcrypt
import json

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def save_password(username, password):
    ValueError = False
    # Charger les données existantes (si le fichier existe)
    try:
        with open('Password.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Vérifier si le nom d'utilisateur est déjà utilisé
    for entry in data:
        stored_username = entry['username']
        if username == stored_username:
            ValueError = True
    if not ValueError:
        # Hacher le mot de passe
        hashed_password = hash_password(password)

        # Enregistrer le nom d'utilisateur et le mot de passe haché
        new_entry = {'username': username, 'password': hashed_password.decode('utf-8')}
        data.append(new_entry)

        # Écrire les données dans le fichier
        with open('Password.json', 'w') as file:
            json.dump(data, file)
    return ValueError

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