# The Driving School Project

Ce projet est un système de recensement des auto-écoles utilisant le framework Django. Il permet aux utilisateurs de s'inscrire à des créneaux horaires pour apprendre à conduire dans différentes auto-écoles. Le système gère également les différents types d'utilisateurs et leurs rôles spécifiques.

## Description
Le projet est composé de plusieurs entités principales :

<u>Auto-écoles</u> : Les établissements qui proposent des cours de conduite.
<u>Utilisateurs</u> : Les individus qui interagissent avec le système, y compris les manageurs, les apprenants élèves et les administrateurs.
<u>Événements</u> : Les créneaux horaires disponibles pour les cours de conduite.
Les utilisateurs sont classés en trois catégories :

<u>Manageurs</u> : Les propriétaires des auto-écoles qui sont responsables de la gestion des établissements et des événements.

<u>Apprenants élèves (non manageurs)</u> : Les utilisateurs qui souhaitent s'inscrire à des créneaux horaires pour apprendre à conduire.

<u>Administrateurs</u> : Les individus qui peuvent accéder à la partie admin du site pour superviser et gérer l'ensemble du système.

## Cahier des charges
Le projet doit répondre aux exigences suivantes :

- Permettre aux manageurs de créer, mettre à jour et supprimer des auto-écoles et des événements.
- Offrir aux apprenants élèves la possibilité de rechercher des auto-écoles et de s'inscrire à des créneaux horaires disponibles pour les cours de conduite.
- Donner aux administrateurs un accès complet à la partie admin du site pour gérer les utilisateurs, les auto-écoles et les événements.
- Gérer l'authentification et les autorisations pour chaque type d'utilisateur.
- Assurer la sécurité et la confidentialité des données utilisateur.

## Technologies utilisées
Langage de programmation : Python

Framework : Django

Base de données : SQLite (par défaut, peut être changé)

## Installation
Clonez le dépôt Git sur votre machine locale.

Installez les dépendances du projet en exécutant pip install -r requirements.txt.

Créez la base de données en lançant python manage.py migrate.

Lancez le serveur de développement avec python manage.py runserver.

Accédez à l'application via votre navigateur en naviguant vers http://localhost:XXXXX.

## Contribution

Si vous souhaitez contribuer au projet, veuillez soumettre une pull request avec vos modifications ou signaler des problèmes en ouvrant une issue sur GitHub.

## Identifiant : 

Utilisateur manageur de 9 auto-écoles = 
    
    Login : SchoolManager
    Password : root1234

Utilisation administrateur du site =
    
    Login : rootroot
    Password : root1234

Utilisateur apprenant = 
    
    Login : BaptisteG
    Password : root1234

## Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.
