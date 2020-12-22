# app-zvitae
Réalisation d'une application pour créer un cv en ligne.

1 - Init github app-curriculum-p13
`git clone https://github.com/BCouble/app_curriculum_p13.git`

2 - Création de l'environnement virtuel
`python -m venv venv`

3 - Installation de Django
`pip install django`

4 - Installation de psycorp2 pour postgresql
`pip install psycopg2`

5 - Création du projet
`django-admin startproject zvitae .`

6.1 - Configuration de la base de données dans le fichier setting
6.2 - Création du super utilisateur

7 - Création d'un dossier apps qui contiendra les application du projet

8 - Création de la première application 'core'
`python manage.py startapp core ./ayomi/apps/core`

9 - Création de la deuxième application 'register'
`python manage.py startapp register ./ayomi/apps/register`

10 - Mise à jour de 'DIRS' dans TEMAPLATE du fichier setting.py

11 - Import des fichiers statics dans l'application core

12 - Tests pour l'application regiter

13 - Fixe l'application register

14 - Création de la troisième application 'manage_zvitae'
`python manage.py startapp manage_zvitae ./ayomi/apps/manage_zvitae`

15 - Testspour l'application manage_zvitae

16 - Fixe l'application zvitae
