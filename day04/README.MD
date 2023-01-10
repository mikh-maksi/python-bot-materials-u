# Функції
У бібліотеці для роботи з телеграмом, яку ми використовуємо, є можливість запускати функції, коли користувач використовує команди.

Програму, яка дозволяє створювати телеграм-бота, можна розділити на такі частини:
Імпорт елементів. У нашому прикладі ми імпортуємо з бібліотеки `telegram.ext` об'єкти `Application, MessageHandler,  CommandHandler, filters`
```py
from telegram.ext import Application, MessageHandler, CommandHandler, filters
```
У наступній частині - ми пишемо функції, з якими працюватимемо. Наприклад, функція `start` - отримує два параметри. Якщо спрощено - `update` дозволяє отримувати повідомлення користувача та відповідати на них, а `context` - відправляти повідомлення незалежно від дій користувача (у цій реалізації функції `start` використовується тільки `context`)


```py
async ef start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привіт! Це own finances bot!")
    await context.bot.send_message(chat_id=chat.id, text=string_out)
```

І остання частина - вона "оживляє" нашого бота:
`application = Application.builder().token("5722992818:AAGS0T-86JnKxqNJIqyebiHYPOzkWn5k5rM").build()` - за допомогою об'єкта `Application` наша програма створює об'єкт(`.builder()`), підключається до бота за токеном (`.token("")`), та робить білд (`.build()`)  
в результаті змінна `application` стає об'єктом ("додатком"), через який надалі можна задавати завдання боту.  
  

`application.add_handler(CommandHandler("start", start))` - додаємо до "додатка" "обробник" (handler), в даному випадку це обробник команд (`CommandHandler`) і, якщо користувач вводить команду start (`"start"` - перший параметр) запускає функцію `start` (другий параметр).

Команда  
`application.run_polling()`  
запускає работу бота

```py
from telegram.ext import Application, MessageHandler, CommandHandler, filters

async def start(update, context):
    chat = update.effective_chat
    string_out = "Привіт! Це own finances bot!"
    await context.bot.send_message(chat_id=chat.id, text=string_out)

application = Application.builder().token("5722992818:AAGS0T-86JnKxqNJIqyebiHYPOzkWn5k5rM").build()

application.add_handler(CommandHandler("start", start))

application.run_polling()
```


```py
from telegram.ext import Application, MessageHandler, filters, CommandHandler

async def start(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Привіт! Это own finances bot!")

async def rule1(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="1. Рахуй дрібні витрати \n Невеликі витрати, які ти зазвичай не рахуєш, у результаті переростають у значну суму. Сьогодні 40 гривень на каву, завтра несподіваний хот-дог.")

async def rule2(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="2. Став довгострокові фінансові цілі Наприклад, ти хочеш відкласти гроші на ноут або на відпустку — це і є ціль. Цілі потрібно знати, щоб тримати їх в умі та розуміти, заради чого ти сьогодні не витратиш 40 гривень на каву. Це психологія – відмовлятися від якихось витрат простіше, якщо ти знаєш, заради чого це робиш.")

async def rule3(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="3. Прокачуйте влсані професійні навички \n Щоб заробляти більше.")

async def rule4(update, context):
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="4. Живи як інвестор Приймаючи рішення, оцінюй їх так, як інвестор оцінює бізнес, у який має намір інвестувати. Задавай собі запитання: а що я з цього матиму? Який результат я отримаю і коли? Як я зможу отримати ще найкращий результат? Ця вправа, яка допомагає прокачати особисту продуктивність, звільнити час від непотрібних занять і наповнити його корисними — і з погляду фінансів, і моральної задоволеності від результату.")


async def costs(update, context):
    string = update.message.text
    elements = string.split(' ')
    
    chat = update.effective_chat
    await context.bot.send_message(chat_id=chat.id, text="Your cost is "+elements[1])


async def echo(update, context):
    await update.message.reply_text(update.message.text)

application = Application.builder().token("").build()


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("rule1", rule1))
application.add_handler(CommandHandler("rule2", rule2))
application.add_handler(CommandHandler("rule3", rule3))
application.add_handler(CommandHandler("rule4", rule4))
application.add_handler(CommandHandler("eat", costs))
application.add_handler(MessageHandler(filters.TEXT, echo))

application.run_polling()

```