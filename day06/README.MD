# Параметры. Функции. Проверка.
# Проверка
В прошлый день мы познакомились с тем, как переводить строку в команды. Для этого мы используем метод `split` который используем со строкой, которую получаем от пользователя.  
  

Пользотели могут вводить разную информацию. Такая информация не всегда будет соответствовать тому шаблону, который мы изначально задали (может неправильно указать команду, не указать параметр как число или же не указать комментарий).
В нашем боте будем проверять то, ввел ли пользователь нужную информацию.
Например - проверим, является ли второй элемент числом.  
```py
string_in="/eat 10 bread"
elements = string_in.split(" ")
if elements[1].isdigit():
    string_out = "It is ok"
else:
    string_out = "Second parameter must be a digit."
```
Проверим - что пользователь ввел 2 или более элемента
```py
string_in="/eat 10 bread"
elements = string_in.split(" ")
if len(elements)>=2:
    string_out = "It is ok"
else:
    string_out = "Please put 2 or more elements, devide by space."
```
* Проверим - является ли первое сообщение командой.
```py
string_in="/eat 10 bread"
elements = string_in.split(" ")
if elements[0][0]=='/':
    string_out = "It is ok"
else:
    string_out = "You message is not command"
```

* Проверим - Присутствует ли команда в списке команд.
```py
string_in="/eat 10 bread"
cat_list = ['eat','transport','coffee','start','help']
elements = string_in.split(" ")
if elements[0][1:] in cat_list:
    string_out = "It is ok"
else:
    string_out = "You command in not in command list."
```

* Механизм - пользователь вводит до того момента, пока не введет.
```py
flag = 1
while flag :
    message = input("Please enter message\n")
    elements = message.split(" ")
    if elements[0][0] == '/':
        flag = 0
        string_out = 'Благодарим за ввод команды'
    else:
        string_out = 'К сожалению, вы не ввели команду'
    print(string_out)

```

-----
В предыдущих двух заданиях мы проверяли тим ввода для того, чтобы убедиться, что при дальнейших проверках не возникнет ошибки. Потому что, для того, чтобы проверить является ли числом параметр, который вводит пользователь после команды этот параметр должен быть, т.к. если мы попробуем проверить то, является ли второй параметр числом - это параметр должен существовать.
Далее - будем проверять второй параметр и работать с ним.


Но пользователю ничего не мешает ввести после первого пробела не число, а текст. Например написать такую строку `/transport ten`. Или же по клавиатуре может пройти кот `'/sfhjhjg jshdf'`. Если мы при обработке таких сообщений будем пытаться второй




В прошлом блоке мы с вами использовали функции для того, чтобы отправить данные пользователю.  
Но в целом - функции используются практически всегда, когда один и тот же код может быть использован несколько раз.
В предыдущих блоках мы рассматривали проверку ввода пользователя. С помощью функций такая проверка программируется намного более компактно и работать с проверками, запрограммирвоаннными с помощью функций намного удобнее.
Первую проверку, которую мы реализуем с помощью функции - это проверка того, есть ли вообще символы во введенной строке.  Без функций данная задача выглядит следующим образом:
```py
string_in = input("Введите команду с параметром\n")
if len(string_in) > 0:
    string_out = 'Your input is correct' 
else:
    string_out = 'Your input is empty' 
print(string_out)
```
Проведем рефакторинг нашего кода. Для этого воспользуемся следующей функцией:
```py
def check(message):
    if len(message) > 0:
        return 'Your input is correct' 
    else:
        return 'Your input is empty'
```

<div class="interesting">
<h5>Интересно</h5>
<p><b>Рефакторинг</b> - это контролируемый процесс улучшения вашего кода, без написания новой функциональности.</p>
</div>

Используем написанную функцию в общей программе:  
```py
def check(message):
    if len(message) > 0:
        return 'Your input is correct' 
    else:
        return 'Your input is empty'

string_in = input("Введите команду с параметром\n")
string_out = check(string_in)
print(string_out)
```

Реализуем проверки ввода:  
* не пустая строка
* команда
* наличие пробела
* при разделении по пробелу второй элемент - число
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

Закодируем все текстовые сообщения такой программы. Для этого создадим список. Наличие той или иной ошибки позволит получить ее номер. И уже по номеру ошибки отправить соответствующее сообщение.

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
Создадим функцию, которая реализует данный функционал.


