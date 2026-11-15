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

        # Если нужно подтверждение при понижении цены (может мешать тестам):
        # current_price = getattr(self, '_Product__price', None)
        # if current_price is not None and new_price < current_price:
        #     user_input = input(f"Цена понижается с {current_price} до {new_price}. Подтвердите (y/n): ")
        #     if user_input.strip().lower() != 'y':
        #         print("Отмена изменения цены.")
        #         return

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
