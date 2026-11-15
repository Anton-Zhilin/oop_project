import pytest
from src.category import Category
from src.product import Product


def test_category_initialization():
    """Проверка корректности инициализации объектов класса Category."""
    prod1 = Product("Prod1", "Desc1", 10.0, 1)
    prod2 = Product("Prod2", "Desc2", 20.0, 2)

    category = Category("Test Category", "Category Description", [prod1, prod2])

    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert len(category.products) == 2
    # Проверяем, что в списке лежат именно те объекты, которые мы передали
    assert category.products[0] is prod1
    assert category.products[1] is prod2


def test_category_count():
    """Проверка подсчета количества категорий (атрибут класса category_count)."""
    # Изначально счетчик сброшен фикстурой и равен 0
    assert Category.category_count == 0

    prod1 = Product("Prod1", "Desc1", 10.0, 1)

    # Создаем первую категорию
    Category("Cat1", "Desc1", [prod1])
    assert Category.category_count == 1

    # Создаем вторую категорию (даже с пустым списком товаров)
    Category("Cat2", "Desc2", [])
    assert Category.category_count == 2