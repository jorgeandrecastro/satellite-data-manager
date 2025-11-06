# Étape 1 : Image de base légère
FROM python:3.11-slim

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Copier pyproject.toml pour installer les dépendances
COPY pyproject.toml ./

# Étape 4 : Installer les dépendances avec Poetry
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Étape 5 : Copier le code source
COPY src ./src
COPY data ./data

# Étape 6 : Commande de démarrage
CMD ["python", "src/main.py"]
