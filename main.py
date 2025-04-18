import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = os.environ.get("CHANNEL_USERNAME")

app = Flask(__name__)
bot = Bot(token=TOKEN)

@app.route("/")
def home():
    return "Bot is running!"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("أهلاً بيك! أرسل /send <رسالتك> للنشر بالقناة.")

def send(update: Update, context: CallbackContext):
    if context.args:
        msg = " ".join(context.args)
        bot.send_message(chat_id=CHANNEL, text=msg)
        update.message.reply_text("تم النشر!")
    else:
        update.message.reply_text("رجاءً أرسل رسالة بعد الأمر.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("send", send))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
