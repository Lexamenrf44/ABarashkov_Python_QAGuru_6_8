import pytest
from models.models import Product, Cart


@pytest.fixture(scope='function', autouse=False)
def product():
    return Product("book", 100, "This is book", 1000)


@pytest.fixture(scope='function', autouse=False)
def cart():
    return Cart()
