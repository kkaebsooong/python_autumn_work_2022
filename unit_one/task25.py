#todo: Убрать повторяющиеся буквы и лишние символы
#Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
#Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.

#Input             	            Output

#apple	                        aple
#25.04.2022 Good morning !!	    godmrni

a = 'apple'
a = ''.join(dict.fromkeys(a))
print(a)


b = '25.04.2022 Good morning !!'

print(b)

b_new = ''.join(i for i in b if i.isalpha())
print(''.join(dict.fromkeys(b_new)))

