import allure
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.product import Locators




class Product:

    def __init__(self,setup):
        self.setup = setup

    def verify_heading_text(self):
        with allure.step('Check if heading text displays "PRODUCTS"'):
            try:
                WebDriverWait(self.setup,10).until(EC.presence_of_element_located((AppiumBy.XPATH,Locators.heading_text_element)))
                actual_heading_text = self.setup.find_element(AppiumBy.XPATH,Locators.heading_text_element).text
                return actual_heading_text
            except TimeoutException:
                return 'Element not found!'
            
    def add_product_to_cart_badge(self):
        with allure.step('Click Add To Cart button'):
            
            product_names = ['Sauce Labs Backpack', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie']
            
            for product_name in product_names:
                added = False
                for attempt in range(5):
                    try:
                        product_element = self.setup.find_element(AppiumBy.XPATH, Locators.product_element(product_name))
                        add_button = product_element.find_element(AppiumBy.XPATH, Locators.add_button_element)
                        add_button.click()
                        print(f"Added: {product_name}")
                        added = True
                        break
                    except NoSuchElementException:
                        if attempt < 4:  
                            device_size = self.setup.get_window_size()
                            self.setup.swipe(
                                start_x=device_size['width'] // 2,
                                start_y=device_size['height'] * 0.7,
                                end_x=device_size['width'] // 2,
                                end_y=device_size['height'] * 0.3,
                                duration=500
                            )

                            time.sleep(3)

                        else:
                            print(f"{product_name} not found")
                
                if not added:
                    raise Exception(f"Failed to add {product_name}")
            return product_names
        
    def verify_remove_button_is_displayed(self):
        with allure.step('Verify Add to Cart button will be replaced with Remove button'):
            try:
                WebDriverWait(self.setup,10).until(EC.presence_of_element_located((AppiumBy.XPATH,Locators.remove_button_element)))
                actual_text_in_button= self.setup.find_element(AppiumBy.XPATH,Locators.remove_button_element).text
                return actual_text_in_button
            except TimeoutException:
                return 'Element not found!'
            
    def verify_product_enter_in_cart_badge(self):
        with allure.step('Verify count of product in the cart badge matches expected quantity'):
            try:
                WebDriverWait(self.setup,10).until(EC.presence_of_element_located((AppiumBy.XPATH,Locators.cart_badge_element)))
                actual_cart_badge= self.setup.find_element(AppiumBy.XPATH,Locators.cart_badge_element).text
                return actual_cart_badge
            except TimeoutException:
                return 'Element not found!'