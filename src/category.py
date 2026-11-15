from src.product import Product


class Category:
    """Класс, представляющий категорию товаров."""

    # Атрибуты класса (общие для всех объектов)
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = products  # Приватный список объектов класса Product

        # Автоматическое обновление атрибутов класса при создании объекта
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет новый товар в категорию.
        """
        self.__products.append(product)
        # При добавлении товара также увеличиваем общий счетчик товаров
        Category.product_count += 1

        @property
        def products(self) -> str:
            """
            Геттер для приватного атрибута __products.
            Возвращает строку с информацией о товарах в заданном формате.
            """
            result = []
            for product in self.__products:
                # Формируем строку для каждого товара
                result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

            # Объединяем все строки через перенос строки
            return "\n".join(result)