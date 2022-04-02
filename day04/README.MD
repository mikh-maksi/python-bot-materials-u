# Функції
У бібліотеці для роботи з телеграмом, яку ми використовуємо, є можливість запускати функції, коли користувач використовує команди.

Програму, яка дозволяє створювати телеграм-бота, можна розділити на такі частини:
Імпорт елементів. У нашому прикладі ми імпортуємо з бібліотеки `telegram.ext` об'єкти `Updater, MessageHandler, Filters, CommandHandler`
```py
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
```
У наступній частині - ми пишемо функції, з якими працюватимемо. Наприклад, функція `start` - отримує два параметри. Якщо спрощено - `update` дозволяє отримувати повідомлення користувача та відповідати на них, а `context` - відправляти повідомлення незалежно від дій користувача (у цій реалізації функції `start` використовується тільки `context`)


```py
def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привіт! Це own finances bot!")
```
І остання частина - вона "оживляє" нашого бота:
`updater = Updater("")` - за допомогою об'єкта `Updater` наша програма підключається до бота.
`dispatcher = updater.dispatcher` - встановлюємо "диспетчера", який контролює те, що надсилає користувач
`dispatcher.add_handler(CommandHandler("start", start))` - додаємо до "диспетчера" "обробник" (handler), даний обробник є обробником команд (CommandHandler) і якщо користувач вводить команду start (`"start"` - перший параметр) запускає функцію 'start' (другий параметр).

Команди  
`updater.start_polling()`  
`updater.idle()`  
запускають работу бота

```py
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def start(update, context):
    chat = update.effective_chat
    string_out = "Привіт! Це own finances bot!"
    context.bot.send_message(chat_id=chat.id, text=string_out)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
```


```py
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привіт! Это own finances bot!")

def rule1(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="1. Рахуй дрібні витрати \n Невеликі витрати, які ти зазвичай не рахуєш, у результаті переростають у значну суму. Сьогодні 40 гривень на каву, завтра несподіваний хот-дог.")

def rule2(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="2. Став довгострокові фінансові цілі Наприклад, ти хочеш відкласти гроші на ноут або на відпустку — це і є ціль. Цілі потрібно знати, щоб тримати їх в умі та розуміти, заради чого ти сьогодні не витратиш 40 гривень на каву. Це психологія – відмовлятися від якихось витрат простіше, якщо ти знаєш, заради чого це робиш.")

def rule3(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="3. Прокачуйте влсані професійні навички \n Щоб заробляти більше.")

def rule4(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="4. Живи як інвестор Приймаючи рішення, оцінюй їх так, як інвестор оцінює бізнес, у який має намір інвестувати. Задавай собі запитання: а що я з цього матиму? Який результат я отримаю і коли? Як я зможу отримати ще найкращий результат? Ця вправа, яка допомагає прокачати особисту продуктивність, звільнити час від непотрібних занять і наповнити його корисними — і з погляду фінансів, і моральної задоволеності від результату.")


def costs(update, context):
    string = update.message.text
    elements = string.split(' ')
    
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])


def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater("")
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("rule1", rule1))
dispatcher.add_handler(CommandHandler("rule2", rule2))
dispatcher.add_handler(CommandHandler("rule3", rule3))
dispatcher.add_handler(CommandHandler("rule4", rule4))
dispatcher.add_handler(CommandHandler("eat", costs))
dispatcher.add_handler(MessageHandler(Filters.all, echo))

updater.start_polling()
updater.idle()

```