#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
#и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.
import random

#Пример вывода:
#Сумма 2   комбинация [(1,1)]
#Сумма 3   комбинация [(1,2),(2,1)]
#Сумма 4   комбинация [(1,3),(3,1),(2,2)]
#........................................
#Выводы комбинаций оформить в список кортежей.
masssive = []
combination = ()
summ_d = [1, 2, 3, 4, 5, 6]
summ_of_comb = int(input('Введите сумму для вывода комбинации: '))

for i in summ_d:
    for j in summ_d:
            if i + j == summ_of_comb:
                combination = i,j
                masssive.append(combination)
            else:
                pass
print(masssive)

