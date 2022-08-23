# Задача 1. Напишите программу, которая принимает на вход
# цифру, обозначающую день недели, и выводит название
# этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение


numbers = int(input('Введите число:  '))
if numbers == 1:
    print('Понедельник')
elif numbers == 2:
    print('Вторник')
elif numbers == 3:
    print('Среда')
elif numbers == 4:
    print('Четверг')
elif numbers == 5:
    print('Пятница')
elif numbers == 6:
    print('Суббота')
elif numbers == 7:
    print('Воскресенье')
else:
    print('Нет такого дня')
