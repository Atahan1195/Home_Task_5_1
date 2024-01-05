import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

terminal_handler = logging.StreamHandler()
file_handler = logging.FileHandler('log.txt')

terminal_handler.setLevel(logging.DEBUG) # Записывать все сообщения уровня DEBUG и выше в терминал
file_handler.setLevel(logging.INFO)  # Записывать все сообщения уровня INFO и выше в файл

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
terminal_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(terminal_handler)
logger.addHandler(file_handler)


class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

    def __str__(self):
        menu_category_str = f"{self.name}:\n"
        for dish in self.dishes:
            menu_category_str += f"{dish}\n"
        return menu_category_str
