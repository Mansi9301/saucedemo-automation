import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage


class TestCart:

    def setup_method(self):
        """Runs before each test — stores page objects"""
        self.login_page = None
        self.cart_page = None

    def test_add_single_item_to_cart(self, driver):
        """Adding one item shows badge count of 1"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        cart = CartPage(driver)
        cart.add_first_item_to_cart()

        assert cart.get_cart_count() == 1

    def test_add_multiple_items_to_cart(self, driver):
        """Adding 3 items shows badge count of 3"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        cart = CartPage(driver)
        cart.add_multiple_items_to_cart(3)

        assert cart.get_cart_count() == 3

    def test_cart_page_shows_added_items(self, driver):
        """Items added appear correctly in cart page"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        cart = CartPage(driver)
        cart.add_multiple_items_to_cart(2)
        cart.go_to_cart()

        assert cart.get_cart_items_count() == 2

    def test_remove_item_from_cart(self, driver):
        """Removing item from cart reduces count"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        cart = CartPage(driver)
        cart.add_multiple_items_to_cart(2)
        cart.go_to_cart()
        cart.remove_first_item_from_cart()

        assert cart.get_cart_items_count() == 1

    def test_empty_cart_has_no_badge(self, driver):
        """Fresh login shows no cart badge"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        cart = CartPage(driver)

        assert cart.get_cart_count() == 0