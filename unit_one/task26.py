#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 classwork/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.


import random
import pickle
data = []
count = 0
guess = range(random.randint(0, 100))
try_count = 10

def menu():
    out = f'1. Новая игра\n2. Продолжить игру\n3. Сохранить игруn\n4. Загрузить игру'
    print(out)

def game():
    menu()
    num = int(input())
    global count
    global try_count
    if num == 1:
        pass
        #Start
        question = input('Введите число: ')
        while count != 9:
            try:
                question = input('Введите число: ')
                question = int(question)
            except:
                pass
            if question == guess:
                print('Вы угадали число!')
            elif question != guess:
                count += 1
                try_count = try_count - 1
                print(f'Вы не угадали число, у вас осталось {try_count} попыток')
                continue
            elif question == 's':
                save_game()
            elif question == 'q':
                break
        print('Вы проиграли')
    elif num == 4:
        open_game()
        num = 1


def save_game():
    data = return_save_game()
    name = input('Введите название для сохранения игры: ')
    save_point = {'name' : name, 'guess_num' : guess, 'count' : count}
    data.append(save_point)
    with open('game_dump.pkl', 'wb') as f:
        pickle.dump(data, f)

def return_save_game():
    with open('game_dump.pkl', 'rb') as og:
        data = pickle.load(og)
        return data

def open_game():
    with open('game_dump.pkl', 'rb') as og:
        data = pickle.load(og)
        cnt = 0
        for dict_ in data:
            cnt += 1
            str = f"{cnt} : {dict_['name']}"
        print(str)
    name_save_game = input('Введите номер сохраненной игры')
    global guess, count
    for dict_ in data:
        if name_save_game == dict_['name']:
            guess = dict_['guess']
            count = dict_['count']
            print(f'Игра восстановленна {dict_["name"]}')
open_game()









