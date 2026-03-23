# saucedemo-automation
## About This Project

This project is an end-to-end automated test suite for a web-based 
e-commerce application (saucedemo.com), built to demonstrate real-world 
QA automation skills. It validates critical user workflows including login 
authentication, shopping cart management, and complete checkout flows
the same scenarios a QA engineer would verify before any production release.

The framework is built in Python using Selenium WebDriver and follows the 
Page Object Model (POM) design pattern, which separates page structure from 
test logic for better maintainability and scalability.

Project 1 — E-Commerce QA Automation Suite

Situation: After my Dell co-op I recognized that most QA job postings in Ottawa were requiring automation skills specifically Selenium and Python which I hadn't formally demonstrated in a project. I had manual testing experience but no portfolio evidence of automation.

Task: I decided to build a complete end-to-end automation framework from scratch, independently, to prove I could design and implement a real test suite — not just follow tutorials.

Action: I built a 16-test automation suite using Selenium WebDriver and Python, following the Page Object Model design pattern to separate page structure from test logic. I created three test files covering login validation, shopping cart workflows, and a complete checkout flow. I set up Pytest fixtures for automatic browser setup and teardown using ChromeDriver and WebDriver Manager, and integrated Pytest-HTML for test reporting. I tested across Windows, Linux, and macOS environments and deployed the entire project to GitHub with a full README.

Result: All 16 tests pass consistently. The project demonstrates real automation architecture skills not just scripting and is publicly visible on GitHub. 

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
git clone https://github.com/Mansi9301/saucedemo-automation.git
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
