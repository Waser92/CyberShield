import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def save_password(username, password):
        ValueError = False
        # Charger les données existantes (si le fichier existe)
        try:
            with open('passwords.txt', 'r') as file:
                data = file.readlines()
        except FileNotFoundError:
            data = []

        # Vérifier si le nom d'utilisateur est déjà utilisé
        for line in data:
            stored_username, _ = line.strip().split(':')
            if username == stored_username:
                ValueError = True
        if ValueError == False:
            # Hacher le mot de passe
            hashed_password = hash_password(password)

            # Enregistrer le nom d'utilisateur et le mot de passe haché
            data.append(f"{username}:{hashed_password.decode('utf-8')}\n")

            # Écrire les données dans le fichier
            with open('passwords.txt', 'w') as file:
                file.writelines(data)
        return ValueError


def check_credentials(username, password):
    Identification = False
    try:
        with open('passwords.txt', 'r') as file:
            data = file.readlines()
            for line in data:
                stored_username, hashed_password = line.strip().split(':')
                if username == stored_username and verify_password(password, hashed_password):
                    Identification = True
                    break  # Arrête la boucle dès qu'une correspondance est trouvée
    except FileNotFoundError:
        Identification = False

    return Identification

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
