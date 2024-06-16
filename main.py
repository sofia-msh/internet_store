import sqlite3
from randoms import random_data as r

if __name__ == '__main__':
    # conn = sqlite3.connect('sonya_db')  # создаем подключение к базе данных
    # cursor = conn.cursor()  # создаём курсор
    #
    # create_table_product_query = (" CREATE TABLE if not exists products " +
    #                               "( " +
    #                               "id integer PRIMARY KEY," +
    #                               "name text not null ," +
    #                               "price integer not null" +
    #                               ")")
    # cursor.execute(create_table_product_query)
    # create_table_catalog_query = ("CREATE TABLE if not exists catalogs(" +
    #                               "id INTEGER PRIMARY KEY," +
    #                               "product_id INTEGER," +
    #                               "FOREIGN KEY (product_id) REFERENCES product(id)" +
    #                               ");"
    #                               )
    # cursor.execute(create_table_catalog_query)
    # # заполним таблицу products наборами данных
    # for i in range(10):
    #     insert_into_products_query = (
    #         "INSERT INTO products (name, price) VALUES (?,?)")
    #     inserting_values=(r.get_some_from_products_lines(r.products),r.give_price_to_smth(100, 200))
    #     cursor.execute(insert_into_products_query,inserting_values)
    # select_products_query = ("SELECT id FROM products WHERE price >125")
    # cursor.execute(select_products_query)
    # insert_into_catalogs_query = ("INSERT INTO catalogs (product_id)   VALUES (?)")
    # ids=cursor.fetchall()
    # for i in ids:
    #     cursor.execute(insert_into_catalogs_query,i)
    # join_query=("SELECT products.id, name,price FROM catalogs  "
    #             "join products on catalogs.product_id=products.id ")
    # cursor.execute(join_query)
    # all=cursor.fetchall()
    # for i in all:
    #     print(i)
    # conn.commit()
    # conn.close()
    import requests

    url = ' https://raptor-artistic-cicada.ngrok-free.app/get_book'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Ошибка при выполнении запроса:', response.status_code)