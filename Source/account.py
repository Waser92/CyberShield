import bcrypt

def hash_password(password):
    # Générer un sel aléatoire
    salt = bcrypt.gensalt()
    
    # Hacher le mot de passe avec le sel
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password

def save_password(username, password):
    # Charger les données existantes (si le fichier existe)
    try:
        with open('passwords.txt', 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        data = []

    # Hacher le mot de passe
    hashed_password = hash_password(password)

    # Enregistrer le nom d'utilisateur et le mot de passe haché
    data.append(f"{username}:{hashed_password.decode('utf-8')}\n")

    # Écrire les données dans le fichier
    with open('passwords.txt', 'w') as file:
        file.writelines(data)

if __name__ == "__main__":
    # Exemple d'utilisation
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    # Enregistrer le mot de passe
    save_password(username, password)
    print("Mot de passe enregistré avec succès.")
