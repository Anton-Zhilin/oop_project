from abc import ABC, abstractmethod

from src.product import Product


class AbstractCategory(ABC):
    """Абстрактный базовый класс для Категории и Заказа."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass


class Category(AbstractCategory):
    """Класс, представляющий категорию товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        super().__init__(name, description)
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в приватный список товаров.
        Проверяет, что product является экземпляром Product или его наследника.
        """
        if not isinstance(product, Product):
            raise TypeError(
                f"Нельзя добавить объект типа {type(product).__name__}. "
                "Можно добавлять только объекты класса Product или его наследников."
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер для приватного атрибута __products.
        """
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def __str__(self) -> str:
        """
        Строковое представление категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Order(AbstractCategory):
    """
    Класс, представляющий заказ.
    Содержит ссылку на один товар, количество и итоговую стоимость.
    """

    def __init__(self, name: str, description: str, product: Product, quantity: int) -> None:
        super().__init__(name, description)
        self.__product = product
        self.__quantity = quantity

    @property
    def product(self) -> Product:
        """Геттер для товара заказа."""
        return self.__product

    @property
    def quantity(self) -> int:
        """Геттер для количества товара в заказе."""
        return self.__quantity

    @property
    def total_price(self) -> float:
        """Вычисляемое свойство: итоговая стоимость заказа."""
        return self.__product.price * self.__quantity

    def __str__(self) -> str:
        """
        Строковое представление заказа.
        """
        return (
            f"{self.name}, описание: '{self.description}', "
            f"товар: {self.__product.name}, "
            f"количество: {self.__quantity} шт., "
            f"итоговая стоимость: {self.total_price} руб."
        )
