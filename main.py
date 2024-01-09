# Task - 1 Для предыдущего проекта (Заказ продуктов в магазине) реализовать возможность
# объединения двух корзин в одну с помощью оператора "+=".

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

terminal_handler.setLevel(logging.DEBUG)  # Записывать все сообщения уровня DEBUG и выше в терминал
file_handler.setLevel(logging.INFO)  # Записывать все сообщения уровня INFO и выше в файл

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
terminal_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)


class Product:
    """Class for product
    Attributes:
        name (str): name of product
        price (int): price of product
        description (str): description of product
    """

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Product: {self.name}, price: {self.price}, description: {self.description}"


class Cart:
    """
    Class for cart
    Attributes:
        customer_name (str): name of customer
        products (dict): dictionary of products
    """

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.products = {}

    def add_product(self, product, quantity):
        """
        Add product to cart
        :param product: product
        :param quantity: quantity of product
        :return: None
        """

        if product not in self.products:
            self.products[product] = 0
        self.products[product] += quantity

    def calculate_total(self):
        """
        Calculate total price of cart
        :return: total price
        """

        total = 0
        for product, quantity in self.products.items():
            total += product.price * quantity
        return total

    def __iadd__(self, other_cart):
        """
        Overload the += operator to combine two carts
        :param other_cart: another cart to be combined
        :return:  cart
        """
        if not isinstance(other_cart, Cart):
            logger.info(f"Unsupported type: {type(other_cart)}")
            raise TypeError("Unsupported type for addition to cart")

        for product, quantity in other_cart.products.items():
            self.add_product(product, quantity)

        return self

    def __str__(self):
        """
        String representation of cart
        :return: string
        """

        cart_str = f""
        for product, quantity in self.products.items():
            cart_str += f"{product.name}: {product.description} - {quantity}\n"
        cart_str += f"Total: {self.calculate_total()}$"
        return cart_str


if __name__ == "__main__":
    cart = Cart(input("Enter your name: "))

    product_1 = Product("Apple", 10, "Green apple")
    product_2 = Product("Orange", 20, "Orange orange")
    product_3 = Product("Banana", 30, "Yellow banana")
    product_4 = Product("Pineapple", 40, "Yellow pineapple")
    product_5 = Product("Grape", 50, "Purple grape")

    cart.add_product(product_1, 2)
    cart.add_product(product_2, 3)
    cart.add_product(product_3, 4)
    cart.add_product(product_4, 5)
    cart.add_product(product_5, 6)
    print(f'Your first cart: \n{cart}\n')

    cart2 = Cart(cart)

    cart2.add_product(product_5, 2)
    cart2.add_product(product_4, 3)
    print(f'Your second cart: \n{cart2}\n')

    cart += cart2

    print(f'Total for everything \n{cart}')










