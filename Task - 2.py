# Task: 2 Для предыдущего проекта (Меню Ресторана)
# реализовать возможность добавления блюд из меню в заказ через оператор "+="

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


class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description} - {self.price}$"


class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes
        if len(self.dishes) > 10:
            logger.warning(f"Too many dishes: {self.name}")
            raise ValueError("Too many dishes")

    def __str__(self):
        menu_category_str = f"{self.name}:\n"
        for dish in self.dishes:
            menu_category_str += f"{dish}\n"
        return menu_category_str


class RestaurantMenu:
    def __init__(self, menu_categories):
        self.menu_categories = menu_categories

    def __str__(self):
        restaurant_menu_str = ""
        for menu_category in self.menu_categories:
            restaurant_menu_str += f"{menu_category}\n"
        return restaurant_menu_str


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item, quantity):
        for _ in range(quantity):
            self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def __iadd__(self, menu_item):
        if isinstance(menu_item, MenuCategory):
            for dish in menu_item.dishes:
                self.add_item(dish, 1)
        elif isinstance(menu_item, Dish):
            self.add_item(menu_item, 1)
        elif isinstance(menu_item, RestaurantMenu):
            for menu_category in menu_item.menu_categories:
                for dish in menu_category.dishes:
                    self.add_item(dish, 1)
        else:
            logger.info(f"Unknown type: {type(menu_item)}")
            raise TypeError("Unknown type")
        return self

    def __str__(self):
        order_str = f"Order for {self.customer_name}:\n"
        for item in self.items:
            order_str += f"{item.name}: {item.description} - {item.price}$\n"
        order_str += f"Total: {self.calculate_total()}$"
        return order_str


if __name__ == "__main__":

    dishes_1 = [
        Dish("Margherita", "Pizza with tomato sauce and mozzarella", 5.00),
        Dish("Marinara", "Pizza with tomato sauce, garlic and basil", 4.50),
        Dish("Salami", "Pizza with tomato sauce, mozzarella and salami", 6.00),
        Dish("Pepperoni", "Pizza with tomato sauce, mozzarella and pepperoni", 7.00),
        Dish("Carbonara", "Pizza with tomato sauce, mozzarella, parmesan, eggs, bacon", 7.50),
        Dish("Frutti di Mare", "Pizza with tomato sauce and seafood", 9.00),
        Dish("Crudo", "Pizza with tomato sauce, mozzarella and prosciutto", 7.50),
        Dish("Napoletana", "Pizza with tomato sauce, mozzarella, oregano, anchovies", 7.50),
    ]
    drinks = [
        Dish("Water 0.5", "Water with gas or without gas", 1.50),
        Dish("Cola 0.5", "Coca-Cola or Pepsi-Cola", 2.00),
        Dish("Tea", "Black or green tea", 1.00),
        Dish("Coffee", "Black or white coffee", 1.50),
        Dish("Juice", "Orange or apple juice", 2.00),

    ]

    pizzas = MenuCategory("Pizzas", dishes_1)
    drink = MenuCategory("Drinks", drinks)
    restaurant_menu = RestaurantMenu([pizzas, drink])

    # Создаем заказ
    order = Order("John")
    order_2 = Order("Jack")

    # Добавляем блюда из меню в заказ
    order += pizzas
    order_2 += drink
    # Выводим информацию о заказе
    print(order)
    print()
    print(order_2)