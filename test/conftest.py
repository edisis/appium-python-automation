import pytest
import allure
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options

@pytest.fixture
def setup(request):
    options = UiAutomator2Options()
    options.udid = 'RRCT6020PMY'
    options.platform_name = 'Android'
    options.app_package = 'com.swaglabsmobileapp'
    options.app_activity = 'com.swaglabsmobileapp.MainActivity'

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    yield driver
    
    with allure.step('Take screenshot for evidence'):
        test_name = request.node.name
        screenshot_path = f'images/screenshot_{test_name}.png'
        png_data = driver.get_screenshot_as_png()
        with open(screenshot_path, 'wb') as file:
            file.write(png_data)
        allure.attach.file(screenshot_path, name=f'Screenshot_{test_name}', attachment_type=allure.attachment_type.PNG)
    driver.quit()