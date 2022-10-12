
# todo: Реализовать логику игры "Морской бой". Задано игровое поле 5 на 5 в виде двухмерного массива(список списков).
#  Значением 1 (единицей) обозначают однопалубный корабль в координатах i-ой строки и j-го столбца.
#  Написать игровую логику которая по вводу пары i,j  проверяет попадание и его фиксирует.
#  Для генерации случайных значений 0 и 1 в массиве использовать lambda выражение. Кол-во кораблей может быть случайное
#  в зависимости от генерации. Кол-во попыток пока не ограничивать.
import random

# Пример:
game_field = []
# нужно заменить статическую инициализацию списка на динамическую с помощью lambda выражения.
row_one   = [(lambda x: random.randint(0,1))(x) for x in range(0,5)]
row_two   = [(lambda x: random.randint(0,1))(x) for x in range(0,5)]
row_three = [(lambda x: random.randint(0,1))(x) for x in range(0,5)]
row_four  = [(lambda x: random.randint(0,1))(x) for x in range(0,5)]
row_five  = [(lambda x: random.randint(0,1))(x) for x in range(0,5)]



game_field.append(row_one)
game_field.append(row_two)
game_field.append(row_three)
game_field.append(row_four)
game_field.append(row_five)
i = 1  # вхождение в первый массив
j = 4  # вхождение в 4-ый элемент текущего массива
# доступ к элементам двухмерного массива
print(game_field[i],[j])