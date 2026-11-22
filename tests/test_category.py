import pytest

from src.category import AbstractCategory, Category, Order
from src.product import LawnGrass, Product, Smartphone
from src.exceptions import ZeroQuantityError


def test_category_initialization():
    """Проверка корректности инициализации объектов класса Category."""
    prod1 = Product("P1", "D1", 10.0, 1)
    prod2 = Product("P2", "D2", 20.0, 2)

    category = Category("Test Category", "Category Description", [prod1, prod2])

    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert "P1" in category.products
    assert "P2" in category.products


def test_add_product():
    """Проверка метода add_product и увеличения счетчика товаров."""
    category = Category("Cat", "Desc", [])
    prod = Product("P1", "D1", 10.0, 1)

    category.add_product(prod)

    assert Category.product_count == 1
    assert "P1" in category.products


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

    with pytest.raises(TypeError) as exc_info:
        category.add_product("Это строка, а не продукт")

    assert "Нельзя добавить объект типа str" in str(exc_info.value)


def test_add_product_invalid_type_int():
    """Проверка, что нельзя добавить число."""
    category = Category("Test", "Desc", [])

    with pytest.raises(TypeError):
        category.add_product(42)


def test_add_product_invalid_type_none():
    """Проверка, что нельзя добавить None."""
    category = Category("Test", "Desc", [])

    with pytest.raises(TypeError):
        category.add_product(None)


def test_products_getter_format():
    """Проверка формата строки, возвращаемой геттером products."""
    prod = Product("Phone", "Desc", 100.0, 5)
    category = Category("Cat", "Desc", [prod])

    expected_string = "Phone, 100.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected_string


def test_category_str():
    """Проверка строкового представления категории (__str__)."""
    p1 = Product("Смартфон", "Описание", 50000.0, 10)
    p2 = Product("Ноутбук", "Описание", 120000.0, 5)

    category = Category("Электроника", "Техника", [p1, p2])

    expected_str = "Электроника, количество продуктов: 15 шт."
    assert str(category) == expected_str


def test_category_count():
    """Проверка подсчета количества категорий."""
    Category.category_count = 0  # Сброс для чистоты теста

    Category("Cat1", "Desc1", [])
    assert Category.category_count == 1

    Category("Cat2", "Desc2", [])
    assert Category.category_count == 2


def test_order_initialization():
    """Проверка корректной инициализации заказа."""
    product = Product("Телефон", "Описание", 50000.0, 10)
    order = Order("Заказ №1", "Покупка телефона", product, 3)

    assert order.name == "Заказ №1"
    assert order.description == "Покупка телефона"
    assert order.product is product
    assert order.quantity == 3


def test_order_total_price():
    """Проверка вычисления итоговой стоимости заказа."""
    product = Product("Телефон", "Описание", 50000.0, 10)
    order = Order("Заказ №1", "Покупка", product, 3)

    # 50000 * 3 = 150000
    assert order.total_price == 150000.0


def test_order_str():
    """Проверка строкового представления заказа."""
    product = Product("Телефон", "Описание", 50000.0, 10)
    order = Order("Заказ №1", "Покупка телефона", product, 2)

    expected = (
        "Заказ №1, описание: 'Покупка телефона', "
        "товар: Телефон, количество: 2 шт., "
        "итоговая стоимость: 100000.0 руб."
    )
    assert str(order) == expected


def test_category_and_order_are_abstract_subclasses():
    """Проверка, что Category и Order — наследники AbstractCategory."""
    assert issubclass(Category, AbstractCategory)
    assert issubclass(Order, AbstractCategory)


def test_middle_price_with_products():
    """Проверка подсчёта средней цены при наличии товаров."""
    p1 = Product("Телефон", "Описание", 10000.0, 5)
    p2 = Product("Ноутбук", "Описание", 20000.0, 3)
    p3 = Product("Планшет", "Описание", 30000.0, 2)

    category = Category("Электроника", "Техника", [p1, p2, p3])

    # (10000 + 20000 + 30000) / 3 = 20000
    assert category.middle_price() == 20000.0


def test_middle_price_single_product():
    """Проверка средней цены при одном товаре."""
    p1 = Product("Телефон", "Описание", 15000.0, 5)
    category = Category("Смартфоны", "Техника", [p1])

    assert category.middle_price() == 15000.0


def test_middle_price_empty_category():
    """
    Проверка, что для пустой категории возвращается 0
    (обрабатывается ZeroDivisionError).
    """
    category = Category("Пустая категория", "Без товаров", [])

    assert category.middle_price() == 0


def test_add_product_success_messages(capsys):
    """
    Проверка, что при успешном добавлении товара
    выводятся сообщения об успехе и завершении обработки.
    """
    category = Category("Test", "Desc", [])
    product = Product("Телефон", "Описание", 50000.0, 5)

    category.add_product(product)

    captured = capsys.readouterr()
    assert "Товар Телефон добавлен в категорию Test." in captured.out
    assert "Обработка добавления товара в категорию 'Test' завершена." in captured.out



def test_order_success_messages(capsys):
    """
    Проверка, что при успешном создании заказа
    выводятся сообщения об успехе и завершении обработки.
    """
    product = Product("Телефон", "Описание", 50000.0, 5)

    Order("Заказ №1", "Покупка", product, 2)

    captured = capsys.readouterr()
    assert "Товар Телефон добавлен в заказ Заказ №1." in captured.out
    assert "Обработка добавления товара в заказ 'Заказ №1' завершена." in captured.out


def test_zero_quantity_error_default_message():
    """Проверка сообщения по умолчанию."""
    error = ZeroQuantityError()
    assert error.message == "Товар с нулевым количеством не может быть добавлен."