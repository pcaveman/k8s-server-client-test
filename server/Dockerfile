# Utiliser l'image de base Alpine
FROM alpine:latest

# Installer Python et pip
RUN apk add --no-cache python3 py3-pip

# Copier le script Python dans le conteneur
COPY server-python.py /my_script.py

COPY requirements.txt /requirements.txt

# Install the requirements
RUN pip3 install -r /requirements.txt

# Exécuter le script Python lors du démarrage du conteneur
CMD ["python3", "/my_script.py"]
