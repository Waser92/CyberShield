import random
import string

def generer_mot_de_passe():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(12))
    return mot_de_passe

mot_de_passe_genere = generer_mot_de_passe()
print(mot_de_passe_genere)

generer_mot_de_passe()