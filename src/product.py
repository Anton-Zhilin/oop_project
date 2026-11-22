from abc import ABC, abstractmethod


class MixinRepr:
    """
    Класс-миксин для вывода информации о создании объекта.
    При инициализации выводит в консоль имя класса и переданные параметры.
    """

    def __init__(self, *args, **kwargs):
        # Сначала вызываем __init__ следующего класса в MRO
        super().__init__(*args, **kwargs)

        # Формируем строку с параметрами
        params = [repr(arg) for arg in args]
        params += [f"{key}={repr(value)}" for key, value in kwargs.items()]

        # Выводим информацию о создании объекта
        print(f"{self.__class__.__name__}({', '.join(params)})")


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs) -> None:
        """Инициализация общих атрибутов продукта."""
        self.name = name
        self.description = description
        self.price = price  # Вызывает сеттер
        self.quantity = quantity
        # kwargs игнорируются — они нужны только для передачи через цепочку наследования

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Абстрактный сеттер для цены."""
        pass

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None) -> "BaseProduct":
        """
        Создает новый объект продукта или обновляет существующий.
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        # Проверка дубликатов, если список передан
        if products_list:
            for product in products_list:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        # Создаём новый объект через конструктор класса
        return cls(name, description, price, quantity)

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового представления."""
        pass

    def __add__(self, other: "BaseProduct") -> float:
        """
        Сложение двух товаров: возвращает общую стоимость всех товаров на складе.
        Складывать можно только товары одинаковых классов.
        """
        # Используем 'is not' вместо '!=' для сравнения типов (исправляет E721)
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одинаковых классов")

        return (self.price * self.quantity) + (other.price * other.quantity)


class Product(MixinRepr, BaseProduct):
    """Класс, представляющий товар (конкретная реализация BaseProduct)."""

    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs) -> None:
        # Передаем все аргументы (включая kwargs) через цепочку наследования
        super().__init__(name, description, price, quantity, **kwargs)

        # Инициализация атрибутов Product
        self.name = name
        self.description = description
        self.price = price  # Вызывает сеттер
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута __price."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута __price с проверкой на положительность."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self.__price = new_price

    def __str__(self) -> str:
        """
        Строковое представление товара.
        Формат: "Название продукта, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    """Класс, представляющий смартфон (наследник Product)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: float,
        color: str,
    ) -> None:
        # Передаем все аргументы через super(), уникальные — как kwargs
        super().__init__(
            name, description, price, quantity, efficiency=efficiency, model=model, memory=memory, color=color
        )
        # Инициализация уникальных атрибутов
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс, представляющий газонную траву (наследник Product)."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        # Передаем все аргументы через super(), уникальные — как kwargs
        super().__init__(
            name, description, price, quantity, country=country, germination_period=germination_period, color=color
        )
        # Инициализация уникальных атрибутов
        self.country = country
        self.germination_period = germination_period
        self.color = color
