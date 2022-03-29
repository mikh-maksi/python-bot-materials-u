from telegram.ext import Updater, MessageHandler, Filters,CommandHandler

def echo(update, context):
    string_in = update.message.text

    if string_in == 'Hello':
        string_out = "How are you?"
    elif string_in == 'Hi':
        string_out = "Glad to see you"
    elif string_in == '/start':
        string_out = "This is bot"
    else:
        string_out = string_in

    update.message.reply_text(string_out)

def start(update, context):
    string_in = update.message.text
    string_out = "This is bot!"
    update.message.reply_text(string_out)


updater = Updater("")

dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
