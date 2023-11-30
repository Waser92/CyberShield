# main.py
import bcrypt
import json

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def load_users(filename='users.json'):
    try:
        with open(filename, 'r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}
    return users

def save_users(users, filename='users.json'):
    with open(filename, 'w') as file:
        json.dump(users, file, indent=4)

if __name__ == "__main__":
    users = load_users()

    # Enregistrez un nouvel utilisateur (simulé)
    new_username = input("Entrez le nom d'utilisateur : ")
    new_password = input("Entrez le mot de passe : ")

    # Hacher le mot de passe avant de le stocker
    hashed_password = hash_password(new_password)

    # Ajouter le nouvel utilisateur à la liste
    users[new_username] = hashed_password

    # Enregistrez la liste mise à jour dans le fichier
    save_users(users)

    # Simuler la récupération du mot de passe depuis la base de données
    retrieved_hashed_password = users.get(new_username, '')

    # Vérifier le mot de passe lors de la connexion
    login_password = input("Entrez le mot de passe : ")

    # Comparer le mot de passe entré avec le hachage stocké
    if check_password(login_password, retrieved_hashed_password):
        print("Connexion réussie !")
    else:
        print("Mot de passe incorrect.")