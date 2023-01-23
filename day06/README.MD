# Параметри. Опції. Перевірка.
# Перевірка
Минулого дня ми познайомилися з тим, як переводити рядок у команди. Для цього ми використовуємо метод `split`, який використовуємо з рядком, який отримуємо від користувача.
   
  
Користувачі можуть вводити різну інформацію. Така інформація не завжди буде відповідати тому шаблону, який ми спочатку задали (користувач може неправильно вказати команду, не вказати параметр як число або не вказати коментар тощо).
У нашому боті будемо перевіряти те, чи ввів користувач потрібну інформацію.
Наприклад - перевіримо, чи є другим елементом числом.  
```py
string_in="/eat 10 bread"
elements = string_in.split(" ")
if elements[1].isdigit():
    string_out = "It is ok"
else:
    string_out = "Second parameter must be a digit."
```
Перевіримо - що користувач ввів 2 або більше елементів

```py
string_in="/eat 10 bread"
elements = string_in.split(" ")
if len(elements)>=2:
    string_out = "It is ok"
else:
    string_out = "Please put 2 or more elements, devide by space."
```
* Перевіримо - чи є перше повідомлення командою.
```py
string_in="/eat 10 bread"
elements = string_in.split(" ")
if elements[0][0]=='/':
    string_out = "It is ok"
else:
    string_out = "You message is not command"
```

* Перевіримо - Чи є команда в списку команд.
```py
string_in="/eat 10 bread"
cat_list = ['eat','transport','coffee','start','help']
elements = string_in.split(" ")
if elements[0][1:] in cat_list:
    string_out = "It is ok"
else:
    string_out = "You command in not in command list."
```

* Механізм - користувач вводить доти, доки введе.
```py
flag = 1
while flag :
    message = input("Please enter message\n")
    elements = message.split(" ")
    if elements[0][0] == '/':
        flag = 0
        string_out = 'Дякуємо за введення команди'
    else:
        string_out = 'Нажаль, ви не вввеои ком'
    print(string_out)

```

-----
У попередніх двох завданнях ми перевіряли тип введення для того, щоб переконатися, що за подальших перевірок не виникне помилки. Тому, щоб перевірити чи є числом параметр, який вводить користувач після команди цей параметр повинен існувати, т.к. якщо ми спробуємо перевірити, чи є другий параметр числом - це параметр повинен існувати.
Далі - перевірятимемо другий параметр і працюватимемо з ним.
  
  
Але користувачеві нічого не заважає ввести після першого пропуску не число, а текст. Наприклад, написати такий рядок `/transport ten`. Або ж по клавіатурі може пройти кіт `/sfhjhjg jshdf`.


У минулому блоці ми з вами використовували функції, щоб надіслати дані користувачеві.
Але в цілому - функції використовуються практично завжди, коли той самий код може бути використаний кілька разів.
У попередніх блоках ми розглядали перевірку введення користувача. За допомогою функцій така перевірка програмується набагато компактніше і працювати з перевірками, запрограмованими за допомогою функцій набагато зручніше.
Першу перевірку, яку ми реалізуємо за допомогою функції - це перевірка того, чи взагалі є символи у введеному рядку. Без функцій це завдання виглядає таким чином:

```py
string_in = input("Введіть команду з параметром\n")
if len(string_in) > 0:
    string_out = 'Your input is correct' 
else:
    string_out = 'Your input is empty' 
print(string_out)
```
Проведемо рефакторинг нашого коду. Для цього скористаємося наступною функцією:
```py
def check(message):
    if len(message) > 0:
        return 'Your input is correct' 
    else:
        return 'Your input is empty'
```

<div class="interesting">
<h5>Цікаво</h5>
<p><b>Рефакторинг</b> - це контрольований процес покращення вашого коду, без написання нової функціональності.</p>
</div>

Використаємо написану функцію у загальній програмі:
```py
def check(message):
    if len(message) > 0:
        return 'Your input is correct' 
    else:
        return 'Your input is empty'

string_in = input("Введіть команду з параметром\n")
string_out = check(string_in)
print(string_out)
```

Реалізуємо перевірки введення:
* не порожній рядок
* команда
* наявність пробілу
* при розподілі за пробілом другий елемент - число
```py
string_out = ''
string_in = input("Please, enter command with parameters\n")
elements = string_in.split(' ')

if not len(string_in) > 0:
    string_out = 'Your input is empty' #string_out =
elif not string_in[0]=='/':
    string_out = 'First symbol of your input is not slash.'#string_out =
elif not ' ' in string_in:
    string_out = 'Your input does not contain spaces'#string_out =
elif not elements[1].isdigit():
    string_out = 'Parameter of command is not digit'#string_out =
else:
    string_out = 'Your input is correct' #string_out =
print(string_out)
```

Закодуємо усі текстові повідомлення такої програми. Для цього створимо перелік. Наявність тієї чи іншої помилки дозволить одержати її номер. І вже за номером помилки надіслати відповідне повідомлення.

```py
string_out = ''
check_strings = ["Your input is correct","Your input is empty","First symbol of your input is not slash.","Your input does not contain spaces","Parameter of command is not digit"]


string_in = input("Please, enter command with parameters\n")
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
print(check_strings[n])
```



