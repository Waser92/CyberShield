# Projet-2

BIENVENUE SUR CYBERSHIELD!

Cybershield est un gestionaire de mots de passe sécurisé, entièrement codé en language python.

Notre application vous propose d'enregistrer vos identifiants et mots de passe de manière sécurisée et localement.
Toutes vos informations sont cryptées (grace a la bibliothèque "bcrypt") c'est à dire que seul vous pouvez y avoir accès.
Si un pirate tente d'accèder à vos informations, il ne pourra pas décryptés vos informations de connexion.

UTILISATION:
Si vous n'avez pas le language python, vous pouvez l'installer gratuitement depuis le microsoft store.

1.Assurez vous d'avoir les extensions nécessaires au bon fonctionement de l'application.
     Veuillez suivre les instructions suivantes pour installer les extensions:
       -Dans la barre de recherche windows, écrivez "cmd" puis appuyez sur la touche "entrer"
       -L'invite de comandes windows va s'ouvrir, dans l'invite de comandes copiez les comandes suivantes corespondants à l'extension à installer.
         pour installer bcrypt:
            pip install bcrypt
        pour installer tkinter:
            pip install tk
        pour installer subprocess
            pip install subprocess

2.Pour lancer Cybershield, rendez vous dans le dossier Password manager et lancez Entry_window.py.
Pour le lancer depuis VsCode, assurez-vous d'avoir installer l'extension Python

Notre programme est constitué de fichiers en language python:

  -account.py  Ce fichier permet la sauvegarde des comptes du logiciel dans le fichier account.txt, il permet aussi la connection en vérifiant les identifiants.

  -Classes.py Ce fichier contient la structure principal de toutes les interfaces de nopte logiciel. Il contient donc des fonctions qui sont récurentes à tout nos fichiers.

  -Connection_window.py Ce fichier contient l'interface de connection, l'utilisateur qui a déjà un compte peut se connecter avec son nom d'utilisateur et son mot de passe. Ce fichier est intimement liés avec account.py

  -Create_account_window.py  Ce fichier contient l'interface de création de compte, l'utilisateur peut y créer un compte en remplissant un nom d'utilisateur et un mot de passe. Ce fichier est intimement liés avec account.py

  -Entry_window.py  Ce fichier contient l'interface d'entrée du logiciel. L'utilisateur peut choisir de creer un compte ou de se connecter.

  -Gestion_data_user.py Ce fichier permet la gestion des données utilisateur
  
  -Main_window.py Ce fichier contient l'interface principal du logiciel. Une fois connecté, l'utilisateur peux y acceder et enregistré ses mots de passe.=

Notre logiciel est également constitués de trois fichiers Data:

        - current_user.json Ce fichier stocke le nom d'utilisateur lorsqu'il est connecté, cela permet de stocker cette valeur pour être récupérés immediatement en cas de besoin.

        - account.txt  Ce fichier texte stocke les comptes des utilisateurs incluant le mot de passe et le nom d'utilisateur. Il permet donc la connection
        - User.json  Chaque utilisateur qui stocke ses données sur le logiciel a automatiquement un fichier commencant par son nom d'utilisateur. Il contient donc les informations et données de l'utilisateur en question.
