import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, driver):
        """Valid user can log in successfully"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        # After login, URL should change to inventory page
        assert "inventory" in driver.current_url

    def test_invalid_password(self, driver):
        """Wrong password shows error message"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "wrong_password")

        error = login.get_error_message()
        assert "Username and password do not match" in error

    def test_invalid_username(self, driver):
        """Wrong username shows error message"""
        login = LoginPage(driver)
        login.open()
        login.login("wrong_user", "secret_sauce")

        error = login.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_username(self, driver):
        """Empty username shows error message"""
        login = LoginPage(driver)
        login.open()
        login.login("", "secret_sauce")

        error = login.get_error_message()
        assert "Username is required" in error

    def test_empty_password(self, driver):
        """Empty password shows error message"""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "")

        error = login.get_error_message()
        assert "Password is required" in error

    def test_locked_out_user(self, driver):
        """Locked out user sees specific error message"""
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", "secret_sauce")

        error = login.get_error_message()
        assert "locked out" in error