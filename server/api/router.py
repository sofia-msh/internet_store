from flask import Flask, request, jsonify
from Internet_Store.model import models as m
from Internet_Store.server.DB import database as d


class Router:
    def __init__(self, app: Flask, database: d.DataBase):
        self.app = app
        self.database = database

    def run(self):
        self.define_routes()
        self.app.run()

    def define_routes(self):
        @self.app.route("/user/reg", methods=["POST"])
        def registration():
            req_data = request.json
            username = req_data["username"]
            if not self.database.SelectUserByName(username):
                email = req_data["email"]
                password = req_data["password"]
                user = m.User(username, email, password)
                self.database.InsertIntoUsers(user)
                self.database.conn.commit()
                return jsonify(f"Thank you for your registration {username}")
            else:
                return jsonify("Name is already taken")

        @self.app.route("/products", methods=["POST"])
        def get_product_info():
            req_data = request.json
            name = req_data["product name"]
            price = req_data["price"]
            product = m.Product(name, price)
            self.database.InsertIntoProducts(product)
            return jsonify(f"{product.name} registered")

        @self.app.route("/user/auth", methods=["POST"])
        def authorization():
            req_data = request.json
            username = req_data.get("username")
            email = req_data.get("email")
            password = req_data.get("password")
            user = m.User(username,email,password)
            if self.database.SelectCurrentUser(user):
                return jsonify("Authorized")
            return jsonify("Incorrect Credentials")

