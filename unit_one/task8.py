#todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
A = 10
B = 3
C = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10



# Пример 2:
A = 2
B = 10
C = 7
# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10


a = 170
b = 500
c = 10

if a > b and b > c and a > c:
    print(c,b,a)
elif a < b and c < b and a > c:
    print(c,a,b)
elif a < b and b < c and a < c:
    print(a,b,c)
elif b < a and b <c and a < c:
    print(b,a,c)
elif a > b and a > c and b < c:
    print(b,c,a)
else:
    print(a,c,b)