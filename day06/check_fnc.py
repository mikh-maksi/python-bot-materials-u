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