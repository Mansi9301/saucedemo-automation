import pytest
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


class TestCheckout:

    def login(self, driver):
        """Helper to log in before each test"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

    def test_complete_checkout_flow(self, driver):
        """Full end-to-end purchase flow completes successfully"""
        self.login(driver)

        checkout = CheckoutPage(driver)
        checkout.add_item_and_go_to_cart()
        checkout.complete_checkout("Mansi", "Patel", "S4T 2B3")

        success = checkout.get_success_message()
        assert "Thank you" in success

    def test_checkout_without_first_name(self, driver):
        """Missing first name shows error on checkout form"""
        self.login(driver)

        checkout = CheckoutPage(driver)
        checkout.add_item_and_go_to_cart()
        checkout.click_checkout()
        checkout.fill_shipping_info("", "Patel", "S4T 2B3")
        checkout.click_continue()

        error = checkout.get_error_message()
        assert "First Name is required" in error

    def test_checkout_without_last_name(self, driver):
        """Missing last name shows error on checkout form"""
        self.login(driver)

        checkout = CheckoutPage(driver)
        checkout.add_item_and_go_to_cart()
        checkout.click_checkout()
        checkout.fill_shipping_info("Mansi", "", "S4T 2B3")
        checkout.click_continue()

        error = checkout.get_error_message()
        assert "Last Name is required" in error

    def test_checkout_without_postal_code(self, driver):
        """Missing postal code shows error on checkout form"""
        self.login(driver)

        checkout = CheckoutPage(driver)
        checkout.add_item_and_go_to_cart()
        checkout.click_checkout()
        checkout.fill_shipping_info("Mansi", "Patel", "")
        checkout.click_continue()

        error = checkout.get_error_message()
        assert "Postal Code is required" in error

    def test_order_summary_shows_total(self, driver):
        """Order summary page displays a total price"""
        self.login(driver)

        checkout = CheckoutPage(driver)
        checkout.add_item_and_go_to_cart()
        checkout.click_checkout()
        checkout.fill_shipping_info("Mansi", "Patel", "S4T 2B3")
        checkout.click_continue()

        total = checkout.get_order_total()
        assert "Total:" in total

    def test_cancel_checkout_returns_to_cart(self, driver):
        """Cancelling checkout returns user to cart page"""
        self.login(driver)

        checkout = CheckoutPage(driver)
        checkout.add_item_and_go_to_cart()
        checkout.click_checkout()
        checkout.click_cancel()

        assert "cart" in driver.current_url