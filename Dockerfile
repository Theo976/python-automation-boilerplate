FROM python:3.9-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie et installe les dépendances (mise en cache Docker pour aller plus vite)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le reste du code
COPY . .

# On définit la variable pour que les logs s'affichent immédiatement
ENV PYTHONUNBUFFERED=1

# La commande qui lance le robot
CMD ["python", "src/main.py"]