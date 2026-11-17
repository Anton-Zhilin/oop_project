class CategoryIterator:
    """
    Вспомогательный класс-итератор для перебора товаров в категории.
    """

    def __init__(self, category):
        self.category = category
        self.index = 0  # Индекс текущего товара

    def __iter__(self):
        return self

    def __next__(self):
        # Получаем доступ к приватному списку товаров категории
        products = self.category._Category__products

        if self.index < len(products):
            # Получаем текущий товар
            product = products[self.index]
            # Увеличиваем индекс для следующего вызова
            self.index += 1
            return product
        else:
            # Если товары закончились, прерываем итерацию
            raise StopIteration

