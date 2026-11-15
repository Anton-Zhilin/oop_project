import pytest
from src.product import Product


def test_product_initialization():
    """Проверка корректности инициализации объектов класса Product."""
    product = Product("Test Phone", "Test Description", 99999.99, 5)

    assert product.name == "Test Phone"
    assert product.description == "Test Description"
    assert product.price == 99999.99
    assert product.quantity == 5


def test_new_product_creation():
    """Проверка создания нового товара через класс-метод new_product."""
    data = {"name": "New Phone", "description": "Desc", "price": 50000.0, "quantity": 2}
    product = Product.new_product(data, [])

    assert product.name == "New Phone"
    assert product.price == 50000.0
    assert product.quantity == 2


def test_new_product_merge():
    """Проверка объединения товаров с одинаковым именем в new_product."""
    data1 = {"name": "Phone", "description": "Desc", "price": 10000.0, "quantity": 5}
    data2 = {"name": "Phone", "description": "Desc", "price": 12000.0, "quantity": 3}

    p1 = Product.new_product(data1, [])
    products_list = [p1]

    p2 = Product.new_product(data2, products_list)

    # Должен вернуться тот же объект
    assert p1 is p2
    # Количество должно сложиться
    assert p1.quantity == 8
    # Цена должна обновиться на более высокую
    assert p1.price == 12000.0


def test_price_setter_valid():
    """Проверка установки валидной цены через сеттер."""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0


def test_price_setter_invalid(capsys):
    """Проверка блокировки нулевой или отрицательной цены."""
    product = Product("Test", "Desc", 100.0, 5)

    # Пытаемся установить отрицательную цену
    product.price = -10.0

    # Проверяем, что цена не изменилась
    assert product.price == 100.0

    # Проверяем, что в консоль вывелось нужное сообщение
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out