import random

while True:
    number = random.randint(1,100)
    print(number)
    result = input('= > <: ')
    if result == '=':
        print('Победа')
        break
    elif result == '>':
        pass
    elif result == '<':
        pass
