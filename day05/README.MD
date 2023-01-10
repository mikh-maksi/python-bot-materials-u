# Введення параметрів команди. Обчислення поточного значення рахунку
## Введення параметрів команди.
Виникає питання – як передати боту числа? Адже команди типу `/20` недоступні.
Для передачі числових значень можна використовувати параметр команди: написати команду а після неї цифрове значення `/income 100`
З точки зору обробника рядка, що вводиться - у нас є два значення, розділених пробілом.
Для отримання таких значень використовується метод `split` - він розділяє рядок на частини по вибраному роздільнику та відправляє кожен елемент між роздільником у список.
Наприклад, програма
```py
string_in = '/income 100'
elements = string_in.split(' ')
print(elements) # Поверне ['/income', '100']
print(elements[0]) # Поверне /income
print(elements[1]) # Поверне 100
```
**Список** - це спеціальна змінна, де може зберігатися кілька значень. До кожного значення можна отримати доступ за номером, при цьому відлік елементів починається з нуля.

Ми, що за допомогою методу `split` - можемо отримувати значення параметрів. У нашому випадку нам необхідний другий елемент (з номером `1`).

```py
string_in = '/income 100'
elements = string_in.split(' ')
print(elements[1]) # Виведе 100
```
Для того, щоб накопичувати значення доходу, нам необхідно створити змінну, в якій будемо зберігати значення рахунку (`account`) і при введенні рядка з параметром - збільшуватимемо її на значення параметра.
```py
account = 0
string_in = '/income 100'
elements = string_in.split(' ')
account = account + elements[1]
```
Така програма викликає помилку `TypeError: unsupported operand type(s) for +: 'int' and 'str'` тому, що результатом роботи методу `split` будуть рядки, тоді як у нас `account` - числова змінна.
Для того, щоб виправити цю помилку, нам необхідно привести рядкове значення до числового, використовуючи функцію `int`. Вона отримує рядкове значення та повертає числове значення. Напривклад: функція `int('100')` поверне число


```py
account = 0
string_in = '/income 100'
elements = string_in.split(' ')
account = account + int(elements[1])
print(account) # виведе 100
```

Але користувач може додавати не тільки доходи, але й витрати і наша програма відрізнятиме додавати значення параметра або віднімати його відповідно до значення команди:

```py
account = 0
string_in = input('Please, enter command with parameter')

elements = string_in.split(' ')

if elements[0]=='/income': 
    account = account + int(elements[1])
    string_out = 'Your income is recived.'
if elements[0]=='/cost':
    account = account - int(elements[1])
    string_out = 'Your cost is recived'
```
До цього функціоналу додамо обробку команди `total`, яка виводитиме підсумкове значення рахунку.
```py
account = 0
string_in = input('Please, enter command with parameter')

elements = string_in.split(' ')

if elements[0]=='/income': 
    account = account + int(elements[1])
    string_out = 'Your income is recived.'
if elements[0]=='/cost':
    account = account - int(elements[1])
    string_out = 'Your cost is recived'
if elements[0]=='/total':
    string_out = account


```
## Реалізація в боті
При написанні бота додамо обробник команди `/income`, який запускатиме функцію `income`: `dispatcher.add_handler(CommandHandler('income', income))`. У функції `income` реалізована функціональність:
* `elements = string_in.split('')` розділення введення на частини за пробілом (`''`) і
* `account = account + int(elements[1])` - додавання значення до змінної `account`, яка зберігає поточний стан вашого рахунку
* `string_out = str(account)` - переклад числове значення змінної `account` у рядкове для виведення користувачеві.
```py
from telegram.ext import Application, MessageHandler, filters, CommandHandler
account = 0

async def income(update, context):
    global account
    string_in = update.message.text
    elements = string_in.split(' ')
    account = account + int(elements[1])
    string_out = str(account)
    await update.message.reply_text(string_out)

async def echo(update, context):
    string_in = update.message.text

    if string_in == '/start':
        string_out = 'Hello! This is own finances bot!'
    else:
        string_out = string_in

    await update.message.reply_text(string_out)

application = Application.builder().token("").build()

application.add_handler(CommandHandler('income', income))
application.add_handler(MessageHandler(filters.TEXT, echo))

```

Додамо нашому боту обробник для команди `/cost` з функціоналом аналогічним обробнику команди `/income` з тією лише відмінністю, що значення параметра при `/cost` буде зменшувати значення змінної `account`

```py
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
account = 0

def income(update, context):
    global account
    string_in = update.message.text
    elements = string_in.split(' ')
    account = account + int(elements[1])
    string_out = str(account)
    update.message.reply_text(string_out)

def cost(update, context):
    global account
    string_in = update.message.text
    elements = string_in.split(' ')
    account = account - int(elements[1])
    string_out = str(account)
    update.message.reply_text(string_out)


def echo(update, context):
    string_in = update.message.text

    if string_in == '/start':
        string_out = 'Hello! This is own finances bot!'
    else:
        string_out = string_in

    update.message.reply_text(string_out)

updater = Updater("")

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('income', income))
dispatcher.add_handler(CommandHandler('cost', cost))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
```
