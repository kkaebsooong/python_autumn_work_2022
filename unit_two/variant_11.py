import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='autoservice_new',
    user='postgres',
    password='a197328456')

cur = conn.cursor()

# 1. Выдавать список услуг, предлагаемых автосервисом с ценой;


SQL_GET_PRICE_SERVICE = f"""SELECT ap.id_application, ap.name, ap.price
                              FROM application as ap """

cur.execute(SQL_GET_PRICE_SERVICE)

records = cur.fetchall()

for row in records:
    print(row)



# 2. Выдавать список машин, находящихся в автосервисе;


SQL_GET_CAR_IN_SERVICE = f"""SELECT car.id_car, car.name_car, car.model
                               FROM car"""

cur.execute(SQL_GET_CAR_IN_SERVICE)

records = cur.fetchall()

for row in records:
    print(row)



#3 Выдавать информацию о данной машине (оказываемые услуги)

id_car = input('Введите id номер машины: ')

SQL_ID_IN_SERVICE = f"""SELECT c.name_car, c.model, app.id_application, app.name, app.price
                          FROM application as app, car as c
                         WHERE c.id_car = app.car_id
                           AND c.id_car = {id_car}"""

cur.execute(SQL_ID_IN_SERVICE)

records = cur.fetchall()

for row in records:
    print(row)

# 4. Выдавать информацию о проделанной данным мастером работе за отчетный период времени (день, месяц, квартал, год)

id_emploee = input('Введите id мастера: ')

SQL_ID_EMPLOEE = f"""SELECT emploee.surname, emploee.name, car.id_car, car.name_car, car.model, car.date_time, car.quarter
                       FROM emploee, car
                      WHERE emploee.id_emploee = car.emploee_id
                    AND car.emploee_id = {id_emploee}"""

cur.execute(SQL_ID_EMPLOEE)

records = cur.fetchall()

for row in records:
    print(f'Фамилия работника: {row[0]}')
    print(f'Имя работника: {row[1]}')
    print(f'ID машины: {row[2]}')
    print(f'Марка машины: {row[3]}')
    print(f'Модель машины: {row[4]}')
    print(f'Дата работы: {row[5]}')
    print(f'Квартал: {row[6]}')

# 5. Рассчитывать стоимость услуг для клиентов.

id_client = input('Введите id клиента: ')

SQL_CLIENT_SUM_PRICE = f"""SELECT cl.surname, cl.name, app.name, app.price
                             FROM client as cl, application as app
                            WHERE cl.id_client = app.client_id
                              AND cl.id_client = {id_client}"""

cur.execute(SQL_CLIENT_SUM_PRICE)

records = cur.fetchall()

sum_price = 0

for row in records:
    sum_price += row[3]
    a = f'Surname : {row[0]}'
    b = f'Name : {row[1]}'
    c = f'Application name : {row[2]}'
    d = f'Price : {row[3]}'
    sum_price += row[3]
    print(a)
    print(b)
    print(c)
    print(d)

print(f'Итоговая сумма составляет {sum_price} рублей')

conn.close()
