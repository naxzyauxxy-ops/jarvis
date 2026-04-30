import telebot
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramBridge:
    def __init__(self, orchestrator):
        self.bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
        self.orchestrator = orchestrator

        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            response = self.orchestrator.process_command(message.text)
            self.bot.reply_to(message, f"Home System: {response}")

    def start_polling(self):
        print("[+] Telegram Gateway Active.")
        self.bot.infinity_polling()
