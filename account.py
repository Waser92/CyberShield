import bcrypt

base_de_donnees_utilisateurs = {}

def hacher_mot_de_passe(mot_de_passe):
    return bcrypt.hashpw(mot_de_passe.encode('utf-8'), bcrypt.gensalt())

def creer_compte(nom_utilisateur, mot_de_passe):
    mot_de_passe_hache = hacher_mot_de_passe(mot_de_passe)
    base_de_donnees_utilisateurs[nom_utilisateur] = mot_de_passe_hache

def authentifier(nom_utilisateur, mot_de_passe):
    mot_de_passe_stocke = base_de_donnees_utilisateurs.get(nom_utilisateur)
    if mot_de_passe_stocke:
        return bcrypt.checkpw(mot_de_passe.encode('utf-8'), mot_de_passe_stocke)
    return False