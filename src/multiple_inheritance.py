from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """
    Абстрактный базовый класс для продуктов.
    """
    @abstractmethod
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
        self._price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        """
        Геттер для атрибута цены.
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """
        Сеттер для атрибута цены.
        :param value: Новое значение цены.
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Строковое представление продукта.
        """
        pass

class LogMixin:
    """
    Миксин для логирования создания объектов.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация миксина.
        """
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {self.__repr__()}")
        print("Миксин LogMixin вызван")  # Отладочный вывод

    def __repr__(self):
        """
        Строковое представление объекта для логирования.
        """
        return f"name={self.name}, description={self.description}, price={self._price}, quantity={self.quantity}"


    def __repr__(self):
        """
        Строковое представление объекта для логирования.
        """
        return f"name={self.name}, description={self.description}, price={self._price}, quantity={self.quantity}"


class Product(LogMixin, BaseProduct):
    """
    Класс для представления продукта.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта.
        """
        super().__init__(name, description, price, quantity)

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
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    def __str__(self):
        """
        Строковое представление продукта.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

class Smartphone(Product):
    """
    Класс для представления смартфона.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: str, color: str):
        """
        Инициализация смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс для представления травы газонной.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Инициализация травы газонной.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
