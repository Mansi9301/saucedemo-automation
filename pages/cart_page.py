from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    # Locators
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_primary.btn_inventory")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn_secondary.btn_inventory")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_item_to_cart(self):
        """Adds the first item on the inventory page to cart"""
        add_buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTON)
        )
        add_buttons[0].click()

    def add_multiple_items_to_cart(self, count):
        """Adds multiple items to cart by count"""
        add_buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTON)
        )
        for i in range(count):
            add_buttons[i].click()

    def get_cart_count(self):
        """Returns the number shown on cart badge"""
        try:
            badge = self.wait.until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        """Clicks the cart icon to open cart page"""
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def get_cart_items_count(self):
        """Returns number of items in cart page"""
        try:
            items = self.wait.until(
                EC.presence_of_all_elements_located(self.CART_ITEMS)
            )
            return len(items)
        except:
            return 0

    def remove_first_item_from_cart(self):
        """Removes first item from cart page"""
        remove_buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".btn_secondary.cart_button")
            )
        )
        remove_buttons[0].click()

    def continue_shopping(self):
        """Clicks continue shopping button"""
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        ).click()