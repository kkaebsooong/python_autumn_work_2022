# todo:Прочитать главу 6 (стр. 119) книги SQL Полное Руководство.
Написать на модели данный ПО "Авторизации" запросы:
1. Простой запрос

select id, id_profile, login
  from account as a, account_group as ag


2. Вычисляемый столбец


select surname, name, (normal_weight - weight)
  from profile as p


3. Выборка всех столбцов

select surname, name, (normal_weight - weight)
  from profile as p


4. Повторяющиеся строки (DISTINCT)


select distinct id, id_profile, login
  from account as a, account_group as ag


5. Отбор строк (WHERE) с оператором ставнения


select distinct id, id_profile, login
  from account as a, account_group as ag
 where id >= 3


6. Выборка одной строки


select distinct id, id_profile, login
  from account as a, account_group as ag
 where id = 5


7. Проверка на принадлежность диапазону (BETWEEN)


select distinct id, id_profile, login
  from account as a, account_group as ag
 where  id between 2 and 5


8. Проверка наличия во множестве (IN)


select distinct id, id_profile, login
  from account as a, account_group as ag
 where id in (1,3,5)


9. Проверка на соответствие шаблону (LIKE)


select distinct id, id_profile, login
  from account as a, account_group as ag
 where login like 'baba%'


10. Проверка на равенство NULL (is NULL)


select id, surname, name, patronim, email
  from profile
 where patronim is null



11. Сопоставление условия отбора (AND, OR и NOT)

select id, surname, name, patronim, email, is_free
  from profile
 where patronim is not null
   and is_free = 'false'
    or weight > 80

12. Сортировка результатов запроса (ORDER ВУ)

select id, surname, name, patronim, email, is_free
  from profile
 where patronim is not null
   and is_free = 'false'
    or weight > 80
 order by surname

13. Объединение результов нескольких запросов (UNION)

select name
  from "group"
 union
select name
  from profile



