import pytest
from src.main import Product, Category, Smartphone, LawnGrass
def test_smartphone_initialization():
    """
    Проверка корректности инициализации объекта класса Smartphone.
    """
    smartphone = Smartphone("iPhone 15", "Смартфон Apple", 100000.0, 5, "High", "iPhone 15", "128GB", "Black")
    assert smartphone.name == "iPhone 15"
    assert smartphone.efficiency == "High"
    assert smartphone.color == "Black"

def test_lawn_grass_initialization():
    """
    Проверка корректности инициализации объекта класса LawnGrass.
    """
    lawn_grass = LawnGrass("Green Grass", "Газонная трава", 500.0, 100, "Россия", "2 недели", "Зеленый")
    assert lawn_grass.name == "Green Grass"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "2 недели"

def test_add_different_classes():
    """
    Проверка попытки сложения объектов разных классов.
    """
    smartphone = Smartphone("iPhone 15", "Смартфон Apple", 100000.0, 5, "High", "iPhone 15", "128GB", "Black")
    lawn_grass = LawnGrass("Green Grass", "Газонная трава", 500.0, 100, "Россия", "2 недели", "Зеленый")
    with pytest.raises(TypeError):
        smartphone + lawn_grass

def test_add_non_product():
    """
    Проверка попытки добавления непродукта в категорию.
    """
    category = Category("Электроника", "Техника для дома")
    with pytest.raises(TypeError):
        category.add_product("Телефон")  # Это строка, а не объект Product
