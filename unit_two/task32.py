# todo: Реализовать класс "Игровой персонаж".
#  Класс должен содержать атрибуты(свойства): Идентификатор, Имя, Здоровье, Раса, Тип персонажа, урон.
#  Инициализация атрибутов(состояние объекта) должна происходить в конструкторе.
#  В классе реализовать метод изменения здоровья по нанесенному урону(параметр функции).
#  Заложить логику: При достижении порога здоровья персонаж погибает
#  В классе реализовать метод получения значения атрибута урона
#  При достижении порога здоровья персонаж погибает
#  Реализовать дандер __repr__ для отладки персонажа
#  Реализовать дандер вычитания __sub__()  написав логику "боя" которая срабатывает
#  в момент вычитания объектов класса obj1 - obj2 и заключается в вычитании из
#  здоровья первого объекта урона наносимого вторым объектом

import random



class Person:
    def __init__(self, identificator, name, race, type_person, hp, dmg):
        self.identificator = identificator
        self.name: str = name
        self.race = race
        self.type_person = type_person
        self.hp = hp
        self.dmg = dmg

    def __sub__(self, enemy):
        enemy.hp -= enemy.dmg
        if enemy.hp < 0:
            enemy.hp = 0

        print(f'{self.name} бьет {enemy.name} и наносит {enemy.dmg} урона')
        print('%s = %d' % (enemy.name, enemy.hp))
    def __repr__(self):
        return f'id: , name: , race: , class: , dmg: , hp: '


class Battle:
    def __init__(self, unit1, unit2):
        self.unit1 = unit1
        self.unit2 = unit2
        self.result = 'Сражения не было'

    def battle(self):
        while self.unit1.hp > 0 and self.unit2.hp > 0:
            n = random.randint(1,2)
            if n == 1:
                self.unit1.__sub__(self.unit2)
            else:
                self.unit2.__sub__(self.unit1)
        if self.unit1.hp > self.unit2.hp:
            self.result = self.unit1.name + ' победил'
        elif self.unit2.hp > self.unit1.hp:
            self.result = self.unit2.name + ' победил'

    def who_win(self):
        print(self.result)

first = Person('1', 'An', 'Human', 'Hero', 100, 10)
second = Person('2', "Rat'tha", 'Guauld', 'Parasite', 100, 10)
b = Battle(first, second)
b.battle()
b.who_win()