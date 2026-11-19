class Product:
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
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

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None) -> "Product":
        """
        Создает новый объект Product или обновляет существующий.
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

        # Создаём новый объект через конструктор
        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        """
        Строковое представление товара.
        Формат: "Название продукта, X руб. Остаток: X шт."
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Сложение двух товаров: возвращает общую стоимость всех товаров на складе.
        Формула: (price1 * quantity1) + (price2 * quantity2)
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        return (self.price * self.quantity) + (other.price * other.quantity)
