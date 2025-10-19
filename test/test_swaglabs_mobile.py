import pytest
import allure
from pages.login import Login
from pages.product import Product
from data.login_data import LoginData


allure.title('Test valid login')
allure.description('Test login with valid credentials')
allure.severity(allure.severity_level.CRITICAL)
def test_login_with_valid_credentials(setup):
    login = Login(setup)
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()

    product = Product(setup)
    expected_heading_text = 'PRODUCTS'
    assert product.verify_heading_text() == expected_heading_text
   
allure.title('Test invalid login')
allure.description('Test login with invalid credentials')
allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username,password,message',LoginData.login_data)
def test_login_with_invalid_credentials(setup,username,password,message):
    login = Login(setup)
    login.input_username(username)
    login.input_password(password)
    login.click_login_button()
    assert login.verify_alert_message() == message

allure.title('Add products')
allure.description('Test add product to the cart badge')
allure.severity(allure.severity_level.CRITICAL)
def test_add_products_to_cart(setup):
    login = Login(setup)
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()

    product = Product(setup)
    product_names = product.add_product_to_cart_badge()

    expected_text_in_button = 'REMOVE'
    assert product.verify_remove_button_is_displayed() == expected_text_in_button

    expected_cart_badge = str(len(product_names))
    assert product.verify_product_enter_in_cart_badge() == expected_cart_badge