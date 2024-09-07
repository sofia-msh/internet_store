import sqlite3
from randoms import random_data as r
from DB import  database as db


if __name__ == '__main__':
    db1=db.DataBase('sonya_db')
    db1.CreateAllTables()
    db1.FillProducts(10)
    db1.shutdown()

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
    # import requests
    #
    # url = ' https://raptor-artistic-cicada.ngrok-free.app/get_book'
    # response = requests.get(url)
    #
    # if response.status_code == 200:
    #     data = response.json()
    #     print(data)
    # else:
    #     print('Ошибка при выполнении запроса:', response.status_code)