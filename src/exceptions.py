class ZeroQuantityError(Exception):
    """
    Исключение, которое вызывается при попытке добавить товар
    с нулевым количеством в категорию или заказ.
    """

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен.") -> None:
        super().__init__(message)
        self.message = message
