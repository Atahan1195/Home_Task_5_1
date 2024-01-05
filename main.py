from dish import Dish
from menu_category import MenuCategory


class RestaurantMenu:
    def __init__(self, menu_categories):
        self.menu_categories = menu_categories

    def __str__(self):
        restaurant_menu_str = ""
        for menu_category in self.menu_categories:
            restaurant_menu_str += f"{menu_category}\n"
        return restaurant_menu_str


if __name__ == "__main__":
    dishes = [
        Dish("Margherita", "Pizza with tomato sauce and mozzarella", 5.00),
        Dish("Marinara", "Pizza with tomato sauce, garlic and basil", 4.50),
        Dish("Salami", "Pizza with tomato sauce, mozzarella and salami", 6.00),
        Dish("Pepperoni", "Pizza with tomato sauce, mozzarella and pepperoni", 7.00),

    ]
    drinks = [
        Dish("Water 0.5", "Water with gas or without gas", 1.50),
        Dish("Cola 0.5", "Coca-Cola or Pepsi-Cola", 2.00),
        Dish("Tea", "Black or green tea", 1.00),
    ]

    pizzas = MenuCategory("Pizzas", dishes)
    drink = MenuCategory("Drinks", drinks)
    restaurant_menu = RestaurantMenu([pizzas, drink])
    print(restaurant_menu)

