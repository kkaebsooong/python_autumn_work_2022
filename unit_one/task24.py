#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'z', 'y', 'z']
decryption = ''
numbers = input()
step = -1

for i in numbers:
    index = numbers.find(i)
    new_index = index + step
    if i in numbers:
        decryption += numbers[new_index]
    else:
        decryption += i
print(decryption)

# def decryption(i):
#     match i:
#         case 1:
#             print('a')
#         case 2:
#             print('b')
#         case 3:
#             print('c')
#         case 4:
#             print('d')
#         case 5:
#             print('e')
#         case 6:
#             print('f')
#         case 7:
#             print('g')
#         case 8:
#             print('h')
#         case 9:
#             print('i')
#         case 10:
#             print('j')
#         case 11:
#             print('k')
#         case 12:
#             print('l')
#         case 13:
#             print('m')
#         case 14:
#             print('n')
#         case 15:
#             print('o')
#         case 16:
#             print('p')
#         case 17:
#             print('q')
#         case 18:
#             print('r')
#         case 19:
#             print('s')
#         case 20:
#             print('t')
#         case 21:
#             print('u')
#         case 22:
#             print('v')
#         case 23:
#             print('w')
#         case 24:
#             print('x')
#         case 25:
#             print('y')
#         case 26:
#             print('z')
#
# decryption(8)
# decryption(5)
# decryption(12)
# decryption(12)
# decryption(15)