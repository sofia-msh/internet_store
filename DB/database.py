import sqlite3
from randoms import random_data as r

class DataBase():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)  # создаем подключение к базе данных
        self.cursor = self.conn.cursor()  # создаём курсор для текущего подключения

    def CreateTableProducts(self):
        sql_code = ("CREATE TABLE if not exists products " +
                    "( " +
                    "id integer PRIMARY KEY," +
                    "name text not null ," +
                    "price integer not null" +
                    ");")
        self.cursor.execute(sql_code)

    def CreateTableCatalogs(self):
        sql_code = ("CREATE TABLE if not exists catalogs(" +
                    "id INTEGER PRIMARY KEY," +
                    "product_id INTEGER," +
                    "FOREIGN KEY (product_id) REFERENCES product(id)" +
                    ");"
                    )
        self.cursor.execute(sql_code)

    def InsertIntoProducts(self, n: str, p: int):
        sql_code = ("INSERT INTO products (name, price) VALUES (?,?)")
        values = (n, p)  # добавляем данные в кортедж
        self.cursor.execute(sql_code, values)  # вставляем данные в бд
    def FillProducts(self,n:int):
        for i in range(n):
            #генерация рандомного продукта
            p_name=r.get_some_from_products_lines()
            p_price=r.give_price_to_smth(100, 200)
            #заполняем бд этим рандомным продуктом
            self.InsertIntoProducts(p_name,p_price)

    def shutdown(self):
        self.conn.commit()
        self.conn.close()

    def CreateAllTables(self):
        self.CreateTableProducts()
        self.CreateTableCatalogs()
