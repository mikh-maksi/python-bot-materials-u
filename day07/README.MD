# Додаткові можливості
## Телеграм бот для обліку фінансів
Ми з вами розібрались із тим, що можна створити бот, він буде отримувати команди із параметрами, та перевіряти те, що вводить користувач.  
  
Код бота (аналогічний попередньому завдання) приведений далі:

```py
from telegram.ext import Application, MessageHandler, filters, CommandHandler
account = 0
check_strings = ["Your input is correct","Your input is empty","First symbol of your input is not slash.","Your input does not contain spaces","Parameter of command is not digit"]


def check_sting_in(string_in):
    elements = string_in.split(' ')
    if not len(string_in) > 0:
        n=1
    elif not string_in[0]=='/':
        n=2
    elif not ' ' in string_in:
        n=3
    elif not elements[1].isdigit():
        n=4
    else:
        n=0
    return n

async def income(update, context):
    global account
    string_in = update.message.text
    elements = string_in.split(' ')
    account = account + int(elements[1])
    string_out = str(account)
    await update.message.reply_text(string_out)

async def cost(update, context):
    global account
    string_in = update.message.text
    elements = string_in.split(' ')
    account = account - int(elements[1])
    string_out = str(account)
    await update.message.reply_text(string_out)


async def echo(update, context):
    string_in = update.message.text
    if not(check_sting_in(string_in)):
        if string_in == '/start':
            string_out = 'Hello! This is own finances bot!'
        else:
            string_out = string_in
    else:
        string_out=check_strings[check_sting_in(string_in)]

    await update.message.reply_text(string_out)

application = Application.builder().token("").build()

application.add_handler(CommandHandler('income', income))
application.add_handler(CommandHandler('cost', cost))
application.add_handler(MessageHandler(filters.TEXT, echo))

application.run_polling()


```

## Додаткова функціональність бота
В майбутньому ви зможете розвинути бота та додати йому розширеної функціональності на курсі Python від GoITeens:

**Основні:**
* Кнопки
* Введення даних без команд
* Збереження даних у файл
**Додаткові:**
* Створення своїх категорій
* Загальні обчислення за наявними записами
* Словники