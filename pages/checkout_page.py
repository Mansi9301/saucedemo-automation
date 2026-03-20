from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    # Locators
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".btn_primary.btn_inventory")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    CANCEL_BUTTON = (By.ID, "cancel")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_item_and_go_to_cart(self):
        """Adds first item and navigates to cart"""
        add_buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS)
        )
        add_buttons[0].click()
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def click_checkout(self):
        """Clicks checkout button from cart page"""
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

    def fill_shipping_info(self, first_name, last_name, postal_code):
        """Fills in the shipping information form"""
        first = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME)
        )
        first.click()
        first.send_keys(first_name)

        last = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME)
        )
        last.click()
        last.send_keys(last_name)

        postal = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE)
        )
        postal.click()
        postal.send_keys(postal_code)

    def click_continue(self):
        """Clicks continue after filling shipping info"""
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def click_finish(self):
        """Clicks finish to complete the order"""
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def get_success_message(self):
        """Returns the order success message text"""
        return self.wait.until(
            EC.presence_of_element_located(self.SUCCESS_MESSAGE)
        ).text

    def get_error_message(self):
        """Returns error message text"""
        return self.wait.until(
            EC.presence_of_element_located(self.ERROR_MESSAGE)
        ).text

    def get_order_total(self):
        """Returns the total price shown on summary page"""
        return self.wait.until(
            EC.presence_of_element_located(self.SUMMARY_TOTAL)
        ).text

    def click_cancel(self):
        """Cancels checkout and goes back"""
        self.wait.until(
            EC.element_to_be_clickable(self.CANCEL_BUTTON)
        ).click()

    def complete_checkout(self, first_name, last_name, postal_code):
        """Full checkout flow in one method"""
        import time
        self.click_checkout()
        time.sleep(1)
        self.fill_shipping_info(first_name, last_name, postal_code)
        time.sleep(1)
        self.click_continue()
        time.sleep(1)
        self.click_finish()
   