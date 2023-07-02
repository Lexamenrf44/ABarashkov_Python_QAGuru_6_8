import pytest
from models.models import Product, Cart


@pytest.fixture(scope='function', autouse=False)
def loaf():
    return Product("bread", 100, "This is bread", 300)


@pytest.fixture(scope='function', autouse=False)
def packet_of_juice():
    return Product("juice", 13, "This is a packet of juice", 100)


@pytest.fixture(scope='function', autouse=False)
def apple_pie():
    return Product("pie", 7.50, "This is a packet of juice", 200)


@pytest.fixture(scope='function', autouse=False)
def cart():
    return Cart()
