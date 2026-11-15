class Product:
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.price = price  # Цена (с учетом копеек)
        self.quantity = quantity  # Количество в наличии (в штуках)