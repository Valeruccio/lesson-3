import random

#Задаем словарь с управлящими элементами. Можно поменять на свое усмотрение
user_control = {'key1': '=', 'key2': '>', 'key3': '<'}

experiment = 1
max_experiment = 3
try_list = []

while experiment != (max_experiment + 1):
    min_number = 1
    max_number = 100
    print(f'Эксперимент {experiment}')
    # Доверим выбор числа программе
    my_choice = random.randint(min_number, max_number)
    comp_number = None
    experiment += 1
    #Переменная для подсчета попыток компа
    count = 0
    while comp_number != my_choice:
        count += 1
        #Будем выводить диапазон выбора в виде списка для наглядности. Можно убрать...
        numbers = range(min_number, (max_number + 1))
        print(list(numbers))
        #Выводим число наше загаданное, о5 же для удобства
        print(f'Я выбрал число {my_choice}')
        #Компьютер выбирает случайное число в заданном диапазоне
        comp_number = random.randint(min_number, max_number)
        user_move = input(f'Компьютер выбирает число: {comp_number}\n'
                          f'Введите следующие ключи для подсказки\n'
                          f'"<" если ваше число меньше,\n'
                          f'">" если ваше число больше\n'
                          f'или "=" если компьютер угадал: ')
        #В условных операторах сокращаем диапазон выбора для компьютера
        if user_move == user_control['key2']:
            min_number = comp_number + 1
        if user_move == user_control['key3']:
            max_number = comp_number - 1
    else:
        print(f'Поздравляю, "консерва", ты угадал. Я загадал {my_choice}')
    print(f'Всего попыток {count}')
    try_list.append(count)

print(try_list)
print('Конец')