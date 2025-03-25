from .models import Product, Category
from .utils import load_data_from_json

if __name__ == "__main__":
    # Загрузка данных из JSON
    categories = load_data_from_json("products.json")

    # Вывод информации о категориях и товарах
    for category in categories:
        print(f"Категория: {category.name}")
        for product in category.products:
            print(f"  Товар: {product.name}, Цена: {product.price}, Количество: {product.quantity}")

    # Вывод общего количества категорий и товаров
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

class Product:
    """
    Базовый класс для представления продукта.
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
        self.__price = price  # Приватный атрибут цены
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
        :param value: Новое значение цены.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

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

    def __str__(self):
        """
        Строковое представление продукта.
        :return: Строка в формате "Название продукта, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения продуктов.
        :param other: Другой объект класса Product.
        :return: Суммарная стоимость всех товаров на складе.
        """
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты класса Product")
        if type(self) != type(other):
            raise TypeError("Складывать можно только объекты одного класса")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """
    Класс для представления смартфона, наследник класса Product.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: str, color: str):
        """
        Инициализация смартфона.
        :param efficiency: Производительность смартфона.
        :param model: Модель смартфона.
        :param memory: Объем встроенной памяти.
        :param color: Цвет смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для представления травы газонной, наследник класса Product.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Инициализация травы газонной.
        :param country: Страна-производитель.
        :param germination_period: Срок прорастания.
        :param color: Цвет травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

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
                self.add_product(product)

    def add_product(self, product):
        """
        Метод для добавления продукта в категорию.
        :param product: Объект класса Product или его наследник.
        """
        if not issubclass(type(product), Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик товаров

    @property
    def products(self):
        """
        Геттер для списка товаров.
        :return: Строка с информацией о товарах.
        """
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        """
        Строковое представление категории.
        :return: Строка в формате "Название категории, количество продуктов: X шт."
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
