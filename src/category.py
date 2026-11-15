class Category:
    """Класс, представляющий категорию товаров."""

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = products  # Список объектов класса Product