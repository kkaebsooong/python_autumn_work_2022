# todo: Шифр Цезаря
#Описание шифра.
#В криптографии шифр Цезаря, также известный шифр сдвига, код Цезаря или сдвиг Цезаря,
#является одним из самых простых и широко известных методов шифрования.
#Это тип подстановочного шифра, в котором каждая буква в открытом тексте заменяется буквой на некоторое
#фиксированное количество позиций вниз по алфавиту. Например, со сдвигом влево 3, D будет заменен на A,
#E станет Б, и так далее. Метод назван в честь Юлия Цезаря, который использовал его в своей частной переписке.

#Задача.
#Считайте файл message.txt и зашифруйте  текст шифром Цезаря, при этом символы первой строки файла должны
#циклически сдвигаться влево на 1, второй строки — на 2, третьей строки — на три и т.д.
#В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.
#В каждой строчке содержатся различные символы. Шифровать нужно только буквы кириллицы.

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыэюя'

decryption = ''
line_1 = -1
line_2 = -2
line_3 = -3
line_4 = -4
line_5 = -5

fd = open('message.txt', 'r', encoding='utf-8')
text = fd.readlines()
fd.close()

new_text1 = str(text[0]).lower()
new_text2 = str(text[1]).lower()
new_text3 = str(text[2]).lower()
new_text4 = str(text[3]).lower()
new_text5 = str(text[4]).lower()

for i in new_text1:
    index = alphabet.find(i)
    new_index = index + line_1
    if i in alphabet:
        decryption += alphabet[new_index]
    else:
        decryption += i


for i in new_text2:
    index = alphabet.find(i)
    new_index = index + line_2
    if i in alphabet:
        decryption += alphabet[new_index]
    else:
        decryption += i


for i in new_text3:
    index = alphabet.find(i)
    new_index = index + line_3
    if i in alphabet:
        decryption += alphabet[new_index]
    else:
        decryption += i


for i in new_text4:
    index = alphabet.find(i)
    new_index = index + line_4
    if i in alphabet:
        decryption += alphabet[new_index]
    else:
        decryption += i


for i in new_text5:
    index = alphabet.find(i)
    new_index = index + line_5
    if i in alphabet:
        decryption += alphabet[new_index]
    else:
        decryption += i

print(decryption)