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
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self):
        """
        Геттер для атрибута цены.
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Сеттер для атрибута цены.
        :param value: Новое значение цены.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового продукта из словаря.
        :param product_data: Словарь с данными продукта.
        :return: Объект класса Product.
        """
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )


class Category:
    """
    Класс для представления категории товаров.
    """
    category_count = 0  # Счетчик категорий
    product_count = 0   # Счетчик товаров

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

        # Увеличиваем количество категорий
        Category.category_count += 1

        # Если переданы продукты, добавляем их
        if products:
            for product in products:
                self.__products.append(product)
                Category.product_count += 1  # Увеличиваем счетчик товаров

    def add_product(self, product):
        """
        Метод для добавления продукта в категорию.
        :param product: Объект класса Product.
        """
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик товаров

    @property
    def products(self):
        """
        Геттер для списка товаров.
        :return: Строка с информацией о товарах.
        """
        return "\n".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products])
