#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.




shift = 6 # определение количества сдвигов
encrypted_text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."

alphabet = 'abcdefghigklmnopqrstuvwxyz'

for i in range(len(alphabet)):
    plain_text = ''
    for j in encrypted_text:
        if j in alphabet:
            n = alphabet.find(j)
            n = n - shift
            if n < 0:
                n + len(alphabet)
            plain_text = plain_text + alphabet[n]
        else:
            plain_text = plain_text + j
    print(plain_text)