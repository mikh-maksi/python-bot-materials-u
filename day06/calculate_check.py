from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

account = 0

check_strings = ["Your input is correct","Your input is empty","First symbol of your input is not slash.","Your input does not contain spaces","Parameter of command is not digit"]

def check(string_in):
    n=0
    elements = string_in.split(' ')

    if not len(string_in) > 0:
        n=1
    elif not string_in[0]=='/':
        n=2
    elif not ' ' in string_in:
        n=3
    elif not elements[1].isdigit():
        n=4
    return n


def costs(update, context):
    global account
    string_in = update.message.text
    if not check(string_in):
        elements = string_in.split(' ')
        account = account - int(elements[1])
        string_out = str(account)
    else:
        string_out = check_strings[check(string_in)]
    update.message.reply_text(string_out)

def income(update, context):
    global account
    string_in = update.message.text
    elements = string_in.split(' ')
    account = account + int(elements[1])
    string_out = str(account)
    update.message.reply_text(string_out)

def echo(update, context):
    string_in = update.message.text

    if string_in == '/start':
        string_out = 'Hello! This is own finances bot!'
    else:
        string_out = string_in

    update.message.reply_text(string_out)

updater = Updater("2034824924:AAFc0q0PYPezeZ6G5kE10uBWhWSurKks-8A")

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('costs', costs))
dispatcher.add_handler(CommandHandler('income', income))
dispatcher.add_handler(MessageHandler(Filters.all, echo))


updater.start_polling()
updater.idle()