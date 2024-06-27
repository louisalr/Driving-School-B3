# Utilisation de l'image de Selenium avec ChromeDriver
FROM selenium/standalone-chrome:latest

# Copier le fichier requirements.txt dans l'image
COPY requirements.txt /app/requirements.txt

# Installer des dépendances Python à partir de requirements.txt
RUN pip install -r /app/requirements.txt

# Copier les fichiers de votre application dans l'image
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Commande par défaut à exécuter lorsqu'un conteneur basé sur cette image est démarré
# Remplacer par la commande spécifique pour exécuter les tests Selenium
CMD ["python", "manage.py", "test", "home.tests_selenium"]