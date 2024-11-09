from Internet_Store.server.DB import database as db
from flask import Flask
from Internet_Store.server.api import router as rt
from Internet_Store.client import main

if __name__ == '__main__':
    app = Flask(__name__)
    db1 = db.DataBase('sonya_db')
    router = rt.Router(app, db1)
    #db1.DropTables()
    #db1.CreateAllTables()
    router.run()
    router.define_routes()

    #db1.FillProducts(20)
    # for i in db1.SelectFromProducts():
    # print(i)
    # product_unique = r.UniqueElements(db1.SelectFromProducts(), 5)
    # for i in range(5):
    # db1.InsertIntoCart(user[0], product_unique[i])
    # for i in db1.JoinSelectUsersProductCart():
    # print(i)
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
