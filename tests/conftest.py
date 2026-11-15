import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """
    Фикстура, которая автоматически сбрасывает атрибуты класса
    перед каждым тестом, чтобы обеспечить независимость тестов.
    """
    Category.category_count = 0
    Category.product_count = 0
    yield
    # Сброс после теста (на случай, если нужно чистить состояние)
    Category.category_count = 0
    Category.product_count = 0
