class Product():
    def __init__(self, name, price, id=0):
        self.name = name
        self.price = price
        self.id = id

    def __str__(self):
        return f"id - {self.id}, name - {self.name}, price - {self.price}"


class Catalogue():
    def __init__(self, number, product_id, id=0):
        self.number = number
        self.product_id = product_id
        self.id = id

    def __str__(self):
        return f"id - {self.id}, number - {self.number}, product id - {self.product_id}"


class User():
    def __init__(self, username, email, password, id=0):
        self.username = username
        self.email = email
        self.password = password
        self.id = id

    def __repr__(self):
        return f"id - {self.id}, username - {self.username}, email - {self.email}, password - {self.password}"


class Favorites():
    def __init__(self, user_id, products_id, id=0):
        self.user_id = user_id
        self.products_id = products_id
        self.id = id

    def __str__(self):
        return f"id - {self.id}, user id - {self.user_id}, product id - {self.products_id}"


class JoinedFavorites():
    def __init__(self, user, products, id):
        self.user = user
        self.products = products
        self.id = id

    def __str__(self):
        return (f"favorites id - {self.id}, "
                f"product id - {self.products.id}, name - {self.products.name}, price - {self.products.price}"
                f"user id - {self.user.id}, username - {self.user.username}, email - {self.user.email}, password - {self.user.password}")


class Cart():
    def __init__(self, user_id, products_id, id=0):
        self.user_id = user_id
        self.products_id = products_id
        self.id = id

    def __str__(self):
        return f"id - {self.id}, user id - {self.user_id}, product id - {self.products_id}"


class JoinedCart():
    def __init__(self, user, products, id):
        self.user = user
        self.products = products
        self.id = id

    def __str__(self):
        return (f"cart id - {self.id}, "
                f"product id - {self.products.id}, name - {self.products.name}, price - {self.products.price}"
                f"user id - {self.user.id}, username - {self.user.username}, email - {self.user.email}, password - {self.user.password}")


class Orders():
    def __init__(self, user_id, products_id, id=0):
        self.user_id = user_id
        self.products_id = products_id
        self.id = id

    def __str__(self):
        return f"id - {self.id}, user id - {self.user_id}, product id - {self.products_id}"


class JoinedOrders():
    def __init__(self, user, products, id):
        self.user = user
        self.products = products
        self.id = id

    def __str__(self):
        return (f"order id - {self.id}, "
                f"product id - {self.products.id}, name - {self.products.name}, price - {self.products.price}"
                f"user id - {self.user.id}, username - {self.user.username}, email - {self.user.email}, password - {self.user.password}")
