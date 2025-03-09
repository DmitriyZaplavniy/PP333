import pytest
from src.models import Product, Category

# Фикстура для создания тестового продукта
@pytest.fixture
def sample_product():
    return Product("Телевизор", "4K UHD", 50000.0, 10)

# Фикстура для создания тестовой категории
@pytest.fixture
def sample_category(sample_product):
    return Category("Электроника", "Техника для дома", [sample_product])

# Фикстура для сброса счетчиков перед каждым тестом
@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0

def test_product_initialization(sample_product):
    """
    Проверка корректности инициализации объекта класса Product.
    """
    assert sample_product.name == "Телевизор"
    assert sample_product.description == "4K UHD"
    assert sample_product.price == 50000.0
    assert sample_product.quantity == 10

def test_category_initialization(sample_category, sample_product):
    """
    Проверка корректности инициализации объекта класса Category.
    """
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома"
    assert sample_category.products == [sample_product]

def test_category_count(sample_category):
    """
    Проверка подсчета количества категорий.
    """
    assert Category.category_count == 1

def test_product_count(sample_category):
    """
    Проверка подсчета количества товаров.
    """
    assert Category.product_count == 1
