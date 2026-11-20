import pytest


from src.category import Category
from src.product import Product, Smartphone, LawnGrass


def test_category_initialization():
    """Проверка корректности инициализации объектов класса Category."""
    prod1 = Product("P1", "D1", 10.0, 1)
    prod2 = Product("P2", "D2", 20.0, 2)

    category = Category("Test Category", "Category Description", [prod1, prod2])

    assert category.name == "Test Category"
    assert category.description == "Category Description"

    # Так как products теперь строка, проверяем наличие имен товаров в ней
    assert "P1" in category.products
    assert "P2" in category.products


def test_add_product():
    """Проверка метода add_product и увеличения счетчика товаров."""
    category = Category("Cat", "Desc", [])
    prod = Product("P1", "D1", 10.0, 1)

    category.add_product(prod)

    # Проверяем, что счетчик класса увеличился
    assert Category.product_count == 1
    # Проверяем, что товар появился в строке геттера
    assert "P1" in category.products


def test_products_getter_format():
    """Проверка формата строки, возвращаемой геттером products."""
    prod = Product("Phone", "Desc", 100.0, 5)
    category = Category("Cat", "Desc", [prod])

    expected_string = "Phone, 100.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected_string


def test_category_count():
    """Проверка подсчета количества категорий."""
    assert Category.category_count == 0

    Category("Cat1", "Desc1", [])
    assert Category.category_count == 1

    Category("Cat2", "Desc2", [])
    assert Category.category_count == 2


# НОВЫЙ ТЕСТ (для __str__)


def test_category_str():
    """Проверка строкового представления категории (__str__)."""
    p1 = Product("Смартфон", "Описание", 50000.0, 10)
    p2 = Product("Ноутбук", "Описание", 120000.0, 5)

    category = Category("Электроника", "Техника", [p1, p2])

    # Сумма quantity: 10 + 5 = 15
    expected_str = "Электроника, количество продуктов: 15 шт."
    assert str(category) == expected_str


def test_add_product_valid():
    """Проверка добавления валидного продукта."""
    category = Category("Test", "Desc", [])
    product = Product("Phone", "Desc", 100.0, 5)

    category.add_product(product)

    assert Category.product_count == 1
    assert "Phone" in category.products


def test_add_product_smartphone():
    """Проверка добавления наследника Smartphone."""
    category = Category("Test", "Desc", [])
    smartphone = Smartphone("iPhone", "Desc", 100000.0, 2, 90.0, "15", 256, "Gray")

    category.add_product(smartphone)

    assert Category.product_count == 1
    assert "iPhone" in category.products


def test_add_product_lawn_grass():
    """Проверка добавления наследника LawnGrass."""
    category = Category("Test", "Desc", [])
    grass = LawnGrass("Трава", "Desc", 500.0, 100, "Россия", "14 дней", "Зеленый")

    category.add_product(grass)

    assert Category.product_count == 1
    assert "Трава" in category.products


def test_add_product_invalid_type():
    """Проверка, что нельзя добавить объект неподходящего типа."""
    category = Category("Test", "Desc", [])

    # Пытаемся добавить строку
    with pytest.raises(TypeError) as exc_info:
        category.add_product("Это строка, а не продукт")

    assert "Нельзя добавить объект типа str" in str(exc_info.value)


