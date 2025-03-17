import pytest
from src.models import Product, Category

# Фикстура для создания тестового продукта
@pytest.fixture
def sample_product():
    return Product("Телевизор", "4K UHD", 50000.0, 10)

# Фикстура для создания тестовой категории
@pytest.fixture
def sample_category():
    return Category("Электроника", "Техника для дома")

def test_product_initialization(sample_product):
    """
    Проверка корректности инициализации объекта класса Product.
    """
    assert sample_product.name == "Телевизор"
    assert sample_product.description == "4K UHD"
    assert sample_product.price == 50000.0
    assert sample_product.quantity == 10

def test_category_initialization(sample_category):
    """
    Проверка корректности инициализации объекта класса Category.
    """
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома"

def test_add_product(sample_category, sample_product):
    """
    Проверка добавления продукта в категорию.
    """
    sample_category.add_product(sample_product)
    assert "Телевизор, 50000.0 руб. Остаток: 10 шт." in sample_category.products

def test_product_price_setter(sample_product):
    """
    Проверка сеттера для цены продукта.
    """
    sample_product.price = -100
    assert sample_product.price == 50000.0  # Цена не должна измениться

    sample_product.price = 60000.0
    assert sample_product.price == 60000.0  # Цена успешно изменилась

def test_new_product():
    """
    Проверка создания продукта через класс-метод.
    """
    product_data = {
        "name": "Ноутбук",
        "description": "16 ГБ ОЗУ",
        "price": 80000.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)
    assert product.name == "Ноутбук"
    assert product.price == 80000.0
    assert product.quantity == 5

def test_category_count():
    """
    Проверка подсчета количества категорий.
    """
    # Сбрасываем счетчик перед тестом
    Category.category_count = 0

    # Создаем несколько категорий
    category1 = Category("Электроника", "Техника для дома")
    category2 = Category("Одежда", "Модная одежда")
    category3 = Category("Мебель", "Мебель для дома")

    # Проверяем значение счетчика
    assert Category.category_count == 3

def test_product_count(sample_category, sample_product):
    """
    Проверка подсчета количества товаров.
    """
    # Сбрасываем счетчик перед тестом
    Category.product_count = 0

    # Добавляем продукты в категорию
    sample_category.add_product(sample_product)
    sample_category.add_product(Product("Ноутбук", "16 ГБ ОЗУ", 80000.0, 5))

    # Проверяем значение счетчика
    assert Category.product_count == 2

def test_product_str(sample_product):
    """
    Проверка строкового представления продукта.
    """
    assert str(sample_product) == "Телевизор, 50000.0 руб. Остаток: 10 шт."

def test_category_str(sample_category, sample_product):
    """
    Проверка строкового представления категории.
    """
    sample_category.add_product(sample_product)
    assert str(sample_category) == "Электроника, количество продуктов: 10 шт."

def test_product_addition():
    """
    Проверка сложения продуктов.
    """
    product1 = Product("Телевизор", "4K UHD", 50000.0, 10)
    product2 = Product("Ноутбук", "16 ГБ ОЗУ", 80000.0, 5)
    total_value = product1 + product2
    assert total_value == 900000.0  # 50000 * 10 + 80000 * 5 = 900000

