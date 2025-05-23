# Utilise une image Python 3.11 slim multi-arch (ARM compatible Raspberry Pi)
FROM python:3.11-slim

# Crée et définit le répertoire de travail
WORKDIR /app

# Copie le script Python externe dans le conteneur
COPY monitor_usd0pp_usd0.py /app/monitor_usd0pp_usd0.py

# Installe les dépendances
RUN pip install --no-cache-dir requests

# Variables d'environnement (surchargeables à l'exécution)
ENV TELEGRAM_BOT_TOKEN=""
ENV TELEGRAM_CHAT_ID=""
ENV PRICE_THRESHOLD="1.01"
ENV POLL_INTERVAL="60"

# Lancement du script
CMD ["python", "monitor_usd0pp_usd0.py"]
