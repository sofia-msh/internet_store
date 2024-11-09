from flask import jsonify, json
import requests
from Internet_Store.randoms import random_data


def user_reg(data):
    user_data = {"username": data.username, "email": data.email, "password": data.password}
    r = requests.post('http://127.0.0.1:5000/user/reg', json=user_data)
    return r.text.encode('utf-8').decode('unicode_escape')

def product_input():
    data = random_data.GetProduct()
    user_data = {"product name": data.name, "price": data.price}
    r = requests.post('http://127.0.0.1:5000/products', json=user_data)
    return r.text.encode('utf-8').decode('unicode_escape')

def user_sign_in(data):
    user_data = {"username": data.username, "password": data.password}
    r = requests.post('http://127.0.0.1:5000/user/auth', json=user_data)
    return r.text.encode('utf-8').decode('unicode_escape')

if __name__ == '__main__':
    user = random_data.GetUser(random_data.find_name_in_file("names.txt"))
    print(user_reg(user))
    #print(product_input())
    print(user_sign_in(user))
