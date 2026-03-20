# saucedemo-automation
# Saucedemo Automation Test Suite

Automated end-to-end test suite for [saucedemo.com](https://www.saucedemo.com) 
built with Python and Selenium WebDriver using the Page Object Model (POM) pattern.

## Tech Stack
- Python 3.11
- Selenium 4.41
- Pytest
- Webdriver Manager
- Page Object Model (POM)

## Test Coverage

### Login Tests (6)
- Valid login
- Invalid password
- Invalid username
- Empty username
- Empty password
- Locked out user

### Cart Tests (5)
- Add single item to cart
- Add multiple items to cart
- Cart page shows added items
- Remove item from cart
- Empty cart has no badge

### Checkout Tests (5)
- Complete end-to-end checkout flow
- Checkout without first name
- Checkout without last name
- Checkout without postal code
- Order summary shows total
- Cancel checkout returns to cart

## How to Run

### 1. Clone the repo
git clone https://github.com/YOURUSERNAME/saucedemo-automation.git
cd saucedemo-automation

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run all tests
pytest -v

### 5. Run specific test file
pytest tests/test_login.py -v
pytest tests/test_cart.py -v
pytest tests/test_checkout.py -v

### 6. Run with HTML report
pytest -v --html=reports/report.html
