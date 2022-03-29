from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def start(update, context):
    string_in = update.message.text

    string_out = 'Hello! This is own finances bot!'

    update.message.reply_text(string_out)

updater = Updater("2034824924:AAFc0q0PYPezeZ6G5kE10uBWhWSurKks-8A")

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))


updater.start_polling()
updater.idle()
