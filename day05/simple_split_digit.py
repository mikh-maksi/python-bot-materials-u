account = 0
string_in = '/income 100'
elements = string_in.split(' ')
account = account + int(elements[1])
print(account)