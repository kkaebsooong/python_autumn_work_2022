#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
#функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
#чтобы каждая функция выполняла одно универсальное действие.
import random


desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
star_answer = []
score = 0

def random_word():
    words = ["оператор", "конструкция", "объект"]
    a = random.choices(words)[0]
    return a




dict = {'Это слово обозначает наименьшую автономную часть языка программирования' : random_word()}
print(dict)

def game():
    global score
    for value in dict.values():
        star_answer = '*' * len(value)
        print(star_answer)
        while score != 10 and (star_answer != value):
            answer = input('Введите букву: ')
            new_answer = ''
            if answer != '':
                if answer in value:
                    for i in range(len(value)):
                        if answer == value[i]:
                            new_answer += answer
                        else:
                            new_answer += star_answer[i]
                    star_answer = new_answer
                    print(star_answer)
                else:
                    score += 1
                    print('Таковй букве нет, у вас', score, 'штрафной(-ых) балл(-ов)')

game()