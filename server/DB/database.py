import sqlite3
from Internet_Store.randoms import random_data as r
from Internet_Store.model import models as m


class DataBase():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)  # создаем подключение к базе данных
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
                    "number INTEGER,"
                    "product_id INTEGER," +
                    "FOREIGN KEY (product_id) REFERENCES products(id)" +
                    ");"
                    )
        self.cursor.execute(sql_code)

    def CreateUsersTable(self):
        sql_code = ("CREATE TABLE IF NOT EXISTS users(" +
                    "id Integer Primary Key," +
                    "username text," +
                    "email text," +
                    "password text" +
                    ");")
        self.cursor.execute(sql_code)

    def CreateFavoritesTable(self):
        sql_code = ("CREATE TABLE IF NOT EXISTS favorites(" +
                    "id Integer Primary Key," +
                    "user_id Integer," +
                    "products_id Integer," +
                    "FOREIGN KEY (user_id) REFERENCES users(id)," +
                    "FOREIGN KEY (products_id) REFERENCES products(id)"
                    ");")
        self.cursor.execute(sql_code)

    def CreateCartTable(self):
        sql_code = ("CREATE TABLE IF NOT EXISTS cart(" +
                    "id Integer Primary Key," +
                    "user_id Integer," +
                    "products_id Integer," +
                    "FOREIGN KEY (user_id) REFERENCES users(id)," +
                    "FOREIGN KEY (products_id) REFERENCES products(id)"
                    ");")
        self.cursor.execute(sql_code)

    def CreateOrdersTable(self):
        sql_code = ("CREATE TABLE IF NOT EXISTS orders(" +
                    "id Integer Primary Key," +
                    "user_id Integer," +
                    "products_id Integer," +
                    "FOREIGN KEY (user_id) REFERENCES users(id)," +
                    "FOREIGN KEY (products_id) REFERENCES products(id)"
                    ");")
        self.cursor.execute(sql_code)

    def InsertIntoProducts(self, product: m.Product):
        sql_code = ("INSERT INTO products (name, price) VALUES (?,?)")
        values = (product.name, product.price)  # добавляем данные в кортедж
        self.cursor.execute(sql_code, values)  # вставляем данные в бд
    def FillProducts(self,n:int):
        for i in range(n):
            #генерация рандомного продукта
            p_name=r.get_some_from_products_lines()
            p_price=r.give_price_to_smth(100, 2000)
            #заполняем бд этим рандомным продуктом
            product = m.Product(p_name,p_price)
            self.InsertIntoProducts(product)
    def InsertIntoCatalogue(self, catalogue: m.Catalogue):
        sql_code = ("INSERT INTO catalogs (number ,product_id) VALUES (?, ?)")
        value = (catalogue.number, catalogue.product_id,)
        self.cursor.execute(sql_code, value)
    def SelectFromProducts(self) -> list[m.Product]:
        sql_code = ("SELECT * FROM products")
        self.cursor.execute(sql_code)
        products = [m.Product(id = i[0], name = i[1], price = i[2]) for i in self.cursor.fetchall()]
        return products

    def SelectUsers(self) -> list[m.User]:
        sql_code = ("SELECT * FROM users")
        self.cursor.execute(sql_code)
        users = [m.User(id = i[0], username = i[1], email = i[2], password = i[3])for i in self.cursor.fetchall()]
        return users

    def SelectCurrentUser(self, user):
        sql_code = ("select Count(*) from users where password = ? and (username = ? or email = ?)")
        self.cursor.execute(sql_code, (user.password,user.username,user.email))
        user = self.cursor.fetchone()
        if user is None:
            return False
        return True

    def SelectUserByName(self, username):
        sql_code = ("select Count(*) from users where username = ?")
        self.cursor.execute(sql_code, (username,))
        user = self.cursor.fetchone()
        if user is None:
            return True
        return False

    def InsertProductIntoCatalogue(self, price):
        for i in self.SelectFromProducts():
            if i[2] > price:
                self.InsertIntoCatalogue("1",i[0])
            else:
                self.InsertIntoCatalogue("2", i[0])

    def JoinSelectProductsCatalogue(self):
        sql_code = ("SELECT name,price,number FROM products as p join catalogs as c on p.id=c.product_id")
        self.cursor.execute(sql_code)
        return self.cursor.fetchall()

    def JoinSelectUsersProductCart(self) -> list[m.JoinedCart]:
        sqlcode = ("SELECT cart.id, products_id, user_id, username, email, password, name, price "
                   "FROM cart "
                   "join users on cart.user_id = users.id "
                   "join products on cart.products_id = products.id")
        self.cursor.execute(sqlcode)
        return [m.JoinedCart(
            user = m.User(id = i[2], username= i[3], email = i[4], password= i[5]),
            products = m.Product(id = i[1], name= i[6], price= i[7]),
            id = i[0]
        ) for i in self.cursor.fetchall()]

    def JoinSelectUsersProductOrders(self) -> list[m.JoinedOrders]:
        sqlcode = ("SELECT orders.id, products_id, user_id, username, email, password, name, price "
                   "FROM orders "
                   "join users on cart.user_id = users.id "
                   "join products on cart.products_id = products.id")
        self.cursor.execute(sqlcode)
        return [m.JoinedOrders(
            user = m.User(id = i[2], username= i[3], email = i[4], password= i[5]),
            products = m.Product(id = i[1], name= i[6], price= i[7]),
            id = i[0]
        ) for i in self.cursor.fetchall()]

    def JoinSelectUsersProductFavorites(self) -> list[m.JoinedFavorites]:
        sqlcode = ("SELECT favorites.id, products_id, user_id, username, email, password, name, price "
                   "FROM favories "
                   "join users on cart.user_id = users.id "
                   "join products on cart.products_id = products.id")
        self.cursor.execute(sqlcode)
        return [m.JoinedFavorites(
            user = m.User(id = i[2], username= i[3], email = i[4], password= i[5]),
            products = m.Product(id = i[1], name= i[6], price= i[7]),
            id = i[0]
        ) for i in self.cursor.fetchall()]

    def SelectFromCatalogue(self) -> list:
        sql_code = ("SELECT * FROM catalogs")
        self.cursor.execute(sql_code)
        catalogue = self.cursor.fetchall()
        return catalogue

    def InsertIntoCart(self, user: m.User, product: m.Product):
        sql_code = ("INSERT INTO cart (user_id, products_id) VALUES (?,?)")
        values = (user.id, product.id)
        self.cursor.execute(sql_code, values)

    def InsertIntoFavorites(self, user: m.User, product: m.Product):
        sql_code = ("INSERT INTO favorites (user_id, products_id) VALUES (?,?)")
        values = (user.id, product.id)
        self.cursor.execute(sql_code, values)

    def InsertIntoOrders(self, user: m.User, product: m.Product):
        sql_code = ("INSERT INTO orders (user_id, products_id) VALUES (?,?)")
        values = (user.id, product.id)
        self.cursor.execute(sql_code, values)

    def InsertIntoUsers(self, user: m.User):
        sql_code = ("INSERT INTO users (username, email, password) VALUES (?,?,?)")
        values = (user.username, user.email, user.password)
        self.cursor.execute(sql_code, values)

    def UserAuth(self, user: m.User):
        sql_code = ("SELECT * from users WHERE password = ? AND (username = ? OR email = ?)")
        values = (user.password, user.username, user.email)
        self.cursor.execute(sql_code, values)
        if self.cursor.fetchone() is None:
            return False
        else:
            return True


    def shutdown(self):
        self.conn.commit()
        self.conn.close()

    def CreateAllTables(self):
        self.CreateTableProducts()
        self.CreateTableCatalogs()
        self.CreateUsersTable()
        self.CreateFavoritesTable()
        self.CreateCartTable()
        self.CreateOrdersTable()

    def DropTables(self):
        sql_code = ("DROP TABLE if exists products")
        sql_code2 = ("DROP TABLE if exists catalogs")
        sql_code3 = ("DROP TABLE if exists users")
        sql_code4 = ("DROP TABLE if exists favorites")
        sql_code5 = ("DROP TABLE if exists cart")
        sql_code6 = ("DROP TABLE if exists orders")
        sql_queries = [sql_code, sql_code2, sql_code3, sql_code4, sql_code5, sql_code6]
        for i in sql_queries:
            self.cursor.execute(i)

