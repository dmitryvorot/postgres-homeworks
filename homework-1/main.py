import psycopg2
import os

# Распаковка всех таблиц из папки north_data, получение списка кортежей.
customers_list = []
employees_list = []
orders_list = []

with open('north_data/customers_data.csv', 'rt') as file:
    for line in file:
        line = line.replace('\n', '')
        customer_tuple = tuple(line.split('\",\"'))
        customers_list.append(customer_tuple)
    customers_list.pop(0)

with open('north_data/employees_data.csv', 'rt') as file:
    for line in file:
        line = line.replace('\n', '')
        employee_tuple = tuple(line.split('\",\"'))
        employees_list.append(employee_tuple)
    employees_list.pop(0)

with open('north_data/orders_data.csv', 'rt') as file:
    for line in file:
        line = line.replace('\n', '')
        order_tuple = tuple(line.split(','))
        orders_list.append(order_tuple)
    orders_list.pop(0)

# Соединение с БД
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="04510451")

# Создание курсора
cur = conn.cursor()

try:
    # Выполнение запросов
    cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)", employees_list)
    cur.execute("SELECT * FROM employees")
    conn.commit()

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers_list)
    cur.execute("SELECT * FROM customers")
    conn.commit()

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders_list)
    cur.execute("SELECT * FROM orders")
    conn.commit()

    rows = cur.fetchall()
    for row in rows:
        print(row)

finally:
    # Закрытие соединения с БД и курсора
    cur.close()
    conn.close()
