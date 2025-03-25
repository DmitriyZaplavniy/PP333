class Product:
    """
    Класс для представления продукта.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта.
        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта в наличии.
        """
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """
        Геттер для атрибута цены.
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Сеттер для атрибута цены.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        """
        Строковое представление продукта.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """
    Класс для представления категории товаров.
    """
    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализация категории.
        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в категории (опционально).
        """
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут списка товаров
        if products:
            for product in products:
                self.add_product(product)

    def add_product(self, product):
        """
        Метод для добавления продукта в категорию.
        :param product: Объект класса Product или его наследник.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)

    @property
    def products(self):
        """
        Геттер для списка товаров.
        :return: Строка с информацией о товарах.
        """
        return "\n".join(str(product) for product in self.__products)

    def average_price(self):
        """
        Метод для подсчета среднего ценника всех товаров в категории.
        :return: Средний ценник или 0, если товаров нет.
        """
        try:
            # Суммируем цены всех товаров
            total_price = sum(product.price for product in self.__products)
            # Подсчитываем количество уникальных товаров
            unique_products_count = len(self.__products)
            return total_price / unique_products_count
        except ZeroDivisionError:
            return 0

