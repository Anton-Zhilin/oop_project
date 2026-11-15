class Category:
    """Класс, представляющий категорию товаров."""

    # Атрибуты класса (общие для всех объектов)
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.products = products  # Список объектов класса Product

        # Автоматическое обновление атрибутов класса при создании объекта
        Category.category_count += 1
        Category.product_count += len(self.products)

