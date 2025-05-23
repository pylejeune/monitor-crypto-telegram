import os
import time
import requests

# Configuration
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
TOKEN_IDS = {
    "usd0pp": "usd0-liquid-bond",  # Slug CoinGecko USD0++
    "usd0": "usual-usd"                 # Slug CoinGecko USD0
}
VS_CURRENCY = "usd"

# Récupère l'intervalle et le seuil depuis les variables d'environnement
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", 60))  # en secondes
UPPER_THRESHOLD = float(os.getenv("UPPER_THRESHOLD", 1.09))  # ratio
LOWER_THRESHOLD = float(os.getenv("LOWER_THERSHOLD", 0.90))

# Configuration Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

def fetch_prices():
    ids = ",".join(TOKEN_IDS.values())
    params = {"ids": ids, "vs_currencies": VS_CURRENCY}
    response = requests.get(COINGECKO_API_URL, params=params)
    response.raise_for_status()
    return response.json()

def compute_ratio(prices):
    price_pp = prices[TOKEN_IDS["usd0pp"]][VS_CURRENCY]
    price_0 = prices[TOKEN_IDS["usd0"]][VS_CURRENCY]
    return price_pp / price_0

def send_telegram_message(text):
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(TELEGRAM_API_URL, data=payload)
    print(response.json())
    response.raise_for_status()

def main():
    print("📈 Démarrage de la surveillance du ratio USD0++/USD0...")
    send_telegram_message("✅ Le script de surveillance USD0++/USD0 a démarré.")

    while True:
        try:
            prices = fetch_prices()
            ratio = compute_ratio(prices)
            #print(f"🔍 Vérification en cours... Ratio actuel USD0++/USD0 : {ratio:.4f}")
            #send_telegram_message(f"🔍 Vérification en cours... Ratio actuel USD0++/USD0 : {ratio:.4f}")

            if ratio > UPPER_THRESHOLD or ratio < LOWER_THRESHOLD:
                message = (
                    f"🚨 *Alerte!* 🚨\n"
                    f"Le ratio USD0++/USD0 a dépassé le seuil.\n"
                    f"*Ratio actuel:* {ratio:.4f}\n"
                    f"*Seuil:* inferieur a {LOWER_THRESHOLD} ou supérieur a {UPPER_THRESHOLD}"
                )
                send_telegram_message(message)
        except Exception as e:
            print(f"❌ Erreur: {e}")
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
