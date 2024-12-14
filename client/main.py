from flask import jsonify, json
import requests
from Internet_Store.randoms import random_data
import time


def user_reg(data):
    user_data = {"username": data.username, "email": data.email, "password": data.password}
    r = requests.post('http://127.0.0.1:5000/user/reg', json=user_data)
    if r.status_code == 200:
        return f"Registered, id - {r.json()}"
    elif r.status_code == 400:
        return f"Username already taken, id {r.json()}"
    elif r.status_code == 429:
        return f"IP {r.json()} is blocked"

def product_input():
    data = random_data.GetProduct()
    user_data = {"product name": data.name, "price": data.price}
    r = requests.post('http://127.0.0.1:5000/products/add', json=user_data)
    return r.json()["id"]

def user_sign_in(data):
    user_data = {"username": data.username, "password": data.password}
    r = requests.post('http://127.0.0.1:5000/user/auth', json=user_data)
    return r.json()

def insert_into_cart(id_product):
    user_data = {"prod_id": id_product}
    r = requests.post('http://127.0.0.1:5000/cart/add', json=user_data)
    return r.text

if __name__ == '__main__':
    user = random_data.GetUser(random_data.find_name_in_file("names.txt"))
    print(user_reg(user))
    print(user_sign_in(user))
    print(insert_into_cart(4))

