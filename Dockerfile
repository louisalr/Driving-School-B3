# Utilisation de l'image de Selenium avec ChromeDriver
FROM selenium/standalone-chrome:latest

WORKDIR /app

# Copie le fichier requirements.txt et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code de l'application dans le conteneur
COPY . .


# Commande par défaut à exécuter lorsqu'un conteneur basé sur cette image est démarré
# Remplacer par la commande spécifique pour exécuter les tests Selenium
CMD ["python", "manage.py", "test", "home.tests_selenium"]