- name: Run Bot Forever
  run: |
    while true; do
      echo "Starting Telegram Bot..."
      python main.py
      echo "Bot crashed or stopped. Restarting in 5 seconds..."
      sleep 5
    done
