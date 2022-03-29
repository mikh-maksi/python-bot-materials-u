# Введение параметров команды. Вычисление текущего значения счета
## Введение параметров команды.
Возникает вопрос - как передать боту числа? Ведь команды типа `/20` не доступны.  
Для передачи боту числовых значений можно использовать параметр команды: написать команду а после нее цифровое значение `/income 100`  
С точки зрения обработчика вводимой строки - у нас есть два значения, разделенных пробелом.  
Для получения таких значений используется метод `split` - он разделяет строку на части по выбранному разделителю и отправляет каждый элементик между разделителем в список.
Например, программа
```py
string_in = '/income 100'
elements = string_in.split(' ')
print(elements) # Выведет ['/income', '100']
print(elements[0]) # Выведет /income
print(elements[1]) # Выведет 100
```
**Список** - это специальная переменная, в которой может хранится несколько значений. К каждому значению можно получить доступ по номеру, при этом отсчет элементов начинается с нуля.

Мы видим, что с помощью метода `split` - можем получать значения параметров. В нашем случае - нам необходим второй элемент (с номером `1`).  
```py
string_in = '/income 100'
elements = string_in.split(' ')
print(elements[1]) # Выведет 100
```
Для того, чтобы накапливать значения дохода нам необходимо создать переменную, в которой будем зранить значение счета (`accaunt`) и при вводе строки с параметром - будем увеличивать ее на значение параметра.
```py
account = 0
string_in = '/income 100'
elements = string_in.split(' ')
account = account + elements[1]
```
Такая программа вызовет ошибку `TypeError: unsupported operand type(s) for +: 'int' and 'str'` потому, что результатом работы метода `split` будут строки, в то время, как у нас `account` - числовая переменная.
Для того, чтобы исправаить эту ошибку нам необходимо привест строковое значение к числовому, используя функцию `int`. Она получает строковое значение и возвращает числовое значение. `int('100')` вернет число

```py
account = 0
string_in = '/income 100'
elements = string_in.split(' ')
account = account + int(elements[1])
print(account) # Выведет 100
```

Но пользователь может добавлять не только доходы, но и расходы и наша программа будет отличать добавлять значение параметра или вычитать по имение команды:
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
К данному функционалу добавим обработку команды `total`, которая будет выводить итоговое значение счета.
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
##  Реализация в боте
При написании бота добавим обработчик команды `/income`, который будет запускать функцию `income`: `dispatcher.add_handler(CommandHandler('income', income))`. В функции `income` реалиpована функциональность:
*  `elements = string_in.split(' ')` разделения ввода на части по пробелу (`' '`) и 
*  `account = account + int(elements[1])` - добавлению значения к переменной `account`, которая хранит текущее состояние вашего счета
*  `string_out = str(account)` - перевод числовое значение переменной `account` в строковое для вывода пользователю.

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
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()
```
Добавим нашему боту обработчик для команды `/cost` с функционалом аналогичным обработчику команды `/income` с тем лишь отличием, что значение параметра при `/cost` будет уменьшать значение переменной `account`


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