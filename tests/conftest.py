import pytest
from src.category import Category

@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасывает атрибуты класса перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield