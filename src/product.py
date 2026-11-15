class Product:
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.price = price  # При присваивании автоматически вызывается сеттер
        self.quantity = quantity  # Количество в наличии (в штуках)

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута __price."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута __price с проверками."""
        # 1. Проверка на нулевую или отрицательную цену
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Получаем текущую цену, если она уже установлена
        current_price = getattr(self, '_Product__price', None)

        # 2. Логика подтверждения при понижении цены
        # Если цена уже была установлена И новая цена меньше текущей
        if current_price is not None and new_price < current_price:
            user_input = input(f"Цена понижается с {current_price} до {new_price}. Подтвердите (y/n): ")
            if user_input.strip().lower() == 'y':
                self.__price = new_price
            else:
                print("Отмена изменения цены.")
        else:
            # Если цена повышается или это первичная установка (current_price is None)
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, products_list: list) -> 'Product':
        """
        Создает новый объект Product или обновляет существующий, если товар с таким именем уже есть.
        """
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        for product in products_list:
            if product.name == name:
                product.quantity += quantity
                product.price = price
                return product

        return cls(name, description, price, quantity)