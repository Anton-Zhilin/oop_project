import pytest

from src.product import LawnGrass, Product, Smartphone


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


# НОВЫЕ ТЕСТЫ (для __str__ и __add__)


def test_product_str():
    """Проверка строкового представления товара (__str__)."""
    product = Product("Смартфон", "Мощный смартфон", 50000.0, 10)
    expected_str = "Смартфон, 50000.0 руб. Остаток: 10 шт."

    assert str(product) == expected_str


def test_product_add():
    """Проверка магического метода сложения (__add__) для одинаковых классов."""
    p1 = Product("Смартфон", "Описание", 50000.0, 10)
    p2 = Product("Ноутбук", "Описание", 120000.0, 5)

    # Оба объекта класса Product, сложение разрешено
    assert p1 + p2 == 1100000.0


def test_smartphone_add():
    """Проверка сложения для наследников (Smartphone + Smartphone)."""
    s1 = Smartphone("iPhone", "Описание", 100000.0, 2, 90.0, "15", 256, "Gray")
    s2 = Smartphone("Samsung", "Описание", 80000.0, 3, 85.0, "S23", 512, "Black")

    # 100000*2 + 80000*3 = 200000 + 240000 = 440000
    assert s1 + s2 == 440000.0


def test_product_add_different_classes_type_error():
    """
    Проверка, что __add__ вызывает TypeError при сложении разных классов продуктов.
    """
    s1 = Smartphone("iPhone", "Описание", 100000.0, 2, 90.0, "15", 256, "Gray")
    g1 = LawnGrass("Трава", "Описание", 500.0, 100, "Россия", "14 дней", "Зеленый")

    with pytest.raises(TypeError):
        s1 + g1


def test_product_add_parent_and_child_type_error():
    """
    Проверка, что нельзя сложить даже родителя и наследника (Product и Smartphone).
    """
    p1 = Product("Зарядка", "Описание", 1000.0, 10)
    s1 = Smartphone("iPhone", "Описание", 100000.0, 2, 90.0, "15", 256, "Gray")

    with pytest.raises(TypeError):
        p1 + s1


# НОВЫЕ ТЕСТЫ ДЛЯ МИКСИНА MixinRepr


def test_mixin_repr_product(capsys):
    """Проверка вывода информации о создании объекта Product."""
    # Не присваиваем переменной, так как проверяем только вывод в консоль (исправляет F841)
    Product("Продукт1", "Описание продукта", 1200, 10)

    captured = capsys.readouterr()
    assert captured.out == "Product('Продукт1', 'Описание продукта', 1200, 10)\n"


def test_mixin_repr_smartphone(capsys):
    """Проверка вывода информации о создании объекта Smartphone."""
    Smartphone("iPhone 15", "512GB", 210000.0, 8, 95.5, "iPhone 15", 512.0, "Gray")

    captured = capsys.readouterr()
    # Разбиваем длинную строку на части для соответствия PEP 8 (исправляет E501)
    expected_output = (
        "Smartphone('iPhone 15', '512GB', 210000.0, 8, "
        "efficiency=95.5, model='iPhone 15', memory=512.0, color='Gray')\n"
    )

    assert captured.out == expected_output


def test_mixin_repr_lawn_grass(capsys):
    """Проверка вывода информации о создании объекта LawnGrass."""
    LawnGrass("Трава газонная", "Для газона", 500.0, 100, "Россия", "14 дней", "Зеленый")

    captured = capsys.readouterr()
    # Разбиваем длинную строку на части для соответствия PEP 8 (исправляет E501)
    expected_output = (
        "LawnGrass('Трава газонная', 'Для газона', 500.0, 100, "
        "country='Россия', germination_period='14 дней', color='Зеленый')\n"
    )

    assert captured.out == expected_output
