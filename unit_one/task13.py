#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.
import random

array = []
for x in range(10):
    x = random.randint(10,99)
    array.append(x)
print(array)

a = 0
result = []
for b in array:
    b = array[a] + 1
    a = a + 1
    result.append(b)
print(result)




