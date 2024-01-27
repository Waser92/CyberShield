import bcrypt

# Génération d'une "salt" fixe
SALT = bcrypt.gensalt()

def hash_password(password):
    # Utilise la fonction bcrypt pour hacher le mot de passe avec la "salt" fixe
    hashed = bcrypt.hashpw(password.encode('utf-8'), SALT)
    return hashed

def save_password(username, password):
    # Vérifie si le nom d'utilisateur est déjà pris
    with open('accounts.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, _ = line.strip().split(':')
            if stored_username == username:
                return True  # Nom d'utilisateur déjà pris

    # Hache le mot de passe avant de le stocker
    hashed_password = hash_password(password)

    # Ajoute le nouveau compte à la liste
    new_account = f"{username}:{hashed_password.decode('utf-8')}\n"
    
    with open('accounts.txt', 'a') as file:
        file.write(new_account)

    return False  # Compte ajouté avec succès

def check_credentials(username, password):
    # Recherche du compte correspondant aux identifiants fournis
    with open('accounts.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = line.strip().split(':')
            if stored_username == username:
                # Vérifie le mot de passe haché avec la "salt" fixe
                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    return True  # Identifiants valides
                else:
                    return False  # Mot de passe incorrect

    return False  # Aucun compte correspondant aux identifiants
