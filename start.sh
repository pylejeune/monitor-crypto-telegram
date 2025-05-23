docker build -t usd0pp-monitor .
docker run -d \
  -e TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN \
  -e TELEGRAM_CHAT_ID=$TELEGRAM_CHAT_ID \
  -e UPPER_THRESHOLD=1.09 \
  -e LOWER_THRESHOLD=0.9 \
  -e POLL_INTERVAL=30 \
  usd0pp-monitor
