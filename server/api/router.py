import datetime

from flask import Flask, request, jsonify, make_response
from Internet_Store.model import models as m
from Internet_Store.server.DB import database as d
from Internet_Store.server.encryption import encryption as e
import time
import jwt


class Router:
    def __init__(self, app: Flask, database: d.DataBase):
        self.app = app
        self.app.config['SECRET_KEY'] = 'world'
        self.database = database
        self.ip_dict = {}
        self.time_delay = 0.03

    def run(self):
        self.define_routes()
        self.define_middleware()
        self.app.run()


    def check_addr_requests(self, addr):
        if addr not in self.ip_dict:
            self.ip_dict[addr] = [time.time()]
        else:
            self.ip_dict[addr].append(time.time())
            for i, j in enumerate(self.ip_dict[addr]):
                t = time.time()
                if t - j >= self.time_delay:
                    self.ip_dict[addr].pop(i)
        if len(self.ip_dict[addr]) > 40:
            return False
    def define_middleware(self):
        @self.app.before_request
        def middleware():
            if request.endpoint in ["cart/add"]:
                token = request.headers.get("Authorization")
                if token is None:
                    return make_response(jsonify({"message": "Token required"}), 403)
    def define_routes(self):
        @self.app.route("/user/reg", methods=["POST"])
        def registration():
            addr = request.remote_addr
            if self.check_addr_requests(addr) == False:
                return make_response(jsonify("Blocked"), 429)
            req_data = request.json
            username = req_data["username"]
            id = self.database.SelectUserByName(username)
            if id is None:
                email = req_data["email"]
                password = e.encryption(req_data["password"])
                user = m.User(username, email, password)
                id = self.database.InsertIntoUsers(user)
                self.database.conn.commit()
                return make_response(jsonify({"id": id}),200)
            else:
                return make_response(jsonify({"id": id}),400)

        @self.app.route("/products/add", methods=["POST"])
        def add_product():
            addr = request.remote_addr
            if self.check_addr_requests(addr) == False:
                return make_response(jsonify("Blocked"), 429)
            req_data = request.json
            name = req_data["product name"]
            price = req_data["price"]
            product = m.Product(name, price)
            id = self.database.InsertIntoProducts(product)
            self.database.conn.commit()
            return make_response(jsonify({"id": id}),200)

        @self.app.route("/cart/add", methods=["POST"])
        def add_product_into_cart():
            addr = request.remote_addr
            if self.check_addr_requests(addr) == False:
                return make_response(jsonify("Blocked"), 429)
            req_data = request.json
            product = req_data["prod_id"]
            id = request.cookies.get("id")
            self.database.InsertIntoCart(id,product)
            return make_response(jsonify(""),200)

        @self.app.route("/user/auth", methods=["POST"])
        def authorization():
            addr = request.remote_addr
            if self.check_addr_requests(addr) == False:
                return make_response(jsonify("Blocked"), 429)
            req_data = request.json
            username = req_data.get("username")
            email = req_data.get("email")
            password = e.encryption(req_data.get("password"))
            user = m.User(username,email,password)
            user = self.database.SelectCurrentUser(user)
            if user != None:

                token = jwt.encode(payload={'username':user.username,
                                            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                                   key=self.app.config['SECRET_KEY'],
                                   algorithm= 'HS256'
                                   )
                r = make_response(jsonify({"status":"Authorized", "token":f"Bearer {token}"}), 200)
                return r
            return make_response(jsonify("Incorrect Credentials"), 429)

