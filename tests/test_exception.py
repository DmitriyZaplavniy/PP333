import pytest
from src.exception import Product, Category

def test_product_zero_quantity():
    """
    Проверка исключения при создании товара с нулевым количеством.
    """
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Телевизор", "4K UHD", 50000.0, 0)

def test_average_price_with_products():
    """
    Проверка подсчета среднего ценника при наличии товаров.
    """
    product1 = Product("Телевизор", "4K UHD", 50000.0, 10)
    product2 = Product("Ноутбук", "16 ГБ ОЗУ", 80000.0, 5)
    category = Category("Электроника", "Техника для дома", [product1, product2])
    assert category.average_price() == 65000.0  # (50000 + 80000) / 2

def test_average_price_no_products():
    """
    Проверка подсчета среднего ценника при отсутствии товаров.
    """
    category = Category("Электроника", "Техника для дома")
    assert category.average_price() == 0

