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


class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        if len(self.name) > 10:
            logger.warning(f"Too many dishes: {self.name}")
            raise ValueError("Too many dishes")
        return f"{self.name}: {self.description} - {self.price}$"
