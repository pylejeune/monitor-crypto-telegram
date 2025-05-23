# USD0++/USD0 Monitor

Moniteur de ratio de prix entre les tokens USD0++ et USD0 avec notifications Telegram.

## Description

Ce projet surveille en temps réel le ratio de prix entre USD0++ (usd0-liquid-bond) et USD0 (usual-usd) via l'API CoinGecko et envoie des alertes Telegram lorsque le ratio dépasse les seuils configurés.

## Structure du projet

```
monitor/
├── monitor_usd0pp_usd0.py  # Script Python principal
├── Dockerfile              # Configuration Docker
├── start.sh               # Script de démarrage
└── README.md              # Documentation
```

## Fonctionnalités

- 📊 Surveillance continue du ratio USD0++/USD0
- 🚨 Alertes automatiques via Telegram
- ⚙️ Configuration flexible via variables d'environnement
- 🐳 Déploiement Docker (compatible ARM/Raspberry Pi)
- 🔄 Polling configurable

## Configuration

### Variables d'environnement requises

| Variable | Description | Exemple |
|----------|-------------|---------|
| `TELEGRAM_BOT_TOKEN` | Token du bot Telegram | `1234567890:ABC...` |
| `TELEGRAM_CHAT_ID` | ID du chat Telegram | `-1001234567890` |
| `UPPER_THRESHOLD` | Seuil supérieur du ratio | `1.09` |
| `LOWER_THRESHOLD` | Seuil inférieur du ratio | `0.9` |
| `POLL_INTERVAL` | Intervalle de vérification (secondes) | `30` |

### Configuration du bot Telegram

1. Créer un bot via [@BotFather](https://t.me/botfather)
2. Récupérer le token du bot
3. Ajouter le bot à votre chat/groupe
4. Récupérer l'ID du chat (utilisez [@userinfobot](https://t.me/userinfobot))

## Installation et démarrage

### Méthode 1: Docker (recommandée)

1. **Configurer les variables d'environnement** dans votre shell :
   ```bash
   export TELEGRAM_BOT_TOKEN="votre_token_bot"
   export TELEGRAM_CHAT_ID="votre_chat_id"
   ```

2. **Lancer le conteneur** :
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

### Méthode 2: Exécution directe

1. **Installer les dépendances** :
   ```bash
   pip install requests
   ```

2. **Configurer les variables d'environnement** :
   ```bash
   export TELEGRAM_BOT_TOKEN="votre_token_bot"
   export TELEGRAM_CHAT_ID="votre_chat_id"
   export UPPER_THRESHOLD="1.09"
   export LOWER_THRESHOLD="0.9"
   export POLL_INTERVAL="30"
   ```

3. **Lancer le script** :
   ```bash
   python monitor_usd0pp_usd0.py
   ```

## Fonctionnement

Le script effectue les actions suivantes :

1. **Récupération des prix** via l'API CoinGecko pour :
   - USD0++ (usd0-liquid-bond)
   - USD0 (usual-usd)

2. **Calcul du ratio** : USD0++ / USD0

3. **Vérification des seuils** :
   - Alerte si ratio > seuil supérieur
   - Alerte si ratio < seuil inférieur

4. **Notification Telegram** en cas de dépassement de seuil

## Messages d'alerte

Le bot enverra un message similaire à :
```
🚨 Alerte! 🚨
Le ratio USD0++/USD0 a dépassé le seuil.
Ratio actuel: 1.1500
Seuil: inferieur a 0.9 ou supérieur a 1.09
```

## Gestion Docker

### Voir les logs
```bash
docker logs -f <container_id>
```

### Arrêter le conteneur
```bash
docker stop <container_id>
```

### Reconstruire l'image
```bash
docker build -t usd0pp-monitor .
```

## Dépendances

- Python 3.11+
- requests
- Docker (optionnel)

## Support

Ce projet est compatible avec :
- Architecture x86_64
- Architecture ARM (Raspberry Pi)
- Systèmes Unix/Linux
- Docker

## Notes techniques

- L'API CoinGecko a des limites de taux (rate limiting)
- Le script gère automatiquement les erreurs de réseau
- Polling minimum recommandé : 30 secondes
- Format Markdown supporté dans les messages Telegram
