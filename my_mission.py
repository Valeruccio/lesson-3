# Добавим рандом
import random
# Делаем бесконечный цикл
while True:
    # Определяем диапазон для числа с помощью ограничителя для рандома от 1 до 100
    number = random.randint(1,100)
    # Печатаем номер, демонстрируя его поользователю
    print(number)
    # Запрашиваем обратную связь от пользлвателя
    result = input('< > =:   ')
# Если результат, выведенный компьютером номер, соответсвует вашему числу, то нажав = мы получим победу
    if result == '=':
         # Печатаем поздравление компьютера
         # Если результат меньше, то пишем <
    elif result == '<':
         # функция пропускается
         pass
        # Если результат больше, то пишем >
    elif result == '>':
         # функция пропускается
         pass
print('Компьютер победил!')