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
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров.
    """
    # Атрибуты класса для подсчета количества категорий и товаров
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.
        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров в категории.
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчик категорий
        Category.category_count += 1
        # Увеличиваем счетчик товаров на количество продуктов в категории
        Category.product_count += len(products)
