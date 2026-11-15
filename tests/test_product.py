import pytest
from src.product import Product
from src.category import Category


def test_product_initialization():
    """Проверка корректности инициализации объектов класса Product."""
    product = Product("Test Phone", "Test Description", 99999.99, 5)

    assert product.name == "Test Phone"
    assert product.description == "Test Description"
    assert product.price == 99999.99
    assert product.quantity == 5


def test_product_count():
    """Проверка подсчета количества продуктов (атрибут класса product_count)."""
    # Изначально счетчик сброшен фикстурой и равен 0
    assert Category.product_count == 0

    prod1 = Product("Prod1", "Desc1", 10.0, 1)
    prod2 = Product("Prod2", "Desc2", 20.0, 2)

    # Создаем категорию с 2 товарами
    Category("Cat1", "Desc1", [prod1, prod2])
    assert Category.product_count == 2

    # Создаем еще одну категорию с 1 товаром
    prod3 = Product("Prod3", "Desc3", 30.0, 3)
    Category("Cat2", "Desc2", [prod3])
    assert Category.product_count == 3  # 2 + 1 = 3