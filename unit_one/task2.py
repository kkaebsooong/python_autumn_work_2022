#Преобразуйте переменную age и foo в число 
age = "23"
foo = "23abc" #здесь содержатся цифры и буквы, поэтому в число преобразовать нельзя, разделим содержимое
foo_1 = foo.split('a')
print(int(age))
print(int(foo_1[0]))
#Преобразуйте переменную age в Boolean

age = "123abc"
age_2 = "123abc"
if age_2 == age:
    print('True')
else:
    print('False')

#Преобразуйте переменную flag в Boolean

flag = 1
if flag > 0:
    print('True')
else:
    print('False')

#Преобразуйте значение  в Boolean
str_one = "Privet"
str_two = ""
if str_one == str_two:
    print('True')
else:
    print('False')
#Преобразуйте значение 0 и 1  в Boolean
x = 0
y = 1

if x > y:
    print(x)
else:
    print(y)