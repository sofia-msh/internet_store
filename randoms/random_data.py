import random
def read_file_into_list(file_path: str) -> list[str]:
    file = open(file_path, "r", encoding='utf-8')
    products_list = []
    for line in file:
        line = line[:len(line) - 1]
        products_list.append(line)
    return products_list

products = read_file_into_list("randoms/products.txt")

def get_some_from_products_lines(products: str) -> str:
    return random.choice(products)


def give_price_to_smth(low_cost: int, high_cost: int) -> int:
    return random.randint(low_cost, high_cost)
