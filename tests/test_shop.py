"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models.models import Product, Cart


@pytest.fixture()
def product():
    return Product("book", 100, "This is book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):

        # TODO напишите проверки на метод check_quantity

        # Проверяем результаты
        assert product.check_quantity(50) == True
        assert product.check_quantity(1050) == False

    def test_product_buy(self, product):

        # TODO напишите проверки на метод buy
        product.buy(50)

        # Проверяем результаты
        assert product.quantity == 950

    def test_product_buy_more_than_available(self, product):

        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(2000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 100)

        # Проверяем резульататы
        assert cart.products[product] == 100

        cart.add_product(product, 100)

        # Проверяем резульататы
        assert cart.products[product] == 200

    def test_remove_product(self, cart, product):
        cart.add_product(product, 50)
        cart.remove_product(product)

        # Проверяем резульататы
        assert product not in cart.products

        cart.add_product(product, 50)
        cart.remove_product(product, 50)

        # Проверяем резульататы
        assert product not in cart.products

        cart.add_product(product, 50)
        cart.remove_product(product, 30)

        # Проверяем резульататы
        assert cart.products[product] == 20

        cart.add_product(product, 50)
        cart.remove_product(product, 100)

        # Проверяем резульататы
        assert product not in cart.products

    def test_clear(self, cart, product):
        cart.add_product(product, 50)

        cart.clear()

        # Проверяем резульататы
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 50)

        cart.get_total_price()

        # Проверяем резульататы
        assert cart.get_total_price() == 5000

    def test_buy(self, cart, product):
        cart.add_product(product, 50)
        cart.buy()

        # Проверяем резульататы
        assert product.quantity == 950

    def test_buy_with_error(self, cart, product):
        cart.add_product(product, 1010)

        with pytest.raises(ValueError):
            cart.buy()

