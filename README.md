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
6.2 - Init bdd : `python manage.py makemigrations` & `python manage.py migrate`
6.3 - Création du super utilisateur : zvitadmin & baptiste.couble@free.fr

7 - Création d'un dossier apps qui contiendra les application du projet

8.1 - Création du dossier "core" pour l'app
8.2 - Création de la première application 'core'
`python manage.py startapp core ./zvitae/apps/core`

9.1 - Configuration 'DIRS' dans TEMAPLATE du fichier setting.py
9.2 - Add app core in INSTALLED_APPS
9.3 - Create urls.py 

10.1 - Création du dossier "register" pour l'app
10.2 - Création de la deuxième application 'register'
`python manage.py startapp register ./zvitae/apps/register`

11 - Import des fichiers statics dans l'application core

12 - Tests pour l'application register

13 - Fixe l'application register

14.1 - Création du dossier zvitae
14.2 - Création de la troisième application 'manage_zvitae'
`python manage.py startapp manage_zvitae ./ayomi/apps/manage_zvitae`

15 - Testspour l'application manage_zvitae

16 - Fixe l'application zvitae
