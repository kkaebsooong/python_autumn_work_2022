#todo: Числа в буквы
#Замените числа, написанные через пробел, на буквы. числа не изменять.

#Пример.
#Input	                            Output
#8 5 12 12 15	                    hello
#8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!




alphabet = ' abcdefghigklmnopqrstuvwxyz,!'
encrypted_text = (8, 5, 12, 12, 15, ',', 0, 23, 15, 18, 12, 4, '!')
new_text =[]

for i in encrypted_text[:encrypted_text.index(',')]:
    new_text.append(alphabet[i])
for j in encrypted_text[encrypted_text.index(',') + 1:encrypted_text.index('!')]:
    new_text.append(alphabet[j])

new_text = ''.join(new_text)
new_text = new_text.rstrip(' ')
new_text = new_text.replace(' ', ', ')

print(f'{new_text}!')