# Appium Python Automation

Automated mobile testing framework built using **Appium**, **Pytest**, and **Allure Report**.  
This project automates testing for the **Swag Labs Mobile App** including login validation and product cart functionality.

---

## Project Structure

```
APPPIUM-PYTHON-AUTOMATION/
│
├── allure-report/
│   └── index.html
│
├── allure-results/
│
├── data/
│   ├── __init__.py
│   └── login_data.py
│
├── images/
│
├── locators/
│   ├── __init__.py
│   ├── login.py
│   └── product.py
│
├── pages/
│   ├── __init__.py
│   ├── login.py
│   └── product.py
│
├── test/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_swaglabs_mobile.py
│
├── virtualenv/
│
├── pytest.ini
├── requirements.txt
└── run.bat
```

---

## Setup Instructions

### Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start Appium Server
Make sure you have the **Appium server** running and the device/emulator connected.

```bash
appium
```

### Run Tests
You can execute the tests using:
```bash
pytest
```

Or using the provided batch file:
```bash
run.bat
```

This will:
- Run all tests under the `test/` directory  
- Generate **Allure results** under `allure-results/`  
- Create a report file in `allure-report/index.html`

---

## Test Scenarios

### `test_login_with_valid_credentials`
- Login using valid username & password
- Verify the heading text **"PRODUCTS"**

### `test_login_with_invalid_credentials`
- Parametrized test using invalid combinations from `LoginData`
- Validate proper error messages

### `test_add_products_to_cart`
- Login with valid credentials
- Add multiple products to the cart
- Verify cart badge and “REMOVE” button

---

## Allure Reporting

To generate and open the report:

```bash
allure generate --single-file allure-results --clean -o allure-report
allure open allure-report
```

Output report path:
```
allure-report/index.html
```

---

## Tech Stack

| Tool / Library | Description |
|----------------|--------------|
| **Python** | Main programming language |
| **Appium** | Mobile automation framework |
| **Pytest** | Test runner |
| **Allure** | Reporting framework |
| **Selenium** | For WebDriver waits and conditions |

---

## Project Highlights

- Page Object Model (POM) structure  
- Centralized locators and test data  
- Allure steps and severity levels for traceability  
- Parametrized test cases with `pytest.mark.parametrize`  
- Easy integration via `run.bat`  

---

## Sample Report Preview

You can find the latest report in:
```
allure-report/index.html
```

Or regenerate it using:
```bash
allure serve allure-results
```