"""
Протестируйте классы из модуля homework/models.py
"""
import pytest


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

            # Проверяем резульататы
            assert product.buy(2000) is ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        with pytest.raises(ValueError):
            assert cart.add_product(product, 0) is ValueError

        cart.add_product(product, 10)
        assert cart.products[product] == 10

