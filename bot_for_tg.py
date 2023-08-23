import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = 'YOUR_BOT_TOKEN'
bot = telegram.Bot(token=token)

def start(update, context):
    update.message.reply_text('Привет! Это бот для рассылок в Telegram.')

def echo(update, context):
    message = update.message.text
    subscribers = get_subscribers()
    for subscriber in subscribers:
        bot.send_message(chat_id=subscriber, text=message)

def get_subscribers():
    subscribers = ['USER_CHAT_ID_1', 'USER_CHAT_ID_2']
    return subscribers

def main():
    updater = Updater(token=token, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

if __name__ == '__main__':
    main()