# Задача 1.2
# Сгенерировать случайное число от 1000 до 1000000. Вывести его и вывести его 4-й знак.

# загружаю модуль генерации случайных чисел
import random

# генерируем случайное число от 1000 до 1000000
rand1 = random.randint(1000, 1000000)

# выводим случайное число
print("случайное число:", rand1)

# находим четвертый знак с конца
rand2 = rand1//1000 - rand1//10000*10

# выводим четвертый знак с конца
print("четвертый знак случайного числа:", rand2)
