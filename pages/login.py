import allure
from locators.login import Locators
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:

    def __init__(self, setup):
        self.setup = setup

    def input_username(self,username):
        with allure.step('Input username'):
            self.setup.find_element(AppiumBy.ACCESSIBILITY_ID,Locators.input_username_element).send_keys(username)
    
    def input_password(self,password):
        with allure.step('Input password'):
            self.setup.find_element(AppiumBy.ACCESSIBILITY_ID,Locators.input_password_element).send_keys(password)

    def click_login_button(self):  
        with allure.step('Click on login button'):  
            self.setup.find_element(AppiumBy.XPATH,Locators.login_button_element).click()

    def verify_alert_message(self):
        with allure.step('Verify alert message is displayed'):
            try:
                WebDriverWait(self.setup,10).until(EC.presence_of_element_located((AppiumBy.XPATH,Locators.error_message_element)))
                actual_alert_message= self.setup.find_element(AppiumBy.XPATH,Locators.error_message_element).text
                return actual_alert_message
            except TimeoutException:
                return 'Element not found!'

        
        
      