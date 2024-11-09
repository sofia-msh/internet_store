import os
import random
import string
from Internet_Store.model import models as m


def read_file_into_list(file_path: str) -> list[str]:
    scriptpath  = os.path.dirname(__file__)
    fullpath = os.path.join(scriptpath, file_path)
    file = open(fullpath, "r", encoding='utf-8')
    products_list = []
    for line in file:
        line = line[:len(line) - 1]
        products_list.append(line)
    return products_list


products = read_file_into_list("products.txt")


def get_some_from_products_lines() -> str:
    product = random.choice(products)
    products.remove(product)
    return product

def give_price_to_smth(low_cost: int, high_cost: int) -> int:
    return random.randint(low_cost, high_cost)

def GetProduct() -> m.Product:
    product = m.Product(get_some_from_products_lines(),give_price_to_smth(100,500))
    return product

def find_name_in_file(file_path) -> list[str]:
    scriptpath = os.path.dirname(__file__)
    fullpath = os.path.join(scriptpath, file_path)
    file = open(fullpath, "r", encoding='utf-8')
    namelists = []
    for line in file:
        line = line[:len(line) - 1]
        namelists.append(line)
    return UniqueElements(namelists, len(namelists))


def GetUsername(list_names: list[str]) -> str:
    username = random.choice(list_names)
    list_names.remove(username)
    return username


def GetEmail(username) -> str:
    email = username
    for i in range(5):
        email += str(random.randint(0,9))
    email += "@gmail.com"
    return email

def GetPassword() -> str:
    pas = ""
    for i in range(10):
        j = random.randint(0,1)
        if j == 0:
            pas += str(random.randint(0, 9))
        else:
            pas += random.choice(string.ascii_lowercase)
    return pas

def GetUser(list_names) -> m.User:
    username = GetUsername(list_names)
    email = GetEmail(username)
    password = GetPassword()
    user = m.User(username, email, password)
    return user

def UniqueElements(list: list, n: int) -> list:
    new_list = []
    dict = {}
    while n != len(new_list):
        b = random.choice(list)
        if b in dict:
            continue
        dict[b] = 1
        new_list.append(b)
    return new_list
