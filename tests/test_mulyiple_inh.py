import pytest
from src.multiple_inheritance import Product, Smartphone, LawnGrass

def test_product_initialization():
    """
    Проверка инициализации объекта класса Product.
    """
    product = Product("Телевизор", "4K UHD", 50000.0, 10)
    assert product.name == "Телевизор"
    assert product.price == 50000.0
    assert product.quantity == 10

def test_smartphone_initialization():
    """
    Проверка инициализации объекта класса Smartphone.
    """
    smartphone = Smartphone("iPhone 15", "Смартфон Apple", 100000.0, 5, "High", "iPhone 15", "128GB", "Black")
    assert smartphone.name == "iPhone 15"
    assert smartphone.efficiency == "High"
    assert smartphone.color == "Black"

def test_lawn_grass_initialization():
    """
    Проверка инициализации объекта класса LawnGrass.
    """
    lawn_grass = LawnGrass("Green Grass", "Газонная трава", 500.0, 100, "Россия", "2 недели", "Зеленый")
    assert lawn_grass.name == "Green Grass"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "2 недели"

def test_log_mixin(capsys):
    """
    Проверка работы миксина LogMixin.
    """
    product = Product("Телевизор", "4K UHD", 50000.0, 10)
    captured = capsys.readouterr()
    print(captured.out)  # Отладочный вывод
    expected_output = "Создан объект класса Product с параметрами: name=Телевизор, description=4K UHD, price=50000.0, quantity=10"
    assert expected_output in captured.out

